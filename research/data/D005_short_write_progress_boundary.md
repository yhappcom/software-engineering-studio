# D005 — Unix VFS short-write progress boundary

Date: 2026-09-19  
Lead: Data, Persistence & Distributed Systems  
Status: **IN STUDY — bounded executable Linux/SQLite evidence; NOT PASS**

## Problem
D005 already had process-death, bounded-capacity, syscall `ENOSPC`, and `fsync/fdatasync=EIO` evidence. A materially different OPEN item was short-write behavior: an OS write may report fewer bytes than requested without being a total failure.

## SOURCE
SQLite's architecture documentation places file writing behind the VFS OS interface. Current Unix VFS source (`src/os_unix.c`, official SQLite source artifact checked 2026-09-19) shows `unixWrite()` repeatedly calling `seekAndWrite()` while the call returns positive progress smaller than the remaining amount. The same code maps a non-progressing write to `SQLITE_FULL`, while negative non-ENOSPC errors map to `SQLITE_IOERR_WRITE`. SQLite's result-code documentation defines `SQLITE_IOERR_WRITE` as a VFS write I/O failure and distinguishes full-disk `SQLITE_FULL`.

Primary sources:
- https://www.sqlite.org/arch.html
- https://sqlite.org/src/artifact/410185df49 (`src/os_unix.c`, official source artifact)
- https://www.sqlite.org/rescode.html

## VALIDATION
Fixture: `research/data/fixtures/D005_short_write_progress_boundary.py`.

Environment observed 2026-09-19: Linux 6.18.44 x86_64, Python 3.13.5, dynamically linked Python `sqlite3`, GCC available. `dart` and `flutter` were not present.

The fixture compiles an `LD_PRELOAD` shim and creates an independently committed baseline SQLite database containing `ledger=[100]`. It then starts a fresh Python process using rollback-journal mode and `synchronous=FULL`, attempts to insert `200`, and intercepts the first target database `pwrite/pwrite64` call.

### Case A — positive-progress short write
Injected observation: requested 512 bytes, underlying syscall was allowed to write 256 bytes and returned 256.

Observed application result: `COMMIT_OK`. Fresh reopen produced `ledger=[100,200]` and `PRAGMA integrity_check=ok`.

### Case B — zero-progress write
Injected observation: requested 512 bytes, shim returned 0 without writing bytes.

Observed application result: Python SQLite surfaced code 13 `SQLITE_FULL` (`database or disk is full`). Fresh reopen produced only baseline `ledger=[100]` and `PRAGMA integrity_check=ok`.

## DEBUG / ROOT CAUSE
The positive-progress result is consistent with and explained by the inspected Unix VFS loop: a partial positive return reduces the remaining amount, advances offset/buffer, and retries. The zero-progress result is consistent with the same source path's `amt>wrote` handling and `SQLITE_FULL` mapping. This is stronger than inferring behavior from a green transaction alone because the lower-layer injected return and the VFS control path were both inspected.

## SYNTHESIS
A short write is not synonymous with a failed logical write. Correctness depends on the caller/VFS contract: positive progress may be retried until the requested logical write is complete, while zero/negative progress crosses a failure boundary. Therefore fault campaigns must record both requested and returned byte counts and must not classify every `returned < requested` event as equivalent.

## CONTRADICTION / refinement
This refines the prior queue wording `short/torn write` into two separate mechanisms. **Short write** is a syscall progress/result condition and can be handled by retry logic. **Torn write** is a persistence/atomicity phenomenon in which only part of an intended sector/page becomes durable, potentially despite a different syscall-level observation. This fixture does not validate torn-write or power-loss behavior.

## EVIDENCE LIMIT / OPEN
- `LD_PRELOAD` syscall interception is not physical disk/filesystem failure.
- Only one positive partial-write placement and one zero-progress placement were exercised; this is not exhaustive across journal/main/temp files or every VFS path.
- No power cut, torn sector/page, lying successful write/sync, WAL/checkpoint, directory persistence, Android/iOS, Dart/Flutter, or production persistence was tested.
- Python's bundled/runtime SQLite version identity was not promoted into a cross-version guarantee; the mechanism was source-checked against current official Unix VFS source and execution was bounded to this environment.
- Direct F001 Dart JIT/AOT and Flutter runtime validation remains OPEN because no trustworthy executable was available.

## RELATED DOMAIN CHECK
- Foundations: F001/F006 considered; OS write completion and application durability remain distinct.
- Architecture: persistence behavior is externally meaningful when it affects transaction/recovery contracts.
- Mobile: real Android/iOS storage stack transfer remains required.
- Data: directly advances D005.
- Quality: failure injection needs byte-progress-aware oracles; `integrity_check` is structural, not sufficient semantic recovery evidence by itself.
- Systems: durability claims must separate short syscall return, torn durable write, synchronization, and power/device behavior.
- Design Studio / Web Manager / Marketing Manager: not materially relevant to this storage mechanism in this block.
- Product repositories: no product behavior audited; no product canonical file changed.

## HANDOFFS
- **Quality:** preserve requested/returned byte count and target file/offset when constructing storage fault matrices; do not collapse positive short writes and zero-progress failures.
- **Systems:** keep torn-write/power-loss claims OPEN; this evidence only covers Unix VFS handling of a bounded syscall short-write condition.
- **Mobile/Data future transfer:** reproduce against the exact persistence library/VFS/platform stack before relying on this behavior in LogMate or MintTap recovery design.
