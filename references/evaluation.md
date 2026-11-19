# Evaluation protocol and observed evidence

The original six tiny probes were passed by both a skill-guided agent and an ordinary prompt. A follow-up audit on 2026-11-19 ran twelve tasks in three fresh arms: baseline, core only, and full package. All three answered every task correctly. A separate three-scenario comparison also tied. One full-package response proposed a more explicit rival-separating test; retrieval introduced no new solution mechanism. These diagnostic/development checks do not establish a general advantage. See the [audit report and complete trial artifacts](https://github.com/Amal-David/metis/blob/main/docs/audit-2026-11-19.md). The protocol below is guidance for stronger future comparisons; the current run limitations are documented in that report.

## Compare three arms

- **baseline:** strong ordinary solving prompt, original puzzle, same allowed tools.
- **skill:** same plus frozen SKILL.md.
- **skill+retrieval:** same plus frozen local cases and retrieval envelopes.

Pin model/version, exact delivered contexts/hashes, reasoning effort, budget (tokens, wall-clock, calls, tool compute), seed/order schedule where controllable, answer format, and external-oracle access. Count retries, controller checks, resets, councils and research calls. Do not credit a larger-context arm for unpriced extra compute.

## Leakage controls

Freeze the skill and case library before choosing a truly **unseen** final set. Prefer privately authored or newly published puzzles with known evaluator-only golds. Do not use the library's taught puzzles as success benchmarks. Audit near-duplicates, source overlap, famous answers and indirect clues in filenames/tags. Evaluator answers and tests must be inaccessible to proposer agents.

Use multiple families: explicit-rule logic; rule induction; visual/spatial transformations; interactive oracle; ambiguity; impossible constraints; multi-stage metas. Consider common formats, unclear transcriptions and adversarial decorations. For interactive tasks, meter every observation request.

## Metrics

- **verified solve rate:** correct full answer, not merely plausible phrase.
- **time/to first productive hypothesis:** independently adjudicated; report assessor rubric.
- **hypothesis diversity:** distinct representation/mechanism families, not word variation.
- **falsification quality:** cheapest relevant discriminating test and whether it was actually run.
- **false finalization rate:** claimed SOLVED with wrong/unverified answer.
- **validity:** original rule fidelity, independence of held-out check, exact domain/coverage.
- **cost:** total tokens, tool calls, wall time, resets, peak resources if relevant.

Report per-family paired outcomes and uncertainty intervals. Use a preregistered success rule, record abstentions and partial progress, publish failures and mistaken mechanisms. A small positive result is not evidence of universal transfer.

## Minimal answer contract

~~~json
{
  "answer": null,
  "status": "unsolved",
  "observations": [],
  "hypotheses": [
    {
      "id": "H1",
      "mechanism": "",
      "prediction": "",
      "falsifier": "",
      "evidence_state": "conjectured"
    }
  ],
  "tests": [],
  "independent_validation": null,
  "uncertainty": "",
  "next_discriminating_test": ""
}
~~~

Evidence states: OBSERVED, CONJECTURED, TESTED_WITHIN_MODEL, INDEPENDENTLY_CHECKED, CONTRADICTED, INCONCLUSIVE, SOLVED. These labels are reporting conventions, not a certificate of truth.
