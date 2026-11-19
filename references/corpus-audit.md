# Practitioner corpus audit

Audit date: **2026-11-19**. Canonical data: [cases.json](cases.json), schema version 2.

## Result and counting rules

The canonical collection contains **29 cards from 29 distinct primary source URLs**. Its **27 non-null puzzle identifiers** comprise **25 named puzzle designs and two reusable game families**, Net and Mines. The other **two cards are general guides** and have `puzzle_id: null`. Net and Mines are not particular generated instances. A source page, a card, a puzzle design, and a solver trial are different units.

| Collection | Cards | Distinct source URLs | Interpretation |
| --- | ---: | ---: | --- |
| Original installed JSONL collection | 21 | 21 | Broad starting collection; some entries mixed events from several puzzles. |
| Proposed Metis checkout | 21 | 11 | Repeated lessons from Net, CRUMS, and other shared sources had displaced original breadth. |
| Audited canonical collection | 29 | 29 | All 21 original URLs retained; six CRUMS pages, Mines, and one previously listed practitioner account added. |

There are no repeated non-null puzzle identifiers. This is a manual identity audit, not proof of statistical independence: shared hunts, authors, mechanisms, and feeder dependencies remain. There are **16 official-solution cards, seven solver-retrospective cards, and six constructor-note cards**, organized under **12 mechanism-family labels**. Labels support retrieval and exclusion; they do not establish contamination-free splits.

## What was inspected

The local comparison covered the proposed `AGENTS.md`, `references/cases.json`, and `references/source-notes.md`, plus the installed skill, `cases-hunt.jsonl`, `cases-solver.jsonl`, and `sources.md`. Every retained card was checked against the relevant primary-source passages on the audit date. The five additional practitioner references in the original `sources.md` were also inspected in the limited scopes listed below. One became a new card, yielding **33 distinct practitioner source URLs inspected overall**; four remain contextual references.

Several Galactic solution pages could not be opened through the search interface, although direct retrieval returned their original pages successfully. The large CRUMS flag-solution PDF was likewise inspected through direct PDF text extraction after the search interface rejected its size. These access failures were not treated as evidence against the sources. Text inspection does not amount to independently identifying every image, replaying every animation, checking every crossing, or proving every solution. Each card states its actual reading scope.

This report covers practitioner case provenance. Research-paper and benchmark claims belong to the separate research audit. No benchmark task was inspected or used to construct these cards, and no unspoiled puzzle-solving experiment was performed as part of this source audit.

## Corrections and consolidation

### CRUMS reconstruction

The sources are genuine, and their central mechanisms and cited construction changes are supported. Three character associations had been substituted for actual puzzle titles:

