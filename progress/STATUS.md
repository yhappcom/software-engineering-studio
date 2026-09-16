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
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two blocks + D004 first block + D005 two restore blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D004 — cache/offline visibility must not collapse confirmed base, pending mutation and authority
Canonical: `research/data/D004_cache_offline_first_data_ownership.md`  
Fixture: `research/data/fixtures/D004_cache_offline_ownership.py`

Executable bounded evidence (Python 3.13.5 / Linux):
- a destructive reconnect refresh overwrote a locally accepted visible edit 90 with stale remote-confirmed base 60 when both semantic roles shared one replaceable slot;
- a comparison model preserving `confirmed base` and `pending mutation` separately kept visible state at 90 while allowing the base to remain 60;
- an empty/unpopulated cache reported absence while the modeled authoritative remote still contained the record.

Current Firebase primary documentation independently exposes cache/server source distinctions, warns cache-origin Firestore data may be stale or incomplete, and distinguishes local pending writes from backend acknowledgement. The fixture is a mechanism model only; no Firestore/FlutterFire runtime claim is made.

Root-cause boundary: cache location, freshness, completeness, mutation acceptance and global/remote acknowledgement are separate semantics. Refresh/invalidation must state which layer it may replace.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001:** state/persistence/durability/authority model + SQLite application-process-kill evidence.
- **D002:** representation/publication/transaction/index plus DELETE/WAL application-process-exit recovery evidence.
- **D003:** mixed reader/writer compatibility, migration publication/rollback, constraint-transform failure and FK validation evidence.
- **D004:** cache/freshness/authority separation + stale-refresh failure/pending-overlay alternative.
- **D005:** actual restore acceptance plus corrupt/contract-incompatible failures and validate-before-publish recovery boundary.
- **Q001/Q002:** oracle/reproducibility plus test-level evidence boundaries.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. Prior exact-ref evidence described durable ledger/configuration persistence/Sync/Backup-Export as not implemented, so D004/D005 remain transfer candidates rather than existing product defects. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Architecture:** confirmed base, pending mutation and derived cache/projection are distinct semantic ownership roles even if physically colocated.
- **Mobile:** reproduce offline write + process death + reconnect/cache behavior on exact FlutterFire/Android/iOS stack.
- **Quality:** test stale refresh/cache miss/rejection/reconnect and distinguish local visibility from backend acknowledgement.
- **Systems:** persistent-cache confidentiality/eviction and durable publication remain separate concerns.
- **Design Studio:** `saved`, `pending`, `synced`, `failed` states must reflect actual engineering acknowledgement boundaries.
- **LogMate:** define local commit vs remote acknowledgement and protect pending records from destructive refresh before Sync implementation; no product repository edited.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

D004 closes the previously untouched Stage-1 cache/offline ownership prerequisite at first-block depth. Strong next candidates:
1. `D006` replication/synchronization/consistency/idempotency/conflict foundations — highest independent leverage now that pending-vs-confirmed ownership is explicit;
2. continue D004 only if a trustworthy Firestore/FlutterFire SDK/emulator becomes available for pending-write/cache-source/process-death evidence;
3. `Q003` nondeterminism/concurrency mechanics, especially before distributed retry/conflict validation;
4. `M002/M003` when trustworthy Android/iOS platform evidence becomes available.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.