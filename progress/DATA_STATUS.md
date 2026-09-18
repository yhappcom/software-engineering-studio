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
**IN STUDY — nine integrated executable/model blocks; real WAL crash/checkpoint/main-file-copy boundary added.** Canonical includes `research/data/D005_backup_restore_recovery_acceptance.md`, process-crash/capacity/syscall-fault notes, `research/data/D005_short_write_progress_boundary.md`, `research/data/D005_torn_write_recovery_model.md`, and `research/data/D005_wal_crash_checkpoint_backup_boundary.md`.

Prior Linux/Python/SQLite evidence distinguishes uncommitted rollback from committed persistence, forces bounded `SQLITE_FULL`, injects syscall-level `pwrite/pwrite64=ENOSPC`, injects `fsync/fdatasync=EIO`, and shows positive syscall short progress can be retried while zero progress fails. A bounded executable MODEL separates torn durable image from syscall short progress.

New Python 3.13.5 / SQLite 3.46.1 / Linux WAL evidence disables auto-checkpoint, commits row `200` in a child, then exits with `os._exit(77)`. Before checkpoint, a copy of only the main DB remained structurally valid but contained only baseline `100`, while normal reopen with the retained WAL observed committed `100,200`. After explicit checkpoint, a new main-file-only copy contained `100,200`. This transfer validates that COMMIT and CHECKPOINT are distinct and that `integrity_check=ok` on a main-file-only copy is not a semantic-completeness oracle for active WAL state.

### D006 — Replication, synchronization, consistency, idempotency and conflicts
**IN STUDY — five integrated blocks; exact-ref LogMate protocol transfer added.** Canonical: `research/data/D006_replication_sync_consistency_idempotency_conflicts.md`, `research/data/D006_real_tcp_ambiguous_retry_restart.md`, `research/data/D006_network_namespace_link_interruption.md`, `research/data/D006_logmate_inbound_cursor_atomicity_transfer.md`.

Real boundaries cover server death after commit/before ACK and live-process isolated kernel link-down/timeout/recovery/retry. Exact-ref LogMate transfer establishes that durable replication progress must not outrun required durable semantic effects unless an independently validated replay/reconciliation mechanism exists. Actual LogMate persistence/Sync remains unimplemented at the inspected ref.

## Product transfer retained
Exact LogMate ref rechecked: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-19`. Production identity is unknown; default branch is not assumed to equal production. D005 does not claim LogMate currently uses SQLite WAL.

## Gate assessment
Data Stage 1 remains **NOT PASS**. D001-D006 cover the planned Foundation mechanisms with executable evidence. D005 now includes actual WAL process-crash/checkpoint behavior in addition to rollback-journal process death, logical capacity, syscall ENOSPC, syscall sync-EIO, syscall short-progress handling and a bounded torn durable-image MODEL. Physical filesystem/device/power behavior, truthful-vs-lying fsync, checkpoint interruption/concurrency, live Online Backup API under WAL, mobile/backend behavior and Dart/Flutter transfer remain incomplete.

## Dependencies / handoffs
- **Foundations:** F001 direct Dart/Flutter remains OPEN; F006 process/I/O and transport/apply/commit/ACK distinctions retained.
- **Architecture:** transaction, recovery, durability, backup consistency points and replication progress publication are semantic/state-ownership contracts.
- **Mobile:** reproduce WAL/process-death/backup-export, storage exhaustion, sync failure and recovery on the exact Android/iOS/Flutter stack.
- **Quality:** backup/recovery oracles must compare semantic completeness with structural health; add committed-but-uncheckpointed WAL state to future suites.
- **Systems:** journal/synchronous/VFS/filesystem/device assumptions are part of durability claims; COMMIT visibility is not a blanket power-loss guarantee.
- **LogMate:** define backup consistency point and atomic inbound entity/tombstone/revision/receipt effects before persistence/Sync implementation.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable after environment recheck 2026-09-19.
- D005 physical full filesystem/device, physical torn durable write, truthful-vs-lying fsync under power loss, directory fsync, WAL checkpoint interruption/starvation, live Online Backup API under WAL concurrency, OS/power crash and Android/iOS transfer remain OPEN. The torn-write fixture is MODEL evidence only; the WAL block is real SQLite process-crash/checkpoint evidence, not physical power-loss evidence.
- D006 exact server cursor/batch/receipt semantics, remote/packet faults, concurrent retry, dedup retention/GC, external side effects, tombstone GC and real multi-writer/backend evidence remain OPEN.
- No Data Foundation PASS yet.

## Next work
Use Balance Loop. Do not repeat equivalent rollback crash, `max_page_count`, `pwrite=ENOSPC`, ordinal `fsync=EIO`, positive-short-write sizes, torn-sector-count, or simple WAL row-count variants. F001 direct Dart/Flutter execution remains first if a trustworthy SDK appears. Otherwise advance only to a materially stronger rung such as WAL checkpoint interruption/concurrency or Online Backup API behavior, physical/platform transfer, real CI/attestation, natural release/ADR evidence, independent product build, or another track's stronger gap.
