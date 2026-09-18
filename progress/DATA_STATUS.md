# Data Specialist Status

Track: Data, Persistence & Distributed Systems  
Prefix: `D###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-19

## Mission
Build rigorous knowledge of data representation, integrity, persistence, transactions, schema evolution, migrations, caching, offline-first systems, replication, synchronization, conflict handling, backup/restore, and distributed-system semantics.

## Current evidence

### D001 — State, persistence, durability, source of truth and invariants
**IN STUDY — substantial first block complete.** Canonical: `research/data/D001_state_persistence_durability_source_of_truth.md`.

### D002 — Representation, files, databases, indexes and transaction fundamentals
**IN STUDY — two integrated executable Foundation blocks complete.** Canonical: `research/data/D002_representation_files_database_indexes_transactions.md`.

### D003 — Schema evolution, migration, rollback and compatibility
**IN STUDY — two integrated executable Foundation blocks complete.** Canonical: `research/data/D003_schema_evolution_migration_rollback_compatibility.md`. Reader/writer/schema compatibility is relational; split publication can create mismatched schema/version state; transactional fail-closed handling can restore the old contract at bounded failure points.

### D004 — Cache semantics and offline-first data ownership
**IN STUDY — first integrated Foundation block complete.** Canonical: `research/data/D004_cache_offline_first_data_ownership.md`. Cache authority/freshness/completeness/confirmation separation plus destructive-refresh failure and pending-vs-confirmed alternative established. Real SDK/durable pending/process-death evidence remains OPEN.

### D005 — Backup, restore, recovery acceptance and crash/storage boundaries
**IN STUDY — six integrated executable blocks; process crash + capacity/write + sync fault boundaries.** Canonical: `research/data/D005_backup_restore_recovery_acceptance.md`, `research/data/D005_process_crash_transaction_boundary.md`, `research/data/D005_bounded_sqlite_full_transaction_boundary.md`, `research/data/D005_syscall_enospc_fault_injection.md`, `research/data/D005_syscall_fsync_eio_fault_injection.md`.

Prior Linux/Python/SQLite evidence distinguishes uncommitted rollback from committed persistence, forces bounded `SQLITE_FULL`, and injects syscall-level `pwrite/pwrite64=ENOSPC`. New Linux `LD_PRELOAD` evidence allows ordinary writes but returns `EIO` at selected target `fsync`/`fdatasync` calls under rollback-journal `synchronous=FULL`. Three independently reset failure placements each surfaced extended code 1034 `SQLITE_IOERR_FSYNC`; fresh reopen preserved only the committed baseline semantic row and `integrity_check=ok`. No-fault and too-late-fault controls committed `[100,200]`. This adds a materially different durability-synchronization failure class, but is not physical power-loss/device evidence or proof that a successful fsync is truthful.

### D006 — Replication, synchronization, consistency, idempotency and conflicts
**IN STUDY — five integrated blocks; exact-ref LogMate protocol transfer added.** Canonical: `research/data/D006_replication_sync_consistency_idempotency_conflicts.md`, `research/data/D006_real_tcp_ambiguous_retry_restart.md`, `research/data/D006_network_namespace_link_interruption.md`, `research/data/D006_logmate_inbound_cursor_atomicity_transfer.md`.

Real boundaries cover server death after commit/before ACK and live-process isolated kernel link-down/timeout/recovery/retry. Exact-ref LogMate transfer establishes that durable replication progress must not outrun required durable semantic effects unless an independently validated replay/reconciliation mechanism exists. Actual LogMate persistence/Sync remains unimplemented at the inspected ref.

## Product transfer retained
Exact LogMate ref: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-18`. Production identity is unknown; default branch is not assumed to equal production.

## Gate assessment
Data Stage 1 remains **NOT PASS**. D001-D006 cover the planned Foundation mechanisms with executable evidence. D005 now includes actual process termination, logical capacity, syscall ENOSPC and syscall sync-EIO boundaries. Physical filesystem/device exhaustion, truthful-vs-lying fsync under power loss, short/torn writes, WAL/checkpoint behavior, mobile/backend behavior and Dart/Flutter transfer remain incomplete.

## Dependencies / handoffs
- **Foundations:** F001 direct Dart/Flutter remains OPEN; F006 transport/apply/commit/ACK distinctions retained.
- **Architecture:** transaction, recovery, durability and replication progress publication are semantic/state-ownership contracts.
- **Mobile:** reproduce storage exhaustion, sync failure, process death and recovery on the exact Android/iOS/Flutter stack.
- **Quality:** recovery oracles must compare semantic state with structural health and durable progress; API error identity and `integrity_check=ok` are insufficient alone.
- **Systems:** future fault injection should distinguish short/torn write, truthful/lying sync, directory sync, rename/delete and WAL checkpoint boundaries; hostile replay/authorization remains separate from idempotency.
- **LogMate:** define atomic inbound entity/tombstone/revision/receipt effects and cursor advancement before Sync persistence implementation.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable after environment recheck 2026-09-19.
- D005 physically full filesystem/device, quota, short/torn write, truthful-vs-lying fsync under power loss, directory fsync, WAL/checkpoint, OS/power crash and Android/iOS transfer remain OPEN. Injected syscall faults must not be generalized to those mechanisms.
- D006 exact server cursor/batch/receipt semantics, remote/packet faults, concurrent retry, dedup retention/GC, external side effects, tombstone GC and real multi-writer/backend evidence remain OPEN.
- No Data Foundation PASS yet.

## Next work
Use Balance Loop. Do not repeat `max_page_count`, equivalent `pwrite=ENOSPC`, or additional ordinal variants of the same `fsync=EIO` fixture. F001 direct Dart/Flutter execution remains first if a trustworthy SDK appears. Otherwise advance only to a materially different evidence rung such as short/torn-write or WAL/checkpoint behavior, real platform/power-loss transfer, natural release/ADR evidence, real CI/attestation, or another track's stronger gap.