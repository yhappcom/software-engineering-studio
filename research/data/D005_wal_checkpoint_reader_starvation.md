# D005 — WAL checkpoint reader-starvation boundary

Date: 2026-09-19
Status: **IN STUDY — EXECUTABLE SQLITE CONCURRENCY EVIDENCE**

## Problem
Prior D005 evidence established that committed WAL state can exist beyond the main database file. The next distinct question is whether a checkpoint can always consolidate that state while readers are active.

## SOURCE
SQLite WAL documentation states that each reader fixes an end mark for its transaction. A checkpoint may run concurrently with readers but must stop before overwriting database pages needed by a reader. SQLite documents checkpoint starvation: long-running or continuously overlapping readers can prevent checkpoint completion/reset and allow WAL growth. `SQLITE_CHECKPOINT_PASSIVE` does as much work as possible without waiting; RESTART/TRUNCATE are stronger modes but can be blocked by readers.

Primary sources checked 2026-09-19:
- https://sqlite.org/wal.html
- https://sqlite.org/c3ref/wal_checkpoint_v2.html
- https://sqlite.org/c3ref/c_checkpoint_full.html

## VALIDATION
Environment: Python 3.13.5 / SQLite 3.46.1 / Linux.

Setup:
1. enable WAL and disable auto-checkpoint on the writer;
2. create `ledger`, insert baseline `100`, and truncate-checkpoint it;
3. open a second connection, begin a read transaction and observe only `100`;
4. writer commits `200` and `300` after the reader's end mark;
5. a third connection with `busy_timeout=0` attempts PASSIVE and TRUNCATE checkpoints;
6. end the reader transaction and retry TRUNCATE.

Observed:
- WAL size with pinned reader and later commits: 16512 bytes;
- `PRAGMA wal_checkpoint(PASSIVE)` returned `(0, 4, 0)`: four log frames, zero checkpointed in this fixture;
- `PRAGMA wal_checkpoint(TRUNCATE)` while the reader remained active returned `(1, 4, 0)` and the WAL remained 16512 bytes;
- the reader continued to observe its stable snapshot `[100]`;
- after reader COMMIT, TRUNCATE returned `(0, 0, 0)`, WAL size became 0, fresh/current state was `[100,200,300]`, and `integrity_check=ok`.

## SYNTHESIS
`committed WAL state exists` does not imply `checkpoint can immediately consolidate/reset WAL`. Reader snapshot lifetime is an input to checkpoint progress. A backup/maintenance strategy that assumes an immediate checkpoint without accounting for active readers can fail or stall even though the database remains semantically correct.

Checkpoint progress and application data correctness are different properties. In this run, the blocked checkpoint preserved the reader's snapshot and later succeeded after the reader ended; the busy/incomplete result is therefore an operational progress signal, not evidence of data corruption.

## ENGINEERING JUDGMENT
For products that deliberately manage WAL checkpoints, checkpoint outcomes and long-lived reader lifetimes should be observable. A policy should define whether to retry, defer to a reader gap, or use a stronger checkpoint mode with an explicit blocking budget. This is not a product decision for LogMate or MintTap.

## CONTRADICTION / refinement
Any earlier shorthand that treats explicit checkpoint as an unconditional consolidation step is too strong. Explicit invocation is an attempt whose completion depends on concurrency and checkpoint mode.

## EVIDENCE LIMIT
This is process-level SQLite concurrency on one Linux host, not power loss, filesystem/device failure, Android/iOS behavior, Flutter plugin behavior, multi-process mobile lifecycle evidence, or production evidence. It does not validate Online Backup API behavior or prove a particular checkpoint policy is optimal.

## RELATED DOMAIN CHECK
- Foundations: F004/F006 concurrency and process/I/O boundaries apply; direct Dart/Flutter remains OPEN.
- Architecture: reader lifetime and maintenance ownership can become explicit persistence contracts.
- Mobile: real app lifecycle/process/background transfer remains OPEN.
- Data: directly extends D005 WAL crash/checkpoint evidence.
- Quality: checkpoint tests need a progress/busy oracle distinct from semantic-integrity oracles.
- Systems: WAL growth, blocking budget and storage pressure are operational/resource concerns.
- Design Studio / Web Manager / Marketing Manager: considered; no canonical decision there changes this storage mechanism.
- Product source: no product implementation claim was required for this mechanism block.

## OPEN / VALIDATION / CHANGE WATCH
- Online Backup API under concurrent writes/readers;
- checkpoint interruption during copy/reset;
- continuous-reader starvation campaign and resource-growth thresholds;
- Android/iOS/Flutter persistence-stack transfer;
- physical power-loss/device behavior.

## HANDOFFS
- Quality: future recovery suites should distinguish checkpoint busy/incomplete from semantic corruption and verify eventual progress after the blocking reader ends.
- Systems: checkpoint policy needs WAL-size/resource observability and a bounded blocking/retry strategy when adopted.
- Mobile/Data product work: validate exact persistence library/journal mode and lifecycle before transferring this mechanism into a product decision.
