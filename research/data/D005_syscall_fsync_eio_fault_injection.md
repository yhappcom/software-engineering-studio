# D005 — Syscall-level fsync/fdatasync EIO fault injection

Date: 2026-09-19  
Lead: Data  
Status: **VALIDATION — bounded Linux/SQLite sync fault; NOT PASS**

## Selection
F001 direct Dart/Flutter execution was attempted first. The runtime still exposes neither `dart` nor `flutter`; Python 3.13.5 and GCC 14.2.0 are available. Balance Loop therefore selected D005's explicitly OPEN sync-failure class rather than repeating capacity/write-denial evidence. This changes the failure mechanism from `pwrite=ENOSPC` to failure while flushing previously written bytes toward persistent storage.

## SOURCE
- SQLite result codes: `SQLITE_IOERR_FSYNC` (1034) means an I/O error occurred in the VFS while flushing previously written content from OS/disk-control buffers toward persistent storage; on Unix this corresponds to an `fsync()`-class problem: https://www.sqlite.org/rescode.html
- SQLite atomic commit (rollback mode) documents flush/fsync at key commit points and states that SQLite relies on the OS/filesystem/device honoring those primitives: https://www.sqlite.org/atomiccommit.html

## Claim and validation contract
**CLAIM:** in this rollback-journal/FULL-synchronous fixture, an injected `EIO` at a target database/journal `fsync`/`fdatasync` boundary causes the transaction to fail rather than be accepted as committed semantic state; after reopening, the prior committed baseline remains observable.

- **TARGET:** Python 3.13.5 `sqlite3` on Linux 6.18.44, SQLite runtime used by Python; rollback journal `DELETE`, `synchronous=FULL`.
- **FIXTURE:** `research/data/fixtures/D005_ld_preload_fsync_eio_boundary.py`.
- **PRESTATE:** committed `ledger=[100]`.
- **ATTEMPT:** transaction inserts `200` and commits.
- **FAULT:** Linux `LD_PRELOAD` shim intercepts matching `fsync`/`fdatasync`; selected synchronization call returns `-1`, `errno=EIO`.
- **ORACLE:** control must commit `[100,200]`; injected cases must surface SQLite extended code 1034 / `SQLITE_IOERR_FSYNC`; fresh connection must observe only `[100]` and `PRAGMA integrity_check='ok'`.
- **ENVIRONMENT OBSERVED:** Python 3.13.5; GCC 14.2.0; Linux x86_64 6.18.44.

## VALIDATION / FAILURE
A control run with no injected sync failure produced three matching `fdatasync` calls and `COMMIT_OK`; fresh reopen observed `[100,200]` and `integrity_check=ok`.

Three deliberate failure placements were then executed independently from the same baseline:

1. fail matching sync call 1 → `OperationalError: disk I/O error`, code `1034`, `SQLITE_IOERR_FSYNC`; reopen `[100]`, integrity `ok`;
2. fail matching sync call 2 → same extended error; reopen `[100]`, integrity `ok`;
3. fail matching sync call 3 → same extended error; reopen `[100]`, integrity `ok` (SQLite attempted an additional sync during error handling).

A `FAIL_SYNC_N=4` negative control did not inject because the successful path had only three matching sync calls; commit succeeded and reopen observed `[100,200]`.

**VERDICT:** PASS only for the bounded claim above. D005 and Data Stage 1 remain NOT PASS.

## DEBUG / ROOT CAUSE
The causal intervention is materially different from prior `ENOSPC` evidence: ordinary writes are allowed, then a synchronization primitive is forced to report `EIO`. SQLite's extended result identity independently classifies the failure as `SQLITE_IOERR_FSYNC`, matching the injected operation class. The no-fault and too-late-fault controls commit successfully, while failure at each observed sync point rejects the attempted semantic publication.

## SYNTHESIS
A successful userspace write and a successful durability synchronization are separate evidence claims. Recovery acceptance must not infer durability from “the write syscall succeeded” or from database structural health alone. For durability-sensitive state, the exact persistence mode and failed VFS/syscall boundary are part of the evidence identity.

## CONTRADICTION / SUPERSESSION
The prior D005 OPEN item “fsync/fdatasync failure absent” is narrowed: a syscall-level `EIO` synchronization fault now exists for Linux/SQLite rollback-journal FULL mode. This does **not** supersede OPEN physical power-loss/device behavior, lying/broken fsync implementations, WAL/checkpoint semantics, or mobile persistence behavior.

## EVIDENCE LIMIT / OPEN
- fault is injected at libc `fsync`/`fdatasync`, not a physical disk/controller/filesystem failure;
- no claim that successfully returning `fsync` actually survived real power loss;
- no short write, torn write, directory-fsync, rename/delete, WAL checkpoint, corruption, quota, or real full-device test;
- call ordinal is fixture-specific and must not be generalized as a stable SQLite implementation sequence;
- no Dart/Flutter, Android/iOS, product persistence stack, or production evidence.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F006 checked; direct Dart/Flutter execution remains blocked.
- **Architecture:** durable publication is an externally meaningful semantic boundary when application correctness depends on recovery.
- **Mobile:** exact Android/iOS filesystem/database/plugin durability semantics still require transfer validation.
- **Data:** extends D005 from write denial to a distinct synchronization-failure class.
- **Quality:** fault identity plus semantic reopen oracle and negative controls improve causal discrimination; structural health alone remains insufficient.
- **Systems:** persistence evidence must bind storage mode, sync policy and exact fault boundary; this is not device durability certification.
- **Design Studio / Web Manager / Marketing Manager:** considered under collaboration rules; not materially relevant to this storage mechanism, so no canonical files were inspected or edited.
- **Product source/ref:** not inspected because this block makes no claim about MintTap/LogMate implementation.

## HANDOFFS
- **TO Mobile/Quality:** when trustworthy Flutter/device infrastructure exists, reproduce failure/restart on the exact product persistence stack and judge semantic state, not only API error or DB health.
- **TO Systems:** future durability/release validation should distinguish write success, sync success, truthful sync semantics, checkpoint/rename/directory persistence and actual power-loss evidence.
