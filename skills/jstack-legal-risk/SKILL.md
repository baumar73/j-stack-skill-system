---
name: jstack-legal-risk
description: Use for a pre-publication legal-risk screen of journalism or public commentary, including defamation/libel, German Verdachtsberichterstattung, privacy, copyright, data protection, and active litigation risks.
version: 1.0.0
author: J-Stack project for Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [jstack, safety, journalism, gbrain]
    related_skills: [jstack-command-center]
---

# J-Stack Legal Risk

## Overview

Provide a structured publication-safety screen, not final legal advice.

J-Stack treats journalism as a transparent production system: a story moves from editorial mission to evidence, claims, countercase, legal/ethics review, drafting, red-team, ship gate, and post-publication accountability. This skill is one role inside that system, not a magic all-purpose journalist.

Core law:

> No public claim ships above its evidence grade. Strong opinion is allowed; weak factual basis is not.

## When to Use

- A draft names people, companies, institutions, criminal allegations, misconduct, sanctions, money, corruption, litigation, or private facts.

## Do Not Use For

- Do not present this as attorney-client legal advice for public users.
- Do not clear publication when red claims remain unsupported.

## Role in the J-Stack Newsroom

- **Skill family:** `safety`
- **Primary responsibility:** Provide a structured publication-safety screen, not final legal advice.
- **Upstream inputs:** mission brief, editorial line, source map, claim ledger, or story hub as applicable.
- **Downstream consumers:** command center, drafting, legal/ethics, red-team, ship gate, distribution, or post-publication tracking.

## Inputs

- Story slug or working title.
- Editorial Mission Brief, if available.
- Existing GBrain story/source/claim pages, if available.
- User-provided notes, documents, links, claims, or draft text.
- Explicit constraints: jurisdiction, language, public voice, publication venue, deadline, and sensitivity.

## Outputs

- Legal Risk Register
- Required fixes
- Right-of-reply / Gelegenheit zur Stellungnahme needs
- Legal-review flag
- Safe wording options

## Workflow

1. Classify risk areas: reputation, privacy, copyright, data, court, active proceeding, platform policy.
2. Map each risk to claim IDs and wording.
3. Flag unsupported allegations of crime, corruption, agency, espionage, sanctions evasion, money laundering, sexual misconduct, or intentional deceit.
4. For adverse claims about identifiable people, companies, institutions, or groups, require a documented pre-publication opportunity to comment before ship status can be green.
5. Return ship status: no-ship, legal-review-required, publish-after-fixes, or legally lower-risk.

## German Press-Law Gate: Gelegenheit zur Stellungnahme

For German publication contexts, especially **Verdachtsberichterstattung** or other reputation-affecting allegations, J-Stack treats the opportunity to respond before publication as a hard fairness and risk gate:

- Ask whether the affected subject is identifiable directly or indirectly.
- Send only evidence-backed, concrete allegations/questions; do not ambush with vague accusations.
- Give a fair deadline under the circumstances and record the deadline, channel, recipient, and exact request text.
- Track the answer, partial answer, denial, correction, or non-response in the source map, claim ledger, timeline, and legal-risk register.
- Reflect the response fairly in the draft or explain that no response was received despite a documented request.
- If the opportunity to comment is needed but missing, mark `LEGAL_REVIEW_REQUIRED` or `NOT_READY`; do not mark `PUBLICATION_READY`.

## GBrain Integration

### Reads from GBrain

- `claim ledger`
- `countercase`
- `draft`
- `source map`
- `entity pages`

### Writes or Proposes in GBrain

- legal-risk register page
- links risk -> claim/draft section
- tags for legal-review-required/no-ship

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
# jstack-legal-risk Output

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

1. **Giving false legal certainty.**
2. **Ignoring jurisdiction.**
3. **Letting a headline overstate the body.**

## Verification Checklist

- [ ] Objective and artifact type are explicit.
- [ ] Evidence grade is not overstated.
- [ ] Facts, interpretation, thesis, and rhetoric are separated.
- [ ] GBrain read/write behavior is clear.
- [ ] Sensitive information is excluded or minimized.
- [ ] Output can be reviewed by a skeptical editor.
- [ ] Required pre-publication `Gelegenheit zur Stellungnahme` / right-of-reply outreach is identified, drafted, or explicitly marked as not required.
- [ ] No external publication/send/post action is taken without human approval.

## One-Shot Recipe

```text
Use jstack-legal-risk on <story/topic>.
Inputs: <mission brief, links, notes, existing GBrain slugs>.
Produce the required artifact, separate facts from interpretation, update/propose GBrain pages and links, and return the next J-Stack step.
```
