# Frozen diagnostic protocol

## Scope

This is a newly authored twelve-task diagnostic, not a creativity benchmark. Its author read repository `AGENTS.md` and `references/evaluation.md`, but not `SKILL.md`, cases, retrieval implementation, or teaching documents. This reduces tailoring; it does not prove absence of structural overlap with conventional puzzles or model training. The coordinator supplied core snapshot hash `cf13d14021620fac0036611473138cc5b985197189a9d40f923140b69ce4041c`; the coordinator must document what that hash covers.

The raw solver material is `tasks.json` only. Answers and finite checks are in `private/`; never deliver these to a solver. Q01/Q02 were revised before any trial to remove sentences explicitly revealing their mechanisms. They now request a simple fitted mechanism, conditional prediction, and a uniqueness assessment. That change corrects an authoring defect, not a reaction to model outcomes.

**Scope limitation:** Q01/Q02 test open rule induction, Q03 tests geometric transfer from supplied coordinates, and Q04 identifies a hidden finite swap graph. Q06 supplies an additional global-invariant opportunity. This is not a set of four strong unconstrained hidden-mechanism problems. No visual perception trial or SVG is included in this time-limited checkpoint. Do not claim visual performance or general creativity from it. Q09 evaluates a query plan; no oracle replies will be delivered in the initial run.

## Matched arms

Use three fresh conversations with identical model/version, reasoning effort, generic prompt, selected raw tasks, task order, allowed general tools, and total budgets:

1. **Baseline:** generic prompt and tasks only.
2. **Skill:** same plus frozen `SKILL.md`.
3. **Skill plus retrieval:** same plus the identical frozen skill and access to frozen local retrieval/cases.

Reading the skill and retrieving cases consume the same overall budget. Record the added input size and all calls. No web access, evaluator access, or cross-arm communication. Do not expose other arms' responses. A shared filesystem with instructions excluding certain files is **not an OS-enforced secrecy boundary**; disclose this limitation. Ideally deliver selected task objects and treatment material into separate directories or sandboxes. Do not claim isolation that was not implemented.

Suggested initial budget: twelve tasks, 4,500 response words, twelve total tool calls including reads/retrieval, twelve minutes wall time, no retry/council/subagents. Record any actual deviation before comparing results. If the host does not enforce a budget, label it requested rather than enforced. Missing token telemetry is unavailable, never zero. A strong baseline should retain normal tools and verification ability.

Primary task order: Q01 through Q12. Optional fixed robustness order: Q08,Q03,Q11,Q05,Q01,Q09,Q06,Q12,Q02,Q10,Q04,Q07. Rerun all arms, or the same subset chosen before outcomes. A new order on the same tasks is not a new independent held-out set. A seed is uncontrolled unless the model service actually exposes one.

## Generic solver prompt

> Solve the supplied independent tasks as accurately as you can. You are an experienced general problem solver. Use the available tools when they help and check answers against the stated conditions. Report conclusions and concise evidence needed to assess them, not a private reasoning transcript. Return one JSON array, with an object per task containing `id`, `status` (`SOLVED`, `PARTIAL`, `UNSOLVED`, or `PLAN`), `answer`, and `evidence`. Include `alternatives` or `next_test` when needed to answer that task. Some tasks may not have a unique answer or may ask for a plan. Do not claim a tool result or oracle reply unless you actually obtained it. Preserve the task rules. Do not inspect evaluator files, other arms' artifacts, or outside reference material. Stay within the assigned response, tool, and time limits. Cover every task.

Treatment-only addition: “The attached frozen skill is available; apply it where useful.” The retrieval arm also receives its exact permitted command. Do not add the skill's tactics to the baseline prompt.

## Verification and recording

Run `python evaluation/private/checkers.py` before reading responses. This writes `evaluation/private/gold.json` and verifies exact finite results. Save exact delivered prompts, contexts, retrieval corpus hashes, raw outputs, tool logs, order, timestamps, and available token data. The evaluator's independent checks must not be credited as actions performed by the solver. Use `private/rubric.md` for scoring; do not revise it after viewing responses. Blind arm labels during assessment if feasible. Report every task outcome, including equal results and failures.

Primary outcome is the number of fully correct answers, paired by item. Secondary outcomes are false finalization, mechanism/alternative/test/calibration scores, and observed cost. An exploratory skill signal requires at least two additional fully correct items versus baseline with no increase in false finalization. This threshold is registered before responses, but passing it would remain a small diagnostic signal rather than a general performance claim. A ceiling or tie is inconclusive. Exact paired sign tests may be reported on discordant outcomes with the caveat that these deliberately related items are not independent samples of user tasks.

Public release turns these tasks into development fixtures. Future confirmatory evaluation needs a newly authored and frozen held-out set.
