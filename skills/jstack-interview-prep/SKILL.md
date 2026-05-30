---
name: jstack-interview-prep
description: Use when preparing interviews, requests for comment, expert calls, hostile-subject questions, source briefings, or right-of-reply outreach drafts.
version: 1.1.0
author: J-Stack project for Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [jstack, research, journalism, gbrain]
    related_skills: [jstack-command-center]
---

# J-Stack Interview Prep

## Overview

Prepare fair, precise, evidence-linked questions that advance the story and protect publication safety.

J-Stack treats journalism as a transparent production system: a story moves from editorial mission to evidence, claims, countercase, legal/ethics review, drafting, red-team, ship gate, and post-publication accountability. This skill is one role inside that system, not a magic all-purpose journalist.

Core law:

> No public claim ships above its evidence grade. Strong opinion is allowed; weak factual basis is not.

## US Edition v1.1 — Jurisdiction Overlay

When the publication, audience, platform, source, or subject has a United States nexus, apply `references/us-publication-context.md` before final status. Do not transplant German/EU press-law assumptions into US work. At minimum, identify the relevant state(s), federal forum, publication venue, subject status, public-record posture, and platform context.

Track US-specific risks where relevant: First Amendment/public-concern framing, public official/public figure/private figure status, actual malice/negligence, fact vs opinion, fair-report/public-record privileges, anti-SLAPP and retraction statutes, privacy torts, reporter shield/source protection, recording/access/CFAA issues, copyright/fair use/DMCA, FTC/native-ad disclosures, election/securities sensitivities, and platform rules.

Treat request-for-comment as a US fairness and risk-mitigation practice, not as a single nationwide statutory right of reply. If state law, subpoena/source protection, privacy, defamation, copyright, or platform exposure is material and unresolved, mark `US_LOCAL_COUNSEL_REQUIRED`, `LEGAL_REVIEW_REQUIRED`, or `NOT_READY` rather than `PUBLICATION_READY`.

## When to Use

- The story needs interviews or right of reply.
- A named subject must be asked for comment.
- The user wants expert questions or hostile interview prep.

## Do Not Use For

- Do not send the request. Draft only.
- Do not misrepresent identity, purpose, or evidence.

## Role in the J-Stack Newsroom

- **Skill family:** `research`
- **Primary responsibility:** Prepare fair, precise, evidence-linked questions that advance the story and protect publication safety.
- **Upstream inputs:** mission brief, editorial line, source map, claim ledger, or story hub as applicable.
- **Downstream consumers:** command center, drafting, legal/ethics, red-team, ship gate, distribution, or post-publication tracking.

## Inputs

- Story slug or working title.
- Editorial Mission Brief, if available.
- Existing GBrain story/source/claim pages, if available.
- User-provided notes, documents, links, claims, or draft text.
- Explicit constraints: jurisdiction, language, public voice, publication venue, deadline, and sensitivity.

## Outputs

- Interview brief
- Question list
- Evidence-backed right-of-reply draft
- Follow-up plan

## Workflow

1. Define interview objective and what each answer could prove.
2. Map questions to claims and evidence gaps.
3. Separate factual confirmation, context, response, and opinion questions.
4. Prepare fair wording for adverse allegations.
5. For German press-law or analogous fairness contexts, prepare the pre-publication `Gelegenheit zur Stellungnahme` package: concrete allegation list, evidence references, response deadline, recipient/channel, and publication-use note.
6. For US contexts, prepare request-for-comment as a fairness and defamation-risk-mitigation package, not as a universal statutory right of reply; document state/jurisdiction uncertainty, subject status, recording-consent/source-protection issues, and whether outreach is withheld for safety or legal reasons.
7. Document outreach attempts and responses as source cards, timeline events, and claim-ledger updates.

## Stellungnahme / Right-of-Reply Drafting Rules

When a named or otherwise identifiable subject may be adversely affected:

- Draft questions so the subject can understand the core allegations and meaningfully respond.
- Ask about the strongest adverse claims, not only soft context questions.
- Do not disclose unnecessary source identities, confidential material, or unpublished evidence beyond what fairness requires.
- State the response deadline and intended publication context where appropriate.
- Track `requested`, `responded`, `declined`, `no response`, or `deadline extended` as explicit statuses.
- If no request has been sent yet, output a draft only; never contact the subject without explicit human approval.

## GBrain Integration

### Reads from GBrain

- `claim ledger`
- `source map`
- `entity profile`
- `countercase`

### Writes or Proposes in GBrain

- interview-prep page
- source card for response when received
- timeline event for outreach/response

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
# jstack-interview-prep Output

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

1. **Asking speeches instead of questions.**
2. **Failing to give fair opportunity to respond.**
3. **Letting an interviewee’s denial erase independent evidence without analysis.**

## Verification Checklist

- [ ] Objective and artifact type are explicit.
- [ ] Evidence grade is not overstated.
- [ ] Facts, interpretation, thesis, and rhetoric are separated.
- [ ] GBrain read/write behavior is clear.
- [ ] Sensitive information is excluded or minimized.
- [ ] Output can be reviewed by a skeptical editor.
- [ ] Right-of-reply / `Gelegenheit zur Stellungnahme` draft includes concrete allegations, response deadline, recipient/channel, and evidence references where appropriate.
- [ ] US context is classified as `US_CONTEXT_NOT_REQUIRED` or reviewed under `references/us-publication-context.md`.
- [ ] No external publication/send/post action is taken without human approval.

## One-Shot Recipe

```text
Use jstack-interview-prep on <story/topic>.
Inputs: <mission brief, links, notes, existing GBrain slugs>.
Produce the required artifact, separate facts from interpretation, update/propose GBrain pages and links, and return the next J-Stack step.
```
