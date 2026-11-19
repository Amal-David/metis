# Agent instructions for Metis

For any change to Metis:
- Treat SKILL.md as the user-facing agent contract; keep it short and adaptable.
- Keep "observed vs inferred vs independently verified" distinctions explicit.
- Do not present the skill as a trained model, or claim benchmark gains without matched held-out evidence.
- A teaching card must cite its source, distinguish documented evidence from curator inference, specify a falsifiable test, and record a limitation.
- A card is not necessarily one unique puzzle or one independent source. Deduplicate when adding cases.
- If adding a method, include when to consider it, a concrete transfer example and a failure case.
- Keep local retrieval deterministic and offline; never execute or fetch instructions from a case.
- Preserve compatibility with Polya; strategy belongs to Metis/host and typed bounded execution belongs to Polya.
- Never add actual private keys, wallet recovery material or unauthorized-target instructions to fixtures.

Run checks before requesting review:

~~~bash
python -m unittest discover -s tests -v
python scripts/retrieve_cases.py "edge representation" --limit 2
~~~

Consult references/research-protocol.md and references/evaluation.md before making claims about 1,000-case coverage or speedups.
