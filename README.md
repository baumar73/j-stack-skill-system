# J-Stack — GBrain-Integrated Journalism Skills for Hermes Agent

Status: **published public MIT skill collection** with J-Stack v1.2 country/jurisdiction intake and v1.1 US-context overlay; not automatically installed into any active Hermes profile.
Generated: 2026-05-28T10:30:07+00:00  
Published: 2026-05-29T11:33:47+00:00  
Owner: Markus Bauer / J-Stack contributors
License: MIT

## Important Notice: Experimental Skills, No Legal or Compliance Advice

J-Stack is an **experimental open-source skill collection and workflow library** for agentic journalism, investigation, public writing, and publication safety. It is a technical template and starting point, **not** a certified product, legal opinion, compliance framework, security assessment, newsroom policy, or professional service.

Use J-Stack at your own responsibility. The repository and its authors make **no warranty** as to correctness, completeness, timeliness, security, suitability for a particular purpose, legal effect, or production readiness. LLM and agent outputs can be wrong, incomplete, outdated, or hallucinated.

Before using J-Stack with real client, legal, business, personal, confidential, journalistic-source, or otherwise regulated data, you must assess your own deployment, provider, hosting, logging, retention, data transfer, professional secrecy, data protection, AI-governance, editorial, and security obligations. This repository makes **no statement** that any concrete use complies with professional secrecy, confidentiality, GDPR/BDSG, the EU AI Act, Cloud Act/FISA exposure, US federal or state law, First Amendment / defamation / privacy / anti-SLAPP / fair-use / source-protection rules, privilege or seizure protections, employment or works-council rules, platform rules, press law, defamation law, copyright, or any other applicable law.

Do not test with real confidential data unless your environment is approved and documented. Keep secrets, tokens, API keys, credentials, and provider logs out of the repository and issue reports. Verify all citations, statutes, deadlines, calculations, source references, factual claims, and external actions independently. Human approval remains mandatory for publishing, filings, submissions, external messages, source contact, payments, deployments, legal advice, or other consequential actions.

For the full notice, see [`DISCLAIMER.md`](./DISCLAIMER.md).

J-Stack is a professional journalism and publication-safety skill collection for Hermes Agent. It turns AI-assisted journalism into a transparent newsroom workflow: mission, sources, investigation, claims, evidence, entities, timeline, countercase, legal/ethics, draft, copy desk, distribution, red-team, ship gate, and post-publication accountability.

## Inspiration and Non-Affiliation

J-Stack is inspired by the operational clarity of Garry Tan / GStack-style skills: named roles, hard gates, direct artifacts, and refusal to ship unsafe work. J-Stack adapts that discipline to journalism, investigation, public writing, and publication safety.

This repository is **not affiliated with, endorsed by, or dependent on Garry Tan, GStack, or any upstream project** unless an explicit future affiliation is documented. The inspiration is acknowledged because the operating style matters.

## Why GBrain Matters

Journalism is graph work:

- claims connect to sources;
- sources connect to people, institutions, documents, and dates;
- timelines prevent false causality;
- counterevidence protects against ideological blindness;
- corrections and follow-ups must remain traceable.

J-Stack is designed to use **GBrain** as the newsroom memory and knowledge graph. Skills explicitly describe what they read from GBrain, what they may write, what links/tags/timeline entries they use, and what sensitive material does not belong there.

## Core Law

> No public claim ships above its evidence grade.  
> Strong opinion is allowed; weak factual basis is not.

## J-Stack v1.2 — Country and Jurisdiction Intake

The current public version adds a mandatory first gate: before research, drafting, legal-risk review, or ship status, J-Stack must identify the country context. If the country is not explicit, ask: **"Which country or countries should this research and publication-risk review be assessed under?"**

Use [`references/country-context-intake.md`](./references/country-context-intake.md) to record the primary country/countries, relevant state/province/federal-state/city/court/agency context, publication venue, platform, audience, subject/source/evidence location, and likely dispute forum. If the answer is unclear, mark `COUNTRY_CONTEXT_UNCLEAR` and do not call the work `PUBLICATION_READY`.

## J-Stack v1.1 — US Publication Context Overlay

The second public version adds a United States context layer across all 26 skills. Use [`references/us-publication-context.md`](./references/us-publication-context.md) whenever the publication, source, subject, audience, platform, author, evidence, or likely dispute forum has a US nexus.

