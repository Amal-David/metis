# Metis

**Metis — creative, evidence-first reasoning for unfamiliar puzzles.**

Metis is an agent skill for inventing *new representations and testable mechanisms* when the puzzle does not tell you the rules. It is inspired by how strong human solvers and puzzle constructors recognize an unusual detail, change what a clue *does*, and then verify that the interpretation predicts evidence not used to invent it.

> Observe → Reframe → Invent → Contrast → Test → Verify → Continue.

## Start here

Read [SKILL.md](SKILL.md) to apply Metis to visual, logical, spatial, linguistic, interactive, and multi-layer puzzles. A Codex-style agent can use the repo itself as an installed skill:

```text
Use the Metis skill in SKILL.md to approach this unfamiliar puzzle.
Propose genuinely different mechanisms, not just variations on one guess.
Prioritize cheap tests that make leading mechanisms disagree.
Keep claims separate: observed, conjectured, tested, independently verified, solved.
```

**The skill guides strategy; it does not claim to be a solver that always finds the answer.** Use [Polya](https://github.com/Amal-David/polya) when bounded operations, constraint solving, replay, and evidence ledgers help. Metis complements Polya rather than replacing it.

## Contents

- [SKILL.md](SKILL.md): compact agent contract and ten principles
- [references/hypothesis-operators.md](references/hypothesis-operators.md): nine creative moves with triggers, examples, and falsifiers
- [references/cases.json](references/cases.json): 21 annotated teaching cards; some cards share a source
- [scripts/retrieve_cases.py](scripts/retrieve_cases.py): deterministic local case lookup, with provenance
- [references/research-protocol.md](references/research-protocol.md): collecting 1,000 distinct cases without invented discovery histories
- [references/evaluation.md](references/evaluation.md): paired, blinded evaluation; no unmeasured gains claimed
- [references/source-notes.md](references/source-notes.md): source URLs, attribution, and rights/limitations
- [examples/hypothesis-ledger.md](examples/hypothesis-ledger.md): sample investigation format
- [tests/test_retrieve_cases.py](tests/test_retrieve_cases.py): registry and query checks

## Local retrieval

```bash
python scripts/retrieve_cases.py "edge representation connectivity" --limit 3
python -m unittest discover -s tests -v
```

The retriever reads only local JSON and never fetches or executes external source content.

## What is verified?

This repository package preserves the method described in the preceding design conversation. The earlier ChatGPT-installed skill package is not exported by the available interface, so **this is a faithful reconstruction, not a byte-identical export**. Its source cards are independently rewritten summaries, *not* reproduction of third-party pages or an authorized training corpus.

The previously reported six small puzzle checks were passed by **both** skill and ordinary-prompt agents; they do **not** establish a relative advantage. No new agent performance claim is made by this repo. A larger preregistered comparison is specified under [evaluation](references/evaluation.md).

## Scope

For benign, authorized puzzle solving and educational research. Do not target real wallets, accounts, authentication secrets, or access controls. Preserve original observations, source versions, interpretation alternatives, costs and independent checks. A bounded no-hit is not an impossibility theorem. An attractive extraction is not proof of puzzle-author intent.
