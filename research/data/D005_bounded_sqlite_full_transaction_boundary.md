# D005 — Bounded SQLite SQLITE_FULL Transaction Boundary

Status: **IN STUDY — executable storage-capacity failure evidence**  
Date: 2026-09-18  
Lead: Data, Persistence & Distributed Systems

## Problem
D005 already had backup/restore acceptance, validate-before-publish, and real application-process crash/restart evidence. A named gap remained around storage-full/I/O failure. The current environment cannot mount a constrained tmpfs (`mount: permission denied`), so an actual filesystem/device `ENOSPC` was not fabricated. This block instead exercises SQLite's own documented database-growth limit, which returns `SQLITE_FULL`, and keeps OS/filesystem exhaustion explicitly OPEN.

## SOURCE
Primary SQLite documentation checked 2026-09-18:
- SQLite result codes: `SQLITE_FULL` means a write could not complete because the disk is full; it may also arise from temporary-file storage.
- SQLite implementation limits: `PRAGMA max_page_count` can limit database growth; an insertion requiring growth beyond the limit returns `SQLITE_FULL`.
- SQLite atomic-commit documentation: transaction atomicity relies on journal/commit protocol and stated OS/filesystem/device assumptions; storage and power-failure claims must not exceed those assumptions.

## SYNTHESIS
`capacity/growth failure → statement/transaction error → rollback/recovery path → semantic state oracle → physical integrity oracle`

A storage-capacity error is not itself evidence that application state is safely recoverable. The application must preserve the transaction boundary and verify the post-failure state it depends on.

## EXECUTABLE VALIDATION
Fixture: `research/data/fixtures/D005_sqlite_full_transaction_boundary.py`  
Environment: Python 3.13.5 / SQLite 3.46.1 / Linux.

### CLAIM
Within SQLite's documented `max_page_count` growth-limit mechanism, a transaction that cannot grow the database and returns `SQLITE_FULL` can be rolled back without publishing the attempted semantic row, while the database remains readable and passes `PRAGMA integrity_check`.

### SPEC / PROPERTY
Independent application oracle:
- baseline semantic aggregate is captured before the failing transaction;
- after failure/rollback, aggregate must equal baseline;
- `PRAGMA integrity_check` must return `ok`.

SQLite's documented growth limit supplies the expected error class; the semantic oracle does not derive its expected row state from the attempted implementation path.

### TARGET / INPUT / STATE
- rollback-journal mode, `synchronous=FULL`;
- 512-byte page size;
- one committed baseline row;
- current `page_count=2`, then `max_page_count=4`;
- one 5000-byte BLOB insertion inside `BEGIN IMMEDIATE`, deliberately requiring growth beyond the bounded page limit.

### OBSERVATION
Executed 2026-09-18:
- baseline `(1, 100)`;
- page count `2`, maximum page count `4`;
- insertion raised Python `OperationalError: database or disk is full` with SQLite error code `13`, name `SQLITE_FULL`;
- after explicit rollback, semantic aggregate remained `(1, 100)`;
- `PRAGMA integrity_check` returned `ok`.

### VERDICT
**VALIDATION — PASS for the bounded SQLite growth-limit claim.**

The failure was detected at the intended storage-capacity boundary and the failed transaction did not become accepted semantic state under the oracle.

## ROOT CAUSE / FAILURE BOUNDARY
The deliberately configured database page ceiling prevented allocation of pages needed by the larger insert. SQLite surfaced the documented `SQLITE_FULL` result. Transaction rollback restored the pre-transaction semantic state in this execution.

**CONTRADICTION:** `write attempted` or even partial internal work before an error does not imply an application-level committed effect.

## EVIDENCE LIMIT
This is **not** actual disk exhaustion. `PRAGMA max_page_count` is a deterministic SQLite database-growth constraint used here because privileged filesystem-capacity control was unavailable. It does not establish behavior for:
- OS/filesystem `ENOSPC` on the main DB, rollback journal, WAL, directory entry, or temp storage;
- short writes, `fsync` failure, media error, corruption, kernel crash or power loss;
- WAL/checkpoint capacity failure;
- Android/iOS storage pressure, quota, purge, document provider or cloud-backed paths;
- Flutter/Dart bindings or product behavior.

No claim of power-loss durability or general storage-fault safety is made.

## ALTERNATIVE / NEXT STRONGER EVIDENCE
A materially stronger next storage block requires a trustworthy lower-layer fault mechanism: constrained filesystem/device, SQLite VFS fault injection, or exact platform storage fault controls that can distinguish main-file, journal/WAL, sync and directory failures. Merely adding more `max_page_count` variants would not cross a new failure boundary.

## RELATED DOMAIN CHECK
- **Foundations:** F001 direct Dart/Flutter execution remains OPEN; environment recheck 2026-09-18 found no `dart` or `flutter` executable.
- **Architecture:** transaction/restore boundaries are externally relevant data contracts; no architecture decision changed.
- **Mobile:** actual Android/iOS storage exhaustion and platform persistence remain TRANSFER VALIDATION.
- **Data:** extends D005 from candidate publication and process crash into a bounded capacity-failure class; does not close OS/power/storage-device gaps.
- **Quality:** explicit failure injection plus semantic and integrity oracles used; a raised error alone is not the verdict.
- **Systems:** actual filesystem/device durability and I/O fault injection remain dependencies.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there materially changes this bounded storage mechanism.
- **Product:** no product repository was audited; no MintTap/LogMate implementation claim is made.

## OPEN / VALIDATION
1. Real filesystem/device `ENOSPC`, short-write and sync-error behavior.
2. WAL/checkpoint failure under capacity pressure.
3. OS crash/power loss and filesystem durability.
4. Android/iOS/Flutter storage-pressure transfer.
5. Exact-ref product recovery behavior once implemented.

## HANDOFFS
- **TO Quality:** distinguish deterministic SQLite growth-limit injection from lower-layer filesystem/device faults in recovery campaigns.
- **TO Systems:** a future storage-fault harness should prove which I/O operation failed rather than infer it from an application exception.
- **TO Mobile:** reproduce capacity/quota failures on the exact platform persistence stack before treating this result as mobile evidence.

## Current judgment
This block advances D005 with real SQLite execution of a documented `SQLITE_FULL` capacity boundary and a post-failure semantic/integrity oracle. It does not satisfy the stronger OS/filesystem storage-full requirement. Because privileged constrained-filesystem creation was unavailable, that gap remains explicitly OPEN rather than simulated.
