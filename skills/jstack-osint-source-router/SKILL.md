---
name: jstack-osint-source-router
description: Use when selecting lawful public OSINT databases and public-record sources for a J-Stack story before live research. Routes questions to source classes, warns about access, licensing, automation, privacy, and evidence limits, and produces a source plan linked to the claim/evidence ledger.
version: 1.0.0
author: J-Stack project for Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [jstack, research, osint, sources, journalism, gbrain]
    related_skills: [jstack-source-map, jstack-osint-research, jstack-primary-source-research, jstack-claim-ledger]
---

# J-Stack OSINT Source Router

## Overview

Select OSINT and public-record sources before collecting facts. This skill turns a vague instruction like "use OSINT databases" into a controlled source plan with evidence classes, jurisdiction, access rules, data-protection warnings, and citation requirements.

J-Stack treats journalism as a transparent production system: a story moves from editorial mission to evidence, claims, countercase, legal/ethics review, drafting, red-team, ship gate, and post-publication accountability. This skill is a routing and source-governance role inside that system, not a license to scrape, deanonymize, or publish sensitive data.

Core law:

> No public claim ships above its evidence grade. Strong opinion is allowed; weak factual basis is not.

The seed atlas lives in `sources/osint-sources.json`; its structure is documented in `sources/osint-sources.schema.json`. Treat the atlas as a starting registry. For real work, verify the current source URL, terms, license, access method, and update date before relying on it.

## Country/Jurisdiction Intake — First Gate

Before using this skill for substantive research or publication-risk work, identify the primary country context. If the user has not specified it, ask: "Which country or countries should this research and publication-risk review be assessed under?" Record primary country, relevant subnational jurisdiction, publication venue, audience, subject/source/evidence location, and likely dispute forum. If unclear, mark `COUNTRY_CONTEXT_UNCLEAR` and avoid publication-ready conclusions until clarified.

Use `references/country-context-intake.md` as the routing reference. If the answer includes the United States, also apply `references/us-publication-context.md`; if multiple countries are involved, mark `COUNTRY_CONTEXT_MULTI_JURISDICTION` and split the analysis.

## US Edition v1.1 — Jurisdiction Overlay

When the publication, audience, platform, source, or subject has a United States nexus, apply `references/us-publication-context.md` before final status. Do not transplant German/EU press-law assumptions into US work. At minimum, identify the relevant state(s), federal forum, publication venue, subject status, public-record posture, and platform context.

Track US-specific risks where relevant: First Amendment/public-concern framing, public official/public figure/private figure status, actual malice/negligence, fact vs opinion, fair-report/public-record privileges, anti-SLAPP and retraction statutes, privacy torts, reporter shield/source protection, recording/access/CFAA issues, copyright/fair use/DMCA, FTC/native-ad disclosures, election/securities sensitivities, and platform rules.

Treat request-for-comment as a US fairness and risk-mitigation practice, not as a single nationwide statutory right of reply. If state law, subpoena/source protection, privacy, defamation, copyright, or platform exposure is material and unresolved, mark `US_LOCAL_COUNSEL_REQUIRED`, `LEGAL_REVIEW_REQUIRED`, or `NOT_READY` rather than `PUBLICATION_READY`.

## When to Use

- A story needs a source plan across company registers, sanctions lists, procurement portals, court databases, IP registers, public datasets, archives, geospatial data, transport records, domain infrastructure, or investigative indexes.
- The user asks to "use all known OSINT databases" and needs a lawful, bounded route rather than indiscriminate collection.
- A claim ledger needs each claim mapped to primary, secondary, index, and lead-only sources.
- A multi-jurisdiction story needs source routing by country and evidence class.
- A researcher needs to know which sources may be automated, which require manual review, which include personal data, and which are only leads.

## Do Not Use For

- Do not bypass logins, paywalls, rate limits, robots/terms, CAPTCHAs, or access controls.
- Do not use illegal leaks, private accounts, impersonation, credential misuse, malware, or evasion.
- Do not run bulk scraping merely because a source is public; check the atlas entry and current terms first.
- Do not deanonymize private individuals without strong public interest, legal/ethics review, and source-protection planning.
- Do not treat an index, aggregator, or lead database as final proof of wrongdoing.

## Role in the J-Stack Newsroom

- **Skill family:** `research`
- **Primary responsibility:** Select and govern OSINT/public-record sources before live research.
- **Upstream inputs:** mission brief, country/jurisdiction intake, source map, initial claims, entity graph, or research question.
- **Downstream consumers:** `jstack-osint-research`, `jstack-primary-source-research`, `jstack-data-journalism`, `jstack-claim-ledger`, `jstack-evidence-ledger`, `jstack-legal-risk`, and `jstack-ethics-check`.

## Inputs

