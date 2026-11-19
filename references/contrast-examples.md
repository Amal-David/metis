# Worked contrasts: develop the idea, then check it

These eight examples are **curator-authored teaching constructions**. They are not historical solver traces, benchmarks, or evidence that Metis improves performance. They contrast a promising move with its tempting misuse.

## Contents

1. Exploration before a mechanism
2. A useful query versus confirmation
3. Unique answer versus unique arrangement
4. New representation versus renamed guess
5. Measurement precision versus uniqueness
6. Joint inference versus validation
7. Selected success versus search evidence
8. Failed computation versus false hypothesis

## 1. Exploration before a mechanism

**Situation:** Two transparent sheets each contain scattered partial strokes and the same three registration marks. Neither is readable.

**Temptation:** “Transparency means overlay; therefore the message is solved.” Material suggests an action, not its outcome.

**Action:** Align copies using the registration marks. State the learning goal: determine whether strokes have complementary boundaries. A predicted word is unnecessary before looking.

**Update:** If many strokes complete under one alignment, develop an overlay mechanism and test remaining marks. If only one letter-like shape appears, retain weak evidence or abandon that alignment. Check whether another alignment works equally well.

**Transfer:** Exploration earns a mechanism to test, not a retroactive claim that its output was predicted.

## 2. A query that separates rules

**Situation:** An oracle maps `(2,2)→4` and `(5,5)→10`. Live candidates are `x+y` and `2x`.

**Temptation:** Query `(7,7)`. Both predict 14, leaving the ambiguity intact.

**Action:** Query `(2,3)`: the candidates predict 5 and 4. Declare these responses first.

**Update:** A response of 5 rejects `2x` under this input convention, but does not prove `x+y` is the only possible rule. “Invalid” could reveal a restricted domain.

**Transfer:** A negative example helps because it separates possibilities. Negativity itself is not the goal. If the domain is unknown, first explore it.

## 3. Unique answer without a unique arrangement

**Situation:** Put distinct numbers 1,2,3 in slots P,Q,R. The only clue is `P=2`. The question asks for P.

**Temptation:** Declare the whole puzzle unique after finding `(2,1,3)`, or refuse to answer P because Q and R are unresolved.

**Action:** Enumerate `(2,1,3)` and `(2,3,1)`; project both onto P.

**Result:** P is uniquely 2; the full arrangement has two possibilities.

**Transfer:** Check exactly the quantity asked for. A witness, a unique projection and a unique full state are different claims. A request for all slots remains ambiguous.

## 4. A representation change that exposes constraints

**Situation:** Every letter-indexing attempt needs a different offset. Repeated separators occur inside larger blocks.

**Temptation:** Try more offsets or cipher names while keeping “word” as the primitive unit.

**Action:** Preserve characters and represent boundaries explicitly. Compare parsing by words, repeated separators and larger blocks. Ask which relations become simpler.

**Illustration:** `NOWHERE` can be parsed `NOW HERE` or `NO WHERE`. Spacing, another clue or a consistent cross-row pattern must justify a boundary; the ability to split is insufficient.

**Transfer:** A reframe changes units or relations and yields a consequence. Renaming an arbitrary extraction does not.

## 5. “No ties” can disappear under uncertainty

**Situation:** Lengths are `10.0±0.3` and `10.2±0.3`. A hypothesis sorts them and uses their ranks.

**Temptation:** Sort central estimates and claim a unique order.

**Action:** Preserve intervals `[9.7,10.3]` and `[9.9,10.5]`. Both orders are possible: 10.25 and 10.0 reverse the apparent order while remaining in the intervals.

**Update:** Re-measure, use a larger-margin feature, or propagate both orders. Do not call a rank-dependent extraction robust yet.

**Transfer:** Exact arithmetic on approximate measurements does not make them exact. A tie-free transcription need not imply a stable ordering.

## 6. Joint inference is useful; it is not a holdout

**Situation:** A clue admits `FIR` or `PINE`; a spatial constraint requires four letters.

**Action:** Retain both labels until length selects PINE. Feed it into remaining constraints.

**Temptation:** Claim that length independently confirms PINE after using it to choose PINE.

**Status:** Joint consistency. A genuinely uninspected feature predicted from the frozen assignment could supply a fresh check.

**Transfer:** Let channels help each other during discovery. Record which choices they influenced. Independence is a property of the information flow.

## 7. Search success needs a matching control

**Situation:** After trying many orientations, offsets and dictionaries, one combination returns a word.

**Temptation:** Compare that winner with one arbitrarily broken control and claim strong evidence.

**Action:** Declare the full selection procedure. If a defensible randomized control exists, apply the same search budget and selection rule to each control; compare best results. Preserve all failures and choices.

**Update:** Frequent words under the control weaken the extraction. A rare score supports only what the specified null tests, not automatically author intent or a final solve.

**Transfer:** Search gives more opportunities for luck than one frozen rule. Do not invent probabilities without executing a justified calculation.

## 8. Computation failed; what was learned?

**Situation:** A solver times out after finding one valid assignment. The question asks whether the answer is unique.

**Temptation:** Say “unique” because no second assignment appeared, or “impossible” because search did not finish.

**Action:** Check the witness against original clues. Search for an alternative answer by excluding its answer projection, using complete bounded computation if feasible.

**Update:** A second witness disproves uniqueness. A completed unsatisfiable alternative-search proves uniqueness within the encoded model. Another timeout leaves it unresolved. Exact code can still use a mistaken transcription.

**Transfer:** Match claims to tool guarantees. Failure may motivate a better representation or algorithm; it cannot itself falsify the puzzle hypothesis.

## Practice transfer

Close the example and describe its structural lesson without its objects or answer. Ask where the lesson would fail in the current puzzle. Keep it only if it changes an action or prediction. This learning exercise does not require narrating every thought to the user.
