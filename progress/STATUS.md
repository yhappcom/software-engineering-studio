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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real process crash + bounded capacity + syscall `ENOSPC` write fault + syscall `fsync/fdatasync=EIO`; D006 real transport faults + exact-ref LogMate inbound cursor/apply transfer |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search evidence; Q006 real process-crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 real asymmetric signing + bounded reproducible build + exact-ref LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — syscall-level synchronization failure
Canonical: `research/data/D005_syscall_fsync_eio_fault_injection.md`; fixture: `research/data/fixtures/D005_ld_preload_fsync_eio_boundary.py`.

F001 was attempted first: no `dart` or `flutter` executable was found, so direct Dart/Flutter validation remains OPEN rather than simulated.

Linux/Python/SQLite validation compiled an `LD_PRELOAD` shim that allows writes but returns `EIO` at selected target `fsync`/`fdatasync` calls under rollback-journal `synchronous=FULL`. The control path emitted three matching sync calls and committed `[100,200]`. Independently reset failures at sync calls 1, 2 and 3 each surfaced extended code 1034 `SQLITE_IOERR_FSYNC`; fresh reopen observed only baseline `[100]` and `PRAGMA integrity_check=ok`. A failure ordinal beyond the observed successful sync sequence did not inject and the transaction committed.

**VALIDATION / SYNTHESIS:** this materially changes D005's failure class from write denial/capacity to persistence synchronization failure. It supports the bounded distinction `write succeeded ≠ durability synchronization succeeded`. It does **not** establish physical power-loss safety, truthful successful fsync semantics, short/torn-write behavior, WAL/checkpoint behavior, mobile persistence, or production durability.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process crash, logical capacity, syscall write denial and syscall sync failure; D006 server death, live-process link interruption and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 has real asymmetric-signature, bounded compiler reproducibility and exact-ref product build-identity evidence.

## Cross-track handoffs
- **Mobile/Quality:** when Flutter/device infrastructure exists, reproduce storage/sync failure and process restart on the exact persistence stack with semantic recovery oracles.
- **Systems:** durability evidence must distinguish write, sync, truthful sync, short/torn write, directory persistence, checkpoint and actual power-loss/device behavior.
- **LogMate:** D006 inbound cursor/effect atomicity remains a pre-implementation contract dependency; this D005 fixture makes no claim about current product persistence.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical files were edited and no evidence there changes this storage mechanism.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target and must be retried whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux/GCC are available.

D005 now has process death, logical capacity, syscall `ENOSPC`, and a distinct syscall synchronization-EIO failure. Do not repeat equivalent ordinal or error-code variants. If Dart/Flutter remains unavailable, prefer a genuinely different evidence rung: short/torn write, WAL/checkpoint, actual platform/power-loss transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime and build behavior are version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; injected syscall failures must not be generalized to physical device/power-loss behavior.
- LogMate DATA-001 Sync cursor/batch/receipt semantics remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.
- Exact Flutter SDK/ref and release/production identity for LogMate remain release-evidence dependencies.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