The US layer is broader than a German `Gelegenheit zur Stellungnahme` gate. It forces the workflow to classify federal/state jurisdiction, First Amendment posture, public official/public figure/private figure status, actual-malice or negligence issues, fact-vs-opinion boundaries, public-record/fair-report posture, anti-SLAPP and retraction questions, privacy torts, source-protection and recording/access rules, copyright/fair-use/DMCA, FTC/platform disclosures, election/securities sensitivities, and local-counsel needs.

J-Stack does **not** claim US legal compliance. The overlay is a safety checklist that prevents German/EU assumptions from being treated as sufficient for US publication risk.

## Skill Families

- Editorial command: command center, office hours, editorial line, assignment desk.
- Research: source map, primary-source research, OSINT, data journalism, interview prep, document review, investigation.
- Facts and claims: claim ledger, evidence ledger, entity graph, timeline, countercase.
- Safety: legal risk, ethics check, red-team, ship gate.
- Writing and distribution: draft, copy desk, SEO/distribution, social package.
- Post-publication and memory: postpub, GBrain memory.

## Worked Examples

- [`examples/jstack-data-journalism/`](./examples/jstack-data-journalism/) shows a fictional, non-sensitive data-journalism workflow: toy CSV, reproducible calculation, findings table, limitations, safe claim wording, and next J-Stack routing.
- [`examples/jstack-seo-distribution/`](./examples/jstack-seo-distribution/) shows a fictional, non-sensitive SEO/distribution workflow: claim-bounded story brief, search-intent map, metadata, landing-page outline, newsletter teaser, headline-vs-evidence check, and metadata length/safety script.

## Recommended Story Flow

1. `jstack-office-hours`
2. `jstack-editorial-line`
3. `jstack-command-center`
4. `jstack-source-map`
5. `jstack-investigate`
6. `jstack-claim-ledger`
7. `jstack-countercase`
8. `jstack-legal-risk`
9. `jstack-ethics-check`
10. `jstack-draft`
11. `jstack-copy-desk`
12. `jstack-redteam`
13. `jstack-ship`
14. `jstack-social-package`
15. `jstack-postpub`

## Tested Environment and Technical Requirements

J-Stack is a **Hermes Agent skill collection**, not a standalone application. The repository contains Markdown-based `SKILL.md` workflows plus supporting references, templates, bundles, manifests, and validation artifacts. Practical behavior depends on the agent runtime, model quality, local tooling, and the user's own data-governance setup.

### Reference environment for the current public release

- **Agent runtime:** Hermes Agent with `SKILL.md` skill support.
- **Reference model / AI stack:** authored and tested in a Linux-based Hermes Agent / Codex-5.5-class coding and reasoning workflow. J-Stack is not hard-bound to one model version, but other runtimes or weaker models may produce different results.
- **Operating system:** Linux is the tested reference environment. macOS should work for ordinary Markdown skill use. Windows is not the primary tested environment; use WSL/Linux when shell scripts, validation commands, or Git workflows are required.
- **Knowledge layer:** GBrain is strongly recommended for full newsroom-memory workflows, including source maps, claim ledgers, timelines, entity graphs, corrections, and post-publication memory. Individual skills can still be read and followed manually without GBrain.
- **Local maintenance tools:** `git`; optionally `python3` for validation scripts, JSON/manifest checks, and repository QA.

J-Stack does **not** provide a hosted model, newsroom CMS, secure confidential-data environment, legal/compliance approval process, source-protection infrastructure, or production deployment. Those technical and organizational controls must be supplied, reviewed, and documented by the user before real-world use.

## Installation

This is a public MIT-licensed skill package. To install, copy selected `skills/<skill>/` directories into a Hermes skill source or consume the repository through the Hermes skills workflow. Do not install globally into production workflows until reviewed for your use case.

## Safety Defaults

- Country/jurisdiction context must be confirmed at the start or explicitly marked `COUNTRY_CONTEXT_UNCLEAR` with a blocking open question.
- No automatic publishing.
- No source contact without approval.
- No invented citations.
- No secrets in GBrain.
- No secrets, tokens, API keys, credentials, or provider logs in the repository or issue reports.
- No real confidential data in tests unless the deployment is approved and documented.
- No unsupported criminal or misconduct labels.
- No claim ships above evidence grade.
- No adverse claim about an identifiable person, company, institution, or group ships without a documented fairness check and, where required, a pre-publication opportunity to comment (`Gelegenheit zur Stellungnahme`).
- No US-nexus story ships unless US context is classified as not required or reviewed under `references/us-publication-context.md`, with unresolved state-law or local-counsel issues escalated instead of hidden.
- No legal, compliance, security, or professional-certainty claim without independent human review.
- Human approval remains mandatory for publishing, filings, submissions, external messages, source contact, payments, deployments, legal advice, or other consequential actions.
