# D005 — Syscall-level ENOSPC fault injection

Date: 2026-09-18  
Lead: Data  
Status: **VALIDATION — bounded Linux/SQLite I/O fault; NOT PASS**

## Selection
F001 direct Dart/Flutter remained highest prerequisite severity, but no `dart`/`flutter` executable was found. Official Dart documentation confirms stable SDK installation/archive paths, but this runtime could not retrieve/install a trustworthy SDK. Balance Loop therefore selected D005 because real lower-layer storage-fault evidence was explicitly OPEN and has high data-loss/recovery leverage for LogMate/MintTap.

## Claim and boundary
**CLAIM:** an OS-style `ENOSPC` returned at SQLite's write syscall boundary can be surfaced as `SQLITE_FULL`, and a failed transaction must not be accepted as durable semantic state.

This fixture deliberately intercepts libc `pwrite`/`pwrite64` with `LD_PRELOAD` for the target database/journal pathname and returns `-1` with `errno=ENOSPC`. It therefore exercises a materially lower boundary than `PRAGMA max_page_count`, but it is **not evidence of a physically full filesystem/device**, power loss, short write, fsync failure, or mobile storage behavior.

## SOURCE
SQLite's result-code documentation states that `SQLITE_FULL` means a write could not complete because disk space was unavailable and notes that full-disk conditions normally produce `SQLITE_FULL` rather than `SQLITE_IOERR`: https://sqlite.org/rescode.html

SQLite's atomic-commit documentation explains rollback-mode transaction/journal write and recovery mechanics and explicitly states its underlying OS/filesystem/device assumptions: https://sqlite.org/atomiccommit.html

## Executable validation contract
- **TARGET:** Python 3.13.5 `sqlite3` / SQLite on Linux, rollback-journal default, dynamically linked libc write path.
- **FIXTURE:** `research/data/fixtures/D005_ld_preload_enospc_boundary.py`.
- **PRESTATE:** `ledger=[100]`, committed.
- **FAULT:** target-path `pwrite`/`pwrite64` returns `ENOSPC` while attempting transaction adding `200`.
- **ORACLE:** independent fresh SQLite connection must observe only baseline row and `PRAGMA integrity_check='ok'`; error identity is independently checked as SQLite code 13 / `SQLITE_FULL`.
- **OBSERVATION:** injected run returned `OperationalError: database or disk is full`, code `13`, name `SQLITE_FULL`; fresh reopen observed only baseline row and `integrity_check=ok`.
- **VERDICT:** PASS for the bounded claim; D005 remains NOT PASS globally.

## FAILURE / ROOT CAUSE
The failure is causally injected below SQLite's SQL/transaction layer: matching file-descriptor writes are denied with `ENOSPC`. The same database succeeds without the preload shim. The post-failure semantic oracle rejects publication of the attempted `200` row. This distinguishes an I/O-capacity failure from the earlier logical `max_page_count` ceiling while preserving the same application-level acceptance requirement.

## SYNTHESIS
`SQLITE_FULL` handling is not merely an error-message concern. Recovery acceptance must ask whether the semantic transaction became durable, whether retry/recovery remains possible, and whether the database remains structurally readable. A healthy `integrity_check` alone still cannot establish application-level semantic recovery.

## CONTRADICTION / SUPERSESSION
The prior D005 OPEN item “lower-layer ENOSPC evidence absent” is narrowed: a syscall-level `ENOSPC` injection now exists. The stronger claims “real filesystem/device exhaustion” and “mobile/platform storage-pressure behavior” remain OPEN.

## EVIDENCE LIMIT / OPEN
- no physically full filesystem, quota, tmpfs, flash device, Android/iOS sandbox, or power failure;
- no short-write, fsync/fdatasync failure, journal-delete failure, WAL checkpoint failure, or filesystem corruption;
- LD_PRELOAD interception depends on Linux/glibc-style dynamic linking and `/proc/self/fd`;
- no Dart/Flutter/product persistence stack execution;
- no production evidence.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F006 checked; Dart/Flutter direct execution remains blocked.
- **Architecture:** transaction/recovery publication remains a semantic contract boundary.
- **Mobile:** real Android/iOS storage-full and process lifecycle transfer remains required.
- **Data:** extends D005 from SQLite logical capacity ceiling to injected syscall `ENOSPC`.
- **Quality:** semantic state + structural health are separate recovery oracles.
- **Systems:** fault injector proves the requested syscall failure, not physical-device causation or durability.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this storage mechanism.
- **Product source/ref:** not required; no claim about current product implementation is made.

## HANDOFFS
- **TO Mobile/Quality:** when Flutter/device infrastructure exists, reproduce a real app write under platform-supported storage exhaustion/fault conditions and verify semantic recovery after process restart.
- **TO Systems:** future fault infrastructure should separately target write, short-write, sync, rename/delete and checkpoint boundaries and record exactly which syscall/VFS operation failed.
