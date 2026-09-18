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
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search evidence; Q006 real process-crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 all initiated with executable/professional evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### Q006 — Real process-crash recovery-oracle discrimination
Canonical: `research/quality/Q006_real_crash_recovery_oracle_transfer.md`; fixture: `research/quality/fixtures/Q006_real_crash_recovery_oracle.py`.

Python 3.13.5/Linux/SQLite child-process evidence transfer-tested the D006 cursor/effect invariant as a Quality recovery-oracle problem. Unsafe cursor-first publication committed cursor 1 and terminated before entity apply. Fresh reopen showed entity `(100,1)`, cursor `1`, no modeled replay, and `integrity_check=ok`: a structural DB-health oracle passed while the independent semantic recovery oracle failed. A single transaction terminated before COMMIT reopened at entity `(100,1)`, cursor `0`, preserving replayability; both oracles passed.

This closes Q006's named real process kill/restart + durable-storage recovery gap at a bounded Python/Linux/SQLite level. It does not establish Dart/Flutter/mobile/backend/power-loss/production recovery.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Foundations F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/debt/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process-crash and bounded capacity evidence; D006 server death, live-process link interruption, and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 separates property/oracle strength from search strength; Q006 now demonstrates structural-vs-semantic recovery-oracle discrimination under real process death.
- **Systems:** S001-S006 trust/security/performance/build/release/rollback evidence retained.

## Cross-track handoffs
- **Mobile:** reproduce the Q006 structural-vs-semantic recovery oracle on the exact Flutter/local persistence stack under process death.
- **Data:** recovery acceptance must compare semantic state with durable cursor/progress and replayability; DB structural integrity alone is insufficient.
- **Architecture:** replication progress is externally relevant state and belongs in protocol publication contracts.
- **Systems:** release recovery gates must not substitute storage health or process liveness for semantic recovery acceptance.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this bounded recovery mechanism.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. The latest trustworthy environment evidence still has no `dart` or `flutter` executable; Python 3.13.5 is available.

Q006 now has a materially stronger real process-crash/restart rung, so do not repeat equivalent local crash variants. Highest-value independent work should seek a different real transfer boundary: direct Dart/Flutter/mobile first if the SDK appears; otherwise a tractable real CI/signing/build artifact path, natural product/ADR transfer, or a genuinely different storage/network/platform fault. Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Flutter web build/service-worker/isolate/import and plugin/platform behavior are version-sensitive.
- Browser/PWA install/update/offline/background/storage APIs and iOS/iPadOS behavior are version-sensitive.
- Android storage/permission/backup and Apple Data Protection/Keychain behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; application-process evidence must not be generalized to power loss or lower-layer ENOSPC.
- LogMate DATA-001 Sync cursor/batch/receipt semantics are OPEN product decisions, not implementation facts.
- Deployment rollback, app-store/browser delivery, GitHub attestation/Sigstore behavior are service/version sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
