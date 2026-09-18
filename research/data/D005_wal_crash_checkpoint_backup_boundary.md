# D005 — WAL Crash, Checkpoint & Main-File Backup Boundary

Status: **IN STUDY — EXECUTABLE WAL TRANSFER / NOT PASS**  
Date: 2026-09-19  
Lead: Data, Persistence & Distributed Systems

## Problem
D005 already established rollback-journal process crash, capacity/write/sync faults, short-write progress, and a bounded torn-durable-image model. A named OPEN remained WAL/checkpoint behavior. The high-value question is narrower than “does WAL work?”: after a WAL transaction is committed but before checkpoint, what state constitutes the database for crash recovery and backup/copy purposes?

## SOURCE
Primary SQLite material checked 2026-09-19:
- https://www.sqlite.org/wal.html — WAL commit occurs by appending a commit record; checkpoint later transfers WAL transactions into the original database. SQLite explicitly states the `-wal` file is part of persistent database state and must accompany the database when copied/moved while required.
- https://www.sqlite.org/isolation.html — in WAL mode, changes go to the separate WAL and are later moved into the original database by checkpoint.
- https://www.sqlite.org/fileformat.html — WAL frames contain changed pages; a commit marker defines transaction commit; checkpoint transfers valid WAL content to the main database.
- https://www.sqlite.org/walformat.html — active WAL-mode state spans main database, WAL and WAL-index; unclean process shutdown can leave WAL/SHM present for recovery.

## CLAIM / PROPERTY
**CLAIM:** In WAL mode, a committed transaction can be durable/visible through the WAL before its pages have been checkpointed into the main database file. Therefore a byte copy of only the main database file is not a valid general backup oracle while required committed state remains in WAL.

**PROPERTY / ORACLE:** Starting from baseline row `100`, commit row `200` in WAL and terminate the writer without clean SQLite close. Before checkpoint:
1. a main-file-only copy is expected to contain only the checkpointed baseline;
2. normal reopen of the original database with its WAL is expected to contain `100,200`;
3. after explicit checkpoint, a new main-file-only copy is expected to contain `100,200`.
All opened copies must also report `PRAGMA integrity_check=ok`; structural integrity alone is deliberately insufficient as the semantic oracle.

## EXECUTABLE VALIDATION
Fixture: `research/data/fixtures/D005_wal_crash_checkpoint_backup_boundary.py`.

Environment actually executed: Python 3.13.5 / Python sqlite3 linked SQLite 3.46.1 / Linux. `dart`, `flutter`, and standalone `sqlite3` CLI were not available; F001 direct Dart/Flutter execution remains OPEN.

Setup:
- create `ledger.db`, enable WAL;
- disable automatic checkpointing with `PRAGMA wal_autocheckpoint=0`;
- insert baseline `100`, then explicitly `wal_checkpoint(TRUNCATE)`;
- child process inserts `200`, COMMITs, then calls `os._exit(77)` without clean SQLite close;
- verify `ledger.db-wal` exists;
- copy only `ledger.db` before normal reopen;
- compare main-only copy, authoritative original+WAL reopen, and post-checkpoint main-only copy.

Observed in the executed run:
- child exit: `77`;
- after child death: `ledger.db` 8192 bytes, `ledger.db-wal` 4152 bytes, `ledger.db-shm` 32768 bytes;
- pre-checkpoint main-file-only copy: rows `[(100,)]`, `integrity_check=ok`;
- normal reopen of original WAL database: rows `[(100,), (200,)]`, `integrity_check=ok`;
- after explicit `PRAGMA wal_checkpoint(TRUNCATE)`, main-file-only copy: rows `[(100,), (200,)]`.

**VALIDATION:** the bounded oracle PASSed. The committed row was semantically part of the database before it appeared in a main-file-only copy. Checkpoint changed where the committed state was materialized, not whether the transaction had already committed.

## FAILURE CASE / ROOT CAUSE
The deliberate weak backup implementation is “copy `X.db` only.” It produced a structurally valid SQLite file (`integrity_check=ok`) that silently omitted a committed transaction still represented in `X.db-wal`.

