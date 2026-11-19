"""Metis case registry tests; standard library only."""
from __future__ import annotations

import json
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from scripts.retrieve_cases import load_cases, search_cases, tokens


class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cards, cls.digest = load_cases()

    def test_expected_card_counts_and_provenance(self) -> None:
        self.assertEqual(len(self.cards), 21)
        self.assertEqual(Counter(c["source_type"] for c in self.cards), {
            "official_solution": 10, "solver_account": 7, "constructor_note": 4
        })
        self.assertEqual(len(self.digest), 64)
        self.assertTrue(all(c["documented_evidence"] != c["curator_inference"]
                            for c in self.cards))

    def test_sources_are_not_necessarily_unique(self) -> None:
        urls = {c["source_url"] for c in self.cards}
        self.assertLess(len(urls), len(self.cards))
        self.assertGreaterEqual(len(urls), 8)

    def test_retrieve_representative_move(self) -> None:
        results = search_cases("edge representation graph", self.cards, limit=6)
        self.assertTrue(any(c["puzzle_id"] == "tatham-net" for c in results))
        self.assertTrue(all(c["score"] > 0 and c["matched_terms"] for c in results))

    def test_type_filter(self) -> None:
        results = search_cases("constructor puzzle", self.cards, case_type="constructor_note")
        self.assertTrue(results)
        self.assertTrue(all(c["source_type"] == "constructor_note" for c in results))

    def test_unknown_query_returns_no_hallucinated_matches(self) -> None:
        self.assertEqual(search_cases("zzzzfobulated_987654", self.cards), [])

    def test_bad_query_and_budget(self) -> None:
        for q in ("", "   ", "x" * 4097):
            with self.assertRaises(ValueError):
                search_cases(q, self.cards)
        for limit in (0, 7, -1):
            with self.assertRaises(ValueError):
                search_cases("graph", self.cards, limit=limit)
        with self.assertRaises(ValueError):
            search_cases("graph", self.cards, case_type="imagined_source")

    def test_duplicate_id_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "cases.json"
            p.write_text(json.dumps({"cards": [self.cards[0], self.cards[0]]}), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_cases(p)

    def test_tokens_unicode_and_case(self) -> None:
        self.assertIn("graph", tokens("GRAPH graph!"))
        self.assertIn("π", tokens("π relation"))


if __name__ == "__main__":
    unittest.main()
