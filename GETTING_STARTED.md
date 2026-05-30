# Getting Started with J-Stack

J-Stack is a public MIT-licensed Hermes Agent skill collection for agentic journalism, investigation, public writing, and publication-safety workflows.

It is not a standalone app. It is a library of Markdown `SKILL.md` workflows plus references, templates, bundles, examples, and validation artifacts.

## 1. Read the safety notice first

Before using J-Stack with real material, read:

- [`README.md`](./README.md) — overview and safety defaults.
- [`DISCLAIMER.md`](./DISCLAIMER.md) — full use notice.
- [`PUBLICATION-READINESS.md`](./PUBLICATION-READINESS.md) — readiness and remaining human decisions.
- [`QUALITY-GATES.md`](./QUALITY-GATES.md) — publication gates and review posture.

Short version: J-Stack is experimental. It is not legal, compliance, security, tax, professional, or publication-clearance advice. Human approval remains mandatory for consequential actions.

## 2. Inspect the skill map

Start with:

- [`MANIFEST.md`](./MANIFEST.md) — human-readable skill inventory.
- [`MANIFEST.json`](./MANIFEST.json) — machine-readable inventory.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — package structure.
- [`DISCOVERY.md`](./DISCOVERY.md) — how the skills are meant to be discovered and routed.

The most useful first skills are usually:

1. `jstack-office-hours`
2. `jstack-editorial-line`
3. `jstack-command-center`
4. `jstack-source-map`
5. `jstack-osint-source-router`
6. `jstack-claim-ledger`
7. `jstack-legal-risk`
8. `jstack-ethics-check`
9. `jstack-ship`
10. `jstack-postpub`

For OSINT-heavy stories, review [`sources/osint-sources.json`](./sources/osint-sources.json) and use `jstack-osint-source-router` before live collection. The atlas is a routing aid, not permission to scrape, bypass access controls, or publish sensitive personal data.

## 3. Review the worked examples

The repository includes three fictional, non-sensitive examples:

- [`examples/jstack-data-journalism/`](./examples/jstack-data-journalism/)
- [`examples/jstack-seo-distribution/`](./examples/jstack-seo-distribution/)
- [`examples/jstack-osint-source-router/`](./examples/jstack-osint-source-router/)

They are deliberately small. They show the expected pattern: synthetic input, bounded claims, reproducible reasoning, explicit limitations, and human review gates.

Run the example checks:

```bash
python3 examples/jstack-seo-distribution/metadata-length-check.py
python3 examples/jstack-osint-source-router/route-check.py
```

Expected result: SEO metadata passes its limits and the OSINT route check validates the source atlas and emits a deterministic fictional source plan.

## 4. Validate the repository

From the repository root:

```bash
python3 scripts/validate_jstack.py
python3 scripts/hardening_audit_jstack.py
python3 -m json.tool MANIFEST.json >/dev/null
```

For release-style verification, write the generated reports back to disk:

```bash
python3 scripts/validate_jstack.py > VALIDATION.json
python3 scripts/hardening_audit_jstack.py > HARDENING-AUDIT.json
```

## 5. Use only a small reviewed surface first

Do not globally activate every skill in a production Hermes profile on first contact.

Recommended pilot:

1. Pick one workflow family, for example source mapping, claim ledger, or ship gate.
2. Read the relevant `SKILL.md` file and referenced docs.
3. Test with synthetic or public non-sensitive material.
4. Confirm your data-governance, provider, logging, retention, and publication-review setup.
5. Only then use it with real material, and only under human review.

## 6. Keep real-world work behind human gates

J-Stack can structure work, but it must not silently perform external actions.

Do not let an agent publish, email, message, contact sources, file/submit documents, change infrastructure, store sensitive material, or give professional advice without explicit human approval and a suitable environment.
