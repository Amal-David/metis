# Casebook provenance and scope

The audited library contains **29 source cards from 29 primary source URLs**. These cover **25 named puzzle designs, two reusable game families (Net and Mines), and two general guides**. There are 27 non-null puzzle identifiers; that count includes the two game families and is not a count of 27 particular puzzle instances. The original thousand-case research target remains incomplete.

## What was reviewed

The audit inspected the relevant passages behind every retained card. Read `scope_read` for the actual coverage; a long retrospective was not necessarily read end to end. Original diagrams and full solutions were not independently reconstructed unless a card explicitly says so. [Corpus audit](corpus-audit.md) records title corrections, attribution changes and counting decisions.

All 21 source URLs from the original installed skill are retained. Repeated lessons in the reconstructed GitHub version were consolidated. The library adds verified CRUMS cases, the Mines generator account and a concrete construction account from The Legend.

| Source kind | Cards | What it can establish |
| --- | ---: | --- |
| Official solution | 16 | A published mechanism, sometimes with separately attributed author notes |
| Solver retrospective | 7 | What a solver reports noticing or trying; not necessarily a complete chronology |
| Constructor notes | 6 | Design choices and reported testing, not every solver's discovery |

Twelve cards have a documented trigger, 23 a documented test, and ten a documented false start. Missing fields remain null. A source may present a test without reporting that an unspoiled solver actually performed it. See the wording of the field, not just its presence.

## Read a card correctly

[cases.json](cases.json) separates source observations, representation changes, documented discovery events, curator-proposed tests, applicability, counterconditions and outcome limits. A `source_checked` flag records the curator's review; schema validation cannot prove that the source is true or that the summary is faithful.

The retriever indexes only structural cues, tags and mechanism families. Returned cards contain solution mechanisms, so exclude the current puzzle and related sources during original solving. Source and family exclusions reduce obvious leakage; they do not establish independent discovery or eliminate pretraining overlap.

## Coverage and limits

The corpus covers 12 primary mechanism-family labels. The separate [atlas](mechanism-atlas.md) supplies 18 conditional mechanism entries, and [contrast examples](contrast-examples.md) supplies eight original teaching constructions. These counts describe different resources and must not be added as independent historical cases.

Coverage remains weighted toward English-language hunts and a small set of communities. Physical assembly, language outside English, interactive discovery, and complete contemporaneous solving records remain sparse. The corpus includes wrong representations, ambiguity, shortcuts and incomplete verification; it is not a representative sample of all puzzle solving.

The summaries are short original paraphrases, with source links. No source images or full articles are mirrored. Public accessibility does not establish permission for unrestricted redistribution or model training. The original source material remains with its authors.

Nine research-paper entries and two benchmark entries are retained in [research-sources.md](research-sources.md), with read scopes and limits. Their findings motivate design choices; they do not establish that Metis improves speed or general creativity. Follow [evaluation.md](evaluation.md) before making performance claims and [research-protocol.md](research-protocol.md) before expanding the corpus.
