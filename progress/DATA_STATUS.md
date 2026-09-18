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
**IN STUDY — seven integrated executable blocks; process crash + capacity/write + sync + short-write-progress boundaries.** Canonical: `research/data/D005_backup_restore_recovery_acceptance.md`, `research/data/D005_process_crash_transaction_boundary.md`, `research/data/D005_bounded_sqlite_full_transaction_boundary.md`, `research/data/D005_syscall_enospc_fault_injection.md`, `research/data/D005_syscall_fsync_eio_fault_injection.md`, `research/data/D005_short_write_progress_boundary.md`.

Prior Linux/Python/SQLite evidence distinguishes uncommitted rollback from committed persistence, forces bounded `SQLITE_FULL`, injects syscall-level `pwrite/pwrite64=ENOSPC`, and injects `fsync/fdatasync=EIO`. New `LD_PRELOAD` evidence intercepts the first target database `pwrite64`: a 512→256 positive-progress short write still committed `[100,200]`, while a 512→0 zero-progress return surfaced code 13 `SQLITE_FULL` and fresh reopen preserved baseline `[100]`; both reopened with `integrity_check=ok`. Current official Unix VFS source explains the distinction by retrying positive partial progress and treating non-progress as failure/full. This separates syscall short-write handling from torn durable writes, which remain OPEN.

### D006 — Replication, synchronization, consistency, idempotency and conflicts
**IN STUDY — five integrated blocks; exact-ref LogMate protocol transfer added.** Canonical: `research/data/D006_replication_sync_consistency_idempotency_conflicts.md`, `research/data/D006_real_tcp_ambiguous_retry_restart.md`, `research/data/D006_network_namespace_link_interruption.md`, `research/data/D006_logmate_inbound_cursor_atomicity_transfer.md`.

Real boundaries cover server death after commit/before ACK and live-process isolated kernel link-down/timeout/recovery/retry. Exact-ref LogMate transfer establishes that durable replication progress must not outrun required durable semantic effects unless an independently validated replay/reconciliation mechanism exists. Actual LogMate persistence/Sync remains unimplemented at the inspected ref.

## Product transfer retained
Exact LogMate ref: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-18`. Production identity is unknown; default branch is not assumed to equal production.

## Gate assessment
Data Stage 1 remains **NOT PASS**. D001-D006 cover the planned Foundation mechanisms with executable evidence. D005 now includes actual process termination, logical capacity, syscall ENOSPC, syscall sync-EIO, and bounded positive-progress versus zero-progress write behavior. Physical filesystem/device exhaustion, torn durable writes, truthful-vs-lying fsync under power loss, WAL/checkpoint behavior, mobile/backend behavior and Dart/Flutter transfer remain incomplete.

## Dependencies / handoffs
- **Foundations:** F001 direct Dart/Flutter remains OPEN; F006 transport/apply/commit/ACK distinctions retained.
- **Architecture:** transaction, recovery, durability and replication progress publication are semantic/state-ownership contracts.
- **Mobile:** reproduce storage exhaustion, sync failure, process death and recovery on the exact Android/iOS/Flutter stack.
- **Quality:** storage fault matrices should preserve requested/returned byte counts; recovery oracles must compare semantic state with structural health and durable progress.
- **Systems:** short syscall returns are not torn-write/power-loss evidence; future validation must distinguish truthful/lying sync, torn durable writes, directory sync, rename/delete and WAL checkpoint boundaries.
- **LogMate:** define atomic inbound entity/tombstone/revision/receipt effects and cursor advancement before Sync persistence implementation.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable after environment recheck 2026-09-19.
- D005 physically full filesystem/device, quota, torn durable write, truthful-vs-lying fsync under power loss, directory fsync, WAL/checkpoint, OS/power crash and Android/iOS transfer remain OPEN. Injected syscall faults must not be generalized to those mechanisms.
- D006 exact server cursor/batch/receipt semantics, remote/packet faults, concurrent retry, dedup retention/GC, external side effects, tombstone GC and real multi-writer/backend evidence remain OPEN.
- No Data Foundation PASS yet.

## Next work
Use Balance Loop. Do not repeat `max_page_count`, equivalent `pwrite=ENOSPC`, additional ordinal variants of `fsync=EIO`, or more positive-short-write sizes merely for coverage. F001 direct Dart/Flutter execution remains first if a trustworthy SDK appears. Otherwise advance only to a materially different evidence rung such as torn durable-write/power-loss semantics, WAL/checkpoint behavior, real platform transfer, natural release/ADR evidence, real CI/attestation, or another track's stronger gap.
