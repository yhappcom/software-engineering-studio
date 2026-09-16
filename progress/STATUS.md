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
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two blocks + D005 two restore blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D005 — restore acceptance must precede destructive publication when preserving last known-good state
Canonical: `research/data/D005_backup_restore_recovery_acceptance.md`  
New fixture: `research/data/fixtures/D005_restore_publication_safety.py`

Executable bounded evidence (Python 3.13.5 / SQLite 3.46.1 / Linux):
- destructive publish-before-validation replaced the known-good live database with a structurally valid but application-incompatible artifact;
- isolated candidate validation rejected that same artifact while live accepted state remained intact;
- after a valid candidate passed acceptance, an injected failure before publication left live state intact;
- same-filesystem `os.replace` then published a valid candidate successfully in the bounded POSIX environment.

Root-cause boundary: candidate construction/validation and live publication are separate failure domains. Validation after destructive replacement can be too late to preserve rollback material.

Evidence limit: atomic namespace replacement is not power-loss durability. Active WAL/open handles, fsync/directory durability, cross-filesystem publication, Android/iOS document providers and storage-full/permission failures remain OPEN. SQLite documentation also requires treating an extant WAL file as part of persistent database state; the fixture used closed standalone artifacts and does not validate live-WAL replacement.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **D002:** representation/publication/transaction/index plus DELETE/WAL application-process-exit recovery evidence.
- **D003:** mixed reader/writer compatibility, migration publication/rollback, constraint-transform failure and FK validation evidence.
- **D005 block 1:** actual restore acceptance plus corrupt and physically-valid-but-contract-incompatible failures.
- **Q001/Q002:** oracle/reproducibility plus test-level evidence boundaries.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. Prior exact-ref evidence described durable ledger/configuration persistence/Sync/Backup-Export as not implemented, so D005 remains a transfer candidate rather than an existing product defect. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Architecture:** restore schema/version and rollback expectation are compatibility contracts with the intended reader.
- **Mobile:** reproduce publication interruption, sandbox/document-provider, cross-volume, permission, storage-full and process-death behavior on exact Android/iOS stack.
- **Quality:** recovery tests must cross candidate validation and publication failure points; copy completion is insufficient.
- **Systems:** distinguish atomic namespace replacement from durable publication; confidentiality/authenticity/key lifecycle remain separate.
- **LogMate:** define candidate validation and last-known-good preservation before Backup/Export implementation; no product repository edited.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated.

D005's independently executable Linux boundary is now materially stronger; its next gaps require trustworthy filesystem/power/mobile evidence and must not be simulated. Rebalance candidates:
1. `D004` cache/offline-first data ownership — still a Stage-1 prerequisite with direct MintTap/LogMate reuse and independent executable opportunities;
2. `M002/M003` when trustworthy Android/iOS platform evidence becomes available;
3. `Q002/Q003` when stronger real-system/nondeterminism evidence is obtainable;
4. return to D005 when crash/power/WAL/mobile publication evidence can be tested honestly.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
