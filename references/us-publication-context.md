# US Publication Context Overlay — J-Stack v1.1

This reference adds a United States publication-safety layer to every J-Stack skill. It is a workflow checklist, not legal advice. US media law is federal plus state-specific; do not assume one nationwide answer where state law controls.

## When the US Overlay Applies

Apply this overlay whenever any of these has a US nexus:

- the publication venue, audience, platform, publisher, author, server, or monetization is US-based;
- a subject, source, plaintiff, employer, agency, court, university, company, or dataset is US-based;
- the story uses US records, US litigation, US government data, US elections, US platforms, US copyrighted works, or US social-media material;
- litigation, subpoena, takedown, privacy, employment, securities, election, or consumer-protection risk could arise in the United States.

## Baseline US Differences From a German/EU Press-Law Workflow

1. **Federalism first.** Always identify: federal law, relevant state(s), local court/agency, publication venue, source location, subject domicile, and likely plaintiff forum.
2. **First Amendment frame.** US review starts from speech protection, public concern, newsworthiness, viewpoint neutrality, prior-restraint skepticism, and separation between fact, opinion, rhetorical hyperbole, and advocacy.
3. **Defamation standards differ.** Classify each affected subject as public official, public figure, limited-purpose public figure, private figure, corporation, government body, or group. Track actual malice, negligence, falsity, fault, damages, and republication risk where applicable.
4. **No German-style universal pre-publication right of reply.** In the US, request-for-comment is a strong fairness and risk-mitigation practice, but not a single nationwide statutory `Gelegenheit zur Stellungnahme`. Some contexts still make outreach strategically essential.
5. **Anti-SLAPP is state-specific.** Some states have strong anti-SLAPP protections; others are weak or unavailable. Never treat anti-SLAPP as automatic.
6. **Public-record and fair-report protections matter.** Distinguish court filings, hearing transcripts, agency records, police statements, legislative proceedings, FOIA records, and independently verified facts.
7. **Privacy torts are separate.** Check false light, intrusion upon seclusion, publication of private facts, appropriation/right of publicity, doxxing, revenge-porn/nonconsensual-image statutes, and state constitutional privacy where relevant.
8. **Source protection is uneven.** Reporter shield laws, privilege, subpoena resistance, and confidential-source protections vary by jurisdiction and proceeding type. Federal law is not a universal shield.
9. **Recording and access rules vary.** Wiretap/recording consent, trespass, computer access, scraping, CFAA/state computer-crime theories, public-record terms, and platform terms can matter before publication.
10. **Copyright/fair use is central.** Quotes, photos, screenshots, videos, leaked documents, datasets, thumbnails, and embedded social posts need fair-use, license, DMCA, and attribution review.
11. **Commercial speech and endorsements.** Sponsored content, affiliate links, native ads, product claims, creator endorsements, political ads, and influencer-style distribution may trigger FTC, platform, election, securities, or consumer-protection rules.
12. **Data and minors.** State privacy laws, biometric laws, education records, health facts, children/minors, victims, immigration status, and employment records require separate minimization and public-interest analysis.
13. **Corrections/retractions.** Retraction statutes and correction practice can affect damages or litigation posture; post-publication workflow must preserve exact publication and correction history.
14. **Local counsel flag.** If state-specific law materially affects outcome, mark `US_LOCAL_COUNSEL_REQUIRED` rather than inventing certainty.

## US Status Labels

Use these labels consistently in skill outputs, claim ledgers, legal-risk registers, and ship gates:

- `US_CONTEXT_APPLIES`
- `US_CONTEXT_NOT_REQUIRED`
- `US_STATE_LAW_UNCLEAR`
- `US_LOCAL_COUNSEL_REQUIRED`
- `FIRST_AMENDMENT_REVIEW_REQUIRED`
- `DEFAMATION_REVIEW_REQUIRED`
- `PRIVACY_TORT_REVIEW_REQUIRED`
- `ANTI_SLAPP_CHECK_REQUIRED`
- `FAIR_USE_REVIEW_REQUIRED`
- `SOURCE_PROTECTION_REVIEW_REQUIRED`
- `RECORDING_ACCESS_REVIEW_REQUIRED`
- `FTC_PLATFORM_REVIEW_REQUIRED`

## Minimum US Review Questions

Before any serious US-nexus story is called ready, answer:

- Which US state(s), federal forum, platform, and audience are relevant?
- Is each challenged statement fact, opinion, interpretation, rhetorical hyperbole, allegation, official allegation, or verified finding?
- Is each subject a public official/public figure/limited-purpose public figure/private figure/corporation/group?
- What is the evidence of truth or substantial truth?
- What counterevidence, denial, correction, or innocent explanation exists?
- Was request-for-comment appropriate? If yes, what exact allegations were sent, to whom, through which channel, and with what deadline?
- Does fair-report, public-record, opinion, neutral-reportage, or other privilege potentially apply, and is it state-specific?
- Are privacy, source-protection, recording, access, copyright, FTC/platform, or election/securities issues present?
- Does state anti-SLAPP/retraction law change litigation posture?
- Is local counsel needed before publication?

