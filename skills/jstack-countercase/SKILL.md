---
name: jstack-countercase
description: Use when building the best opposing case against a story, thesis, allegation, or draft before publication, including innocent explanations and subject-side arguments.
version: 1.0.0
author: J-Stack project for Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [jstack, facts-claims, journalism, gbrain]
    related_skills: [jstack-command-center]
---

# J-Stack Countercase

## Overview

Make the argument survive hostile reading by the subject, lawyer, skeptical editor, and intelligent opponent.

J-Stack treats journalism as a transparent production system: a story moves from editorial mission to evidence, claims, countercase, legal/ethics review, drafting, red-team, ship gate, and post-publication accountability. This skill is one role inside that system, not a magic all-purpose journalist.

Core law:

> No public claim ships above its evidence grade. Strong opinion is allowed; weak factual basis is not.

## When to Use

- A draft is sharp, accusatory, or politically/legally controversial.
- Named subjects, institutions, or companies could dispute the piece.

## Do Not Use For

- Do not create fake balance where evidence is one-sided.
- Do not weaken supported facts out of timidity.

## Role in the J-Stack Newsroom

- **Skill family:** `facts-claims`
- **Primary responsibility:** Make the argument survive hostile reading by the subject, lawyer, skeptical editor, and intelligent opponent.
- **Upstream inputs:** mission brief, editorial line, source map, claim ledger, or story hub as applicable.
- **Downstream consumers:** command center, drafting, legal/ethics, red-team, ship gate, distribution, or post-publication tracking.

## Inputs

- Story slug or working title.
- Editorial Mission Brief, if available.
- Existing GBrain story/source/claim pages, if available.
- User-provided notes, documents, links, claims, or draft text.
- Explicit constraints: jurisdiction, language, public voice, publication venue, deadline, and sensitivity.

## Outputs

- Countercase memo
- Innocent explanations
- Subject/lawyer/editor attacks
- Surviving facts

## Workflow

1. State the strongest version of the published thesis.
2. Construct the subject’s best answer.
3. Construct legal, editorial, and reader attacks.
4. Identify innocent explanations and missing context.
5. Return only the claims that still survive and what wording must soften.

## GBrain Integration

### Reads from GBrain

- `claim ledger`
- `legal risk register`
- `source map`
- `entity graph`
- `draft`

### Writes or Proposes in GBrain

- countercase page
- links countercase -> challenges claim
- timeline note if material counterevidence changes story posture

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
# jstack-countercase Output

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

1. **Strawmanning the opponent.**
2. **Confusing fairness with false equivalence.**
3. **Forgetting that innocent explanations can coexist with damaging facts.**

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
Use jstack-countercase on <story/topic>.
Inputs: <mission brief, links, notes, existing GBrain slugs>.
Produce the required artifact, separate facts from interpretation, update/propose GBrain pages and links, and return the next J-Stack step.
```
