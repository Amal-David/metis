#!/usr/bin/env python3
"""Deterministic, offline teaching-case retrieval for Metis.

Sources remain read-only text. This script does not fetch URLs, run source code,
invoke an LLM, or rank hypotheses by their truth.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

LIBRARY = Path(__file__).resolve().parents[1] / "references" / "cases.json"
TYPES = {"official_solution", "solver_account", "constructor_note"}
REQUIRED = {
    "id", "title", "puzzle_id", "source_type", "source_url",
    "reported_discovery_trigger", "documented_evidence",
    "curator_inference", "contrast_test", "limitations", "tags",
}


def tokens(s: str) -> set[str]:
    return set(re.findall(r"[^\W_]+", s.casefold(), flags=re.UNICODE))


def load_cases(path: Path = LIBRARY) -> tuple[list[dict[str, Any]], str]:
    """Validate provenance fields and return cards plus a content fingerprint."""
    raw = path.read_bytes()
    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("cards"), list):
        raise ValueError("expected object with cards array")
    seen: set[str] = set()
    cards = payload["cards"]
    for row in cards:
        if not isinstance(row, dict) or not REQUIRED.issubset(row):
            raise ValueError("missing required provenance field")
        if not isinstance(row["id"], str) or not row["id"] or row["id"] in seen:
            raise ValueError("blank or duplicate card id")
        seen.add(row["id"])
        if row["source_type"] not in TYPES:
            raise ValueError("invalid source_type")
        if not isinstance(row["source_url"], str) or not row["source_url"].startswith("https://"):
            raise ValueError("source_url must be https")
        if not isinstance(row["tags"], list) or not row["tags"] or not all(isinstance(t, str) and t for t in row["tags"]):
            raise ValueError("invalid tags")
        for f in ("documented_evidence", "curator_inference", "contrast_test", "limitations"):
            if not isinstance(row[f], str) or not row[f].strip():
                raise ValueError(f"empty {f}")
    return cards, hashlib.sha256(raw).hexdigest()


def search_cases(
    query: str, cards: list[dict[str, Any]], *, limit: int = 3,
    case_type: str | None = None,
) -> list[dict[str, Any]]:
    """Rank lexical matches; scores describe similarity, not evidence strength."""
    if not isinstance(query, str) or not query.strip() or len(query) > 4096:
        raise ValueError("query must be 1–4096 nonblank characters")
    if not isinstance(limit, int) or not (1 <= limit <= 6):
        raise ValueError("limit must be 1–6")
    if case_type is not None and case_type not in TYPES:
        raise ValueError("invalid case type")
    words = tokens(query)
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for c in cards:
        if case_type is not None and c["source_type"] != case_type:
            continue
        title = tokens(c["title"])
        tags = tokens(" ".join(c["tags"]))
        body = tokens(" ".join([
            c["documented_evidence"], c["curator_inference"],
            c["contrast_test"], c["limitations"],
        ]))
        matched = words & (title | tags | body)
        if not matched:
            continue
        score = sum(4 if w in tags else 3 if w in title else 1 for w in matched)
        scored.append((-score, c["id"], {**c, "score": score, "matched_terms": sorted(matched)}))
    scored.sort(key=lambda x: (x[0], x[1]))
    return [entry for _, _, entry in scored[:limit]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Structure or method keywords (not a memorized puzzle answer)")
    parser.add_argument("--limit", type=int, default=3, help="1–6 (default 3)")
    parser.add_argument("--type", dest="case_type", choices=sorted(TYPES))
    parser.add_argument("--library", type=Path, default=LIBRARY)
    args = parser.parse_args()
    try:
        cards, digest = load_cases(args.library)
        matches = search_cases(args.query, cards, limit=args.limit, case_type=args.case_type)
    except (ValueError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps({
        "matches": matches,
        "library_sha256": digest,
        "scope": "offline curated lexical teaching-case retrieval; no online sources fetched or evaluated",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
