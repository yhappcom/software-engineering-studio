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
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage faults + torn-image model + WAL crash/checkpoint + active-reader checkpoint-progress evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 real crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S001-S006 initiated; S005 real signing + bounded reproducibility + LogMate build-identity transfer |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — active reader lifetime can prevent WAL checkpoint completion/reset
Canonical: `research/data/D005_wal_checkpoint_reader_starvation.md`; fixture: `research/data/fixtures/D005_wal_checkpoint_reader_starvation.py`.

F001 was attempted first on 2026-09-19: no `dart` or `flutter` executable was found; direct Dart/Flutter validation remains OPEN rather than simulated.

Python 3.13.5 / SQLite 3.46.1 / Linux WAL execution established baseline `100`, checkpointed it, then pinned a reader transaction at that snapshot. The writer committed `200` and `300`. With the reader still active, PASSIVE checkpoint returned `(0,4,0)` and TRUNCATE with `busy_timeout=0` returned `(1,4,0)`; WAL remained 16512 bytes and the reader continued to observe `[100]`. After the reader committed, TRUNCATE returned `(0,0,0)`, WAL became 0 bytes, current state was `[100,200,300]`, and `integrity_check=ok`.

**VALIDATION / SYNTHESIS:** explicit checkpoint invocation is not unconditional consolidation. Reader snapshot lifetime and checkpoint mode are progress inputs. Checkpoint busy/incomplete is distinct from semantic corruption: the reader snapshot remained correct and eventual checkpoint completed after the blocker ended.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **Architecture:** A001-A003/A005/A006 cover change pressure, ownership/dependency, semantic contracts, refactoring/evolution and evidence-preserving decision lifecycle.
- **Mobile:** M001-M006 cover planned Foundation boundaries at first professional/model level; real runtime/platform transfer OPEN.
- **Data:** D005 rollback/process/storage faults, short-write/torn-image evidence, WAL crash/main-file completeness and reader/checkpoint concurrency; D006 transport faults + exact-ref inbound progress transfer.
- **Quality:** Q001-Q006 professional boundaries; Q004 mutation/search-strength and Q006 semantic recovery-oracle discrimination retained.
- **Systems:** S001-S006 retained; S005 real asymmetric signature, bounded compiler reproducibility and exact-ref product build-identity evidence.

## Cross-track handoffs
- **Quality:** checkpoint tests need a progress/busy oracle distinct from semantic-integrity oracles; verify eventual progress after blockers end.
- **Mobile:** reproduce journal/checkpoint/backup behavior on the exact Flutter/Android/iOS persistence stack when available.
- **Systems:** if manual checkpoint policy is adopted, WAL size, reader lifetime, blocking budget and retry/defer behavior become operational inputs.
- **LogMate:** retained exact-ref context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-19`; production identity unknown. No claim that current LogMate uses SQLite WAL.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical files edited and no decision there changes this low-level mechanism.

## Current Balance Loop
Direct Dart/Flutter execution remains the highest-prerequisite target whenever a trustworthy SDK appears. The runtime still has no `dart`/`flutter`; Python/Linux are available.

D005 has now advanced through actual WAL crash/main-file completeness and active-reader checkpoint-progress behavior. Do not repeat reader-count, row-count, or simple checkpoint-mode variants. If Dart/Flutter remains unavailable, prefer Online Backup API under live WAL concurrency, checkpoint interruption, physical/platform transfer, natural ADR/release evidence, real CI/attestation, independent product build, or another track's stronger gap.

## CHANGE WATCH
- Flutter/Dart runtime/build behavior is version-sensitive; exact SDK/ref matters.
- Browser/PWA and Android/iOS storage/background/backup behavior is platform/version sensitive.
- SQLite WAL durability depends on synchronous mode and VFS/OS/filesystem/device behavior; current process/concurrency evidence is not hard-power-loss evidence.
- LogMate Sync and backup consistency mechanisms remain OPEN product decisions.
- GitHub attestation/Sigstore, OpenSSL/provider and compiler/linker behavior are service/toolchain sensitive.

## Evidence rule
No PASS from reading alone. Expected progression where applicable: `SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
