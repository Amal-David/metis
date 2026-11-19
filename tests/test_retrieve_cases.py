"""Behavioral contracts for offline analogy retrieval; no solving-gain claims."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SKILL_ROOT = Path(os.environ.get('METIS_SKILL_ROOT', Path(__file__).resolve().parents[1]))
SCRIPT = SKILL_ROOT / 'scripts' / 'retrieve_cases.py'
spec = importlib.util.spec_from_file_location('metis_retrieval_under_test', SCRIPT)
assert spec is not None and spec.loader is not None
retrieval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retrieval)


def card(case_id='case-a', **changes):
    result = {
        'id': case_id, 'puzzle_id': 'puzzle-' + case_id,
        'source_title': 'A documented teaching example',
        'source_kind': 'solver_retrospective',
        'source_url': 'https://example.org/' + case_id,
        'scope_read': 'Relevant passage, with unknown history preserved.',
        'accessed': '2026-11-19', 'review_status': 'source_checked',
        'mechanism_family': 'representation-change',
        'retrieval_cues': ['edge state', 'partial certainty'],
        'tags': ['graph', 'representation'],
        'observed': 'Some edge states are known while object state is unresolved.',
        'representation_shift': 'Record partial relations independently.',
        'documented_trigger': None, 'documented_test': None,
        'documented_false_start': None,
        'suggested_test': {'origin': 'curator_proposal', 'description': 'Check a tiny boundary case.'},
        'transfer_when': 'Partial relational certainty is hidden by object states.',
        'dont_transfer_when': 'The new relations do not preserve legal object states.',
        'outcome_limit': 'This is a teaching example, not an independent solve.',
        'lesson': 'Look for useful partial information.',
    }
    result.update(changes)
    return result


def payload(cards=None):
    return {'schema_version': 2, 'cards': [card()] if cards is None else cards}


class CorpusValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'cases.json'

    def load_payload(self, value):
        self.path.write_text(json.dumps(value), encoding='utf-8')
        return retrieval.load_cases(self.path)

    def assert_bad_card(self, value):
        with self.assertRaises(ValueError) as ctx:
            self.load_payload(payload([value]))
        self.assertIn('card', str(ctx.exception))

    def test_valid_card_retains_unknowns_and_byte_fingerprint(self):
        cards, digest = self.load_payload(payload())
        self.assertIsNone(cards[0]['documented_trigger'])
        self.assertEqual(digest, hashlib.sha256(self.path.read_bytes()).hexdigest())
        self.assertEqual((cards, digest), retrieval.load_cases(self.path))
        self.path.write_text(self.path.read_text() + '\n', encoding='utf-8')
        same_cards, changed_digest = retrieval.load_cases(self.path)
        self.assertEqual(cards, same_cards)
        self.assertNotEqual(digest, changed_digest)

    def test_wrong_wrapper_shapes_and_empty_corpus_are_rejected(self):
        bad = [None, [], 'text', {}, {'cards': [card()]},
               {'schema_version': 2, 'cards': []},
               {'schema_version': 2, 'cards': {}},
               {'schema_version': 2, 'cards': [card()], 'extra': 1}]
        bad.extend({'schema_version': v, 'cards': [card()]} for v in (True, 2.0, '2', 1, None))
        for value in bad:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.load_payload(value)

    def test_every_field_is_required_and_unknown_fields_rejected(self):
        for field in card():
            value = card()
            del value[field]
            with self.subTest(field=field):
                self.assert_bad_card(value)
        self.assert_bad_card(card(extra_field='unsupported'))

    def test_malformed_field_types_produce_readable_errors(self):
        for field in retrieval.TEXT_FIELDS:
            for wrong in (None, [], {}, True, 4, '', '   '):
                with self.subTest(field=field, wrong=wrong):
                    self.assert_bad_card(card(**{field: wrong}))
        for field in retrieval.NULLABLE_FIELDS:
            for wrong in ([], {}, False, 4, '', '   '):
                with self.subTest(field=field, wrong=wrong):
                    self.assert_bad_card(card(**{field: wrong}))
        for wrong in (None, [], 'text', 5):
            with self.subTest(row=wrong):
                self.assert_bad_card(wrong)

    def test_identifiers_lists_and_provenance_are_validated(self):
        for field in ('id', 'mechanism_family', 'puzzle_id'):
            for wrong in ('Bad ID', '', 'snake_case', ['identifier'], False):
                with self.subTest(field=field, wrong=wrong):
                    self.assert_bad_card(card(**{field: wrong}))
        for field in ('tags', 'retrieval_cues'):
            for wrong in (None, 'edge', [], [''], ['edge', 4], ['EDGE', ' edge ']):
                with self.subTest(field=field, wrong=wrong):
                    self.assert_bad_card(card(**{field: wrong}))
        for field, wrong in [('source_kind', 'imagined'), ('review_status', 'verified_by_program')]:
            self.assert_bad_card(card(**{field: wrong}))
        for wrong in (None, [], {'origin': 'source_reported', 'description': 'test'},
                      {'origin': 'curator_proposal', 'description': ''},
                      {'origin': 'curator_proposal', 'description': ['test']},
                      {'origin': 'curator_proposal', 'description': 'test', 'extra': True}):
            with self.subTest(suggestion=wrong):
                self.assert_bad_card(card(suggested_test=wrong))
        self.load_payload(payload([card(puzzle_id=None, review_status='unverified')]))

    def test_url_and_date_syntax_are_validated(self):
        bad_urls = ['relative/path', 'file:///tmp/case', 'https:///missing-host',
                    'https://user:password@example.org/case', 'https://example.org/a b',
                    'https://example.org:99999/case', 'https://example.org:wrong/case',
                    'https://example.org/%GG', 'https://exa\\mple.org/case', 'https://[broken']
        for url in bad_urls:
            with self.subTest(url=url):
                self.assert_bad_card(card(source_url=url))
        for value in ('2026-2-03', '2026-02-30', '2026-13-01', '19/11/2026'):
            with self.subTest(date=value):
                self.assert_bad_card(card(accessed=value))
        self.load_payload(payload([card(source_url='http://example.org/case?q=1#part', accessed='2024-02-29')]))

    def test_duplicate_ids_and_duplicate_json_fields_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate id'):
            self.load_payload(payload([card(), card()]))
        raw = json.dumps(payload()).replace('"schema_version": 2', '"schema_version": 2, "schema_version": 2')
        self.path.write_text(raw, encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'duplicate JSON field'):
            retrieval.load_cases(self.path)

    def test_invalid_json_utf8_and_missing_file_are_readable(self):
        for raw in (b'{bad json', b'\xff', b''):
            self.path.write_bytes(raw)
            with self.subTest(raw=raw), self.assertRaisesRegex(ValueError, 'valid UTF-8 JSON'):
                retrieval.load_cases(self.path)
        self.path.unlink()
        with self.assertRaisesRegex(ValueError, 'cannot read'):
            retrieval.load_cases(self.path)


class RetrievalBehaviorTests(unittest.TestCase):
    def test_returned_card_keeps_provenance_and_unknowns(self):
        original = card()
        result = retrieval.search_cases('edge', [original])[0]
        for key, value in original.items():
            self.assertEqual(value, result[key])
        self.assertGreater(result['score'], 0)
        self.assertEqual(['edge'], result['matched_terms'])

    def test_ranking_ignores_title_and_solution_prose(self):
        cards = [card('case-a'), card('case-b', tags=['graph'])]
        before = retrieval.search_cases('edge graph', cards)
        changed = copy.deepcopy(cards)
        for row in changed:
            for field in ('source_title', 'observed', 'representation_shift', 'outcome_limit',
                          'lesson', 'documented_trigger', 'documented_test', 'documented_false_start',
                          'transfer_when', 'dont_transfer_when', 'scope_read'):
                row[field] = 'zebraword edge graph ' * 20
            row['suggested_test']['description'] = 'zebraword edge graph ' * 20
        after = retrieval.search_cases('edge graph', changed)
        signature = lambda rows: [(r['id'], r['score'], r['matched_terms']) for r in rows]
        self.assertEqual(signature(before), signature(after))
        self.assertEqual([], retrieval.search_cases('zebraword', changed))

    def test_no_match_and_unchecked_cards_are_never_forced(self):
        self.assertEqual([], retrieval.search_cases('unseenword', [card()]))
        self.assertEqual([], retrieval.search_cases('edge', [card(review_status='unverified')]))
        self.assertEqual([], retrieval.search_cases('!!!', [card()]))

    def test_deterministic_results_do_not_depend_on_corpus_order(self):
        cards = [card('case-c'), card('case-a'), card('case-b')]
        self.assertEqual(retrieval.search_cases('edge', cards), retrieval.search_cases('edge', list(reversed(cards))))
        self.assertEqual(['case-a', 'case-b', 'case-c'], [r['id'] for r in retrieval.search_cases('edge', cards)])

    def test_family_diversity_beats_a_higher_ranked_repeated_family(self):
        cards = [card('case-a', tags=['graph', 'edge', 'representation']),
                 card('case-b', tags=['graph', 'edge']),
                 card('case-c', mechanism_family='calibration', retrieval_cues=['edge'], tags=['oracle'])]
        diversified = retrieval.search_cases('edge graph representation', cards, limit=2)
        by_score = retrieval.search_cases('edge graph representation', cards, limit=2, diversify=False)
        self.assertEqual(['case-a', 'case-c'], [r['id'] for r in diversified])
        self.assertEqual(['case-a', 'case-b'], [r['id'] for r in by_score])

    def test_duplicate_source_and_original_puzzle_are_never_returned(self):
        cards = [card('case-a', source_url='https://EXAMPLE.org/shared/#one'),
                 card('case-b', source_url='http://example.org/shared#two', mechanism_family='calibration'),
                 card('case-c', puzzle_id='puzzle-case-a', mechanism_family='invariant'),
                 card('case-d', mechanism_family='ordering')]
        for diversify in (True, False):
            results = retrieval.search_cases('edge', cards, limit=6, diversify=diversify)
            self.assertEqual(['case-a', 'case-d'], [r['id'] for r in results])

    def test_guides_with_null_puzzle_ids_remain_independent_sources(self):
        cards = [card('guide-a', puzzle_id=None), card('guide-b', puzzle_id=None)]
        self.assertEqual(2, len(retrieval.search_cases('edge', cards)))

    def test_exclusions_apply_before_high_ranked_card_can_block_replacement(self):
        cards = [card('case-a', tags=['edge', 'graph'], puzzle_id='same-puzzle'),
                 card('case-b', mechanism_family='calibration', puzzle_id='same-puzzle'),
                 card('case-c', mechanism_family='invariant'),
                 card('case-d', mechanism_family='ordering')]
        results = retrieval.search_cases('edge graph', cards, limit=6,
                                         exclude_families=['Representation Change', 'invariant'])
        self.assertEqual({'case-b', 'case-d'}, {r['id'] for r in results})
        results = retrieval.search_cases('edge graph', cards, limit=6,
                                         exclude_sources=['https://example.org/case-a/#part'],
                                         exclude_puzzles=['puzzle-case-c', 'puzzle-case-d'])
        self.assertEqual(['case-b'], [r['id'] for r in results])

    def test_source_type_filter_supports_legacy_aliases(self):
        cards = [card('solver'), card('constructor', source_kind='constructor_notes'),
                 card('official', source_kind='official_solution')]
        for query_type, expected in [('solver_account', 'solver'), ('solver_retrospective', 'solver'),
                                     ('constructor_note', 'constructor'), ('constructor_notes', 'constructor'),
                                     ('official_solution', 'official')]:
            with self.subTest(query_type=query_type):
                results = retrieval.search_cases('edge', cards, case_type=query_type)
                self.assertEqual([expected], [r['id'] for r in results])

    def test_invalid_query_limits_filters_and_cards_raise_value_error(self):
        for query in (None, [], 2, '', ' ', 'x' * 4097):
            with self.subTest(query=query), self.assertRaises(ValueError):
                retrieval.search_cases(query, [card()])
        for limit in (True, False, 0, 7, -1, 2.0, '3', None):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                retrieval.search_cases('edge', [card()], limit=limit)
        for kwargs in ({'case_type': []}, {'case_type': 'unknown'}, {'diversify': 1},
                       {'exclude_families': 'representation-change'}, {'exclude_puzzles': [None]},
                       {'exclude_sources': ['not-a-url']}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                retrieval.search_cases('edge', [card()], **kwargs)
        for cards in ([], None, [False], [card(source_kind=[])], [card(), card()]):
            with self.subTest(cards=cards), self.assertRaises(ValueError):
                retrieval.search_cases('edge', cards)

    def test_unicode_tokens_and_maximum_result_limit(self):
        self.assertIn('graph', retrieval.tokens('GRAPH graph!'))
        self.assertIn('π', retrieval.tokens('π relation'))
        with self.assertRaises(ValueError):
            retrieval.tokens(None)
        cards = [card('case-' + letter) for letter in 'abcdefgh']
        self.assertEqual(6, len(retrieval.search_cases('edge', cards, limit=6)))


class StatisticsAndCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'cases.json'
        self.cards = [card('case-a', documented_trigger='A reported observation.'),
                      card('case-b', puzzle_id='puzzle-case-a', source_url='https://example.org/case-a/#second'),
                      card('guide-a', puzzle_id=None, source_kind='constructor_notes'),
                      card('guide-b', puzzle_id=None, review_status='unverified')]
        self.path.write_text(json.dumps(payload(self.cards)), encoding='utf-8')

    def run_cli(self, *arguments):
        return subprocess.run([sys.executable, str(SCRIPT), '--library', str(self.path), *arguments],
                              text=True, capture_output=True, timeout=10, check=False)

    def test_statistics_distinguish_cards_sources_puzzles_guides_and_unknowns(self):
        stats = retrieval.statistics(self.cards)
        self.assertEqual(4, stats['card_count'])
        self.assertEqual(4, stats['distinct_source_urls'])
        self.assertEqual(3, stats['normalized_source_count'])
        self.assertEqual(1, stats['distinct_nonnull_puzzle_ids'])
        self.assertEqual(2, stats['guide_card_count'])
        self.assertEqual(3, stats['retrievable_card_count'])
        self.assertEqual({'constructor_notes': 1, 'solver_retrospective': 3}, stats['source_kinds'])
        self.assertEqual(3, stats['missing_documented_fields']['documented_trigger'])
        self.assertEqual(4, stats['missing_documented_fields']['documented_false_start'])
        self.assertIn('not source truth', stats['provenance_note'])

    def test_cli_query_stats_and_validation_modes(self):
        for arguments in (('edge', '--limit', '2'), ('--stats',), ('--validate',)):
            with self.subTest(arguments=arguments):
                result = self.run_cli(*arguments)
                self.assertEqual(0, result.returncode, result.stderr)
                output = json.loads(result.stdout)
                self.assertEqual(hashlib.sha256(self.path.read_bytes()).hexdigest(), output['library_sha256'])
                self.assertIn('Offline', output['scope'])
        matches = json.loads(self.run_cli('edge', '--type', 'constructor_note').stdout)['matches']
        self.assertEqual(['guide-a'], [r['id'] for r in matches])

    def test_cli_repeated_exclusion_flags_and_no_match(self):
        result = self.run_cli('edge', '--exclude-source', 'https://example.org/case-a',
                              '--exclude-source', 'https://example.org/guide-a')
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual([], json.loads(result.stdout)['matches'])
        result = self.run_cli('edge', '--exclude-family', 'representation-change',
                              '--exclude-family', 'calibration', '--exclude-puzzle', 'not-present',
                              '--exclude-puzzle', 'another-puzzle')
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual([], json.loads(result.stdout)['matches'])

    def test_cli_invalid_arguments_fail_without_traceback(self):
        for arguments in ((), ('edge', '--limit', '0'), ('edge', '--limit', '7'),
                          ('edge', '--limit', 'True'), ('edge', '--type', 'imaginary'),
                          ('edge', '--stats'), ('--stats', '--validate'),
                          ('edge', '--exclude-source', 'not-a-url')):
            with self.subTest(arguments=arguments):
                result = self.run_cli(*arguments)
                self.assertEqual(2, result.returncode)
                self.assertNotIn('Traceback', result.stderr)
                self.assertTrue(result.stderr.strip())

    def test_cli_malformed_corpus_is_a_clear_error_not_type_error(self):
        self.path.write_text(json.dumps(payload([card(source_kind=[])])), encoding='utf-8')
        result = self.run_cli('--validate')
        self.assertEqual(2, result.returncode)
        output = json.loads(result.stderr)
        self.assertEqual('invalid', output['status'])
        self.assertIn('source_kind must be a nonblank string', output['error'])
        self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