- Country/jurisdiction context: primary country/countries, subnational jurisdiction, publication venue/platform, audience, and likely dispute forum.
- Story slug or working title.
- Research objective and claim IDs, if available.
- Entities, aliases, jurisdictions, identifiers, domains, document types, or datasets to route.
- Sensitivity flags: personal data, minors, source protection, security-sensitive infrastructure, sanctions, criminal allegations, litigation, election/securities context.
- Constraints: no-login, no-paid-sources, API-only, manual-only, no bulk collection, languages, deadline, and publication venue.

## Outputs

- OSINT Source Plan
- Source Class Matrix
- Source cards to create or update
- Access/licensing/automation warnings
- Personal-data and safety-risk flags
- Claim-to-source routing table
- Missing-source list
- Next J-Stack skill route

## Workflow

1. **Frame the research question.** Split the story into source needs: entity identity, ownership/control, filings, sanctions/debarment, contracts/procurement, court/legal records, IP, archive history, datasets, geospatial evidence, transport traces, domain infrastructure, media footprint, or academic/public-health/economic data.
2. **Load the atlas conceptually.** Use `sources/osint-sources.json` as a seed. Do not assume it is complete or current.
3. **Select source classes.** Pick primary sources first, then indexes/aggregators, then secondary/lead-only sources. State why each source is included.
4. **Classify evidence weight.** For every selected source, mark `primary`, `secondary`, `index`, or `lead-only` and what it can and cannot prove.
5. **Check access and automation.** Record whether use should be `manual-first`, `api-preferred`, `bulk-download-ok`, `no-bulk`, or `do-not-automate`. Do not automate restricted or high-risk sources without human approval and terms review.
6. **Flag personal-data and safety risks.** For high-risk entries, require minimization, redaction, and legal/ethics routing before publication.
7. **Map to claim IDs.** Each source must support, contradict, contextualize, or merely suggest a claim. Missing primary sources become an explicit output.
8. **Prepare citation rules.** Specify exact citation fields: register number, filing/accession number, docket, notice ID, dataset timestamp, capture timestamp, DOI, scene ID, or list update date.
9. **Route next step.** Send live collection to `jstack-osint-research` or `jstack-primary-source-research`; send data-heavy analysis to `jstack-data-journalism`; send publishable assertions to `jstack-claim-ledger`.

## Source Class Matrix

| Source class | Typical examples | Evidence role | Default caution |
| --- | --- | --- | --- |
| Company registers / filings | Companies House, SEC EDGAR, GLEIF, national registers | Primary or index | Identity and control need date-specific corroboration. |
| Sanctions / debarment | OFAC, EU, UN, OpenSanctions, World Bank, SAM exclusions | Primary or index | Name-only matches are not enough; preserve official allegation wording. |
| Procurement / spending | TED, SAM.gov, USAspending, UNGM, World Bank projects | Primary | Awards do not prove misconduct; values and lots need definitions. |
| Courts / law | EUR-Lex, CourtListener/RECAP, national courts, HUDOC | Primary or secondary | Allegations in filings are not findings. |
| IP registers | WIPO, Espacenet, EUIPO, USPTO, DPMA | Primary or index | Publication/status does not prove validity or infringement. |
| Archives / media | Wayback, GDELT, Common Crawl, Wikidata | Secondary, index, or lead-only | Capture/index presence is not proof of truth or authorship. |
| Investigative indexes | ICIJ Offshore Leaks, OCCRP Aleph, LittleSis | Lead-only or index | High reputational and legal risk; verify underlying documents. |
| Geospatial / satellite / environment | OSM, NASA FIRMS, Copernicus, USGS, NOAA | Primary or secondary | Interpretation requires expertise and metadata. |
| Transport / infrastructure | ADS-B Exchange, OpenSky, FAA registry, Equasis, crt.sh, RDAP | Primary, index, or lead-only | High privacy/security risk; minimize operational details. |

## GBrain Integration

### Reads from GBrain

- Story hub and editorial mission brief.
- Existing source map and source cards.
- Claim ledger and evidence ledger.
- Entity graph with known identifiers, aliases, jurisdictions, domains, registration numbers, sanctions-list IDs, procurement IDs, and docket numbers.
- Prior OSINT source plans and post-publication corrections.

### Writes or Proposes in GBrain

- `sources/<story>/osint-source-plan` with selected source classes, access rules, risks, and citation fields.
- Source cards for each selected database/source.
- Links: `source -> supports/contradicts/contextualizes/leads_to -> claim`.
- Tags: `jstack`, `osint-source-router`, `source-atlas`, `primary-source`, `index-source`, `lead-only`, `personal-data-risk`, `manual-first`, `api-preferred`.
- Timeline entries for source retrieval dates only when they matter for a story chronology or publication record.

### Tool Pattern

When available, prefer these GBrain tools:

- `mcp_gbrain_get_page` for exact story/source/claim pages.
- `mcp_gbrain_query` for semantic recall of prior investigations, similar source plans, and reusable source cards.
- `mcp_gbrain_search` for exact source names, URLs, entity IDs, docket IDs, or claim IDs.
- `mcp_gbrain_put_page` only for concise, non-secret source plans and source cards.
- `mcp_gbrain_add_link` for typed links between sources, claims, evidence, entities, and timelines.
- `mcp_gbrain_add_tag` for retrieval and risk tags.

If GBrain is unavailable, write the same artifacts as Markdown under the story workspace and keep a manifest for later import.

## Source and Evidence Rules

- Primary sources beat indexes and commentary when both are available.
- An aggregator can identify a lead; it does not automatically prove the underlying fact.
- Official allegations, court filings, sanctions list entries, debarments, procurement awards, and final judicial findings are distinct evidence classes.
- Every source card must state what the source proves, what it does not prove, and whether the source is date-sensitive.
- Name matches require identifiers, aliases, dates of birth, registration numbers, addresses, or other corroborating fields before being treated as a match.
- Translation risk must be noted for non-original-language materials.
- Missing official records are an output; do not hide them.

## Legal and Ethical Boundaries

- This skill provides editorial source routing and risk screening, not legal, compliance, security, or professional advice.
- Do not fabricate citations, databases, official status, identifiers, or source access claims.
- Do not publish unsupported allegations of crime, corruption, espionage, sanctions evasion, money laundering, sexual misconduct, intentional deceit, or hidden control as fact.
- Do not expose private addresses, accounts, family details, health details, travel movements, or unrelated personal data unless a documented public-interest, legal, and ethics gate justifies it.
- Do not include exploit-enabling infrastructure details or live tracking details unless a senior human editor approves a clear public-interest reason and safety mitigation.
- Do not send, post, file, contact sources, query paid/login systems at scale, or externally publish without explicit human approval.

## Output Format

```markdown
# jstack-osint-source-router Output

- Story / slug:
- Country / jurisdiction context:
- Research objective:
- Sensitivity flags:
- Status: SOURCE_PLAN_READY | COUNTRY_CONTEXT_UNCLEAR | TERMS_REVIEW_REQUIRED | LEGAL_REVIEW_REQUIRED | NOT_READY

## Source plan
| Claim/source need | Preferred source(s) | Evidence weight | Access/automation | Personal-data risk | What it can prove | What it cannot prove | Citation fields |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Missing sources
- ...

## GBrain pages/links/tags proposed or written
- ...

## Next recommended J-Stack skill
- ...
```

## Worked Example

See `examples/jstack-osint-source-router/` for a fictional, non-sensitive routing example. It uses a toy transnational public-contracts question, selects source classes from `sources/osint-sources.json`, and runs `route-check.py` to validate the atlas and produce a deterministic source-plan summary.

## Common Pitfalls

1. **Treating public as automatically usable.** Public access does not erase terms, privacy, copyright/database rights, rate limits, or source-protection duties.
2. **Using lead-only databases as proof.** ICIJ, OCCRP Aleph, LittleSis, GDELT, Common Crawl, Wikidata, and similar sources often point to evidence; they do not replace the underlying source.
3. **Name-only matching.** A matching name is a lead, not an identity finding.
4. **Automating login or high-risk sources.** Manual-first means manual-first until terms and safety review say otherwise.
5. **Ignoring jurisdiction.** Company, court, procurement, privacy, defamation, and source-protection rules change by country and forum.

## Verification Checklist

- [ ] Country/jurisdiction context is confirmed or marked `COUNTRY_CONTEXT_UNCLEAR` with a blocking open question.
- [ ] Source classes are mapped to concrete claim/source needs.
- [ ] `sources/osint-sources.json` or an updated source registry was checked for relevant sources.
- [ ] Each selected source has evidence weight, access/automation status, terms/license warning, and personal-data risk.
- [ ] Primary sources are preferred for final factual assertions.
- [ ] Index and lead-only sources are labelled as such.
- [ ] Facts, interpretation, thesis, and rhetoric remain separated.
- [ ] GBrain read/write behavior is clear.
- [ ] Sensitive information is excluded, minimized, or escalated.
- [ ] Output can be reviewed by a skeptical editor.
- [ ] US context is classified as `US_CONTEXT_NOT_REQUIRED` or reviewed under `references/us-publication-context.md`.
- [ ] No external publication/send/post action is taken without human approval.

## One-Shot Recipe

```text
Use jstack-osint-source-router on <story/topic>.
Inputs: <country context, mission brief, claim/source needs, entities/identifiers, constraints>.
Select lawful public source classes from sources/osint-sources.json, mark evidence weight and risks, produce a source plan, propose GBrain source cards, and route the next live research step.
```
