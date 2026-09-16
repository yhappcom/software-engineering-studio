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
| Data | Stage 1 IN STUDY — D001 substantial + D002 two integrated mechanism blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D002 — Journal/recovery mode versus durability scope
Canonical: `research/data/D002_representation_files_database_indexes_transactions.md`  
New fixture: `research/data/fixtures/D002_journal_mode_process_exit.py`

Executable bounded evidence (Python 3.13.5 / SQLite 3.46.1 / Linux):
- real SQLite `journal_mode=DELETE` and `journal_mode=WAL`, both `synchronous=FULL`;
- child process inserted B inside `BEGIN IMMEDIATE` and terminated via `os._exit(99)` without normal connection cleanup;
- when exit occurred before COMMIT, reopen recovered only baseline A in both modes;
- when COMMIT completed before the same abrupt exit, reopen recovered A+B in both modes;
- `PRAGMA integrity_check` returned `ok` in all cases.

Root-cause boundary: the experiment supports COMMIT as the semantic committed/uncommitted boundary across this **application-process exit** failure. It does not imply DELETE and WAL use the same mechanism, nor does it establish OS-crash/power-loss/fsync durability.

Current SQLite primary documentation reinforces that journal mode and `synchronous` policy are separate durability dimensions; WAL + NORMAL can preserve consistency while losing recently committed transactions under power/system failure. Therefore `WAL enabled` is not a complete durability specification.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **D002 block 1:** representation/publication/transaction/index distinctions.
- **Q001/Q002:** oracle/reproducibility plus test-level evidence boundaries.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained transfer context: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → version 1.0.0+1 → evidence date 2026-09-16`. No local-ledger storage/journal implementation is inferred and no database choice is made.

## Cross-track handoffs
- **Architecture:** semantic transaction boundaries follow invariants/authority, not journal configuration.
- **Mobile:** reproduce storage/recovery on exact Android/iOS stack before transferring Linux evidence.
- **Quality:** classify application-process exit separately from OS/power-loss; evidence must cross the actual claimed failure domain.
- **Systems:** measure synchronous/journaling/checkpoint costs and validate lower storage-stack durability assumptions.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated.

D002 now has enough bounded journal-mode evidence that further progress would require trustworthy OS/power-loss/mobile execution or performance measurement. The highest-value independent prerequisite is therefore:
1. `D003` schema evolution/migration/rollback/compatibility — high data-loss risk, enabled by A003 compatibility contracts + D002 transactions, reusable across MintTap/LogMate;
2. `M002` Android/iOS process/storage/background semantics when trustworthy platform execution evidence becomes available;
3. `Q002/Q003` when a stronger real-system or nondeterminism validation opportunity exists.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
