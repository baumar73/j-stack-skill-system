# J-Stack Data Journalism Worked Example

This example demonstrates how `jstack-data-journalism` turns a small dataset into cautious, reproducible story findings.

**Important:** This is a fictional, non-sensitive demonstration dataset. It does not describe real people, real agencies, real public services, or real performance.

## Scenario

A reporter wants to test a narrow public-service question:

> Are weekend opening hours evenly distributed across a fictional city's public service desks?

Country/jurisdiction context is intentionally explicit:

- Primary country: fictional demonstration / no real jurisdiction
- Publication venue: internal tutorial
- Audience: J-Stack users learning the workflow
- Status: `COUNTRY_CONTEXT_NOT_RELEVANT` for legal-risk conclusions because the dataset is fictional

## Files

- `sample-public-service-hours.csv` — tiny fictional dataset
- `worked-example.md` — full data note, method, findings, limitations, and safe claim wording

## What this example teaches

1. Confirm provenance and jurisdiction before analysis.
2. Define denominators before writing percentages.
3. Separate data observations from editorial interpretation.
4. Convert findings into evidence-bounded claim language.
5. Record limitations instead of hiding them.

## Reproduce the toy calculation

```bash
python3 - <<'PY'
import csv
from pathlib import Path
rows = list(csv.DictReader(Path('examples/jstack-data-journalism/sample-public-service-hours.csv').open()))
branches = len(rows)
open_saturday = sum(int(r['saturday_hours']) > 0 for r in rows)
open_sunday = sum(int(r['sunday_hours']) > 0 for r in rows)
print({'branches': branches, 'open_saturday': open_saturday, 'open_sunday': open_sunday})
PY
```

Expected output:

```text
{'branches': 6, 'open_saturday': 4, 'open_sunday': 1}
```
