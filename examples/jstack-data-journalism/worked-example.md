# Worked Example — Fictional Public Service Opening Hours

## 1. Intake

- Story / slug: `examples/fictional-public-service-hours`
- Country / jurisdiction context: fictional tutorial dataset; no real publication-risk jurisdiction
- Country context label: `COUNTRY_CONTEXT_NOT_RELEVANT`
- Artifact type: data note + method summary + findings table
- Status: `RESEARCH_READY` for tutorial use only; not a real-world publication package

## 2. Dataset provenance

- File: `examples/jstack-data-journalism/sample-public-service-hours.csv`
- Source: fictional data created for J-Stack documentation
- License / rights: repository documentation example under the repository license
- Unit of analysis: one fictional branch/service desk
- Row count: 6
- Sensitive data: none
- Known limitation: toy dataset; not statistically meaningful; no real-world inference permitted

## 3. Data dictionary

| Field | Meaning | Notes |
|---|---|---|
| `branch_id` | Fictional branch identifier | Not a real branch |
| `branch_area` | Fictional area grouping | North / central / south / east |
| `weekday_hours` | Weekly weekday opening hours | Numeric |
| `saturday_hours` | Saturday opening hours | Numeric; 0 means closed |
| `sunday_hours` | Sunday opening hours | Numeric; 0 means closed |
| `notes` | Demonstration note | Repeats that the row is fictional |

## 4. Reproducible calculation

```bash
python3 - <<'PY'
import csv
from pathlib import Path
rows = list(csv.DictReader(Path('examples/jstack-data-journalism/sample-public-service-hours.csv').open()))
branches = len(rows)
open_saturday = sum(int(r['saturday_hours']) > 0 for r in rows)
open_sunday = sum(int(r['sunday_hours']) > 0 for r in rows)
areas = sorted(set(r['branch_area'] for r in rows))
print('branches', branches)
print('areas', areas)
print('open_saturday', open_saturday, f'{open_saturday}/{branches}')
print('open_sunday', open_sunday, f'{open_sunday}/{branches}')
PY
```

Expected output:

```text
branches 6
areas ['central', 'east', 'north', 'south']
open_saturday 4 4/6
open_sunday 1 1/6
```

## 5. Findings table

| Finding | Evidence | Safe wording | Evidence grade |
|---|---|---|---|
| 4 of 6 fictional branches list Saturday hours above zero. | Count of `saturday_hours > 0` in CSV. | "In the fictional sample, four of six branches list some Saturday opening hours." | B for the toy dataset only |
| 1 of 6 fictional branches list Sunday hours above zero. | Count of `sunday_hours > 0` in CSV. | "Sunday opening is rare in this fictional sample: one of six branches." | B for the toy dataset only |
| Central branch has the broadest weekend access in the toy data. | B1 has 6 Saturday + 4 Sunday hours. | "The fictional central branch has the most weekend hours in this sample." | B for the toy dataset only |

## 6. Limitations

- This dataset is invented and tiny; it cannot support real claims about any city.
- There is no date field, so changes over time cannot be assessed.
- There is no population, demand, staffing, budget, or service-volume denominator.
- `weekday_hours`, `saturday_hours`, and `sunday_hours` are assumed to be comparable, but that assumption is not independently verified.
- The toy calculation does not prove fairness, inequality, intent, neglect, or policy failure.

## 7. Claim-ledger conversion

Use cautious language:

- **Allowed:** "In the fictional sample, four of six branches list Saturday hours."
- **Allowed:** "The toy dataset would require more context before any public-service fairness claim."
- **Not allowed:** "The city neglects the south" — the sample cannot prove that.
- **Not allowed:** "Officials intentionally restrict weekend access" — no evidence of intent exists.

## 8. GBrain proposal if used in a real story

For a real non-confidential story, propose rather than blindly write:

- Story hub: `stories/<slug>`
- Dataset page: `datasets/<slug>/public-service-hours`
- Method page: `methods/<slug>/opening-hours-analysis`
- Claim pages: `claims/<slug>/saturday-coverage`, `claims/<slug>/sunday-coverage`
- Links: story → dataset; claims → dataset; claims → method

Do not store raw confidential records, source identities, credentials, or provider logs in GBrain.

## 9. Next J-Stack step

After this skill, route to:

1. `jstack-claim-ledger` to turn each quantitative finding into controlled publishable claims.
2. `jstack-countercase` to test innocent explanations and missing denominators.
3. `jstack-legal-risk` only if the example becomes a real story about identifiable actors or institutions.
