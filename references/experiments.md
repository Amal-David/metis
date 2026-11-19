# Designing informative puzzle experiments

## Contents

- Hypotheses and tests
- Holdouts and controls
- Geometry and formal models
- Stopping and handoff

## Hypotheses and tests

Generate ideas freely, then formalize the promising ones. Keep brief records of observations, uncertain readings, representation, operation, fitted choices, prediction, rival, test, actual result, and next decision. A proposed experiment is not an executed one.

A good test makes plausible explanations disagree. If one rule requires increasing values and another consecutive increasing values, another consecutive example teaches little. A nonconsecutive increasing example separates them. Seek discrimination, which can come from positive or negative results.

Favor low-cost tests with reliable measurements and consequences that split the surviving mechanisms. If predictions and probabilities are unavailable, state a qualitative ranking; do not invent information-gain scores. Use a small toy to learn a rule or check code, then verify the actual artifact.

Distinguish:
- Contradiction with an accurately observed explicit condition: reject that version.
- Approximate mismatch with an uncertain reading: recheck or retain uncertainty.
- Program crash, resource limit, or unsupported model: inconclusive.
- Complete finite enumeration: a result only for that model and its domains.
- A satisfying witness: validity, with uniqueness still a separate question.

## Holdouts and controls

Reserve instances, relations, or fine details before choosing a mechanism. Record adjustable choices: origin, direction, ordering, grouping, thresholds, alphabet, and exceptions. Freeze them before revealing held-out evidence.

Masking already-seen information is a consistency check, not a blind test. Swapping training and test halves after tuning on both does not restore independence. Keep dependent units, such as paired glyphs and instances from one template, together. Distinguish an unseen instance of a familiar mechanism from discovery of a new mechanism family.

Controls should challenge the relationship claimed. If an anchor allegedly determines a pairing, compare similarly plausible anchors while holding other choices fixed. If geometry is the claim, randomizing labels tests a different question from randomizing positions. An arbitrary broken input is a weak control.

When searching many transformations, compare the selected best result with the best results from the same entire search on null data. Post-selection success rates and tiny per-test probabilities are not automatically valid evidence. Do not invent a p-value without a defensible null model and actual calculation.

## Geometry and formal models

Preserve original image dimensions and measurement provenance. Record coordinate uncertainty. Check whether rankings, orientations, or pairings survive plausible perturbations. A unique ranking on rounded coordinates may disappear under measurement error. A measured margin is more informative than “no ties” from one transcription.

Separate pixels from segmentation, identity, graph construction, and interpretation. Two implementations can agree on a mistaken transcription. Recheck critical relationships against the original, preferably through another measurement method.

For discrete logic, specify domains and every clue. Enumerate small models when feasible. Check the requested answer projection: several full models may agree on the requested answer. A single witness cannot establish uniqueness. For geometric impossibility, define transforms and tolerances; give an invariant, exhaustive argument, or clearly scoped numerical result.

## Stopping and handoff

After several uninformative tests, ask what observation is missing rather than expanding arbitrary parameters. If a mechanism seems right but extraction fails, audit the boundary between layers: identification, ordering, indexing, orientation, or answer format.

Persist originals, observations, rejected test identities, surviving hypotheses, exact evidence, unresolved anomalies, and the next separating question. Keep speculative narratives out of the initial packet for an independent proposer.

Report supported intermediate mechanisms as intermediate. End with a checked answer, a precise ambiguity, or the strongest hypothesis and its next useful test. Do not repeat rejected experiments without changed evidence.
