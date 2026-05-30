# J-Stack Quality Gates

Generated: 2026-05-28T10:30:07+00:00

## Per-Skill Rubric, 100 Points

- Clarity of trigger and non-trigger: 10
- Professional usefulness: 15
- Journalistic rigor: 15
- Technical feasibility in Hermes: 10
- GBrain integration: 15
- Legal/ethical safety: 15
- Output stability and templates: 10
- Reusability/public-readiness: 10

## Minimum Scores

- Core skills: 95+
- Helper/secondary skills: 90+
- Anything below 90 is not publication-ready.

## Story Ship Gate

A story cannot be marked `PUBLICATION_READY` unless:

- mission brief exists;
- country/jurisdiction context is confirmed under `references/country-context-intake.md`, or marked `COUNTRY_CONTEXT_UNCLEAR` / `LOCAL_REVIEW_REQUIRED` with publication blocked;
- editorial line is explicit or intentionally neutral;
- source map exists;
- claim ledger covers all factual claims;
- yellow/red claims are softened, caveated, removed, or escalated;
- countercase exists for controversial claims;
- legal and ethics screens are complete;
- required German `Gelegenheit zur Stellungnahme` / right-of-reply outreach is documented or explicitly not required;
- US context is classified as `US_CONTEXT_NOT_REQUIRED` or reviewed under `references/us-publication-context.md`, with unresolved state-law/local-counsel issues escalated;
- red-team blockers are resolved;
- headline, teaser, captions, and social snippets do not overstate evidence;
- GBrain or fallback dossier contains enough record for later correction;
- human approval is explicit for any external publication.

## Evidence Grades

- **A** — Direct primary evidence or authoritative record, independently verifiable.
- **B** — Strong evidence from reliable sources, minor gaps remain.
- **C** — Plausible but materially incomplete or dependent on secondary reporting.
- **D** — Weak, single-source, ambiguous, or context-dependent.
- **E** — Unverified allegation or lead only.
- **F** — Contradicted, withdrawn, or unsafe to use.

## Publication Colors

- **Green:** Can be stated as fact with citation.
- **Yellow:** Use cautious wording; mark as allegation, report, assertion, analysis, or unresolved.
- **Red:** Do not publish as factual claim; remove, investigate further, or legal review required.

## Country/Jurisdiction Intake Gate

Before a J-Stack workflow leaves the mission stage, it must record a country-context label from `references/country-context-intake.md`. If the user did not specify a country, ask the mandatory first question. `COUNTRY_CONTEXT_UNCLEAR`, unresolved multi-jurisdiction issues, or material local-law uncertainty require `LOCAL_REVIEW_REQUIRED`, `LEGAL_REVIEW_REQUIRED`, or `NOT_READY`, not `PUBLICATION_READY`.

## US Edition v1.1 Gate

For any US-nexus story, the ship gate must record either `US_CONTEXT_NOT_REQUIRED` or a completed US-context review. Material unresolved questions about state law, First Amendment/defamation posture, anti-SLAPP, retraction statutes, privacy torts, source protection, recording/access, copyright/fair use, FTC/platform rules, or election/securities sensitivities require `US_LOCAL_COUNSEL_REQUIRED`, `LEGAL_REVIEW_REQUIRED`, or `NOT_READY`.
