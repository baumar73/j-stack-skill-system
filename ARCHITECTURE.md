# J-Stack Architecture

Generated: 2026-05-28T10:30:07+00:00

## Concept

J-Stack is a modular newsroom operating system for Hermes skills. Each skill represents a newsroom function and produces reviewable artifacts instead of opaque prose.

## System Layers

1. **Mission layer** — define public interest, audience, artifact type, editorial line, falsification standard.
2. **Research layer** — source map, primary sources, OSINT, data, interviews, documents.
3. **Evidence layer** — claim ledger, evidence ledger, entity graph, timeline, countercase.
4. **Safety layer** — legal risk, ethics, red-team, ship gate.
5. **Production layer** — drafting, copy desk, SEO, social package.
6. **Memory layer** — GBrain import, links, tags, timeline, post-publication updates.

## Skill Interface Contract

Each skill should accept:

- story slug / working title;
- mission brief or upstream artifact;
- links to GBrain pages or workspace files;
- language, jurisdiction, publication venue, sensitivity;
- requested output format.

Each skill should return:

- artifact status;
- key decisions/findings;
- evidence/risk labels where relevant;
- GBrain pages read/written/proposed;
- next recommended J-Stack skill;
- blockers.

## GBrain as Shared Memory

Recommended page namespaces:

- `stories/<slug>` — story hub.
- `stories/<slug>/mission` — editorial mission brief.
- `stories/<slug>/drafts/<version>` — draft versions.
- `claims/<slug>/<claim-id>` — atomic claim pages.
- `evidence/<slug>/<evidence-id>` — evidence cards.
- `sources/<slug>/<source-id>` — source cards.
- `entities/<entity-slug>` — people, organizations, publications, institutions.
- `timelines/<slug>` — chronology index if timeline is too large for story page.
- `risks/<slug>/legal` and `risks/<slug>/ethics` — risk registers.
- `ship/<slug>` — final ship-gate report.

## Link Vocabulary

- `has_source`, `has_claim`, `supported_by`, `contradicted_by`, `mentions`, `about`, `part_of`, `challenges`, `requires_review`, `published_as`, `corrected_by`, `updates`, `follows_up`, `evidence_for`, `risk_for`.

## Publication Statuses

- `IDEA`
- `MISSION_READY`
- `RESEARCH_READY`
- `CLAIMS_READY`
- `DRAFT_READY`
- `LEGAL_REVIEW_REQUIRED`
- `REDTEAM_BLOCKED`
- `PUBLICATION_READY`
- `APPROVED_TO_PUBLISH`
- `PUBLISHED`
- `CORRECTION_REQUIRED`
- `UPDATED`

## Design Principle

The collection must be transparent enough that a skeptical editor can reconstruct why a sentence was allowed to ship.
