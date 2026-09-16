# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated Foundation block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two blocks + D005 first restore block |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — backup creation is not recovery proof
Canonical: `research/data/D005_backup_restore_recovery_acceptance.md`  
Fixture: `research/data/fixtures/D005_backup_restore_acceptance.py`

Executable bounded evidence (Python 3.13.5 / SQLite 3.46.1 / Linux):
- created a SQLite backup, deliberately destroyed live semantic rows, restored into an isolated target, and passed an independent oracle requiring physical integrity + schema version + exact semantic rows;
- a real non-empty backup file with a corrupted SQLite header existed but could not be opened as a database;
- a structurally valid database with `integrity_check=ok` but application-managed `user_version=99` failed the declared schema/application contract.

Root-cause boundary: artifact existence, SQLite physical integrity, schema compatibility, semantic validity and application recovery answer different questions. A backup job/file can be green while recovery is still unproven.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **D002:** representation/publication/transaction/index plus DELETE/WAL application-process-exit recovery evidence.
- **D003:** mixed reader/writer compatibility, migration publication/rollback, constraint-transform failure and FK validation evidence.
- **Q001/Q002:** oracle/reproducibility plus test-level evidence boundaries.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context rechecked: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. Repository head remained at this commit. Prior exact-ref evidence described durable ledger/configuration persistence/Sync/Backup-Export as not implemented, so D005 is a transfer candidate rather than an existing product defect. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Architecture:** restored schema/version is a compatibility contract with the intended reader.
- **Mobile:** reproduce restore interruption, sandbox/document-provider, permission and storage-full behavior on exact Android/iOS stack.
- **Quality:** recovery PASS must exercise restore and independently validate physical/schema/domain acceptance; backup-job success is insufficient.
- **Systems:** confidentiality/authenticity/key lifecycle and release-artifact compatibility remain separate from recoverability.
- **LogMate:** define recoverability acceptance before Backup/Export implementation; no product repository edited.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated.

D005 now has the highest-value coherent continuation because its recovery professional boundary is incomplete. Priority:
1. `D005` restore publication/interruption safety — validate candidate before replacing live state and inject failure before publication;
2. `M002/M003` when trustworthy Android/iOS platform evidence becomes available;
3. `D004` cache/offline-first ownership after recovery boundary is materially stronger;
4. `Q002/Q003` when stronger real-system/nondeterminism validation opportunities exist.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
