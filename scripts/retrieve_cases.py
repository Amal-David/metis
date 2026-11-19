#!/usr/bin/env python3
"""Offline structural analogy retrieval with provenance and exclusions."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import urlsplit

LIBRARY = Path(__file__).resolve().parents[1] / 'references' / 'cases.json'
TYPES = {'official_solution', 'solver_retrospective', 'constructor_notes'}
TYPE_ALIASES = {'solver_account': 'solver_retrospective', 'constructor_note': 'constructor_notes'}
TEXT_FIELDS = ('id', 'source_title', 'source_kind', 'source_url', 'scope_read', 'accessed',
               'review_status', 'mechanism_family', 'observed',
               'representation_shift', 'transfer_when', 'dont_transfer_when', 'outcome_limit', 'lesson')
NULLABLE_FIELDS = ('documented_trigger', 'documented_test', 'documented_false_start')
REQUIRED = set(TEXT_FIELDS) | set(NULLABLE_FIELDS) | {'puzzle_id', 'tags', 'retrieval_cues', 'suggested_test'}
IDENTIFIER = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
REVIEW_STATUSES = {'source_checked', 'unverified'}
SEARCH_FIELDS = {'retrieval_cues': 3, 'tags': 4, 'mechanism_family': 4}
PROVENANCE_NOTE = ('source_checked records a curator provenance claim; validation checks '
                   'schema and consistency, not source truth or automated source review.')

def tokens(value: str) -> set[str]:
    if not isinstance(value, str):
        raise ValueError('token input must be a string')
    return set(re.findall(r'[^\W_]+', value.casefold(), flags=re.UNICODE))

def nonblank(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())

def normalize_family(value: str) -> str:
    return re.sub(r'[\s_]+', '-', value.strip().casefold())

def source_key(url: str) -> str:
    parsed = urlsplit(url)
    host = (parsed.hostname or '').casefold()
    if ':' in host:
        host = f'[{host}]'
    port = parsed.port
    if port is not None and not ((parsed.scheme.casefold() == 'https' and port == 443)
                                 or (parsed.scheme.casefold() == 'http' and port == 80)):
        host += f':{port}'
    # Scheme, fragments and trailing slashes do not create independent sources.
    return host + parsed.path.rstrip('/') + ('?' + parsed.query if parsed.query else '')


def valid_source_url(value: object) -> bool:
    if not nonblank(value) or any(ch.isspace() for ch in value) or '\\' in value:
        return False
    if re.search(r'%(?![0-9a-fA-F]{2})', value):
        return False
    try:
        parsed = urlsplit(value)
        parsed.port
        return (parsed.scheme.casefold() in {'http', 'https'} and bool(parsed.hostname)
                and parsed.username is None and parsed.password is None
                and not any(ord(ch) < 32 or ord(ch) == 127 for ch in value))
    except (ValueError, AttributeError):
        return False


def validate_card(card: object, location: str = 'card') -> list[str]:
    """Collect readable schema errors without trusting the types of JSON values."""
    if not isinstance(card, dict):
        return [f'{location}: expected an object']
    errors: list[str] = []
    missing = REQUIRED - card.keys()
    unknown = card.keys() - REQUIRED
    if missing:
        errors.append(f'{location}: missing fields: {", ".join(sorted(missing))}')
    if unknown:
        errors.append(f'{location}: unknown fields: {", ".join(sorted(map(str, unknown)))}')
    for field in TEXT_FIELDS:
        if field in card and not nonblank(card[field]):
            errors.append(f'{location}: {field} must be a nonblank string')
    for field in NULLABLE_FIELDS:
        if field in card and card[field] is not None and not nonblank(card[field]):
            errors.append(f'{location}: {field} must be a nonblank string or null')
    for field in ('id', 'mechanism_family'):
        value = card.get(field)
        if isinstance(value, str) and not IDENTIFIER.fullmatch(value):
            errors.append(f'{location}: {field} must be a lowercase hyphenated identifier')
    puzzle_id = card.get('puzzle_id')
    if puzzle_id is not None and (not isinstance(puzzle_id, str) or not IDENTIFIER.fullmatch(puzzle_id)):
        errors.append(f'{location}: puzzle_id must be a lowercase hyphenated identifier or null for a guide')
    kind = card.get('source_kind')
    if isinstance(kind, str) and kind not in TYPES:
        errors.append(f'{location}: invalid source_kind {kind!r}')
    review = card.get('review_status')
    if isinstance(review, str) and review not in REVIEW_STATUSES:
        errors.append(f'{location}: review_status must be source_checked or unverified')
    if 'source_url' in card and not valid_source_url(card['source_url']):
        errors.append(f'{location}: source_url must be an absolute HTTP(S) URL without credentials')
    accessed = card.get('accessed')
    if isinstance(accessed, str):
        try:
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', accessed):
                raise ValueError('format')
            date.fromisoformat(accessed)
        except ValueError:
            errors.append(f'{location}: accessed must be a valid YYYY-MM-DD date')
    for field in ('tags', 'retrieval_cues'):
        values = card.get(field)
        if not isinstance(values, list) or not values or not all(nonblank(value) for value in values):
            errors.append(f'{location}: {field} must be a nonempty list of nonblank strings')
        elif len({value.strip().casefold() for value in values}) != len(values):
            errors.append(f'{location}: {field} must not contain duplicates')
    suggestion = card.get('suggested_test')
    if not isinstance(suggestion, dict):
        errors.append(f'{location}: suggested_test must be an object')
    else:
        if set(suggestion) != {'origin', 'description'}:
            errors.append(f'{location}: suggested_test requires only origin and description')
        if suggestion.get('origin') != 'curator_proposal':
            errors.append(f'{location}: suggested_test.origin must be curator_proposal')
        if not nonblank(suggestion.get('description')):
            errors.append(f'{location}: suggested_test.description must be a nonblank string')
    return errors


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f'duplicate JSON field {key!r}')
        value[key] = item
    return value


def validate_cards(cards: object) -> list[str]:
    if not isinstance(cards, list) or not cards:
        return ['cards must be a nonempty array']
    errors: list[str] = []
    seen: dict[str, int] = {}
    for number, card in enumerate(cards, 1):
        errors.extend(validate_card(card, f'card {number}'))
        if isinstance(card, dict) and isinstance(card.get('id'), str):
            case_id = card['id']
            if case_id in seen:
                errors.append(f'card {number}: duplicate id {case_id!r} (first in card {seen[case_id]})')
            else:
                seen[case_id] = number
    return errors


def load_cases(path: Path = LIBRARY) -> tuple[list[dict[str, Any]], str]:
    """Read a complete v2 corpus; do not fetch or execute its source material."""
    path = Path(path)
    try:
        raw = path.read_bytes()
        payload = json.loads(raw.decode('utf-8'), object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f'{path}: cannot read valid UTF-8 JSON: {exc}') from exc
    if not isinstance(payload, dict):
        raise ValueError(f'{path}: expected a corpus object')
    required = {'schema_version', 'cards'}
    if set(payload) != required:
        missing = required - payload.keys()
        extra = payload.keys() - required
        details = []
        if missing:
            details.append(f'missing fields: {", ".join(sorted(missing))}')
        if extra:
            details.append(f'unknown fields: {", ".join(sorted(extra))}')
        raise ValueError(f'{path}: ' + '; '.join(details))
    if type(payload['schema_version']) is not int or payload['schema_version'] != 2:
        raise ValueError(f'{path}: schema_version must be integer 2')
    errors = validate_cards(payload['cards'])
    if errors:
        raise ValueError(f'{path}: invalid corpus:\n' + '\n'.join(errors))
    return payload['cards'], hashlib.sha256(raw).hexdigest()


def statistics(cards: list[dict[str, Any]]) -> dict[str, Any]:
    errors = validate_cards(cards)
    if errors:
        raise ValueError('invalid cards:\n' + '\n'.join(errors))
    return {
        'card_count': len(cards),
        'distinct_source_urls': len({card['source_url'] for card in cards}),
        'normalized_source_count': len({source_key(card['source_url']) for card in cards}),
        'distinct_nonnull_puzzle_ids': len({card['puzzle_id'] for card in cards if card['puzzle_id'] is not None}),
        'guide_card_count': sum(card['puzzle_id'] is None for card in cards),
        'source_kinds': dict(sorted(Counter(card['source_kind'] for card in cards).items())),
        'mechanism_families': dict(sorted(Counter(card['mechanism_family'] for card in cards).items())),
        'review_statuses': dict(sorted(Counter(card['review_status'] for card in cards).items())),
        'retrievable_card_count': sum(card['review_status'] == 'source_checked' for card in cards),
        'missing_documented_fields': {field: sum(card[field] is None for card in cards) for field in NULLABLE_FIELDS},
        'provenance_note': PROVENANCE_NOTE,
        'counting_note': ('Card, source URL and puzzle ID counts are separate. Null puzzle IDs identify guides. '
                          'Puzzle IDs are curator assignments, not an automated proof of corpus independence.'),
    }


def _exclusions(values: object, field: str) -> set[str]:
    if values is None:
        return set()
    if not isinstance(values, (list, tuple, set, frozenset)) or not all(nonblank(v) for v in values):
        raise ValueError(f'{field} exclusions must be a collection of nonblank strings')
    if field == 'source':
        if not all(valid_source_url(value) for value in values):
            raise ValueError('source exclusions must be absolute HTTP(S) URLs without credentials')
        return {source_key(value) for value in values}
    if field == 'family':
        return {normalize_family(value) for value in values}
    return {value.strip() for value in values}


def search_cases(
    query: str, cards: list[dict[str, Any]], *, limit: int = 3,
    case_type: str | None = None, exclude_families: list[str] | None = None,
    exclude_puzzles: list[str] | None = None, exclude_sources: list[str] | None = None,
    diversify: bool = True,
) -> list[dict[str, Any]]:
    """Retrieve checked structural analogies, preserving provenance and limitations.

    Scores describe lexical overlap only. No source text is fetched or executed.
    """
    if not isinstance(query, str) or not query.strip() or len(query) > 4096:
        raise ValueError('query must contain 1–4096 nonblank characters')
    if type(limit) is not int or not 1 <= limit <= 6:
        raise ValueError('limit must be an integer from 1 to 6')
    if type(diversify) is not bool:
        raise ValueError('diversify must be a boolean')
    if case_type is not None:
        if not isinstance(case_type, str):
            raise ValueError('case_type must be a supported source kind')
        case_type = TYPE_ALIASES.get(case_type, case_type)
        if case_type not in TYPES:
            raise ValueError('case_type must be a supported source kind')
    errors = validate_cards(cards)
    if errors:
        raise ValueError('invalid cards:\n' + '\n'.join(errors))
    excluded_families = _exclusions(exclude_families, 'family')
    excluded_puzzles = _exclusions(exclude_puzzles, 'puzzle')
    excluded_sources = _exclusions(exclude_sources, 'source')
    query_terms = tokens(query)
    ranked: list[tuple[int, str, list[str], dict[str, Any]]] = []
    for card in cards:
        if card['review_status'] != 'source_checked':
            continue
        if case_type is not None and card['source_kind'] != case_type:
            continue
        if (normalize_family(card['mechanism_family']) in excluded_families
                or card['puzzle_id'] in excluded_puzzles
                or source_key(card['source_url']) in excluded_sources):
            continue
        score = 0
        matched: set[str] = set()
        for field, weight in SEARCH_FIELDS.items():
            value = ' '.join(card[field]) if isinstance(card[field], list) else card[field]
            overlap = query_terms & tokens(value)
            score += weight * len(overlap)
            matched.update(overlap)
        if score:
            ranked.append((score, card['id'], sorted(matched), card))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    results: list[dict[str, Any]] = []
    used_sources: set[str] = set()
    used_puzzles: set[str] = set()
    used_families: set[str] = set()
    # First give each family a chance, then fill from remaining ranked cards.
    # Exclusions precede both passes; removed high scorers cannot block peers.
    for require_new_family in ([True, False] if diversify else [False]):
        for score, _, matched, card in ranked:
            source = source_key(card['source_url'])
            puzzle = card['puzzle_id']
            family = normalize_family(card['mechanism_family'])
            if (source in used_sources or (puzzle is not None and puzzle in used_puzzles)
                    or (require_new_family and family in used_families)):
                continue
            results.append({**card, 'score': score, 'matched_terms': matched})
            used_sources.add(source)
            if puzzle is not None:
                used_puzzles.add(puzzle)
            used_families.add(family)
            if len(results) == limit:
                return results
    return results


def _limit(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError('limit must be an integer from 1 to 6') from exc
    if not 1 <= number <= 6:
        raise argparse.ArgumentTypeError('limit must be an integer from 1 to 6')
    return number


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', help='structural observations or method keywords')
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--stats', action='store_true', help='report counts and missing source documentation')
    modes.add_argument('--validate', action='store_true', help='validate schema; does not verify sources')
    parser.add_argument('--library', type=Path, default=LIBRARY)
    parser.add_argument('--limit', type=_limit, default=3, help='1–6 results (default: 3)')
    parser.add_argument('--type', dest='case_type', choices=sorted(TYPES | TYPE_ALIASES.keys()))
    parser.add_argument('--exclude-family', action='append', default=[], help='repeat for each mechanism family')
    parser.add_argument('--exclude-puzzle', action='append', default=[], help='repeat for each original puzzle ID')
    parser.add_argument('--exclude-source', action='append', default=[], help='repeat for each source URL')
    parser.add_argument('--no-diversify', action='store_true', help='score order; still deduplicate sources and puzzles')
    args = parser.parse_args(argv)
    if (args.stats or args.validate) and args.query is not None:
        parser.error('query cannot be combined with --stats or --validate')
    if not (args.stats or args.validate) and args.query is None:
        parser.error('supply a query, --stats, or --validate')
    try:
        cards, digest = load_cases(args.library)
        if args.stats:
            output = statistics(cards)
        elif args.validate:
            output = {'status': 'valid', 'card_count': len(cards), 'provenance_note': PROVENANCE_NOTE}
        else:
            matches = search_cases(args.query, cards, limit=args.limit, case_type=args.case_type,
                                   exclude_families=args.exclude_family, exclude_puzzles=args.exclude_puzzle,
                                   exclude_sources=args.exclude_source, diversify=not args.no_diversify)
            output = {
                'query': args.query, 'matches': matches, 'returned': len(matches),
                'scoring': 'Weighted structural lexical overlap, not confidence or evidence strength.',
                'indexed_fields': list(SEARCH_FIELDS),
                'diversification': 'mechanism families first' if not args.no_diversify else 'score order',
                'excluded_families': args.exclude_family, 'excluded_puzzles': args.exclude_puzzle,
                'excluded_sources': args.exclude_source, 'provenance_note': PROVENANCE_NOTE,
            }
            if not matches:
                output['message'] = 'No matching checked cases. Try another structural description.'
        output['library_sha256'] = digest
        output['scope'] = 'Offline local corpus only; no sources fetched, executed or automatically verified.'
    except (ValueError, OSError) as exc:
        print(json.dumps({'status': 'invalid', 'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
