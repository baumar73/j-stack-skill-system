# Worked Example — J-Stack OSINT Source Router

This example is fictional and non-sensitive. It does **not** perform live OSINT lookups. It demonstrates how `jstack-osint-source-router` turns a broad research request into a lawful source plan before collection.

## Fictional prompt

> We are considering a story about whether fictional company **CivicBridge Systems Ltd.** and a similarly named subsidiary appear in public contracts and sanctions/debarment records across the UK, EU, and US. Build the source plan only; do not contact anyone, do not publish, and do not scrape.

## Files

- `worked-example.md` — source plan, routing table, warnings, and next steps.
- `route-check.py` — deterministic registry and routing smoke test.

## Reproduce

From the repository root:

```bash
python3 examples/jstack-osint-source-router/route-check.py
```

Expected result: the script validates required atlas fields, counts sources/categories, and prints a deterministic source-plan summary for the fictional story.
