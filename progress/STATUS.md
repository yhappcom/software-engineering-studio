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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real process crash + bounded capacity + syscall `ENOSPC` + syscall sync-EIO + bounded short-write progress handling; D006 real transport faults + exact-ref LogMate inbound cursor/apply transfer |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search evidence; Q006 real process-crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 real asymmetric signing + bounded reproducible build + exact-ref LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — positive short write versus zero progress
Canonical: `research/data/D005_short_write_progress_boundary.md`; fixture: `research/data/fixtures/D005_short_write_progress_boundary.py`.

F001 was attempted first: no `dart` or `flutter` executable was found, so direct Dart/Flutter validation remains OPEN rather than simulated.

Linux/Python/SQLite validation compiled an `LD_PRELOAD` shim that intercepts the first target database `pwrite/pwrite64`. Returning 256 bytes from a 512-byte request still produced a successful transaction and fresh-reopen semantic state `[100,200]`. Returning zero bytes from the same requested size surfaced code 13 `SQLITE_FULL`; fresh reopen preserved baseline `[100]`. Both cases had `PRAGMA integrity_check=ok`.

Current official SQLite Unix VFS source explains the distinction: `unixWrite()` retries positive partial progress by advancing the buffer/offset and reducing the remaining amount; non-progress crosses its failure path. **VALIDATION / SYNTHESIS:** a syscall short write is a progress condition, not automatically a failed logical write. This also sharpens the queue: syscall short write and torn durable write are distinct mechanisms. The fixture does not establish torn-write, physical power-loss/device, WAL/checkpoint, mobile persistence, or production durability.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 process crash, logical capacity, syscall write denial, syscall sync failure and short-write progress; D006 server death, live-process link interruption and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 has real asymmetric-signature, bounded compiler reproducibility and exact-ref product build-identity evidence.

## Cross-track handoffs
- **Quality:** storage fault campaigns should record requested/returned byte counts and distinguish positive short progress from zero/negative failure.
- **Mobile/Quality:** when Flutter/device infrastructure exists, reproduce storage/sync failure and process restart on the exact persistence stack with semantic recovery oracles.
- **Systems:** do not treat syscall short-write handling as torn-write or power-loss durability evidence.
- **LogMate:** D006 inbound cursor/effect atomicity remains a pre-implementation contract dependency; this D005 fixture makes no claim about current product persistence.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical files were edited and no evidence there changes this storage mechanism.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target and must be retried whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux/GCC are available.

D005 now has process death, logical capacity, syscall `ENOSPC`, synchronization-EIO, and bounded positive-short-write versus zero-progress evidence. Do not repeat equivalent byte-size/ordinal variants. If Dart/Flutter remains unavailable, prefer a genuinely different evidence rung: torn durable write/power-loss semantics, WAL/checkpoint, actual platform transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime and build behavior are version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior are platform/version sensitive.
- SQLite durability depends on documented OS/filesystem/device assumptions; injected syscall failures must not be generalized to physical device/power-loss behavior.
- LogMate DATA-001 Sync cursor/batch/receipt semantics remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.
- Exact Flutter SDK/ref and release/production identity for LogMate remain release-evidence dependencies.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
