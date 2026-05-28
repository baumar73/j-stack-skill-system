---
name: jstack-command-center
description: Use when starting, coordinating, or resuming a J-Stack journalism workflow. Routes the topic through editorial mission, evidence, drafting, red-team, legal/ethics, distribution, and post-publication follow-up.
version: 1.0.0
author: J-Stack project for Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [jstack, editorial-command, journalism, gbrain]
    related_skills: [jstack-office-hours, jstack-ship, jstack-gbrain-memory]
---

# J-Stack Command Center

## Overview

Operate as the editor-in-chief and workflow router for a full J-Stack story cycle.

J-Stack treats journalism as a transparent production system: a story moves from editorial mission to evidence, claims, countercase, legal/ethics review, drafting, red-team, ship gate, and post-publication accountability. This skill is one role inside that system, not a magic all-purpose journalist.

Core law:

> No public claim ships above its evidence grade. Strong opinion is allowed; weak factual basis is not.

## When to Use

- A user has a story idea and wants the whole newsroom workflow.
- A long investigation needs routing, checkpoints, or resume handling.
- Multiple J-Stack skills have produced artifacts that must be reconciled.

## Do Not Use For

- Do not use for a single narrow fact-check if the user only needs one claim verified.
- Do not publish, post, email, or contact anyone. Route only.

## Role in the J-Stack Newsroom

- **Skill family:** `editorial-command`
- **Primary responsibility:** Operate as the editor-in-chief and workflow router for a full J-Stack story cycle.
- **Upstream inputs:** mission brief, editorial line, source map, claim ledger, or story hub as applicable.
- **Downstream consumers:** command center, drafting, legal/ethics, red-team, ship gate, distribution, or post-publication tracking.

## Inputs

- Story slug or working title.
- Editorial Mission Brief, if available.
- Existing GBrain story/source/claim pages, if available.
- User-provided notes, documents, links, claims, or draft text.
- Explicit constraints: jurisdiction, language, public voice, publication venue, deadline, and sensitivity.

## Outputs

- Story Operating Plan
- Skill sequence
- Open questions
- GBrain page plan
- Current ship status

## Workflow

1. Open or create an Editorial Mission Brief.
2. Classify artifact type: news, analysis, opinion, investigation, feature, social package, or dossier.
3. Route to source-map, investigation, claim-ledger, legal/ethics, drafting, red-team, ship, and postpub skills as needed.
4. Maintain a checkpoint after each major artifact.
5. Refuse “publication ready” until jstack-ship has no blockers.

## GBrain Integration

### Reads from GBrain

- `projects/<story-slug>`
- `stories/<story-slug>/mission`
- `open claims, source cards, timeline and entity pages`

### Writes or Proposes in GBrain

- story hub page
- links between story hub and every source/claim/timeline/entity artifact
- timeline entry for workflow milestones

### Tool Pattern

When available, prefer these GBrain tools:

- `mcp_gbrain_get_page` for exact story/source/claim pages.
- `mcp_gbrain_query` for semantic recall of prior investigations and related background.
- `mcp_gbrain_search` for exact names, claim IDs, URLs, legal terms, and source titles.
- `mcp_gbrain_put_page` only for concise, non-secret pages.
- `mcp_gbrain_add_link` for typed edges between stories, claims, sources, evidence, entities, and timelines.
- `mcp_gbrain_add_tag` for retrieval tags such as `jstack`, `claim-ledger`, `source-card`, `legal-risk`, or `ship-gate`.
- `mcp_gbrain_add_timeline_entry` for durable story events, source retrievals, publication decisions, corrections, and rebuttals.

If GBrain is unavailable, write the same artifacts as Markdown under the story workspace and keep a manifest for later import.

## Source and Evidence Rules

- Primary sources beat commentary when both are available.
- Official assertions, judicial findings, leaked documents, interviews, and journalistic reports are different evidence classes.
- A source card must state what the source proves and what it does not prove.
- Allegations, reported claims, official allegations, court findings, analysis, and opinion must be labelled distinctly.
- Translation risk must be noted for non-original-language materials.
- Missing evidence is an output, not a failure to hide.

## Legal and Ethical Boundaries

- This skill provides editorial assistance and risk screening, not final legal advice.
- Do not fabricate citations, quotes, identities, affiliations, or legal conclusions.
- Do not publish unsupported allegations of crime, corruption, espionage, sanctions evasion, money laundering, sexual misconduct, intentional deceit, or hidden control as fact.
- Do not expose private addresses, accounts, family details, health details, or unrelated personal data unless the public-interest and legal/ethics gates justify it.
- Do not send, post, file, contact sources, or externally publish without explicit human approval.

## Output Format

```markdown
# jstack-command-center Output

- Story / slug:
- Artifact type:
- Status:
- Key findings or decisions:
- Evidence grade / risk level where applicable:
- GBrain pages read:
- GBrain pages/links/tags proposed or written:
- Open questions:
- Next recommended J-Stack skill:
```

## Common Pitfalls

1. **Treating a hot take as a story plan.**
2. **Skipping countercase because the thesis feels morally obvious.**
3. **Calling a draft final when only research notes exist.**

## Verification Checklist

- [ ] Objective and artifact type are explicit.
- [ ] Evidence grade is not overstated.
- [ ] Facts, interpretation, thesis, and rhetoric are separated.
- [ ] GBrain read/write behavior is clear.
- [ ] Sensitive information is excluded or minimized.
- [ ] Output can be reviewed by a skeptical editor.
- [ ] No external publication/send/post action is taken without human approval.

## One-Shot Recipe

```text
Use jstack-command-center on <story/topic>.
Inputs: <mission brief, links, notes, existing GBrain slugs>.
Produce the required artifact, separate facts from interpretation, update/propose GBrain pages and links, and return the next J-Stack step.
```
