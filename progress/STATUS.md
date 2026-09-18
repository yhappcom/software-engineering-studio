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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback-process/storage-fault evidence + torn-image model + real WAL crash/checkpoint/main-file-copy boundary; D006 real transport faults + exact-ref LogMate inbound cursor/apply transfer |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search evidence; Q006 real process-crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 real asymmetric signing + bounded reproducible build + exact-ref LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — committed WAL state can outrun the main database file
Canonical: `research/data/D005_wal_crash_checkpoint_backup_boundary.md`; fixture: `research/data/fixtures/D005_wal_crash_checkpoint_backup_boundary.py`.

F001 was attempted first: no `dart` or `flutter` executable was found, so direct Dart/Flutter validation remains OPEN rather than simulated.

Python 3.13.5 / SQLite 3.46.1 / Linux WAL execution disabled auto-checkpointing, established baseline row `100`, then had a child commit row `200` and terminate via `os._exit(77)` without clean SQLite close. The retained WAL was 4152 bytes. Before checkpoint, a copy of only the main DB was structurally valid (`integrity_check=ok`) but contained only `100`; normal reopen of the original DB with WAL observed committed `100,200`. After explicit checkpoint, a new main-file-only copy contained `100,200`.

**VALIDATION / SYNTHESIS:** WAL COMMIT and CHECKPOINT are distinct. A structurally healthy main database file is not a semantic-completeness oracle while committed state remains in WAL. This directly strengthens backup/recovery acceptance: a raw main-file-only copy can silently omit committed data. It does not establish hard-power-loss durability, checkpoint-failure/concurrency behavior, live Online Backup API semantics, or mobile behavior.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback process crash, capacity/syscall faults, short-write handling, torn durable-image model, and real WAL crash/checkpoint boundary; D006 server death, live-process link interruption and exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 has real asymmetric-signature, bounded compiler reproducibility and exact-ref product build-identity evidence.

## Cross-track handoffs
- **Quality:** future backup/recovery suites should include committed-but-uncheckpointed WAL state and require semantic completeness in addition to structural integrity.
- **Mobile/Quality:** when Flutter/device infrastructure exists, reproduce exact journal/synchronous configuration under process death and backup/export with semantic recovery oracles.
- **Systems:** journal mode, synchronous mode, VFS/filesystem/device assumptions are inputs to durability claims; COMMIT visibility is not a blanket hard-power-loss guarantee.
- **LogMate:** exact ref rechecked `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19`; production identity unknown. D005 does not claim current SQLite WAL use. Future backup consistency point remains a pre-implementation dependency.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical files were edited and no decision there changes this low-level persistence mechanism.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target and must be retried whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux/GCC are available.

D005 has now advanced from rollback-journal/process/storage-fault evidence into actual SQLite WAL crash/checkpoint behavior. Do not repeat simple WAL row-count or main-file-copy variants. If Dart/Flutter remains unavailable, prefer a genuinely stronger/different rung: WAL checkpoint interruption/concurrency or Online Backup API behavior, physical/platform transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime and build behavior are version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior are platform/version sensitive.
- SQLite WAL semantics are documented, but durability still depends on synchronous mode and VFS/OS/filesystem/device behavior; this process-crash evidence must not be generalized to hard power loss.
- LogMate DATA-001 Sync cursor/batch/receipt semantics and backup consistency mechanism remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.
- Exact Flutter SDK/ref and release/production identity for LogMate remain release-evidence dependencies.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
