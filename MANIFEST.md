# J-Stack Manifest

Generated: 2026-05-28T10:30:07+00:00

Status: public MIT skill collection.

Published: 2026-05-29T11:33:47+00:00.

Last hardened: 2026-05-28T11:08:22+00:00.

## Review Artifacts

- `VALIDATION.json` — latest deterministic skill validation, 26 skills, 0 errors.
- `HARDENING-AUDIT.json` — second-pass hardening audit, 0 blockers, 0 important issues, 0 nits.
- `REDTEAM-HARDENING-REPORT.md` — human-readable second-pass review summary.
- `scripts/validate_jstack.py` — frontmatter/structure validator.
- `scripts/hardening_audit_jstack.py` — read-only hardening audit script.

## Skills

- `jstack-command-center` (editorial-command): 97/100 — Use when starting, coordinating, or resuming a J-Stack journalism workflow. Routes the topic through editorial mission, evidence, drafting, red-team, legal/ethics, distribution, and post-publication follow-up.
- `jstack-office-hours` (editorial-command): 96/100 — Use when testing whether a journalism idea, public thesis, investigation lead, or commentary concept is worth pursuing before spending research or drafting effort.
- `jstack-editorial-line` (editorial-command): 96/100 — Use when an author, newsroom, or project has a public voice or worldview that should guide framing without changing evidence grades or factual findings.
- `jstack-assignment-desk` (editorial-command): 95/100 — Use when breaking a journalism project into newsroom assignments, beats, deadlines, research tasks, review stages, and deliverables for humans or agents.
- `jstack-source-map` (research): 97/100 — Use when building a complete source universe for a story: primary sources, secondary sources, adversarial sources, expert sources, missing sources, and archive status.
- `jstack-primary-source-research` (research): 95/100 — Use when locating and interpreting primary public sources such as statutes, court records, official registers, corporate filings, sanctions lists, press releases, datasets, or original documents.
- `jstack-osint-research` (research): 95/100 — Use when conducting lawful open-source research across public websites, social profiles, domains, corporate pages, media archives, map traces, public videos, and metadata visible to ordinary users.
- `jstack-data-journalism` (research): 94/100 — Use when a story relies on datasets, tables, statistics, scraping outputs, budgets, filings, measurements, or repeatable quantitative analysis.
- `jstack-interview-prep` (research): 95/100 — Use when preparing interviews, requests for comment, expert calls, hostile-subject questions, source briefings, or right-of-reply outreach drafts.
- `jstack-document-review` (research): 95/100 — Use when extracting facts, parties, dates, claims, contradictions, and evidence from documents, PDFs, filings, contracts, letters, reports, screenshots, transcripts, or archives.
- `jstack-investigate` (research): 97/100 — Use when testing a factual hypothesis, suspicion, allegation, or investigative lead before drafting. Splits claims, identifies evidence paths, and reports confidence honestly.
- `jstack-claim-ledger` (facts-claims): 98/100 — Use when converting every publishable assertion into a controlled claim with evidence grade, counterevidence, safe wording, legal risk, and publication color.
- `jstack-evidence-ledger` (facts-claims): 96/100 — Use when building a litigation-grade evidence record for facts, documents, quotes, datasets, interviews, screenshots, and public records that support or contradict claims.
- `jstack-entity-graph` (facts-claims): 96/100 — Use when mapping people, organizations, publications, domains, funders, locations, aliases, relationships, and confidence levels in a story or investigation.
- `jstack-timeline` (facts-claims): 96/100 — Use when reconstructing dated events, statements, filings, publications, decisions, denials, corrections, and consequences so a story does not imply false sequence or causality.
- `jstack-countercase` (facts-claims): 97/100 — Use when building the best opposing case against a story, thesis, allegation, or draft before publication, including innocent explanations and subject-side arguments.
- `jstack-legal-risk` (safety): 96/100 — Use for a pre-publication legal-risk screen of journalism or public commentary, including defamation/libel, German Verdachtsberichterstattung, privacy, copyright, data protection, and active litigation risks.
- `jstack-ethics-check` (safety): 95/100 — Use when reviewing fairness, public interest, harm, vulnerable people, source protection, conflicts, framing, privacy, and correction duties before publication.
- `jstack-draft` (writing): 96/100 — Use when drafting news, analysis, opinion, investigation, feature, briefing, LinkedIn, X thread, or longform text from a prepared mission brief and claim ledger.
- `jstack-copy-desk` (writing): 95/100 — Use when tightening, restructuring, headline-testing, style-checking, and copyediting a draft without changing the evidence level or editorial mission.
- `jstack-seo-distribution` (distribution): 94/100 — Use when turning a publishable story into search-intent, metadata, landing-page, newsletter, and audience-development material without overstating claims.
- `jstack-social-package` (distribution): 95/100 — Use when creating X, LinkedIn, newsletter, short-video, podcast, or thread drafts from a publication-ready story while preserving evidence boundaries and human approval.
- `jstack-redteam` (safety): 97/100 — Use for hostile pre-publication review by personas such as subject lawyer, skeptical editor, hostile opponent, platform moderator, fact checker, and ordinary intelligent reader.
- `jstack-ship` (safety): 98/100 — Use as the final publication gate for J-Stack work. Verifies mission, sources, claims, countercase, legal/ethics, red-team fixes, headlines, social snippets, GBrain record, and human approval.
- `jstack-postpub` (post-publication): 95/100 — Use after publication to monitor corrections, rebuttals, legal letters, new evidence, source rot, reader questions, follow-up stories, and GBrain timeline updates.
- `jstack-gbrain-memory` (gbrain): 97/100 — Use when turning J-Stack story artifacts into durable GBrain knowledge: story hubs, source cards, claim pages, evidence pages, entity graph links, timelines, corrections, and reusable background.
