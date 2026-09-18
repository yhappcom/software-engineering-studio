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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 signing/reproducibility/product identity; S006 directory-sync publication failure evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### S006 — rename visibility does not complete a directory-synchronized publication protocol
Canonical: `research/systems/S006_directory_fsync_publication_boundary.md`; fixture: `research/systems/fixtures/S006_directory_fsync_publication_boundary.py`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was found; direct Dart/Flutter validation remains OPEN rather than simulated.

Linux/Python/GCC execution generated a private candidate, synchronized its file data, renamed it to the final pathname, then synchronized the containing directory. An LD_PRELOAD shim injected `EIO` only into directory `fsync()`. Control publication succeeded. Under the injected failure, the publisher failed while the final pathname was already visible and contained the expected bytes. **VALIDATION:** final-path visibility is not a sufficient success oracle for a protocol whose contract includes successful directory synchronization.

**SYNTHESIS:** candidate validity → file-data synchronization → rename visibility → directory-metadata synchronization → accepted publication are separate claims. This extends D005's backup candidate/completion/publication boundary into Systems-owned filesystem publication evidence.

**EVIDENCE LIMIT:** this is syscall-failure/oracle evidence, not a physical power-loss/reboot test. It does not establish what survives controller/filesystem failure, lying-successful fsync, ext4/APFS/mobile behavior or current LogMate behavior.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decisions.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/storage/WAL/checkpoint/live backup/interruption evidence; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 asymmetric signing/reproducibility/product build identity; S006 now includes directory-sync publication failure evidence.

## Cross-track handoffs
- **Data:** model database-aware completion separately from file-data sync, rename/replacement and directory-metadata sync where the target platform requires them.
- **Quality:** a visible final artifact is not by itself a durability-success oracle; inject post-rename synchronization failure in real product paths when applicable.
- **Mobile:** reproduce the publication protocol against exact Android/iOS/Flutter storage APIs/filesystems; Unix syscall semantics are not assumed portable.
- **LogMate:** no current implementation claim. Backup consistency/completion/validation/publication/durability semantics remain product decisions.
- **Design Studio / Web Manager / Marketing Manager:** considered under cross-repo contract; no canonical files edited and no owned decision changed.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux are available.

Do not repeat directory-fsync EIO, rename-visibility, D005 process-kill-at-progress, row-count, reader-count, checkpoint-mode or single-concurrent-write variants. If Dart/Flutter remains unavailable, prefer a genuinely higher/different rung: physical/platform publication durability, exact mobile transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- Filesystem publication durability depends on OS/filesystem/device and synchronization semantics; current EIO injection is not hard-power-loss evidence.
- SQLite WAL/backup behavior depends on SQLite version, wrapper, VFS/OS/filesystem/device and synchronization mode.
- LogMate Sync and backup consistency/publication mechanisms remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
