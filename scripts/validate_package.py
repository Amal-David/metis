#!/usr/bin/env python3
"""Validate the authored skill bundle and detect drift against a saved manifest."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_FILES = (
    'SKILL.md', 'scripts/retrieve_cases.py',
    'references/cases.json', 'references/contrast-examples.md',
    'references/corpus-audit.md', 'references/evaluation.md',
    'references/experiments.md', 'references/hypothesis-operators.md',
    'references/mechanism-atlas.md', 'references/polya.md',
    'references/research-protocol.md', 'references/research-sources.md',
    'references/sources.md',
)


def fingerprint(root: Path) -> dict[str, str]:
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
            for name in sorted(RUNTIME_FILES)}


def check_content(root: Path) -> list[str]:
    errors = []
    text = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match or not re.search(r'^name: metis$', match.group(1), re.M):
        errors.append('SKILL.md must have name: metis in YAML frontmatter')
    if not match or not re.search(r'^description: .+', match.group(1), re.M):
        errors.append('SKILL.md must have a description in YAML frontmatter')
    if len(text.splitlines()) >= 500:
        errors.append('SKILL.md exceeds the compact-core line budget')
    for name in RUNTIME_FILES:
        path = root / name
        if name.endswith('.py'):
            try:
                ast.parse(path.read_text(encoding='utf-8'), filename=name)
            except SyntaxError as exc:
                errors.append(f'{name}: {exc}')
        if not name.endswith('.md'):
            continue
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            target = link.split('#', 1)[0]
            if not target or '://' in target or target.startswith('mailto:'):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                errors.append(f'{name}: missing or external local link {target}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-manifest', action='store_true', help='refresh after reviewing authored content changes')
    parser.add_argument('--against', type=Path, help='also verify another installed copy against this manifest')
    args = parser.parse_args()
    try:
        errors = check_content(ROOT)
        actual = fingerprint(ROOT)
        manifest_path = ROOT / 'skill-manifest.json'
        if args.write_manifest:
            if errors:
                raise ValueError('\n'.join(errors))
            payload = {'schema_version': 1, 'files': actual,
                       'scope': 'Authored reasoning, knowledge and retrieval files. Platform-managed UI metadata and repository evaluation tools are excluded.'}
            manifest_path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
        payload = json.loads(manifest_path.read_text(encoding='utf-8'))
        if payload.get('schema_version') != 1 or payload.get('files') != actual:
            errors.append('Authored bundle differs from skill-manifest.json; review changes before refreshing it')
        if args.against is not None:
            other = fingerprint(args.against)
            errors.extend(f'Installed copy differs: {name}' for name in actual if other[name] != actual[name])
        if errors:
            raise ValueError('\n'.join(errors))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Package invalid: {exc}', file=sys.stderr)
        return 1
    print(f'Package valid: {len(actual)} authored files; local links and manifest agree.')
    if args.against is not None:
        print('Installed authored files match the repository byte for byte.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
