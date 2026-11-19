# Metis

**Creative, evidence-led reasoning for unfamiliar puzzles.**

Metis is an agent skill for discovering useful representations, developing hypotheses, choosing informative actions, and checking the result. It combines an adaptable reasoning policy with a small, source-audited knowledge base.

The key decision is **what is blocking progress**: an uncertain observation, missing knowledge, an unproductive representation, competing mechanisms, difficult execution, or unfinished extraction. Exploration is allowed before a hypothesis is precise; a promoted conclusion needs checkable evidence.

## Use it

Ask an agent to read [SKILL.md](SKILL.md) with the puzzle's original material and your desired hint/spoiler level:

```text
Use Metis to make progress on this puzzle.
Preserve uncertain observations, develop clue-grounded mechanisms,
choose a useful next action, and verify the result.
```

The core is about 1,500 words. It loads references selectively instead of requiring every puzzle to follow a long checklist. Explicit, easy puzzles can be solved directly.

Metis supplies strategy. [Polya](https://github.com/Amal-David/polya) is an optional source of bounded computation and execution records; Metis also works with ordinary inspection, scripts or other suitable tools.

## Knowledge base

| Resource | Current scope |
| --- | --- |
| [Generation moves](references/hypothesis-operators.md) | Nine ways to develop a new interpretation, with triggers and failure boundaries |
| [Mechanism atlas](references/mechanism-atlas.md) | 18 conditional mechanism entries: what to notice, what to try, and when transfer fails |
| [Worked contrasts](references/contrast-examples.md) | Eight original teaching examples distinguishing a useful move from its misuse |
| [Source cards](references/cases.json) | 29 compact cards from 29 primary URLs |
| [Research evidence](references/research-sources.md) | Nine paper entries and two benchmark entries, with claim limits |
| [Experiment guidance](references/experiments.md) | Measurement uncertainty, controls, finite search and verification |
| [Corpus audit](references/corpus-audit.md) | Source inspection register, corrections, counts and missing discovery history |

The source cards cover **25 named puzzle designs, two reusable game families, and two guides**. They include 16 official solutions, seven solver retrospectives and six constructor accounts. They are not 29 independent discovery traces and are not a completed 1,000-case review.

Unknown triggers and failed attempts remain unknown. A proposed curator experiment is explicitly separate from a test reported by a source. [Sources and limitations](references/sources.md) explains the counting and provenance.

## Retrieve structural analogies

```bash
python scripts/retrieve_cases.py "example orientation ordering" --limit 3
python scripts/retrieve_cases.py "folding faces physical representation" --limit 3
python scripts/retrieve_cases.py "graph connectivity" --exclude-puzzle game-net-tatham
python scripts/retrieve_cases.py --stats
python scripts/retrieve_cases.py --validate
```

The retriever works offline and indexes structural cues, tags and mechanism families, not titles or solution prose. It preserves provenance, diversifies families and deduplicates sources and original puzzles. Repeated `--exclude-family`, `--exclude-puzzle` and `--exclude-source` flags help keep related material out. A no-match or unusable analogy is an acceptable result.

Returned cards can still contain solution mechanisms. Exclusions do not guarantee freedom from prior knowledge. Retrieve after an independent first look and explain both the mapping and its mismatch.

## Audit and evaluation

See [the audit report](docs/audit-2026-11-19.md) for findings, repairs and observed results. The [evaluation directory](evaluation/) preserves raw tasks, frozen rubrics, exact checkers, delivered prompts, responses and assessment. Answer files are evaluator material; exclude them from solver contexts.

The initial six small checks in the design conversation were passed by both ordinary and skill-guided agents. The new twelve-task diagnostic produced 12/12 correct results in each of three fresh arms: baseline, core only, and core with knowledge resources. Both arms also passed all three open-ended action scenarios. No general performance advantage was demonstrated; one full-package response supplied a more explicit rival-separating test. These are diagnostic/development checks, not a general creativity benchmark. Do not infer a speedup or general solving advantage from package validation or a ceiling result.

Publishing the tasks makes them development fixtures. Future improvement claims require a new held-out set, repeated trials, recorded model/settings and adequate cost measurement. See [evaluation guidance](references/evaluation.md) and [the research protocol](references/research-protocol.md).

## Validate changes

```bash
python -m unittest discover -s tests -v
python scripts/retrieve_cases.py --validate
python scripts/validate_package.py
python evaluation/private/checkers.py
```

The package manifest fingerprints 13 authored reasoning, knowledge and retrieval files. It can compare an installed copy:

```bash
python scripts/validate_package.py --against /path/to/installed/metis
```

After reviewing intentional runtime edits, refresh with `python scripts/validate_package.py --write-manifest`. Platform-managed UI metadata and repository evaluation tooling are outside that content comparison.

This audited revision reconciles the original installed skill and the GitHub reconstruction into the same authored package. It preserves original source breadth, corrects reconstructed claims, and adds concrete exploration and knowledge-acquisition guidance.
