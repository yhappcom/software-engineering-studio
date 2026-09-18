# Data Specialist Status

Track: Data, Persistence & Distributed Systems  
Prefix: `D###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-18

## Mission
Build rigorous knowledge of data representation, integrity, persistence, transactions, schema evolution, migrations, caching, offline-first systems, replication, synchronization, conflict handling, backup/restore, and distributed-system semantics.

## Current evidence

### D001 — State, persistence, durability, source of truth and invariants
**IN STUDY — substantial first block complete.** Canonical: `research/data/D001_state_persistence_durability_source_of_truth.md`.

### D002 — Representation, files, databases, indexes and transaction fundamentals
**IN STUDY — two integrated executable Foundation blocks complete.** Canonical: `research/data/D002_representation_files_database_indexes_transactions.md`.

### D003 — Schema evolution, migration, rollback and compatibility
**IN STUDY — two integrated executable Foundation blocks complete.** Canonical: `research/data/D003_schema_evolution_migration_rollback_compatibility.md`.

Established: reader/writer/schema compatibility is relational; split publication can create mismatched schema/version state; transactional fail-closed handling can restore the old contract at bounded failure points; caught constraint failures can otherwise falsely publish a new version; FK enforcement and persisted-data validation are separate obligations.

### D004 — Cache semantics and offline-first data ownership
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/data/D004_cache_offline_first_data_ownership.md`.

Established cache authority/freshness/completeness/confirmation separation plus destructive-refresh failure and pending-vs-confirmed alternative. Real SDK/durable pending/process-death evidence remains OPEN.

### D005 — Backup, restore, recovery acceptance and crash boundary
**IN STUDY — three integrated executable blocks; real application-process crash evidence added.**  
Canonical: `research/data/D005_backup_restore_recovery_acceptance.md`, `research/data/D005_process_crash_transaction_boundary.md`.

Prior blocks established independent physical/schema/semantic recovery acceptance and isolated validate-before-publication safety in bounded SQLite/POSIX fixtures. A Linux/Python/SQLite WAL fixture uses separate OS child processes and abrupt `os._exit`: an active uncommitted transaction disappears after restart while an explicitly committed transaction remains visible to a fresh process, with `integrity_check=ok`. This closes the application-process crash/restart gap only; OS crash, power loss, filesystem/device durability and mobile transfer remain OPEN.

### D006 — Replication, synchronization, consistency, idempotency and conflicts
**IN STUDY — three integrated blocks; real TCP + process-restart ambiguous-retry evidence added.**  
Canonical: `research/data/D006_replication_sync_consistency_idempotency_conflicts.md`, `research/data/D006_real_tcp_ambiguous_retry_restart.md`.  
Fixture: `research/data/fixtures/D006_real_tcp_ambiguous_retry_restart.py`.

Prior model blocks established retry/idempotency, delivery/application/ACK separation, bounded LWW information loss and stale-update/delete resurrection. The 2026-09-18 Linux/Python fixture now uses real localhost TCP, separate server processes and SQLite durable state. Server 1 commits `op-1:+10` then terminates via `os._exit(33)` before ACK bytes; the client sees EOF. After server restart, stable operation identity + durable dedup returns 10 and leaves one effect/one op record. Under the same failure schedule without dedup, retry produces 20. This advances D006 from modeled ambiguous ACK loss to real socket/process/persistent-state evidence. It is not WAN, multi-host, mobile, Firestore, Flutter or exactly-once evidence.

## Product transfer retained
Exact prior LogMate ref: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1`. It remains a transfer candidate, not production evidence. No product repository was audited in the latest D006 block, so no new MintTap/LogMate implementation claim is made.

## Gate assessment
Data Stage 1 remains **NOT PASS**. D001-D006 cover authority/durability, representation/transactions, migration, cache/offline ownership, restore/recovery and first synchronization/conflict mechanics. D005 contains actual application-process termination/restart evidence; D006 now contains actual TCP ACK-loss ambiguity across server restart with durable dedup comparison. Stronger OS/power/storage faults, remote/multi-host network behavior, real mobile/backend behavior and Dart/Flutter transfer remain incomplete.

## Dependencies / handoffs
- **Foundations:** F006 transport/apply/commit/ACK distinctions are now reproduced with real TCP/process restart; F001 direct Dart/Flutter remains OPEN.
- **Architecture:** operation identity and dedup retention are protocol/state-ownership contracts; commit and acknowledgement remain separate.
- **Mobile:** reproduce process/network interruption and retry on the exact Android/iOS/Flutter persistence/sync stack.
- **Quality:** reuse commit → kill-before-ACK → restart → retry with a fresh semantic oracle.
- **Systems:** hostile replay/authorization is separate from correctness idempotency; stronger durability still requires lower-layer faults.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this bounded mechanism.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable after environment recheck 2026-09-18; Python 3.13.5 is available.
- D005 OS-crash/power-loss, WAL/checkpoint interruption, storage-full/I/O faults, filesystem durability and Android/iOS transfer remain OPEN.
- D006 real remote/network-namespace interruption, concurrent retry, dedup retention/GC, external side effects, operation-id collision, concurrent delete/recreate, tombstone GC and real multi-writer/backend evidence remain OPEN.
- No Data Foundation PASS yet.

## Next work
Use Balance Loop. Do not repeat localhost retry schedules merely for volume. Prefer a materially stronger boundary: controllable network namespace/interruption or storage/I/O fault if privileges make it trustworthy; otherwise exact-ref product transfer or another track's stronger real evidence gap. Direct Dart/Flutter/mobile execution remains first-attempt work whenever a trustworthy SDK/device environment becomes available.
