# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change executable evidence; A006 decision-lifecycle + bounded executable governance evidence |
| Mobile | Stage 1 IN STUDY — M001-M006 first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real process crash + bounded `SQLITE_FULL`; D006 real transport faults + exact-ref LogMate inbound cursor/apply transfer |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 generated shrinking + mutation/exhaustive-search evidence |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### D006 — LogMate inbound replication progress publication
Canonical: `research/data/D006_logmate_inbound_cursor_atomicity_transfer.md`; fixture: `research/data/fixtures/D006_inbound_cursor_atomicity.py`.

Exact product evidence: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-18`; production identity unknown and default branch is not treated as production.

The product data contract defines `Operation`, `Receipt`, immutable `RevisionHistory`, `SyncState.lastAppliedCursor`, tombstone/restore semantics and explicitly requires local entity mutation + outbound Operation enqueue to share one transaction. Canonical persistence/Sync remain NOT IMPLEMENTED / DATA-001 OPEN. The inbound semantic-apply/cursor publication transaction is not yet frozen.

A Python 3.13.5/Linux/SQLite child-process fixture transfer-tested the missing invariant. Unsafe split publication committed cursor 1 and then terminated before applying server change 1; fresh reopen showed entity `(100,1)`, cursor `1`, `integrity_check=ok`, and the bounded server model returned no remaining change. A single transaction updating entity + cursor, terminated before COMMIT, reopened at entity `(100,1)`, cursor `0`, leaving change 1 replayable. This isolates protocol publication ordering from database structural integrity.

This is not a current LogMate defect: the audited ref does not implement canonical Sync. It is a pre-implementation protocol constraint and validation target.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process-crash and bounded capacity evidence; D006 server death, live-process link interruption, and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries retained; Q004 separates property/oracle strength from search strength.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **LogMate product:** before implementing Sync persistence, define the atomic inbound acceptance unit for entity/tombstone/revision/receipt effects and cursor advancement; crash-test fresh-process replay.
- **Quality:** recovery oracles must compare semantic state with durable cursor/progress state; structural DB integrity alone cannot detect this failure.
- **Mobile:** reproduce the same process-death schedule on the exact Flutter/local persistence stack when available.
- **Architecture:** replication progress is externally relevant state; publication ordering belongs in the protocol contract.
- **Systems:** storage durability and artifact identity remain separate from protocol atomicity.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this bounded sync invariant.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. The latest trustworthy environment evidence still has no `dart` or `flutter` executable; Python 3.13.5 is available.

The highest-value independent block shifted from more synthetic/local transport variants to exact-ref product transfer. D006 now exposes a concrete LogMate pre-implementation invariant: durable progress must not outrun durable semantic acceptance. Do not deepen it with arbitrary model variants. Continue only when LogMate freezes receipt/cursor/batch semantics or when real Flutter/mobile/backend execution becomes available; otherwise choose another track's strongest real evidence gap. Direct F001 Dart/Flutter execution immediately outranks these if a trustworthy SDK appears.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; application-process evidence must not be generalized to power loss or lower-layer ENOSPC.
- LogMate DATA-001 Sync cursor/batch/receipt semantics are OPEN product decisions, not implementation facts.
- Deployment rollback, app-store/browser delivery, GitHub attestation/Sigstore behavior are service/version sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
