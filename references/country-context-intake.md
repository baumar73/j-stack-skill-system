# Country and Jurisdiction Intake — J-Stack v1.2

Every J-Stack workflow starts by identifying the country or legal/media context for the research. Do this before substantive research, drafting, risk scoring, or publication-readiness labels.

## Mandatory First Question

If the country context is not already explicit, ask:

> Which country or countries should this research and publication-risk review be assessed under?

If needed, follow with:

- Which state, province, canton, federal state, territory, city, court, agency, or platform jurisdiction matters?
- Where will the piece be published and where is the likely audience?
- Where are the subject, source, records, platform, publisher, and likely dispute forum located?
- Is the output for journalism, opinion, advocacy, commercial content, legal analysis, internal research, or social distribution?

## Country Context Labels

Use these labels consistently in mission briefs, skill outputs, ledgers, GBrain pages, and ship gates:

- `COUNTRY_CONTEXT_CONFIRMED`
- `COUNTRY_CONTEXT_MULTI_JURISDICTION`
- `COUNTRY_CONTEXT_UNCLEAR`
- `COUNTRY_CONTEXT_NOT_RELEVANT`
- `LOCAL_REVIEW_REQUIRED`

## Minimum Fields

Record at least:

- Primary country or countries.
- Subnational jurisdiction if relevant.
- Publication venue and platform.
- Primary audience.
- Subject/source/evidence location.
- Likely legal or procedural forum if a dispute arises.
- Applicable context references, e.g. `references/us-publication-context.md` for US nexus.

## Routing Rule

- If the answer is Germany/EU, apply German/EU press-law and data-protection assumptions only where they fit the facts.
- If the answer includes the United States, apply `references/us-publication-context.md`.
- If multiple countries are involved, mark `COUNTRY_CONTEXT_MULTI_JURISDICTION` and split the analysis by jurisdiction.
- If the country is unknown and the user cannot clarify, mark `COUNTRY_CONTEXT_UNCLEAR` and avoid `PUBLICATION_READY`.
- If state-specific, local, platform, or sector-specific rules materially affect publication risk, mark `LOCAL_REVIEW_REQUIRED` rather than inventing certainty.

## Non-Legal Use

This intake is not legal advice. It is a routing and safety control so the agent does not silently apply the wrong country context to research, interviews, evidence handling, wording, distribution, or publication gates.
