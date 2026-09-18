# D005 — Process-Crash Transaction Boundary

Status: **IN STUDY — real application-process crash evidence added**  
Date: 2026-09-18  
Lead: Data, Persistence & Distributed Systems

## Problem
D005 previously had SQLite/POSIX executable restore evidence but explicitly lacked crash evidence. This block tests one narrower real boundary available in the current environment: abrupt application-process termination before versus after an SQLite transaction commit.

## SOURCE
Checked 2026-09-18.

- SQLite `transactional.html`: SQLite states that transactions are atomic/durable across program crash, OS crash, or power failure, subject to its documented storage/OS assumptions.
- SQLite `wal.html`: in WAL mode, changes are appended to the WAL and a transaction commits when the commit record is appended.
- SQLite `atomiccommit.html`: explains crash recovery and the filesystem/sync assumptions behind atomic commit; its detailed rollback-journal mechanism is not silently transferred to WAL.
- SQLite `lang_transaction.html`: explicit transactions persist until COMMIT/ROLLBACK and are rolled back when the connection closes; the fixture deliberately uses abrupt process exit rather than a normal close path.

## SYNTHESIS
`SQL statement executed → transaction has pending changes → commit boundary crossed → process terminates → next process opens database → recovery/read → application acceptance`

These are distinct states. In particular, executing an INSERT before process death is not evidence that the effect was committed, while a successful COMMIT followed by application-process death is a materially different boundary.

## EXECUTABLE VALIDATION
Fixture: `research/data/fixtures/D005_process_crash_transaction_boundary.py`.

Environment observed 2026-09-18: Python 3.13.5 / Linux; Python `sqlite3` runtime accepted `journal_mode=WAL` and `synchronous=FULL`. The standalone `sqlite3` CLI was not installed. Direct Dart/Flutter execution was unavailable.

### CLAIM
On this host/runtime, an abruptly terminated child process with an active uncommitted WAL transaction does not publish the inserted row to the next process, while an explicitly committed transaction remains visible after the child immediately exits without orderly connection shutdown.

### SPEC / PROPERTY
Independent acceptance property for this bounded fixture:
- `PRAGMA integrity_check` must return `ok`;
- baseline row must remain;
- the uncommitted child row must be absent after abrupt exit;
- the committed child row must be present after abrupt exit.

### TARGET / FAILURE INJECTION
A parent process creates the database. Separate child processes execute `BEGIN IMMEDIATE` + INSERT. The uncommitted child calls `os._exit(24)` without COMMIT/close. The committed child calls `commit()` then immediately `os._exit(23)`, also bypassing orderly close.

### OBSERVATION
Observed output:

```text
journal_mode= wal
uncommitted_exit= 24 rows= [('baseline', 'baseline')]
committed_exit= 23 rows= [('baseline', 'baseline'), ('committed', 'committed')]
D005 process-crash transaction boundary: PASS
```

### VALIDATION
PASS for the stated application-process-crash boundary on this environment. This is stronger than the prior synthetic failure injection because an actual OS process is terminated with an open SQLite transaction and a fresh process performs the acceptance read.

### DEBUG / ROOT-CAUSE BOUNDARY
The distinguishing intervention is whether the SQLite COMMIT completes before abrupt process exit. The same database, journal mode, synchronous setting, statement shape and acceptance oracle are retained. The observation is consistent with SQLite's transaction/WAL model: the uncommitted effect is not accepted as committed state, while the committed effect is recovered/read by the next process.

This does **not** prove the internals of every filesystem write in this run, nor does it independently reproduce power-loss behavior.

## CONTRADICTION / INVALID SHORTCUTS
- `INSERT returned` ≠ durable committed effect.
- `process died` ≠ committed data must be lost.
- application-process crash evidence ≠ OS-crash evidence.
- application-process crash evidence ≠ power-cut evidence.
- `synchronous=FULL` on one Linux runtime ≠ every filesystem/device honors the assumptions identically.
- successful SQLite recovery ≠ application semantic recovery for arbitrary schemas/data.

## ALTERNATIVES / NEXT FAILURE BOUNDARIES
A stronger next rung would use a controlled crash/power-failure harness or storage fault injection that can distinguish filesystem/page/WAL persistence states. That requires trustworthy infrastructure not available in this run. Mobile process death, Android/iOS storage behavior, Flutter database plugin behavior, open-handle restore, WAL checkpoint interruption and storage-full remain separate transfer tests.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F006 process and OS-boundary distinctions apply. `dart`/`flutter` executables remain unavailable; direct transfer OPEN.
- **Architecture:** A003 contract distinction applies: transaction commit semantics and application acceptance are separate contracts.
- **Mobile:** actual Android/iOS process death and plugin/storage stack remain TRANSFER VALIDATION.
- **Data:** extends D005 and supports D001/D002 transaction/durability boundaries; does not close power-loss/WAL restore questions.
- **Quality:** uses a real process-crash failure case, fresh-process acceptance oracle, and controlled intervention; production reliability is not inferred.
- **Systems:** filesystem/device durability assumptions remain outside the application-process evidence boundary.
- **Design Studio:** recovery UI semantics could consume committed/pending distinctions, but no design canonical decision changes here.
- **Web Manager:** not materially relevant.
- **Marketing Manager:** not materially relevant.
- **Product:** no product repository was audited; no MintTap/LogMate implementation claim is made.

## OPEN / VALIDATION
1. OS crash and actual/simulated power-loss persistence.
2. WAL/checkpoint interruption and companion-file handling during restore.
3. filesystem/fsync/device behavior and storage-full/I/O faults.
4. Android/iOS + exact Flutter persistence stack transfer.
5. application/domain recovery invariants beyond the fixture's simple row oracle.

## HANDOFFS
- **TO Quality:** reuse this child-process crash pattern for recovery/regression tests where the target stack can be launched out-of-process.
- **TO Mobile:** reproduce the pre/post-commit termination boundary on the exact Android/iOS persistence implementation rather than assuming SQLite/Python transfer.
- **TO Systems:** stronger durability claims require a fault model below application-process termination.

## Current judgment
This closes one named D005/Quality evidence gap: **real application-process crash/restart** is now observed rather than modeled. It does not close OS-crash, power-loss, mobile, or production durability, so Data Foundation remains NOT PASS.
