# Research sources and claim boundaries

Access dates use the user timezone, Asia/Kolkata (UTC+05:30).

Consult these sources when revising the method or designing an evaluation. They are supporting evidence, not mandatory reading during every solve. Nine research papers and two benchmark entries are listed. Read-scope describes the portions inspected while creating this reference; it does not imply every appendix was read. Design inferences remain hypotheses about the skill until tested. Sources were inspected on 2026-11-19.

## 1. Representation change

**Knoblich et al. (1999), _Constraint Relaxation and Chunk Decomposition in Insight Problem Solving_.** [Primary paper](https://www.hf.uni-koeln.de/data/fgpsych/File/Haider/Knoblich_etal_1999.pdf).

**Read-scope:** Introduction, mechanism definitions, and results/general discussion. **Supported:** Human matchstick experiments supported predictions about relaxing inappropriate constraints and decomposing perceptual units. **Design inference:** Separate stated rules from imported assumptions; reconsider what counts as one object. **Limit:** This does not demonstrate that these prompts cause an LLM to discover novel puzzle mechanisms.

## 2. Structural analogy

**Gick and Holyoak (1983), _Schema Induction and Analogical Transfer_.** [Publisher record](https://www.sciencedirect.com/science/article/pii/0010028583900026); [author-hosted scan](https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Gick_Holyoak1983_SchemaInduction.pdf).

**Read-scope:** Primary abstract; full scanned text was not readable through the research tools. **Supported:** The paper investigates analogy noticing and schema induction from concrete examples. **Design inference:** Compare cases for shared relations rather than surface themes. **Limit:** Do not attribute numerical gains or detailed experimental findings to this inspection.

## 3. Independent hypothesis generation

**Kohn and Smith (2011), _Collaborative Fixation: Effects of Others' Ideas on Brainstorming_.** [Primary full text](https://onlinelibrary.wiley.com/doi/full/10.1002/acp.1699).

**Read-scope:** Abstract, experimental results, and general discussion. **Supported:** Exposure to others' ideas produced conformity; category breadth and idea quantity showed different effects. **Design inference:** Generate alternatives independently before sharing a favored mechanism. **Limit:** Human brainstorming results do not establish an optimal LLM team size or guarantee that multiple agents improve solving.

## 4. Discriminating tests

**Wason (1960), _On the Failure to Eliminate Hypotheses in a Conceptual Task_.** [Primary paper](https://bear.warrington.ufl.edu/brenner/mar7588/Papers/wason-qjep1960.pdf).

**Read-scope:** Abstract, task procedure, and quantitative results. **Supported:** The task exposed premature acceptance of narrower rules that fit positive examples. **Design inference:** Seek an observation on which plausible rivals disagree. **Limit:** This deliberately constructed task does not prove that negative tests are always preferable; a positive result can also discriminate hypotheses.

## 5. Branching and backtracking

**Yao et al. (2023), _Tree of Thoughts: Deliberate Problem Solving with Large Language Models_.** [Primary paper](https://arxiv.org/html/2305.10601v2).

**Read-scope:** Main method, task descriptions, and compute-cost appendix. **Supported:** Candidate generation, search, and evaluation improved results on the tested tasks, with additional computation. **Design inference:** Keep a bounded set of distinct mechanisms and revisit choices when predictions fail. **Limit:** Task-specific historical gains do not establish this skill's effectiveness or current-model performance.

## 6. Self-correction evaluation pitfalls

**Huang et al. (2024), _Large Language Models Cannot Self-Correct Reasoning Yet_.** [ICLR paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf).

**Read-scope:** Introduction, evaluation critique, and limitations. **Supported:** Intrinsic self-correction sometimes degraded tested reasoning performance; oracle feedback, unequal budgets, and unequal instructions can confound comparisons. **Design inference:** Use complete baseline instructions, matched resources, and observable checks. **Limit:** The title is not a timeless impossibility claim about every model or correction method.

## 7. Independent verification

**Stechly et al. (2025), _On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks_.** [ICLR paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3c5e56274140e0420baa3916c529210-Paper-Conference.pdf).

**Read-scope:** Abstract, study scope, and methodological discussion. **Supported:** In tested formal domains, sound external verification outperformed self-critique across most domains. **Design inference:** A skeptic should supply a failed constraint or counterexample rather than a vote. **Limit:** Formal task verification does not automatically validate an ambiguous puzzle interpretation.

## 8. Reconstructing a withheld condition

**Wu et al. (2024), _Large Language Models Can Self-Correct with Key Condition Verification_.** [EMNLP paper](https://aclanthology.org/2024.emnlp-main.714.pdf).

**Read-scope:** Abstract, method overview, and limitations. **Supported:** ProCo masks a condition and uses a proposed answer to reconstruct it; the paper reports gains in its tested settings. **Design inference:** Ask a mechanism to predict unused features. **Limit:** Problems were generally short with numerical or entity answers. A feature seen while choosing the mechanism is not an independent holdout.

## 9. Incubation boundaries

**Baird et al. (2012), _Inspired by Distraction: Mind Wandering Facilitates Creative Incubation_.** [Author-hosted paper](https://www.cmhp.ucsb.edu/sites/default/files/2018-12/Baird%20et%20al.%20%282012%29%20Inspired%20by%20distraction.pdf).

**Read-scope:** Abstract, results, and discussion. **Supported:** An undemanding intervening task improved unusual-use performance on previously encountered problems in this experiment, not newly encountered ones. **Design inference:** A fresh representation or independent agent may interrupt fixation. **Limit:** No evidence here supports making an LLM process idle or claiming that wall-clock waiting generates insight.

## 10. PuzzleWorld

**Li et al. (2026), _PuzzleWorld: A Benchmark for Multimodal, Open-Ended Reasoning in Puzzlehunts_.** [ICLR paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/1403ccd14eeecb2477ba0eabfa882fd5-Paper-Conference.pdf); [official card](https://huggingface.co/datasets/hzli1202/PuzzleWorld/blob/main/README.md).

**Read-scope:** Data construction, annotation, evaluation methods, and card. **Supported:** 667 puzzles; published solutions were annotated into steps. Cases with multiple ground truths, incomplete solutions, or required physical activity were excluded. **Design inference:** Diagnose intermediate progress but supplement missing task classes. **Limit:** These are solution annotations, not chronological discovery traces; historical scores are not current leaderboard claims.

## 11. EnigmaEval

**Wang et al. (2025), _EnigmaEval: A Benchmark of Long Multimodal Reasoning Challenges_.** [Original paper](https://static.scale.com/uploads/654197dc94d34f66c0f5184e/EnigmaEval%20v4.pdf); [official current card](https://huggingface.co/datasets/cais/EnigmaEval).

**Read-scope:** Collection methods and full public card. **Supported:** Original: 1,184 puzzles. Card inspected: cleaned v2, 1,161 rows, including 827 Puzzled Pint puzzles; files gated. **Design inference:** Pin releases, preserve necessary meta inputs, and remove hints from unassisted tests. **Limit:** No chronological discovery traces; overlap with PuzzleWorld requires deduplication. Do not add benchmark totals as independent cases.
