# Installation and Pilot Use

J-Stack is a Hermes Agent skill package. It is designed to be inspected and piloted before being installed into any active profile.

## Prerequisites

- Git.
- Python 3 for validation scripts.
- A Hermes Agent installation if you want to load the skills into an agent runtime.
- A reviewed data-governance setup before using real confidential, personal, regulated, client, source-sensitive, or unpublished material.

## Clone

```bash
git clone https://github.com/baumar73/j-stack-skill-system.git
cd j-stack-skill-system
```

## Verify before use

```bash
python3 scripts/validate_jstack.py
python3 scripts/hardening_audit_jstack.py
python3 examples/jstack-seo-distribution/metadata-length-check.py
```

A clean release should show:

- 26 skills.
- 0 validation errors.
- 0 hardening blockers / important issues / nits.
- SEO metadata example PASS.

## Pilot approach

Prefer a small pilot rather than activating the entire package at once.

1. Pick one or two skills from `skills/`.
2. Read each `SKILL.md` fully.
3. Read any referenced files under `references/`, `templates/`, `bundles/`, or `examples/`.
4. Test only with synthetic, public, or redacted material.
5. Keep publishing, source contact, external communication, filings/submissions, infrastructure changes, and professional advice behind explicit human approval.

## Loading into Hermes Agent

Hermes skill loading depends on your local Hermes version and profile setup.

Safe manual pilot pattern:

1. Keep this repository as the reviewed source of truth.
2. Copy only selected `skills/<skill-name>/` directories into a reviewed Hermes skill source for a non-production profile, or configure an external skill directory if your Hermes build supports that workflow.
3. Start a new Hermes session so skill discovery reloads.
4. Confirm the skills appear with `hermes skills list` or by loading a representative skill explicitly.
5. Do not copy secrets, logs, real case files, source material, credentials, or unpublished evidence into the repository.

Do not install J-Stack globally into a production workflow until your editorial, legal, data-protection, provider, logging, retention, source-protection, and security controls are reviewed.

## Update pattern

When updating from this repository:

```bash
git fetch origin
git checkout main
git pull --ff-only origin main
python3 scripts/validate_jstack.py
python3 scripts/hardening_audit_jstack.py
```

Then review the changed skills before replacing any locally piloted copy.

## Uninstall / rollback

If you copied selected skills into a Hermes profile, remove only those copied `jstack-*` skill directories from that profile or revert your external skill-directory configuration.

Keep the Git repository untouched as the audit trail unless you intentionally want to delete your clone.
