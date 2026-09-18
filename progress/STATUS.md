# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change + natural LogMate evolution transfer; A006 decision governance evidence |
| Mobile | Stage 1 IN STUDY — M001-M006 first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage faults + torn-image + WAL crash/checkpoint + reader progress + live Online Backup concurrency |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 real signing + bounded reproducibility + LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — Online Backup API under live WAL writes restarts and includes the concurrent commit
Canonical: `research/data/D005_online_backup_live_wal_concurrency.md`; fixture: `research/data/fixtures/D005_online_backup_live_wal_concurrency.py`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was found; direct Dart/Flutter validation remains OPEN rather than simulated.

Python 3.13.5 / SQLite 3.46.1 / Linux WAL execution began an incremental backup from a 502-page source, then committed one new row through a separate source connection after two backup progress callbacks. Remaining pages first fell 497→492, then rose to 497 after the external commit, matching SQLite's documented automatic-restart behavior. The completed destination reached `SQLITE_DONE`, contained all 501 rows including the post-start concurrent row, and returned `integrity_check=ok`.

**VALIDATION / SYNTHESIS:** Online Backup is database-aware and materially stronger than raw main-file copy for live WAL state, but an incremental backup under external writes is not safely modeled as a fixed semantic cut at invocation time. Completion, semantic completeness and bounded progress/starvation are separate properties. Official high-level “snapshot when copying commenced” wording must not be operationalized as a guaranteed invocation-time point-in-time cut without a stronger transaction/mechanism contract; the current C API documentation explicitly describes restart after external modification.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/process/storage faults, short-write/torn-image evidence, WAL crash/main-file completeness, reader/checkpoint concurrency and live-writer Online Backup behavior; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 real asymmetric signature, bounded compiler reproducibility and exact-ref product build-identity evidence.

## Cross-track handoffs
- **Quality:** backup tests need distinct structural-integrity, semantic-completeness, completion and bounded-progress/starvation oracles.
- **Mobile:** reproduce journal/checkpoint/Online Backup behavior on the exact Flutter/Android/iOS persistence stack when available.
- **Systems:** if Online Backup is productized, timeout/resource budget, temporary destination lifecycle and atomic publication become operational inputs.
- **LogMate:** retained exact-ref context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19`; production identity unknown. No claim that current LogMate uses SQLite WAL or Online Backup API. Backup consistency point and concurrent-write inclusion semantics remain product decisions.
- **Design Studio / Web Manager / Marketing Manager:** bounded repository search considered; no canonical files edited and no evidence found that changes this low-level mechanism.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux are available.

D005 has now advanced through actual WAL crash/main-file completeness, active-reader checkpoint progress, and live-writer Online Backup behavior. Do not repeat row-count, reader-count, checkpoint-mode or single-concurrent-write backup variants. If Dart/Flutter remains unavailable, prefer backup interruption/safe destination publication, sustained-writer starvation only if it adds a materially different failure class, physical/platform transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- SQLite WAL/backup behavior depends on SQLite version, wrapper, VFS/OS/filesystem/device and synchronization mode; current process/concurrency evidence is not hard-power-loss evidence.
- LogMate Sync and backup consistency mechanisms remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
