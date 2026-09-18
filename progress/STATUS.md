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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage faults + torn-image + WAL/checkpoint + live backup concurrency + interruption/publication evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 real signing + bounded reproducibility + LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — interrupted Online Backup separates candidate existence/progress from accepted publication
Canonical: `research/data/D005_online_backup_interruption_publication.md`; fixture: `research/data/fixtures/D005_online_backup_interruption_publication.py`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was found; direct Dart/Flutter validation remains OPEN rather than simulated.

Python 3.13.5 / SQLite 3.46.1 / Linux execution used a 1,505-page WAL source and killed the backup-producing child after the Online Backup progress callback reported `0,1504,1505`. A final-looking destination pathname already existed, but in the observed run it was 0 bytes and lacked the expected source table. **VALIDATION:** pathname existence and progress are invalid completion or publication oracles.

A materially different alternative kept the prior accepted backup at `published.db` and generated the replacement at a private candidate path. Killing the candidate backup at the same progress boundary left the published artifact SHA-256 unchanged; fresh reopen still returned its prior 10-row semantic state and `integrity_check=ok`. **SYNTHESIS:** candidate generation → database-aware completion → validation → publication are separate state transitions. This is process-interruption evidence only; it does not prove crash-durable rename, file/directory fsync ordering or hard-power-loss safety.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/process/storage faults, short-write/torn-image evidence, WAL crash/main-file completeness, reader/checkpoint concurrency, live-writer Online Backup behavior and interrupted candidate/publication evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 real asymmetric signature, bounded compiler reproducibility and exact-ref product build-identity evidence.

## Cross-track handoffs
- **Quality:** backup tests need distinct completion, structural-integrity, semantic-completeness, progress and publication-state oracles; file existence/progress must not be accepted as success.
- **Mobile:** reproduce backup candidate/completion/publication behavior on the exact Flutter/Android/iOS persistence stack when available.
- **Systems:** next publication evidence must address replacement primitive plus file/directory synchronization and hard-power-loss scope rather than infer durability from process-kill safety.
- **LogMate:** retained prior exact-ref context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19`; production identity unknown. No claim that current LogMate uses SQLite WAL or Online Backup API. Backup consistency/completion/publication semantics remain product decisions.
- **Design Studio / Web Manager / Marketing Manager:** considered under cross-repo contract; no canonical files edited and no low-level evidence changes this mechanism.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux are available.

D005 has now advanced through WAL crash/main-file completeness, active-reader checkpoint progress, live-writer Online Backup behavior and interrupted candidate/publication semantics. Do not repeat process-kill-at-progress, row-count, reader-count, checkpoint-mode or single-concurrent-write variants. If Dart/Flutter remains unavailable, prefer a genuinely higher/different rung: hard-power-loss/publication durability, exact mobile transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- SQLite WAL/backup behavior depends on SQLite version, wrapper, VFS/OS/filesystem/device and synchronization mode; current process/concurrency evidence is not hard-power-loss evidence.
- LogMate Sync and backup consistency/publication mechanisms remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
