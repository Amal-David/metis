# Evaluator-only rubric

Freeze this rubric before inspecting model responses. Assess visible conclusions, evidence, tests, and plans; do not request or score private chain of thought. The checkers independently verify golds, not unrestricted model prose. Keep these scores separate; do not invent a weighted composite after seeing results.

## Dimensions

**Final correctness, all items, 0–2:** 2 means complete correct requested result; 1 means substantive correct partial work with a material omission; 0 means wrong or absent. Proved impossibility, exhaustive ambiguity, and a valid query plan are full answers where requested. Q01/Q02 are conditional induction: the gold mechanism is a simple intended explanation, not a logically forced unrestricted rule. Another genuinely simple mechanism that fits every observation and produces a correctly derived prediction must receive appropriate correctness credit; record it separately. A lookup table with an arbitrary new entry is an ambiguity witness, not evidence of explanatory simplicity. The assessor's simplicity judgment is a limitation and should be exposed if it affects ranking.

**Target mechanism identification, Q01–Q04/Q06–Q08/Q12, 0–2:** 2 identifies and correctly applies the registered representation or invariant; 1 identifies it but applies it incompletely; 0 absent/wrong. Q03 is geometric transfer, not perception or unconstrained discovery. A legitimate alternative rule can earn correctness without earning the intended-mechanism score; report that distinction.

**Meaningful alternatives, Q01–Q05/Q07–Q09, 0–2:** 2 retains or rules out the materially different candidates needed for the task, including all required ambiguity; 1 has a relevant but incomplete alternative comparison; 0 lists paraphrases, irrelevant possibilities, or misses a required alternative. Proof excluding a whole family counts. More hypotheses is not automatically better.

**Discriminating test, Q01/Q02/Q04/Q05/Q07–Q09, 0–2:** 2 executes or specifies a valid check/query with relevant different predicted outcomes, or a complete finite verification; 1 relevant but incomplete/nondiscriminating; 0 invalid/absent. A proof can be decisive without a tool call. Q09 earns planning credit only; do not label a planned oracle test as executed.

**Calibration, all items, 0–2:** 2 matches status/certainty to evidence, without invented execution; 1 correct conclusion with an overstated uniqueness/verification claim; 0 claims a wrong result solved, asserts false uniqueness, or fabricates checking. Conclusive simple answers need no generic hedging. Q05 may be SOLVED if it establishes the complete two-code set. Q09 should use PLAN or explicitly distinguish the solved planning question from the unknown hidden state.

**Response cost:** collect words/characters and measured tokens, calls, execution time, wall time, retries/resets, retrieval calls, and delivered input size where available. Missing measurements are unavailable. Compare Q10/Q11 particularly for needless response cost. Do not mistake verbosity for cognition, and do not use unrecorded efficiency impressions as results.

## Item-specific checks

| Item | Full result and supporting evidence | Distinguishing evidence / key error |
|---|---|---|
| Q01 | Intended model counts exposed unit sides: 14; six cells, five shared sides; all five examples fit; finite examples do not force an unrestricted rule | Same four-tile area has outputs 8,10,16. A 3-by-3 hollow ring separates all exposed boundaries (16) from outer boundary alone (12); neither model is excluded by the original examples. |
| Q02 | Intended model counts state changes at fixed segment positions: 5, split 4 and 1; all examples fit; rule is not unrestrictedly unique | 12→21 rules out total numerical distance, changed digit count, and absolute net change in total lit segments. Do not call a fitted model logically unique. |
| Q03 | Reflection across the vertical midline; (0.80,0.35); no rotation alone | Every corner must match. A one-corner match is insufficient; chirality/orientation changes. |
| Q04 | Only swaps (1,2),(2,3),(3,4); distance 4; valid four-swap witness | Unit readings force three edges; each nonadjacent swap would make its corresponding observed 3/3/5 reading equal to 1. Exact checker enumerates 64 graphs. |
| Q05 | Exactly 143 and 325; a yes/no digit question splitting them, e.g. whether B=4 | The note's uniqueness claim is false. No invented digit-distinctness or leading-zero assumptions. |
| Q06 | No path; 12 cells imply 11 color-flipping moves, but both endpoints have the same checkerboard color | Local path-search failure alone is not proof; exhaustive enumeration or parity is. |
| Q07 | Hidden digit 1; row 3 digit 4 changes from 8 to 9; each repaired row satisfies both equations; no other correction | Do not alter the rules to fit a transcription error. Checker enumerates all 100 valid digit rows and all one-error repairs. |
| Q08 | 2242/4096 = 1121/2048; scans nine overlapping windows for either 0000 or 1111 | 1/16 assesses one specified pattern at one specified window, not the actual post-selection rule. Overlapping windows are dependent. |
| Q09 | First A/B/C; correct four-state sets for either reply; query the remaining bits; worst case 3 | D leaves seven candidates in one branch, which two binary replies cannot distinguish. No observed reply or state exists. |
| Q10 | x=7 | Concise direct solution is enough. |
| Q11 | Box A; truth values false,true,false | Check all three signs under the same candidate. |
| Q12 | Any totals 13 and 14; optimum difference 1 because the total is 27 and hence cannot split evenly | An achieved grouping needs a lower bound for optimality; no exhaustive search is necessary. |

False finalization means an unqualified completed claim with an incorrect or unsupported answer. On Q01/Q02, a conditional prediction under a fitting model is not false finalization merely because an unrestricted rule is nonunique; a claim that the examples prove a unique unrestricted rule is a calibration error. Record invented tool execution separately from ordinary mathematical mistakes.
