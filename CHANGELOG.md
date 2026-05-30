# Changelog

All notable changes to J-Stack are documented here.

J-Stack follows repository releases for public packaging. Individual skill text may carry its own internal workflow/version language, but the GitHub release tag is the package version users should cite.

## [v0.1.0] - 2026-05-30

### Added

- Initial public release package for 26 Hermes Agent journalism and publication-safety skills.
- GBrain-oriented newsroom-memory workflows for source maps, claim ledgers, evidence ledgers, entity graphs, timelines, countercases, post-publication accountability, and durable corrections/follow-ups.
- Country/jurisdiction intake gate for publication-risk context before research, drafting, review, or ship decisions.
- US publication-context overlay for US-nexus stories, including fact/opinion posture, public figure/public official issues, actual malice/negligence prompts, anti-SLAPP/retraction questions, privacy torts, copyright/fair-use/DMCA, FTC/platform concerns, source protection, recording/access rules, and local-counsel escalation.
- Public disclaimer and safety defaults for experimental status, no professional advice, no warranty, human approval for consequential actions, secrets hygiene, data-protection review, professional/source secrecy, LLM hallucination risk, and publication responsibility.
- Validation and hardening scripts:
  - `scripts/validate_jstack.py`
  - `scripts/hardening_audit_jstack.py`
- Release-readiness artifacts:
  - `MANIFEST.md` / `MANIFEST.json`
  - `QUALITY-REPORT.md`
  - `PUBLICATION-READINESS.md`
  - `REDTEAM-HARDENING-REPORT.md`
  - `VALIDATION.json`
  - `HARDENING-AUDIT.json`
- Fictional, non-sensitive worked examples:
  - `examples/jstack-data-journalism/`
  - `examples/jstack-seo-distribution/`

### Quality status

- Skill count: 26.
- Minimum skill score: 95/100.
- Average score: 95.962/100.
- Validation: 0 errors.
- Hardening audit: 0 blockers, 0 important issues, 0 nits.

### Safety notes

- The examples are tutorial-only and use synthetic/fake data.
- No secrets, credentials, provider logs, real sources, real confidential data, or real campaign materials are included.
- J-Stack does not provide legal, compliance, security, professional, or publication-clearance advice.
- Human approval remains mandatory before publication, external messages, source contact, filings/submissions, deployments, payments, legal advice, or other consequential actions.

[v0.1.0]: https://github.com/baumar73/j-stack-skill-system/releases/tag/v0.1.0