| Source | Reconstructed label | Correct puzzle title |
| --- | --- | --- |
| [Solution 2](https://crumspuzzlehunt.com/solutions/2) | Col. Mustard | /r/vexillologygreatcirclejerk |
| [Solution 3](https://crumspuzzlehunt.com/solutions/3) | Mrs. White | Mixed Drinks |
| [Solution 6](https://crumspuzzlehunt.com/solutions/6) | Professor Plum | Inflation |

The flag card now specifies capital-to-capital routes and small regions formed by near-intersections; it does not assert exact triple intersections. For Inflation, the construction account places the crossword idea before the coin motif. The coin is presentation motivation, not the reported source of the initial idea. Spaghetti Stack’s termination device and branch revision are documented constructor events. Accusation’s split after a shortcut is also documented, but a successful shortcut does not establish the intended preceding mechanism. These facts are kept within one card per puzzle.

### Other provenance repairs

- **Merged duplicate teaching cards:** five Net cards became one; separate Word Search II distance/calibration cards became one; Mixed Drinks, Spaghetti Stack, Accusation, and Chen’s combined-loop puzzle likewise have one focused card each. Distinct lessons remain in the summaries and tags without increasing puzzle counts.
- **Official explanation versus discovery history:** suggested footholds in published solutions are no longer presented as actual solver breakthroughs. Published diagnostics are explicitly described as recommendations, examples, or arguments. Constructor events within solution pages are labeled as constructor accounts.
- **Word Search II:** the mechanism is specified as crossed sums of vowel/consonant edit distances, removing the earlier vague reconstruction of a generic distance rule.
- **Net:** partial edge certainty, the exceptional two-square board, and the distinction between implemented deductions and unimplemented parity are preserved together.
- **bENDs:** the reported trigger is frustration with physical manipulation; the source also documents a replaced coordinate representation and incomplete geometric validation. Readable extraction does not erase that limitation.
- **Guide evidence:** Berlin’s illustrative flavor-text failures are not recorded as a specific historical false start. Both general guides use null puzzle identifiers and null event fields where no particular event is reported.
- **Mixed retrospective scopes:** the invitation card is limited to Engagements and other Crimes; an unrelated puzzle’s mistaken dependency assumption was removed from its false-start field. Crossed Out does not inherit the author’s unrelated early-draft failures. Chen’s card focuses on Black or White or Moon or Sun, with its introductory feeder only as context; unrelated visual-artifact remarks are not attributed to this puzzle.
- **Mines:** classified as constructor notes. Its useful contribution is the final replay after perturbations, not an invented solver breakthrough.
- **The Legend:** added from the already listed Irpan account because it documents recursive coordinates and distinguishes unfinished uniqueness checks from the final checked fill. A timeout is not a refutation.

No original source URL was dropped. Source content outside the stated scopes was omitted rather than turned into additional cards. The original JSONL files are baseline provenance material, not extra cases to add to canonical counts.

## Field semantics and missing evidence

`observed` and `representation_shift` summarize what the source reports or demonstrates; they do not imply that this audit independently observed an unspoiled solve. `documented_trigger` records an explicitly reported solver or constructor event, with the actor distinguished. A null value means that the card does not have a reported event in its chosen scope, not that the event never happened.

`documented_test` can describe a reported run or a diagnostic demonstrated or recommended by an official explanation. The wording distinguishes them. It must not be counted as a set of trials conducted by the curator. `documented_false_start` includes reported discarded prototypes, unsuccessful representations, and posted-answer corrections; it is not automatically a falsified mechanism hypothesis.

| Field | Present | Null |
| --- | ---: | ---: |
| documented_trigger | 12 | 17 |
| documented_test | 23 | 6 |
| documented_false_start | 10 | 19 |

Of the 12 trigger fields, **five** are in solver retrospectives, **three** in constructor-note cards, and **four** explicitly describe constructor events embedded in official solution pages. The seven solver-retrospective cards are not seven complete discovery logs. The two remaining solver retrospectives have no reported initial trigger in their retained scope.

Every `suggested_test` is labeled `origin: curator_proposal`. None was executed in this audit. Transfer conditions, failure conditions, retrieval cues, and lessons are curatorial guidance. Retrieval cues describe structures rather than final answers. `review_status: source_checked` means the cited material was actually inspected within `scope_read`; schema validation only checks that this provenance claim is represented consistently.

## Coverage and limits

The collection is still small and deliberately selective. Official hunt explanations dominate: ten come from Galactic Puzzle Hunt, including eight from its 2019 event, and six come from one CRUMS hunt. The corpus is weighted toward English-language hunt communities, wordplay, grids, and accessible written retrospectives. It underrepresents other languages, mechanical puzzles, extensive observational traces, failed unsolved work, and diverse solver populations. Official sources select successful finished mechanisms; retrospective accounts compress or omit intermediate work.

No thousand-case claim is supported. No speed, creativity, reliability, transfer, or training gain follows from this audit. All indexed cases are development material; analogies, rewordings, and close variants require exclusion or explicit overlap handling in later evaluations. A unique URL is not an independent mechanism or solver.

The package contains compact original paraphrases and source links, not mirrored source pages or diagrams. Public access has not been treated as a license to redistribute full works or as clearance for model training. At authoring, the largest card had 198 words across all string values; the largest total across source-facing fields was 107 words. These are size checks, not legal determinations.

## Source inspection register

All rows below were source-checked on **2026-11-19**. Reading a solution is distinct from independently verifying its puzzle.

| Card | Source kind | Primary source and inspected scope |
| --- | --- | --- |
| `hunt-petroglyph` | `official_solution` | [Petroglyph — official solution](https://2023.galacticpuzzlehunt.com/solution/petroglyph) — Complete short solution text; described diagram, not an independent reconstruction. |
| `hunt-word-search-ii` | `official_solution` | [Word Search II — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/word-search-ii.html) — Complete solution text and author notes. |
| `hunt-something-is-off` | `official_solution` | [Something Is Off — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/something-is-off/solution.pdf) — Text of all eight PDF pages; solutions and construction notes, without independently resolving the diagrams. |
| `hunt-colors` | `official_solution` | [Colors — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/colors.html) — Complete solution text and construction notes; exact color values supplied by the source. |
| `hunt-line-plots` | `official_solution` | [Line Plots — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/line-plots.html) — Complete solution text and author notes; graphs not independently reconstructed. |
| `hunt-cuspidation` | `official_solution` | [Cuspidation — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/cuspidation.html) — Complete textual mechanism and construction notes; animations not replayed. |
| `hunt-ministry-word-searches` | `official_solution` | [Ministry of Word Searches — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/ministry-of-word-searches.html) — Main solution and author notes through generator reconstruction; appendix not reviewed. |
| `hunt-make-your-own-crossword` | `official_solution` | [Make Your Own Crossword — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/make-your-own-crossword.html) — Complete solution text, example input/output grids, and author notes. |
| `hunt-holistic` | `official_solution` | [Holistic — official solution and author notes](https://2019.galacticpuzzlehunt.com/solution/holistic.html) — Complete solution text; invariant arguments in questions 4 and 8 inspected, move strings not independently executed. |
| `hunt-beige-flags` | `official_solution` | [Beige Flags — official solution](https://2023.galacticpuzzlehunt.com/solution/beige_flags) — Mechanism explanation and solution table; original flag images not independently identified. |
| `solver-net-tatham` | `solver_retrospective` | [Writing a solver for Net](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/net-solver/) — Complete essay, including local domains, loop avoidance, reachability bounds, and unimplemented parity. |
| `constructor-tatham-generation` | `constructor_notes` | [How to write a new puzzle](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/devel/writing.html) — Sections 6.1 and 6.2.1 on fairness, observational equivalence, and generation; implementation sections excluded. |
| `solver-bends-phenomist` | `solver_retrospective` | [Solving bENDs](https://phenomist.wordpress.com/2021/06/12/solving-bends-password-protected-due-to-spoilers/) — Physical attempt, input model, coordinate representation, pruning, and incomplete-verification sections. |
| `constructor-chen-loop-fusion` | `constructor_notes` | [Teammate Hunt 2025 Author Notes — Black or White or Moon or Sun](https://blog.evanchen.cc/tmh-2025/) — Combined-loop puzzle’s high-level and low-level design sections, including its introductory feeder context. |
| `constructor-berlin-testsolvers` | `constructor_notes` | [Advice To The Puzzlers](https://www.ericberlin.com/2022/01/23/advice-to-the-puzzlers/) — Believe the testsolvers section; surrounding hunt-management advice excluded. |
| `constructor-cjq-operative-semantics` | `constructor_notes` | [Two hundred puzzles, fifty weeks later — Crossed Out](https://mitadmissions.org/blogs/entry/two-hundred-puzzles-2/) — Crossed Out account in group writing sessions; general theme/mechanism discussion also inspected. |
| `solver-rubio-sudoku-poetry` | `solver_retrospective` | [Sudoku as Poetry: A Tag-Fusion Masterpiece — Rubio’s answer](https://puzzling.stackexchange.com/questions/45548/sudoku-as-poetry-a-tag-fusion-masterpiece) — Answer’s solving account and author follow-up comments; completed grid not independently verified. |
| `solver-quarkle-ternary` | `solver_retrospective` | [When math and english collide! — quarkle’s answer](https://puzzling.stackexchange.com/questions/44924/when-math-and-english-collide) — Accepted answer and visible segmentation discussion. |
| `solver-triangular-rule` | `solver_retrospective` | [Find out the rule, then solve it — Beastly Gerbil’s answer](https://puzzling.stackexchange.com/questions/51541/find-out-the-rule-then-solve-it/51544) — Solver’s rule, arithmetic checks, short solving account, and orientation clarification in comments. |
| `solver-word-grid-diagonal` | `solver_retrospective` | [What goes in the diagonal? — answer and corrections](https://puzzling.stackexchange.com/questions/139692/what-goes-in-the-diagonal) — Posted answer and author/commenter corrections; original image constraints not independently recomputed. |
| `solver-phenomist-2025` | `solver_retrospective` | [2025 MIT Mystery Hunt — Engagements and other Crimes](https://phenomist.wordpress.com/2025/01/23/2025-mit-mystery-hunt/) — Invitation-puzzle paragraph; neighboring puzzle comments inspected only to separate their events. |
| `hunt-crums-great-circle` | `official_solution` | [/r/vexillologygreatcirclejerk — official solution and construction notes](https://crumspuzzlehunt.com/solutions/2) — Text of all three PDF pages, including route instructions and construction notes; maps not independently replotted. |
| `hunt-crums-mixed-drinks` | `official_solution` | [Mixed Drinks — official solution and construction notes](https://crumspuzzlehunt.com/solutions/3) — Solution explanation and opening construction notes; grid fills not independently checked. |
| `hunt-crums-spaghetti-stack` | `official_solution` | [Spaghetti Stack — official solution and construction notes](https://crumspuzzlehunt.com/solutions/4) — Mechanism paragraph and construction notes on both PDF pages; full tree labels not independently solved. |
| `hunt-crums-inflation` | `official_solution` | [Inflation — official solution and construction notes](https://crumspuzzlehunt.com/solutions/6) — Text of all three PDF pages, including the coin motivation, inserted crossword, bond clues, and construction history. |
| `hunt-crums-locked-room-murder` | `official_solution` | [Locked Room Murder — official solution and construction notes](https://crumspuzzlehunt.com/solutions/7) — Timeline introduction, selected testimony rows, contradiction/extraction explanation, and construction opening. |
| `hunt-crums-accusation` | `official_solution` | [Accusation — official solution and construction notes](https://crumspuzzlehunt.com/solutions/8) — Complete one-page PDF. |
| `constructor-mines-tatham` | `constructor_notes` | [Writing a soluble-grid generator for Mines](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/mines-solver/) — Complete essay on solver-guided perturbation and the final checking pass. |
| `constructor-irpan-the-legend` | `constructor_notes` | [Writing MIT Mystery Hunt 2023 — The Legend](https://www.alexirpan.com/2023/04/21/mh-2023.html) — The Legend subsection, including recursive coordinates, timed-out checks, testsolving, and final fill selection. |

## Additional practitioner references

| Primary source | Inspected scope | Treatment |
| --- | --- | --- |
| [Allen Rabinovich, Thinking About A Puzzle](https://web.mit.edu/activities/puzzle/resources/thinkingaboutpuzzles.html) | Opening definition; medium, data, structure, and unused-information advice. | Contextual guidance; no additional puzzle case inferred. |
| [Jay Lorch, How to Write a Fun Puzzle](https://s3.amazonaws.com/jaylorch.us/puzzles/HowToWriteAFunPuzzle.pdf) | Abstract and excerpts on hooks, solvability, and confirming intermediate progress. | Contextual construction guidance; no completed test inferred from a recommendation. |
| [Brian Chen, Introduction to Puzzlehunts](https://blog.vero.site/post/puzzlehunts) | Common features and selected extraction definitions. | Contextual genre vocabulary, not an exhaustive mechanism inventory. |
| [Suggestions for Running a Puzzlehunt](https://github.com/fortenforge/suggestions-for-running-a-puzzlehunt) | Testsolving, solution writing, and factchecking sections. | Contextual guidance; explains why a polished solution path need not be a discovery transcript. |
| [Alex Irpan, Writing MIT Mystery Hunt 2023](https://www.alexirpan.com/2023/04/21/mh-2023.html) | Introductory construction context and the complete The Legend subsection. | One focused constructor card; not an additional guide card or a complete review of the long retrospective. |

## Validation

The canonical retriever’s `--validate` command returned `status: valid` for all 29 cards. Its `--stats` output agrees with the counts above. Additional count checks found no lost original source URLs and no duplicate non-null puzzle identifiers. These checks verify schema and counting, not source truth or solving ability.

Canonical `cases.json` SHA-256 at this audit: `eae909c8e57a487ffe104c94e39366ef6944d70cc7a8abc2242d43092f8ff143`.
