# Nine hypothesis-generation moves

These are **launchpads for invention**, not a checklist or a finite set of puzzle types. Independently inspect the artifact before retrieval. Select a move because an observation calls for it, then explore what the new view makes visible. Develop a risky prediction once a mechanism is concrete. An exploratory action can be valuable before rivals have predictions; state what it could teach and how you will use the result.

## 1. Role reassignment

**Trigger:** A conspicuous object seems out of place, or a category-based extraction stagnates.

**Move:** Reclassify a clue from content to **instruction, exemplar, origin, delimiter, compass, parity check, key, or output verifier**. Ask what it *does* rather than what it *names*.

**Seed:** Key and open lock might teach association/direction rather than encode KEY/LOCK.

**Test:** Freeze an operational rule and see if it explains independent pairs and fails natural control anchors. **Failure:** the move fits anything after choosing enough parameters.

## 2. Representation shift

**Trigger:** Familiar units hide constraints.

**Move:** Change the primitive: tiles→edges, words→morphemes, locations→distances/ranks, diagram→graph, visual layout→permutation, symbols→typed relationships.

**Seed:** In Simon Tatham's Net solver, tracking definite/forbidden **edges** as well as uncertain tile orientations exposes deductions unavailable in tile-only reasoning.

**Test:** Derive a new constraint or prediction that could not be expressed economically in the old state; round-trip to original artifact. **Failure:** representation destroys relevant data.

## 3. Structural analogy

**Trigger:** A center, cycle, hierarchy, repeated state transition or nested object resembles a known structure.

**Move:** Transfer an exact relation, not surface appearance: graph isomorphism, cyclic order, matching, folding, finite-state transition, recurrence.

**Seed:** Clock-face order suggests cyclic indexing, but without a distinguished start/direction the model has extra degrees of freedom.

**Test:** List correspondence and where it breaks. **Failure:** recognition supplies no prediction.

## 4. Constructor inversion

**Trigger:** A rule seems too hard to infer, or an odd redundancy looks intentional.

**Move:** Ask what the author needed to make the puzzle discoverable and unambiguous: orientation marks, calibration mini-instance, checksum, constraints preventing shortcut extraction.

**Seed:** A constructor may add numeric counts to confirm a guessed rule set rather than assist the underlying logic grid.

**Test:** Predict the purpose of multiple design details; compare against accidental-detail/null explanation. **Failure:** imagined intent becomes a fact.

## 5. Calibration via tiny controlled changes

**Trigger:** The puzzle permits interactive responses or contains a worked example.

**Move:** Modify exactly one dimension at a time, then compare output deltas. Construct discriminating pairs.

**Seed:** A word-distance game can reveal hidden rules through a short practice round.

**Test:** New minimal pairs distinguish edit distance, letter classes and positional effects. **Failure:** uncontrolled multiple changes or response noise.

## 6. Invariants before search

**Trigger:** Combinatorial search balloons or the board seems impossible.

**Move:** Check parity, degree sum, connectedness, color classes, conservation laws, reachable components, order, bounding boxes or divisibility.

**Seed:** A tiling can fail a coloring/parity invariant even if no easy construction is visible.

**Test:** Prove invariant over allowed moves; construct a counterexample to an invalid invariant. **Failure:** invariant relies on an unstated rule.

## 7. Assumption inversion

**Trigger:** Every method gets blocked by the same invisible rule.

**Move:** Distinguish textual constraints from conventions (must all clues be used once? must a grid be square? must the whole assignment be unique? must objects be read by name?).

**Seed:** Sometimes the requested answer is unique even though many full arrangements satisfy the constraints.

**Test:** Solve under both conventions or seek an input separating them. **Failure:** relaxing an actually explicit rule.

## 8. Cross-channel triangulation

**Trigger:** The artifact combines geometry, wording, sound, typography, count or metadata.

**Move:** Extract constraints from different channels and let them constrain each other while preserving alternative readings. Seek one mechanism satisfying both. Joint fitting is legitimate discovery; it is not independent validation. Do not invent a hybrid solely to patch a contradiction.

**Seed:** A geometric pairing rule may predict both coarse symbol families and fine variants.

**Test:** Recheck earlier constraints after each exchange. When B is genuinely untouched, freeze a rule from A and predict B; otherwise report a retrospective consistency check. **Failure:** jointly optimized channels are called independent, or a guessed label becomes an unquestioned premise.

## 9. Residual inversion

**Trigger:** A rule works mostly but leaves structured error, missing clues or a peculiar tail.

**Move:** Treat the leftover as data: is there a second pass, exception class, orientation flip, wrong initial representation, or distractor?

**Seed:** If all but one item match a transform, the exception may reveal a mistaken glyph reading or an omitted operation.

**Test:** Preserve the complete residual, including negative cases; compare alternative models with fewer special exceptions. **Failure:** cherry-pick only residuals that spell a word.

## Generating a *new* move

Do not stop at these nine. Define a new move when a puzzle demands it:

1. Name the **source observation** that made the move plausible.
2. Specify the **change in object, relation, or allowable operation**.
3. Show the **new consequences** made visible by that change.
4. If the mechanism is concrete, identify a rival and falsifier. If it is a rough seed, choose a cheap exploration that could make it concrete; do not invent precision.
5. Retain a short case note if it transfers across unrelated puzzles.

Avoid rewarding the appearance of novelty alone. Novelty is useful only when it changes what can be tested.
