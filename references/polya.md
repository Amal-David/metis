# Working with Polya

Use Polya as an optional execution and evidence layer. Keep hypothesis selection in the calling agent. Inspect installed contracts before relying on operation names or historical examples.

Sources: [agent workflow](https://github.com/Amal-David/polya/blob/main/docs/agents/workflow.md), [method guidance](https://github.com/Amal-David/polya/blob/main/docs/agents/method-learning.md).

1. Preserve originals, uncertain transcriptions, and the unresolved question.
2. Discover operations with `polya find '<structural question>'` or the available MCP discovery tool. Inspect the exact schema and example.
3. Form the smallest bounded experiment separating current hypotheses. Inspect a typed plan before running it.
4. Retain actual inputs, implementation version, output, and coverage. Independently check that the model represents the source clues.
5. Use existing experiment ranking, Workspace records, and continuation facilities when available. Do not replace Polya's execution ledger with a second purportedly authoritative ledger.
6. Distinguish incomplete search, unavailable backends, errors, and completed negatives. An exact result concerns the declared model, not all interpretations.

Use ordinary inspection or another suitable solver when Polya is unavailable. This skill does not automatically install Polya. Its local casebook is a separate reference aid, not a new Polya operation. Tool integration and improved solve rates have not been benchmarked by creating this package.