**ROOT CAUSE:** WAL changes the persistence state vector. Before checkpoint, authoritative committed state can be distributed across the main database and WAL. A main-file-only copy samples only the checkpointed projection. Structural validity of that projection does not establish semantic completeness.

## SYNTHESIS
- `COMMIT` and `CHECKPOINT` are different events in WAL mode.
- `main DB file is structurally valid` does not imply `main DB file contains every committed transaction`.
- backup correctness depends on the backup mechanism's consistency semantics, not merely on copying a file whose name looks canonical.
- WAL companion state is not an incidental cache when it contains committed, uncheckpointed transactions.

## ALTERNATIVES
For an application backup/export requirement, compare mechanisms rather than inventing file-copy folklore:
- SQLite Online Backup API or another documented consistent-copy mechanism;
- an application-controlled checkpoint/quiescence protocol whose concurrency and failure assumptions are explicitly validated;
- raw file-set copying only under SQLite-documented conditions that preserve required WAL state and consistency.

No mechanism is selected here as a LogMate PROJECT DECISION.

## TRANSFER VALIDATION — LogMate
Product identity rechecked 2026-09-19: `yhappcom/logmate → branch main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-19`. `main` is not assumed to be production. The inspected product remains a transfer target; this study does not claim LogMate currently uses SQLite WAL or has this defect.

**ENGINEERING JUDGMENT:** if future LogMate local persistence uses SQLite WAL and Backup/Export is expected to preserve committed user flight records, acceptance tests must exercise committed-but-uncheckpointed state and must not accept `integrity_check=ok` on a main-file-only copy as sufficient recovery evidence.

## RELATED DOMAIN CHECK
- **Foundations:** F001 attempted first; no Dart/Flutter executable available. F006 process/I/O boundary distinctions support commit/checkpoint/close separation.
- **Architecture:** backup mechanism is an externally relevant durability/recovery contract, not an implementation detail when user-owned data is at stake.
- **Mobile:** Android/iOS filesystem, process death, sandbox, document-provider and backup destination semantics remain TRANSFER VALIDATION.
- **Data:** extends D005 from rollback-journal/storage-fault evidence to actual SQLite WAL/checkpoint behavior.
- **Quality:** semantic row-set oracle intentionally disagrees with the structural `integrity_check` oracle in the weak main-file-copy case.
- **Systems:** filesystem/device durability, fsync truthfulness and artifact authenticity remain separate claims.
- **Design Studio:** considered; no design canonical decision changes this low-level WAL persistence mechanism.
- **Web Manager:** not materially relevant to this local persistence mechanism.
- **Marketing Manager:** not materially relevant to this local persistence mechanism.
- **Product:** exact LogMate ref checked; no product repository file edited.

## OPEN / VALIDATION / CHANGE WATCH
- physical power loss and lying-successful storage remain OPEN;
- checkpoint interruption/failure and concurrent-reader checkpoint starvation remain OPEN;
- Online Backup API under live WAL concurrency has not been executed in this block;
- WAL durability varies with `PRAGMA synchronous` and underlying VFS/filesystem/device behavior; do not generalize this process-crash run to hard power loss;
- Android/iOS/Flutter persistence and backup/export transfer remain OPEN;
- no Data Foundation PASS is awarded.

## HANDOFFS
- **TO Quality:** add a committed-but-uncheckpointed WAL state to future backup/recovery acceptance suites; require semantic completeness in addition to structural integrity.
- **TO Mobile:** when a real Flutter/device persistence stack exists, reproduce process death + backup/export from an exact build and exact journal/synchronous configuration.
- **TO Systems:** bind durability claims to journal mode, synchronous mode, VFS/filesystem/device assumptions; COMMIT visibility is not a blanket power-loss guarantee.
- **TO LogMate:** before choosing a local DB backup/export implementation, define the consistency point and test committed-but-uncheckpointed state. No product file was edited.

## Current judgment
This closes the previously named D005 “WAL behavior” gap at a bounded real SQLite process-crash/checkpoint level. It does **not** close physical durability, checkpoint-failure, live-concurrency backup, mobile transfer, or production recovery evidence. Do not repeat simple WAL row-count variants; advance only to a materially different failure/evidence rung.
