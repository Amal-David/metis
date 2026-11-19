# Mechanism atlas

Use the observed feature to choose a section. This is conditional background for invention, not a list of mechanisms to try exhaustively. The examples below are original teaching constructions, not source discoveries or evaluation items. For real source-backed cases, retrieve the suggested structural terms; inspect each card's provenance and boundaries.

## Contents

- [Objects and representations](#objects-and-representations): roles, order, symmetry, geometry, topology, layers
- [Actions and encodings](#actions-and-encodings): physical operations, time, symbol systems, language, extraction, coupled channels
- [Rules and systems](#rules-and-systems): oracles, constraints, invariants, generators, metas, residue

## Objects and representations

### 1. Roles, anchors and worked examples

**Consider when:** a related pair, special state or conspicuous object does little as ordinary content. A feature can be an instruction, delimiter, origin, orientation cue, sample mapping, or check.

**Try:** enumerate its possible jobs, then ask what each would let a solver do. A sample pair might fix a permutation or a direction. The useful object is the demonstrated relation, not necessarily either label. One anchor rarely fixes every degree of freedom.

**Boundary:** a compatible story is weak if an equally ordinary object produces the same fit or the rule still needs arbitrary choices. Predict another pair before interpreting it.

**Retrieve:** `exemplar calibration role orientation`.

### 2. Orders, permutations and cycles

**Consider when:** items have two independent orders: position versus size, date versus rank, numeric label versus reading order. A reordering is a permutation; its inverse answers a different question.

**Try:** explicitly write “old position → new position.” Keep item identity separate from its location. A cycle needs a start and a direction; a linear list needs orientation. Equal measurements need a justified tie rule.

**Example:** if items at positions 1,2,3 move to 2,3,1, then the destination list is old 3,1,2. Reading source labels in arrow order is not automatically reading arrivals.

**Boundary:** an attractive word obtained by freely choosing order, start and direction is fitted evidence. Check every item.

**Retrieve:** `ordering ranking permutation`.

### 3. Symmetry, composition and inverse operations

**Consider when:** shapes occur in paired orientations, mirrored text survives, or an operation repeats. Reflections, rotations and translations preserve different relations. Composing operations may reveal a simpler rule.

**Try:** represent a few distinctive points. For a centered coordinate system, a half-turn maps `(x,y) → (-x,-y)`; reflection in the vertical axis maps `(x,y) → (-x,y)`. Their composition is a horizontal reflection. These formulas assume those axes, not arbitrary image pixels.

**Boundary:** one matched point cannot determine a general transform. Test off-axis points, orientation and the full correspondence; preserve the coordinate convention.

**Retrieve:** `reflection rotation orientation symmetry`.

### 4. Metric geometry versus affine geometry

**Consider when:** a grid might be stretched, skewed or photographed at an angle. Distinguish exact lengths/angles from relations such as collinearity, parallelism, midpoint and incidence.

**Try:** specify the allowed transform before fitting it. An affine map preserves midpoints: if `M=(A+B)/2`, then `f(M)=(f(A)+f(B))/2`. A perspective projection need not preserve midpoint ratios. Choose an invariant appropriate to the claimed transform.

**Boundary:** failure under rotation alone does not rule out shear; an affine fit does not justify arbitrary projective warping. Pixel measurements need uncertainty margins.

**Retrieve:** `geometry coordinates invariants measurement`.

### 5. Graphs, edges, regions and connectivity

**Consider when:** objects have ports, paths cross, boundaries repeat, or whole-object choices hide partial certainty.

**Try:** compare tile variables, edge variables and region variables. An uncertain tile orientation can still force an edge present or absent. Ask whether crossings are junctions, overpasses or undecided readings. Propagate local deductions and separately check connectedness, cycles and allowed degrees.

**Boundary:** a locally consistent edge assignment may correspond to no legal tile or may disconnect the whole graph. A representation must round-trip to the original objects.

**Retrieve:** `edges boundary connectivity`.

### 6. Layers, negative space and figure-ground changes

**Consider when:** clutter, holes, repeated outlines, transparent sheets or complementary patterns seem unusually deliberate.

**Try:** separate foreground/background, color channels or overlays on copies. Test whether union, intersection or difference explains repeated structure. For two binary masks, intersection keeps shared marks; exclusive-or keeps marks present in exactly one of the two.

**Boundary:** resampling and compression can invent tiny features. A processed view is derived evidence; verify decisive marks in the original. Do not treat every visual artifact as a clue.

**Retrieve:** `overlap visual channels representation`.

## Actions and encodings

### 7. Folding, cutting and assembly

**Consider when:** matching boundaries, tabs, hinges, repeated corner marks or object affordances suggest a physical operation.

**Try:** build the smallest reversible model, mentally or computationally. Preserve front/back, face normals, layer order and orientation, not just where centers end up. Face-center and orientation variables can be simpler than tracking every corner.

**Boundary:** overlapping centers do not establish a physically possible assembly. Verify adjacency, reversed faces and collisions under the actual allowed actions. Without a usable artifact, propose the experiment rather than claiming to have folded it.

**Retrieve:** `folding faces physical representation`.

### 8. Static diagrams as processes

**Consider when:** arrows, numbered snapshots, tracks or repeated intermediate states suggest time rather than a reading order.

**Try:** define state, transition, event ordering and stopping condition. Simulate two or three steps with one fixed convention. Ask whether arrows describe movement, dependencies, elapsed time, or instructions.

**Boundary:** do not silently change simultaneous events into sequential ones. A timing convention is part of the hypothesis and needs a cue or a distinguishing observation.

**Retrieve:** `timeline state transition motion`.

### 9. Alphabets, bases and exact encodings

**Consider when:** symbols fall into a small set, groups recur at fixed lengths, or original machine-readable values are available.

**Try:** determine the alphabet, grouping, bit/significance order and output range before naming a code. Three distinct states suggest testing a ternary representation; they do not specify which state is 0. A fixed group of five binary positions has 32 possible patterns; usefulness depends on the clue's grouping and an evidenced mapping.

**Boundary:** many alphabets and chunk sizes can manufacture text. Named codes such as Braille, Morse or semaphore require their actual conventions and matching structural cues. Look up the smallest missing convention rather than guessing its table. Use exact source color values only when the artifact preserves them.

**Retrieve:** `base alphabet encoding colors`.

### 10. Language units and resegmentation

**Consider when:** awkward wording, repeated affixes, odd spacing, sound cues or bilingual references resist ordinary definition lookup.

**Try:** compare letters, sounds, syllables, morphemes, word boundaries and meanings. A rebus may encode a spatial relation between words; a spoken clue may preserve pronunciation while changing spelling. Ask which channel the artifact actually privileges.

**Example:** the string `NOWHERE` permits `NOW HERE` and `NO WHERE`; typography or another clue must select the relevant boundary.

**Boundary:** specify language, dialect or pronunciation only when supported. A phonetic resemblance that changes across speakers needs qualification. Do not treat a convenient synonym as fixed before checking other constraints.

**Retrieve:** `segmentation language word boundaries`.

### 11. Extraction and indexing

**Consider when:** a mechanism has produced words, positions or ordered objects but the requested answer is still missing.

**Try:** distinguish identification, ordering, selection and conversion. An index requires a carrier and a numbering convention. Test first/last letters, indicated positions or differences only when the artifact supplies a reason. Record whether numbering starts at zero or one.

**Boundary:** answer length can constrain extraction, but changing synonyms, offsets and reading directions until a phrase appears is not validation. Recheck hard entries, not just the first promising letters.

**Retrieve:** `extraction ordering indexing calibration`.

### 12. Coupled channels and checksums

**Consider when:** a word clue suggests multiple labels while a diagram supplies lengths, positions or counts.

**Try:** maintain sets of possible labels and propagate constraints between channels. A length can remove synonyms; remaining synonyms can constrain an ordering. Treat redundant counts as possible checks rather than assuming each number is an index.

**Boundary:** if both channels chose the model, agreement is joint consistency. A held-out check must not have influenced those choices. A checksum can detect some mistakes without proving uniqueness.

**Retrieve:** `cross channel constraints checksum`.

## Rules and systems

### 13. Interactive rule discovery

**Consider when:** a validator accepts inputs, an interface returns scores, or a worked example can be varied.

**Try:** identify variables and choose minimal pairs or boundary cases. Predict rival responses before a discriminating query. Allow exploratory queries when the response schema is unknown. Include negative examples and check whether history affects responses.

**Example:** “positive even” and “positive multiple of four” both accept 8. Query 6 to distinguish them; 12 is another agreement.

**Boundary:** the interface must permit the query. Noise, hidden state or invalid input may explain a response; distinguish these from a mathematical negative.

**Retrieve:** `oracle calibration controlled changes`.

### 14. Finite constraints and projected uniqueness

**Consider when:** rules specify assignments, relative order, all-different conditions or exact counts.

**Try:** define domains and translate each clue independently. Propagate, enumerate small domains, or use a suitable solver. If asked for one item, compare that projection across all valid models; the rest can vary.

**Boundary:** a witness does not establish uniqueness. Unsatisfiability concerns the supplied encoding; check no clue was added or mistranscribed. Keep “one exists,” “all agree on this answer,” and “one full model” distinct.

**Retrieve:** `constraints uniqueness multiple solutions`.

### 15. Invariants, extremal cases and conservation

**Consider when:** a move changes many details but preserves a count, parity, connectivity or total.

**Try:** prove the property for every allowed move, then compare initial and target states. A domino on a checkerboard covers one square of each color; unequal color counts prevent a tiling. Equal counts alone do not guarantee one. An extremal object (largest, smallest, boundary-most) may have fewer possible relations.

**Boundary:** conservation may be only necessary. A new allowed move can destroy an invariant. Failure to find a construction is not a proof.

**Retrieve:** `invariants parity conservation boundary`.

### 16. Repeated outputs and hidden generators

**Consider when:** many instances share a template, data wraps around boundaries, or refreshing changes content without changing structure.

**Try:** compare stable fields, periods, priority rules and state. Infer the generator rather than solving each output independently. Contrast row-wise with column-wise traversal, or ordinary with wrapped adjacency.

**Boundary:** template instances are dependent evidence. A rule from one generation mode may fail after a mode change. Do not count near duplicates as independent confirmation.

**Retrieve:** `generator periodicity repeated instances`.

### 17. Meta puzzles and answers used as data

**Consider when:** earlier answers, categories or subpuzzle outputs are explicitly supplied as new inputs.

**Try:** ask what survives beyond spelling: lengths, meanings, positions, provenance or relations between answers. Determine whether the meta uses the whole set, groups or a cross-group constraint. Feed corrected subanswers through later steps.

**Boundary:** missing feeder inputs can block a meta. A shortcut can be valid even if it bypasses the intended route; check the stated task rather than forcing a historical solution path.

**Retrieve:** `meta answers relations shortcut`.

### 18. Residue, error structure and multiple stages

**Consider when:** a coherent mechanism leaves a recurring mismatch, unused marks, extra letters or a stable exception class.

**Try:** describe the entire residual before decoding it. Compare a second stage, wrong representation, transcription error and decoration. Systematic boundary residue differs from random failures.

**Boundary:** selecting only leftovers that spell a desired word manufactures an extraction. A successful first layer may leave the puzzle unsolved. Check both the selection rule and the next operation.

**Retrieve:** `residual extra letters verification`.

## When this atlas is insufficient

Name the missing knowledge precisely: a notation's direction, a material's allowed motion, a word sense, a format, or a mathematical property. Consult a primary reference or domain tool when available. Obtain what is needed, then return to a clue-grounded experiment. Record the assumption if the fact remains uncertain.

Do not turn a familiarity gap into unlimited brute force. Knowing many mechanisms does not determine which applies. Notice a useful relation, build an operation around it, and check its consequences.
