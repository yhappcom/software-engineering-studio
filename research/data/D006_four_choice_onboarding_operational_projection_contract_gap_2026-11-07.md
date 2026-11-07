# D006 — Four-choice onboarding versus three-value remote operational projection

**Evidence date:** 2026-11-07 Asia/Seoul. **Status:** SOURCE / CROSS-CONTRACT CONTRADICTION / ENGINEERING JUDGMENT / OPEN. No product or Studio runtime tests executed.

## Exact source identity and limits

- Product: `yhappcom/logmate → verify/w013-target-file-resume-20261107@472e3fa90c4e5f8c346aadc19d42f9e6ddd7ef24 → pubspec.yaml 1.0.0+1 → 2026-11-07`. Production/deployed ref unknown. Open Draft PR #46; 61 branches and 12 open PRs enumerated this run. PR #42–46 are a separate stacked product-evidence chain from #39–41; none is assumed merged.
- `MASTER.md §0`: four **owner-approved** first-use choices, including `Restore from backup file`; current main implements three choices; Restore Activation NOT IMPLEMENTED.
- `docs/specs/sync-activity-member-operations-spec.md`: remote operational projection currently declares `onboardingMethod = newLogbook | previousTotal | import | null`. This is a *three-method* enum with no explicit restore case. The same document says local onboarding state is canonical and remote projection is non-authoritative.
- `docs/specs/backup-file-flow-spec.md`: initial recovery versus intentional global Restore differ in Generation/Event semantics. A file picked, validated, staged or reviewed is not an activated logbook.
- `docs/specs/local-first-manual-delta-sync-contract.md`: automatic and manual Delta approved; production server Sync and metadata writer NOT IMPLEMENTED.

## New discriminator: approved UI choice is not necessarily a completed method

The four-choice first-use policy and three-value operational projection cannot represent all approved terminal onboarding outcomes without a **new explicit mapping decision**. In particular, silently mapping successful `Restore from backup file` to `import`, `newLogbook` or `null` loses the source/semantics distinction. But simply adding `restore` to the server enum now is also premature: no implementation or versioned wire migration is approved, and choosing a file does not establish successful Activation.

**Two independent authority axes must remain separate:**
1. Local setup state (notStarted / inProgress / completed, method and accepted completion) is routing authority. File picker, B1 validation, staging, Review and Activation are distinct steps.
2. Remote `accountOperationalMeta/{uid}` is a best-effort server-observed support projection written by the real authenticated Sync path, not a source of local completion or a standalone activity endpoint.

**Failure and ambiguity matrix (contract-derived, not executed):**

| Event | Local setup authority | Remote projection / member reporting |
| --- | --- | --- |
| Restore choice selected; file picker cancelled | Not completed | Must not claim completed restore |
| File B1 valid; isolated staging Review shown | Not completed | Must not claim completed restore |
| Activation fails or is rejected | Not completed | Must not claim completed restore |
| Accepted Activation receipt, same verified UID | Completed only after durable local acceptance | Needs a versioned, explicit method representation; currently OPEN |
| Activation completed offline; no Sync yet | Local completion stands | Remote unknown/stale is legitimate, not proof of incomplete |
| Auto Sync after accepted Activation | No change to local authority | May project status per approved semantics, but cannot advance `lastSyncAt` |
| Explicit successful Manual Sync | No change to local authority | May update projection and server-time `lastSyncAt` after authenticated success |
| Manual Sync fails or is indeterminate | No change to local authority | Must not assert success or advance activity timestamp |

The existing three-method projection is a **documented contract coverage gap**, not evidence that current code misclassifies real restored users; the fourth UI and Activation remain unimplemented.

## Required product handoff (not a Studio policy decision)

Before implementing W-013 Activation plus the production operational metadata writer, the product owner/implementer must resolve:
- whether successful first-use file Restore is a distinct `onboardingMethod` wire value, and its exact stable spelling, schema/wire version and backward-compatible report behavior;
- whether *initial recovery* and *intentional global replacement* share the same local setup method or have separate reporting metadata; avoid treating an existing user's later Restore as first-use onboarding;
- the authoritative completion point (durable Activation receipt, not staging), including crash/restart and offline acceptance;
- unknown/unrecognized enum values in old member tooling: preserve `unknown` rather than coercing to `import` or `incomplete`;
- the server-owned authenticated writer and explicit Manual versus Automatic activity semantics.

## Independent acceptance oracles

At an exact product implementation ref, exercise: (1) cancel, invalid file, B1 valid/staged, and accepted Activation; (2) restart between Activation and projection; (3) offline accepted Activation then Auto Catch-up; (4) zero-delta explicit Manual Sync; (5) failed/unauthenticated/indeterminate Sync; (6) old report reader encountering new method value; (7) same UID with later intentional Restore, not a fresh onboarding. Assert local canonical state, remote projection, server-time activity field and member-report label separately. **No tests were executed in this Studio analysis.**

## RELATED DOMAIN CHECK

- **Architecture:** local canonical state versus derived operational projection; versioned interface evolution and backward compatibility.
- **Mobile:** native and running PWA offline/cancel/restart/provider differences; real file custody and Activation remain separate gates.
- **Data:** W-013 generation/restore lineage and D006 projection wire contract; no synthetic completion or new server writer.
- **Quality:** fail-closed negative matrix, crash boundary, exact-source fixture and old-reader compatibility.
- **Systems:** verified UID, server-only metadata authority, deletion erasure of operational projection, no heartbeat endpoint.
- **Foundations:** enum representation, partial-state observations and asynchronous failure ordering.

## HANDOFFS

- **LogMate/Codex Work, READ-ONLY advisory:** reconcile `MASTER.md §0`, `sync-activity-member-operations-spec.md` and Backup Activation semantics before coding the fourth method or server writer. No product edits, PRs, CI dispatch or deployment authorized by this Studio note.
- **Studio D005/S007:** ensure post-deletion/owner-switch reporting cannot carry an earlier owner's onboarding projection. This is a future acceptance requirement, not a demonstrated current failure.

**Validation state:** contract comparison only; no release PASS, no observed production defect, no approval of a new product enum or migration.
