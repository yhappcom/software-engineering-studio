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
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two migration blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D003 — failed transforms must fail the migration protocol
Canonical: `research/data/D003_schema_evolution_migration_rollback_compatibility.md`  
New fixture: `research/data/fixtures/D003_constraint_fk_migration_failure.py`

Executable bounded evidence (Python 3.13.5 / SQLite 3.46.1 / Linux):
- strengthening a persisted invariant to `seconds >= 0` caused migration copy failure on deliberately incompatible legacy data;
- a weak protocol caught the statement error, continued, set `user_version=2`, and committed an internally inconsistent migration state: empty V2 copy plus incompatible legacy table;
- a fail-closed comparison rolled back the entire transaction, including the incompatible legacy mutation, and retained V1 metadata/schema/data;
- disabling FK enforcement allowed an orphan to persist; re-enabling enforcement did not repair it, while `PRAGMA foreign_key_check` exposed the violation.

Root-cause boundary: SQLite default statement ABORT behavior does not imply application migration rollback. `statement failed`, `transaction rolled back`, `migration succeeded`, `version published`, and `persisted invariants validated` are separate claims. Migration acceptance needs an application-level success predicate and post-transform validation.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **D002:** representation/publication/transaction/index plus DELETE/WAL application-process-exit recovery evidence.
- **D003 block 1:** mixed reader/writer compatibility window, split schema/version publication failure, transactional rollback alternative, destructive-contract old-reader failure.
- **Q001/Q002:** oracle/reproducibility plus test-level evidence boundaries.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → version 1.0.0+1 → evidence date 2026-09-17`. Current inspected evidence described durable ledger/configuration persistence/Sync/Backup-Export as not implemented, so D003 remains a transfer candidate rather than an existing migration defect. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Architecture:** strengthened persisted invariants are compatibility changes; historical-state handling is part of the contract.
- **Mobile:** reproduce upgrade/startup/process-death migration and restart behavior on exact Android/iOS stack.
- **Quality:** migration PASS oracle must require every transform/validation step; caught statement errors must not permit version publication.
- **Systems:** release rollback must bind authorized artifact identity to schema compatibility and migration-success evidence.
- **LogMate:** define nonconforming-history policy, fail-closed publication and recovery oracle before durable ledger/configuration implementation; no product repository edited.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated.

D003 now has two coherent executable blocks and its local constraint/FK failure boundary is materially stronger. Highest-value independent candidates:
1. `D005` backup/restore fundamentals — migration safety requires actual restore + contract acceptance evidence, not backup creation alone;
2. `D003` actual rollback-release evidence when a trustworthy old-artifact/new-schema execution context is available;
3. `M002` Android/iOS process/storage/background semantics when trustworthy platform evidence is available;
4. `Q002/Q003` when stronger real-system/nondeterminism validation opportunities exist.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