## Skill-by-Skill US Adjustments

### Editorial command skills

- `jstack-command-center`: add US jurisdiction routing early; assign legal-risk, source-protection, copyright/fair-use, and platform-policy review where US nexus exists.
- `jstack-office-hours`: test whether a US story is public-interest journalism, protected opinion, advocacy, commercial speech, or high-risk allegation before resources are spent.
- `jstack-editorial-line`: preserve viewpoint and ideological voice, but do not let partisan framing convert weak factual support into defamatory fact assertion.
- `jstack-assignment-desk`: assign state-law, public-record, FOIA, anti-SLAPP, source-protection, recording-consent, and fair-use research tasks explicitly.

### Research skills

- `jstack-source-map`: separate federal, state, county, municipal, court, agency, campaign-finance, corporate, university, police, and platform sources.
- `jstack-primary-source-research`: distinguish FOIA, state open-records acts, PACER/dockets, SEC/EDGAR, FEC/state election records, court rules, and sealed/protective-order limits.
- `jstack-osint-research`: screen scraping, account access, geolocation, metadata, recording, impersonation, platform terms, CFAA/state-computer-crime, and doxxing risks.
- `jstack-data-journalism`: document data provenance, government/public-record status, statistical uncertainty, privacy minimization, and state/federal data-use restrictions.
- `jstack-interview-prep`: draft US request-for-comment and adversarial interview packages; track exact allegation text and deadline without treating it as a universal statutory right.
- `jstack-document-review`: mark court filings, official allegations, sealed material, protective orders, leaks, copyright status, authenticity, and fair-report/fair-use posture.
- `jstack-investigate`: classify US allegations by defamation/privacy/copyright/source-risk exposure while separating public-record facts from independent assertions.

### Facts and claims skills

- `jstack-claim-ledger`: add US subject status, defamation fault standard, publication privilege, fair-report/fair-use flags, and request-for-comment status to each risky claim.
- `jstack-evidence-ledger`: preserve original source provenance, custody, retrieval date, public-record basis, license/fair-use rationale, and contradiction history.
- `jstack-entity-graph`: track US domicile, official role, public-figure status, corporate/government status, aliases, related entities, and jurisdiction links.
- `jstack-timeline`: distinguish event date, filing date, publication date, correction date, retraction demand, response deadline, and litigation/subpoena milestones.
- `jstack-countercase`: build US defenses and attacks: falsity, actual malice, negligence, damages, opinion, fair report, privacy invasion, copyright misuse, and public-interest rebuttals.

### Safety skills

- `jstack-legal-risk`: run the full US matrix: First Amendment, defamation, privacy torts, public-record privilege, anti-SLAPP, retraction, source protection, recording/access, copyright/fair use, FTC/platform.
- `jstack-ethics-check`: separate what US law may allow from what ethical journalism requires; test fairness, harm, private facts, minors, vulnerable people, and request-for-comment.
- `jstack-redteam`: include personas for plaintiff lawyer, anti-SLAPP counsel, platform moderator, FOIA/open-records skeptic, source-protection lawyer, copyright claimant, and ordinary US juror.
- `jstack-ship`: do not mark `PUBLICATION_READY` until US context is either not applicable or the required US review labels are resolved or escalated.

### Writing and distribution skills

- `jstack-draft`: use US-safe wording: attribute allegations, distinguish official records from proven facts, avoid unsupported criminal/misconduct labels, and keep opinion clearly non-factual where intended.
- `jstack-copy-desk`: headline, dek, captions, thumbnails, pull quotes, and social snippets must not overstate the body; US defamation risk often appears in compressed packaging.
- `jstack-seo-distribution`: search snippets and metadata are republication surfaces; avoid clickbait that adds unsupported factual sting or commercial/FTC confusion.
- `jstack-social-package`: apply the same US claim discipline to X/LinkedIn/short video/podcast scripts; preserve context and avoid defamatory truncation.

### Post-publication and memory skills

- `jstack-postpub`: preserve retraction/correction requests, takedowns, legal letters, platform notices, subpoena contacts, and updates with exact timestamps and unchanged archival copies.
- `jstack-gbrain-memory`: store US-context labels, jurisdiction, request-for-comment record, public-record provenance, fair-use rationale, and legal-review status without storing secrets or protected source data.

## Ship-Gate Rule for US Edition v1.1

A US-nexus story can only move to `PUBLICATION_READY` when one of these is true:

1. `US_CONTEXT_NOT_REQUIRED` is documented; or
2. all applicable US review labels are resolved with supporting notes; or
3. unresolved issues are explicitly escalated to `US_LOCAL_COUNSEL_REQUIRED`, `LEGAL_REVIEW_REQUIRED`, or `NOT_READY`.

Do not use this reference to give legal advice. Use it to prevent the agent from pretending that German/EU press-law gates, or generic journalism instincts, are sufficient for US publication risk.
