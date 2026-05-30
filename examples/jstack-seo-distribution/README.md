# J-Stack SEO Distribution Worked Example

This directory contains a fictional, non-sensitive worked example for `jstack-seo-distribution`.

The example shows how to turn a publication-ready toy story into truthful distribution material without adding factual sting, clickbait, or unsupported claims.

## Scenario

- Story type: tutorial data-story package.
- Dataset/story: the same fictional public-service opening-hours scenario used in the data-journalism example.
- Country context: `COUNTRY_CONTEXT_NOT_RELEVANT` because this is a toy example, not a real publication-risk assessment.
- Publication status: tutorial-only; no external publication or posting is authorized by this example.

## Files

- `story-brief.md` — fictional story brief and claim boundaries.
- `worked-example.md` — complete SEO/distribution package with intent map, metadata, newsletter copy, landing-page outline, and review gates.
- `metadata-length-check.py` — small deterministic check for title/meta/slug length and unsafe wording markers.

## Reproduce the metadata checks

From the repository root:

```bash
python3 examples/jstack-seo-distribution/metadata-length-check.py
```

Expected result:

```text
seo_title_chars=44 limit=60 status=PASS
meta_description_chars=143 limit=160 status=PASS
slug_chars=28 limit=80 status=PASS
unsafe_terms_hits=[]
```

## Review questions this example demonstrates

1. Does the search title stay within the evidence boundary?
2. Does the meta description describe the tutorial rather than imply a real public-service failure?
3. Are search intent, newsletter copy, and landing-page sections separated?
4. Is unsupported language such as "scandal", "failure", or "exposed" excluded?
5. Is human approval still required before real publication or posting?
