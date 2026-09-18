# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-19  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002-F006 initiated with executable/model evidence |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 repeated-change evidence + natural exact-ref LogMate evolution transfer; A006 decision-lifecycle + bounded governance evidence |
| Mobile | Stage 1 IN STUDY — M001-M006 first professional/model boundaries; direct Flutter/native/browser/EFB transfer OPEN |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real process crash + bounded capacity + syscall `ENOSPC` + sync-EIO + short-write progress + bounded torn durable-image model; D006 real transport faults + exact-ref LogMate inbound cursor/apply transfer |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search evidence; Q006 real process-crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 real asymmetric signing + bounded reproducible build + exact-ref LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — torn durable image is not syscall short progress
Canonical: `research/data/D005_torn_write_recovery_model.md`; fixture: `research/data/fixtures/D005_torn_write_recovery_model.py`.

F001 was attempted first: no `dart` or `flutter` executable was found, so direct Dart/Flutter validation remains OPEN rather than simulated.

A Python 3.13.5/Linux executable MODEL divides a 4096-byte page into eight 512-byte sectors and models power interruption after three sectors of the new page become durable. The resulting page is neither the independently defined old nor new atomic state. A complete old pre-image reconstructs the accepted old state; a deliberate partial-pre-image mutant fails the same oracle.

Current SQLite primary material explicitly assumes rollback-mode sector/page writes need not be atomic and documents crash-test VFS simulation of incomplete, reordered and corrupted unsynchronized writes. **VALIDATION / SYNTHESIS:** API-level short-write progress and post-crash torn durable state are different failure classes. This run is MODEL evidence only; it does not execute SQLite's crash VFS or establish physical device/power-loss, WAL/checkpoint or mobile durability.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process crash, logical capacity, syscall write denial, syscall sync failure, short-write progress and torn durable-image model; D006 server death, live-process link interruption and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 has real asymmetric-signature, bounded compiler reproducibility and exact-ref product build-identity evidence.

## Cross-track handoffs
- **Quality:** treat syscall short-return and post-crash torn-persistence as distinct injected failure classes with distinct observations/oracles.
- **Mobile/Quality:** when Flutter/device infrastructure exists, reproduce storage/sync failure and process restart on the exact persistence stack with semantic recovery oracles.
- **Systems:** storage atomicity/PSOW are capability assumptions, not consequences of a successful application write.
- **LogMate:** D006 inbound cursor/effect atomicity remains a pre-implementation contract dependency; this D005 model makes no claim about current product persistence.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical files were edited and no decision there changes this low-level persistence mechanism.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target and must be retried whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux/GCC are available.

D005 now has process death, logical capacity, syscall `ENOSPC`, synchronization-EIO, bounded positive-short-write behavior, and a separate torn durable-image model. Do not repeat equivalent byte/sector-count variants. If Dart/Flutter remains unavailable, prefer a genuinely stronger evidence rung: actual SQLite crash-VFS/WAL behavior, physical/platform transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime and build behavior are version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; injected syscall faults and the torn-write model must not be generalized to physical device/power-loss behavior.
- LogMate DATA-001 Sync cursor/batch/receipt semantics remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.
- Exact Flutter SDK/ref and release/production identity for LogMate remain release-evidence dependencies.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
