# J-Stack OSINT Source Atlas

This directory contains a curated seed registry of public OSINT and public-record sources for J-Stack research routing.

Files:

- `osint-sources.json` — source registry used by `jstack-osint-source-router`.
- `osint-sources.schema.json` — JSON Schema for the registry structure.

## Boundary

The atlas is **not** an instruction to scrape the web or bypass access controls. Each source entry includes access, automation, license/terms, evidence weight, personal-data risk, and citation notes. Use it to pick sources and plan review gates before live research.

## Review rule

Before a source is used for a real story, verify:

1. the current official URL,
2. current terms/license/access rules,
3. whether login, payment, rate limits, or API registration apply,
4. whether the data includes personal, source-sensitive, security-sensitive, or legally sensitive material,
5. whether the source is primary evidence, an index, secondary analysis, or lead-only.
