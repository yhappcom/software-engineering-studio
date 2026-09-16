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
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 first migration block |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D003 — Schema evolution as compatibility/publication protocol
Canonical: `research/data/D003_schema_evolution_migration_rollback_compatibility.md`  
Fixture: `research/data/fixtures/D003_schema_migration_compatibility.py`

Executable bounded evidence (Python 3.13.5 / SQLite 3.46.1 / Linux):
- V2 expand/backfill/fallback-read/dual-write preserved bounded old/new reader-writer contracts;
- deliberately splitting schema mutation and application-managed `user_version` across commits produced a reopened mismatch: V2-shaped schema with version metadata still at 1;
- placing schema change, backfill and version update in one transaction and injecting failure before COMMIT rolled all of them back to the V1 contract;
- V3 destructive retirement of the old `minutes` representation preserved migrated data for the new reader but caused the old reader to fail.

Root-cause boundary: schema migration success and cross-version application compatibility are distinct. Compatibility must be tested across reader/writer/schema/migration-state combinations; transaction boundaries can eliminate some partial-publication states but do not by themselves prove downgrade, backup/restore, mobile or distributed compatibility.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **D002:** representation/publication/transaction/index plus DELETE/WAL application-process-exit recovery evidence.
- **Q001/Q002:** oracle/reproducibility plus test-level evidence boundaries.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
`yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → version 1.0.0+1 → evidence date 2026-09-17`. Current exact-ref evidence describes local ledger/configuration persistence/Sync/Backup-Export as not implemented, so D003 is a transfer candidate rather than an existing migration finding. MintTap repository identity was not resolved from accessible GitHub repository search; no MintTap implementation claim is made.

## Cross-track handoffs
- **Architecture:** persisted schema compatibility follows retained semantic consumer contracts, not shape alone.
- **Mobile:** reproduce upgrade/startup/process-death migration behavior on exact Android/iOS stack.
- **Quality:** build reader/writer/schema/migration-state matrices and inject interruption around publication boundaries.
- **Systems:** release rollback must state whether an older artifact can open newer persisted state; artifact version and schema version are separate identities.
- **LogMate:** define migration/version metadata, compatibility window, destructive-retirement criteria and recovery oracle before durable ledger/configuration implementation; no product repository edited.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated.

D003 now has a first coherent executable boundary and should continue if downgrade/rollback-release or failed-transform evidence can materially close the migration topic. Highest-value candidates:
1. `D003` continuation — old binary/new schema rollback-release, constraint/FK transform failure and recovery;
2. `D005` backup/restore fundamentals — migration safety requires restore evidence, not backup creation alone;
3. `M002` Android/iOS process/storage/background semantics when trustworthy platform execution evidence becomes available;
4. `Q002/Q003` when stronger real-system/nondeterminism validation opportunities exist.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
