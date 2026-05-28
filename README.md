# J-Stack — GBrain-Integrated Journalism Skills for Hermes Agent

Status: **publish-ready candidate draft**, not yet installed into the active Hermes profile and not yet published.  
Generated: 2026-05-28T10:30:07+00:00  
Owner: Markus Bauer / Hermes draft workspace

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

## Skill Families

- Editorial command: command center, office hours, editorial line, assignment desk.
- Research: source map, primary-source research, OSINT, data journalism, interview prep, document review, investigation.
- Facts and claims: claim ledger, evidence ledger, entity graph, timeline, countercase.
- Safety: legal risk, ethics check, red-team, ship gate.
- Writing and distribution: draft, copy desk, SEO/distribution, social package.
- Post-publication and memory: postpub, GBrain memory.

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

## Installation Candidate

This is a draft package. To install later, copy selected `skills/<skill>/` directories into a Hermes skill source or publish the repository through the Hermes skills workflow. Do not install globally until reviewed.

## Safety Defaults

- No automatic publishing.
- No source contact without approval.
- No invented citations.
- No secrets in GBrain.
- No unsupported criminal or misconduct labels.
- No claim ships above evidence grade.
