# Worked Example — J-Stack SEO Distribution

## 1. Intake

- Skill: `jstack-seo-distribution`.
- Artifact type: SEO/distribution package.
- Story: fictional service-desk opening-hours data story.
- Country / jurisdiction context: `COUNTRY_CONTEXT_NOT_RELEVANT`.
- Status: `TUTORIAL_ONLY_NOT_FOR_PUBLICATION`.
- Required upstream artifact: `examples/jstack-seo-distribution/story-brief.md`.

## 2. Search-intent map

| Reader intent | Query examples | Distribution response | Evidence boundary |
| --- | --- | --- | --- |
| Learn a workflow | `data journalism worked example`, `claim ledger headline example` | Present as a tutorial package. | Do not imply real public-service findings. |
| Improve metadata | `truthful SEO title journalism`, `safe meta description investigation` | Show title/meta variants and length checks. | Metadata cannot add claims absent from the story. |
| Build newsletter copy | `newsletter teaser evidence limits` | Provide restrained teaser copy and review gate. | Teaser must not be more aggressive than the article. |
| Find real service hours | `city office weekend hours` | Exclude / redirect. | This example is fictional and not a directory. |

## 3. Recommended metadata

```yaml
seo_title: "Toy Data Story: Fictional Service Desk Hours"
meta_description: "A J-Stack SEO example that packages a fictional service-hours dataset with truthful search intent, metadata, newsletter copy, and review gates."
slug: "toy-service-hours-data-story"
canonical_topic: "jstack-worked-examples"
status: "review-required-before-publication"
```

Why this passes:

- The title says `Toy` and `Fictional`.
- The meta description says `example` and `fictional`.
- The slug is descriptive and not sensational.
- No line claims a real public-service failure.

## 4. Headline and deck options

| Option | Text | Status | Reason |
| --- | --- | --- | --- |
| H1 | Toy Data Story: Fictional Service Desk Hours | Recommended | Clear, truthful, and tutorial-framed. |
| H2 | How to Package a Data-Journalism Finding Without Overclaiming | Acceptable | Focuses on method, not a real allegation. |
| H3 | Weekend Hours Across Six Fictional Branches | Acceptable | Accurate, but less useful for workflow search intent. |
| Reject | Service Access Failure Exposed | Reject | Adds unsupported factual sting and real-world implication. |
| Reject | City Offices Deny Weekend Access | Reject | Implies real subjects and a conclusion not in evidence. |

## 5. Landing-page outline

1. **What this example is** — fictional tutorial, no real-world claim.
2. **Input artifacts** — toy dataset and story brief.
3. **Claim boundaries** — what each claim proves and does not prove.
4. **SEO package** — title, meta, slug, canonical topic.
5. **Distribution variants** — newsletter and social handoff, not automatic publication.
6. **Review gates** — evidence, legal/ethics, editor, and human approval.
7. **Next J-Stack routing** — `jstack-social-package` or `jstack-ship` only after review.

## 6. Newsletter teaser

> New J-Stack worked example: a fictional service-hours dataset becomes a cautious distribution package. The example shows how to write search metadata, a landing-page outline, and newsletter copy that stay inside the claim ledger instead of turning a toy dataset into a real-world allegation.

Review note: this teaser is safe because it repeatedly marks the example as fictional and method-focused.

## 7. Audience notes

- Primary audience: journalists, editors, agent-builders, and researchers who need evidence-safe packaging.
- Secondary audience: readers comparing J-Stack to generic AI writing workflows.
- Avoided audience: people looking for actual branch opening hours or complaints about a real service.
- Distribution risk: snippets are short and can become more aggressive than the story; keep `fictional`, `toy`, or `example` in compressed surfaces.

## 8. Headline-vs-evidence check

| Distribution surface | Allowed | Not allowed |
| --- | --- | --- |
| SEO title | Toy / fictional / data-story language. | Real city, scandal, failure, corruption, denial. |
| Meta description | Method and packaging focus. | Claiming public harm or official misconduct. |
| Newsletter | Cautious learning objective. | Urgent call to action against real actors. |
| Social handoff | Link to example and method. | Viral outrage framing or unsupported allegations. |

## 9. GBrain proposal

If imported into GBrain, propose only non-secret tutorial pages:

- `projects/jstack/examples/seo-distribution-toy-service-hours`
- Tags: `jstack`, `worked-example`, `seo-distribution`, `claim-ledger-safe`
- Link to:
  - `projects/jstack/examples/data-journalism-public-service-hours`
  - `concepts/jstack-claim-boundary`

Do not write real campaign, source-contact, or publication-decision pages from this tutorial.

## 10. Review gates

Before any real use, confirm:

- [ ] The story itself is publishable and has passed claim-ledger review.
- [ ] Country/jurisdiction context is real, not `COUNTRY_CONTEXT_NOT_RELEVANT`.
- [ ] SEO and newsletter copy do not add allegations.
- [ ] Link previews, captions, and thumbnails match the article body.
- [ ] Human approval is explicit before posting, sending, or publishing.

## 11. Next J-Stack routing

- Use `jstack-social-package` to create platform-specific drafts after this package is approved.
- Use `jstack-ship` before any real publication or external distribution.
- Use `jstack-postpub` only after a human-approved publication exists.
