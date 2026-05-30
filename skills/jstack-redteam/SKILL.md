---
name: jstack-redteam
description: Use for hostile pre-publication review by personas such as subject lawyer, skeptical editor, hostile opponent, platform moderator, fact checker, and ordinary intelligent reader.
version: 1.2.0
author: J-Stack project for Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [jstack, safety, journalism, gbrain]
    related_skills: [jstack-command-center]
---

# J-Stack Red Team

## Overview

Find the failure modes before subjects, lawyers, platforms, or readers do.

J-Stack treats journalism as a transparent production system: a story moves from editorial mission to evidence, claims, countercase, legal/ethics review, drafting, red-team, ship gate, and post-publication accountability. This skill is one role inside that system, not a magic all-purpose journalist.

Core law:

> No public claim ships above its evidence grade. Strong opinion is allowed; weak factual basis is not.

## Country/Jurisdiction Intake — First Gate

Before using this skill for substantive research or publication-risk work, identify the primary country context. If the user has not specified it, ask: "Which country or countries should this research and publication-risk review be assessed under?" Record primary country, relevant subnational jurisdiction, publication venue, audience, subject/source/evidence location, and likely dispute forum. If unclear, mark `COUNTRY_CONTEXT_UNCLEAR` and avoid publication-ready conclusions until clarified.

Use `references/country-context-intake.md` as the routing reference. If the answer includes the United States, also apply `references/us-publication-context.md`; if multiple countries are involved, mark `COUNTRY_CONTEXT_MULTI_JURISDICTION` and split the analysis.

## US Edition v1.1 — Jurisdiction Overlay

When the publication, audience, platform, source, or subject has a United States nexus, apply `references/us-publication-context.md` before final status. Do not transplant German/EU press-law assumptions into US work. At minimum, identify the relevant state(s), federal forum, publication venue, subject status, public-record posture, and platform context.

Track US-specific risks where relevant: First Amendment/public-concern framing, public official/public figure/private figure status, actual malice/negligence, fact vs opinion, fair-report/public-record privileges, anti-SLAPP and retraction statutes, privacy torts, reporter shield/source protection, recording/access/CFAA issues, copyright/fair use/DMCA, FTC/native-ad disclosures, election/securities sensitivities, and platform rules.

Treat request-for-comment as a US fairness and risk-mitigation practice, not as a single nationwide statutory right of reply. If state law, subpoena/source protection, privacy, defamation, copyright, or platform exposure is material and unresolved, mark `US_LOCAL_COUNSEL_REQUIRED`, `LEGAL_REVIEW_REQUIRED`, or `NOT_READY` rather than `PUBLICATION_READY`.

## When to Use

- A draft is ready for serious review.
- The story is controversial, reputationally risky, or strategically important.

## Do Not Use For

- Do not red-team an empty outline as if it were a draft.
- Do not treat red-team objections as automatically correct.

## Role in the J-Stack Newsroom

- **Skill family:** `safety`
- **Primary responsibility:** Find the failure modes before subjects, lawyers, platforms, or readers do.
- **Upstream inputs:** mission brief, editorial line, source map, claim ledger, or story hub as applicable.
- **Downstream consumers:** command center, drafting, legal/ethics, red-team, ship gate, distribution, or post-publication tracking.

## Inputs

- Country/jurisdiction context: primary country/countries, subnational jurisdiction, publication venue/platform, audience, and likely dispute forum.
- Story slug or working title.
- Editorial Mission Brief, if available.
- Existing GBrain story/source/claim pages, if available.
- User-provided notes, documents, links, claims, or draft text.
- Explicit constraints: jurisdiction, language, public voice, publication venue, deadline, and sensitivity.

## Outputs

- Red-team report
- Blockers
- Fix list
- Ship status recommendation

## Workflow

1. Read draft, claim ledger, source map, countercase, and legal/ethics notes.
2. Attack from subject lawyer, skeptical editor, hostile opponent, platform moderator, fact checker, and ordinary reader perspectives.
3. Classify findings as blocker, major, minor, or style.
4. Propose exact fixes.
5. Return NO_SHIP, SHIP_AFTER_FIXES, SHIP_WITH_CONCERNS, or SHIP_READY.

## GBrain Integration

### Reads from GBrain

- `draft`
- `claim ledger`
- `source map`
- `countercase`
- `legal risk register`

### Writes or Proposes in GBrain

- red-team report page
- links red-team finding -> claim/draft section
- tags for blockers and ship status

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
# jstack-redteam Output

- Story / slug:
- Country / jurisdiction context:
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

1. **Making only stylistic comments.**
2. **Failing to attack the headline and social snippets.**
3. **Ignoring what a hostile but intelligent reader will misunderstand.**

## Verification Checklist

- [ ] Country/jurisdiction context is confirmed or marked `COUNTRY_CONTEXT_UNCLEAR` with a blocking open question.
- [ ] Objective and artifact type are explicit.
- [ ] Evidence grade is not overstated.
- [ ] Facts, interpretation, thesis, and rhetoric are separated.
- [ ] GBrain read/write behavior is clear.
- [ ] Sensitive information is excluded or minimized.
- [ ] Output can be reviewed by a skeptical editor.
- [ ] US context is classified as `US_CONTEXT_NOT_REQUIRED` or reviewed under `references/us-publication-context.md`.
- [ ] No external publication/send/post action is taken without human approval.

## One-Shot Recipe

```text
Use jstack-redteam on <story/topic>.
Inputs: <mission brief, links, notes, existing GBrain slugs>.
Produce the required artifact, separate facts from interpretation, update/propose GBrain pages and links, and return the next J-Stack step.
```
