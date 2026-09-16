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
| Data | Stage 1 IN STUDY — D001 substantial + D002 two blocks + D003 two blocks + D004 first + D005 two + D006 first block |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D006 — retry/idempotency and convergence/conflict semantics are distinct
Canonical: `research/data/D006_replication_sync_consistency_idempotency_conflicts.md`  
Fixture: `research/data/fixtures/D006_retry_conflict_semantics.py`

Executable bounded evidence (Python 3.13.5 / Linux):
- modeled server applies `+10`, response/ACK is lost, retry applies the same intent again: unsafe total becomes 20;
- stable logical operation identity + server-side deduplication keeps the same bounded effect at 10 under duplicate delivery;
- therefore retry policy does not itself establish idempotency, and timeout/failed acknowledgement does not establish non-application;
- concurrent writers changing independent fields from one base were fed to whole-record last-write-wins; it converged to one record but discarded writer A's valid `night` update;
- a fieldwise comparison preserved both changes only because the fixture deliberately defined the fields as independent; it is not a universal merge algorithm.

Current RFC 9110 defines idempotency by repeated intended server effect and explicitly motivates retries after ambiguous communication failure. Current Firestore docs separately document offline last-write-wins and transaction callback retries under contention. The fixture is a mechanism model only; no network/Firestore runtime claim is made.

Root-cause boundary: attempt identity, logical operation identity, delivery, application, acknowledgement, replication and conflict resolution are separate semantics. Convergence alone does not prove preservation of user intent.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **D001-D005:** authority/durability, representation/transactions, migration, cache/offline ownership, restore acceptance/publication evidence retained.
- **D006:** lost-ACK retry duplication, operation-id dedup alternative and LWW concurrent-intent-loss evidence.
- **Q001/Q002:** oracle/reproducibility plus test-level evidence boundaries.
- **A001-A003:** information hiding/change pressure, state ownership/dependency direction, semantic contract/API compatibility.
- **M001:** Flutter/runtime/UI/lifecycle source model + skipped-lifecycle-notification failure model.
- **S001:** artifact identity plus integrity/authenticity/authorization/provenance separation.

## Product transfer
Retained exact-ref context: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. Prior exact-ref evidence described durable ledger/configuration persistence/Sync/Backup-Export as not implemented, so D004-D006 remain transfer candidates rather than existing product defects. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Architecture:** operation identity and conflict unit are semantic contracts, not transport details.
- **Mobile:** reproduce retry/pending/process-death/connectivity behavior on the exact eventual sync stack.
- **Quality:** Q003/Q006 should exercise lost ACK, duplicate/reordered delivery and concurrent writer schedules.
- **Systems:** replay/security identity is distinct from correctness idempotency identity.
- **Design Studio:** `saved`, `pending`, `synced`, `conflicted`, `failed` states must reflect actual acknowledgement/conflict boundaries.
- **LogMate:** specify FlightRecord identity, duplicate/retry semantics, concurrent edit and delete/tombstone policy before selecting LWW or another sync policy; no product repository edited.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

D006 closes the previously untouched Stage-1 replication/idempotency/conflict prerequisite at first-block depth. Strong next candidates:
1. `Q003` determinism/nondeterminism/concurrency/flaky-test mechanics — highest cross-track leverage for validating D006 ordering/retry/conflict failures;
2. continue D006 with reordered delivery and stale-delete/tombstone only if it yields a coherent stronger distributed failure block;
3. `F004/F005/F006` concurrency/async/network foundations, especially if Q003 exposes missing execution-model prerequisites;
4. `M002/M003` when trustworthy Android/iOS platform evidence becomes available.

Selection remains risk/evidence/prerequisite driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.