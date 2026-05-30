# Worked Example — OSINT Source Router

## Scenario

Fictional, tutorial-only story seed:

- Working title: `CivicBridge public contracts source plan`
- Country context: `COUNTRY_CONTEXT_MULTI_JURISDICTION`
- Relevant jurisdictions: United Kingdom, European Union, United States
- Publication venue: internal J-Stack training note
- Subject: fictional company `CivicBridge Systems Ltd.` and fictional affiliate `CivicBridge Civic Data LLC`
- Constraint: source plan only; no live lookups; no scraping; no publication.

## Source needs

| Need | Why it matters | Required evidence class |
| --- | --- | --- |
| Entity identity | Avoid name-only mismatch. | Official company register or securities filing. |
| Contract awards | Test whether public-contract records exist. | Official procurement/spending portals. |
| Sanctions/debarment | Avoid publishing unsupported risk language. | Official sanctions/debarment lists; aggregators only as leads. |
| Archived website claims | Preserve historical public statements if later researched. | Web archive with capture timestamp; live site if available. |
| Claim ledger routing | Keep every assertion below its evidence grade. | J-Stack claim/evidence ledger. |

## Source route

| Need | Preferred source(s) | Evidence weight | Access/automation | Risk | What it can prove | What it cannot prove |
| --- | --- | --- | --- | --- | --- | --- |
| UK entity identity | UK Companies House | Primary | API-preferred/manual-first | High personal-data risk | UK company number, filings, officers/PSC records as of retrieval date. | That a similarly named entity is the same as another entity without identifiers. |
| EU procurement | TED | Primary | Manual-first | Medium | EU procurement notice/award details above thresholds. | Misconduct, performance, or hidden ownership. |
| US awards | SAM.gov and USAspending | Primary | Manual-first/API where allowed | Medium | Federal notice/award/recipient records. | That the recipient performed badly or that a contract was improper. |
| Sanctions/debarment | OFAC, EU consolidated list, UN list, SAM exclusions, World Bank debarred firms | Primary | Manual-first | High | Official list membership when identifiers match. | Broader criminality or moral conclusions beyond the official entry. |
| Aggregated screening | OpenSanctions | Index | API-preferred after terms check | High | Cross-list lead and source pointer. | Final designation fact without original list verification. |
| Historical web claims | Internet Archive Wayback | Secondary | Manual-first | Medium | That a captured page existed at a capture timestamp. | Truth of the captured content or current status. |

## Status

`SOURCE_PLAN_READY_FOR_MANUAL_RESEARCH`

This is **not** `PUBLICATION_READY`. It is only a lawful source-routing artifact. Live collection should be handled by `jstack-osint-research` or `jstack-primary-source-research`, then every publishable assertion goes to `jstack-claim-ledger`.

## GBrain proposal

- Create `sources/civicbridge-training/osint-source-plan`.
- Tag: `jstack`, `osint-source-router`, `source-atlas`, `training-example`.
- Add source cards for Companies House, TED, SAM.gov, USAspending, OFAC, EU sanctions list, UN sanctions list, OpenSanctions, and Wayback.
- Link future evidence to claim IDs only after live retrieval and citation.

## Human gates

- Terms/license review before any automated collection.
- Legal/ethics review before naming sanctions/debarment risk in public copy.
- Privacy minimization before using officer, address, aircraft, transport, or domain-registration data.
- Human approval before source contact, publication, external messages, or live campaign use.
