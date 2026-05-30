# GBrain Integration for J-Stack

Generated: 2026-05-28T10:30:07+00:00

## Purpose

J-Stack uses GBrain as a newsroom memory graph, not a dumping ground. The goal is durable retrieval and defensibility: sources, claims, evidence, timelines, entities, corrections, and editorial decisions remain linkable and auditable.

## Safe Storage Rules

Store:

- concise source cards;
- claim summaries and evidence grades;
- story mission briefs;
- entity pages when public-interest justified;
- timeline events;
- risk registers with minimized sensitive detail, including jurisdiction labels and US context labels where relevant;
- publication and correction decisions.

Do not store:

- secrets, credentials, tokens;
- unnecessary raw personal data;
- private addresses/accounts/family details unless publication-safety review justifies the metadata;
- long copyrighted excerpts unless allowed;
- confidential raw leaks without explicit approval and security planning.

## Minimal Story Hub Frontmatter

```yaml
---
title: "<Story title>"
type: story
status: IDEA
source: jstack
tags:
  - jstack
  - journalism
  - <topic>
updated: <ISO timestamp>
---
```

## Claim Page Schema

```yaml
---
title: "Claim <ID>: <short claim>"
type: claim
story: <story-slug>
evidence_grade: A|B|C|D|E|F
publication_color: green|yellow|red
status: proven|well_supported|plausible|unverified|contradicted|withdrawn
tags: [jstack, claim-ledger]
---
```

Sections:

- Atomic claim.
- What would prove it.
- Best supporting evidence.
- Counterevidence.
- Safe wording.
- Unsafe wording.
- Legal/ethics flags.
- US context labels: `US_CONTEXT_NOT_REQUIRED`, `US_CONTEXT_APPLIES`, `US_STATE_LAW_UNCLEAR`, or `US_LOCAL_COUNSEL_REQUIRED`.

## Source Card Schema

```yaml
---
title: "Source: <title>"
type: source-card
story: <story-slug>
source_class: primary|official|court|dataset|interview|journalism|osint|expert|opinion
reliability: high|medium|low|unknown
tags: [jstack, source-card]
---
```

Sections:

- Citation / URL / issuer / date.
- Retrieval date.
- What this source proves.
- What it does not prove.
- Bias/interest/proximity.
- Archive status.
- Translation risk.

## Verification Pattern

After writing pages:

1. `mcp_gbrain_get_page` for direct readback.
2. `mcp_gbrain_search` for exact title/claim ID/name.
3. `mcp_gbrain_query` for semantic retrieval.
4. `mcp_gbrain_get_links` and `get_backlinks` for at least one story/claim/source pair.

## Fallback

If GBrain is unavailable, create markdown pages under `gbrain-export/` and list them in `gbrain-export/MANIFEST.json` for later import.
