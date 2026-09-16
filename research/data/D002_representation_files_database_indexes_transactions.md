# D002 — Representation, Files, Databases, Indexes & Transaction Fundamentals

Status: **IN STUDY — two integrated executable Foundation blocks complete**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem

Application data work often collapses several different mechanisms into “storage”: serialization format, file publication, database transaction, journal mode, index, and durability. D001 separated state/persistence/durability/authority. D002 asks what each concrete mechanism actually contributes and which guarantees it does not provide.

## SOURCE

Primary sources checked/rechecked 2026-09-17:

- IETF RFC 8259: JSON is a structured-data text serialization format; it does not define transaction or durability semantics.
- SQLite, *Atomic Commit In SQLite*: rollback journaling implements all-or-nothing transaction mechanics under documented storage/VFS assumptions.
- SQLite, *Write-Ahead Logging*: WAL reverses rollback-journal write ordering: original database pages remain in the database while changes are appended to the WAL; a commit record in WAL marks commit. WAL adds checkpointing and has different concurrency/file-lifecycle properties. The `-wal` file is part of persistent database state while relevant committed content has not been checkpointed and must not be casually separated from the database.
- SQLite `PRAGMA synchronous`: durability depends on journal mode and synchronous policy. In particular, SQLite documents WAL + `synchronous=NORMAL` as consistent but potentially losing recently committed transactions after power/system failure, while application crashes preserve transactions; `FULL` adds a WAL sync after each commit for stronger power-loss durability.
- SQLite, *Query Planning*: indexes are auxiliary access structures; query semantics remain distinct from chosen access path.

## SYNTHESIS — separate the mechanisms

Baseline:

`semantic data → serialization/encoding → publication/update mechanism → transaction boundary → journal/recovery mechanism → synchronous/durability policy → indexes/projections → query/read contract`

These roles are not interchangeable.

### Serialization
Serialization maps semantic values to bytes/text. Valid representation does not imply atomic replacement, durability, schema compatibility, or authority.

### File publication
A destructive overwrite can expose a partial representation if interrupted. Staging construction separately can preserve the old canonical file before publication, but that bounded model does not establish filesystem crash/power-loss atomicity.

### Database transaction and journal mode
A transaction defines an all-or-nothing semantic mutation boundary. Journal mode is a mechanism used to realize recovery/commit behavior; it does not define the application's domain invariant. Rollback journal and WAL can both preserve the bounded committed/uncommitted distinction while using materially different physical mechanisms.

### Durability policy
`COMMIT`, journal mode, and durability scope must not be collapsed. SQLite's own documentation distinguishes application crash from OS/power failure and distinguishes synchronous policies. Therefore “WAL enabled” is not a complete durability specification.

### Index
An index is an access structure, not a second semantic authority. It may change the query plan while preserving the same result.

## EXECUTABLE VALIDATION

Fixtures:
- `research/data/fixtures/D002_representation_transaction_index.py`
- `research/data/fixtures/D002_journal_mode_process_exit.py`

Environment for current executable evidence:
- Python 3.13.5
- SQLite 3.46.1
- Linux 6.18.44 x86_64 / glibc 2.41

### Block 1 — representation / transaction / index

Previously reproduced:
- interrupted destructive JSON overwrite left invalid canonical JSON;
- interruption before staged publication left the old canonical JSON intact in the bounded process model;
- explicit SQLite transaction failure before commit + rollback left only baseline A;
- adding an index changed `EXPLAIN QUERY PLAN` from scan to indexed search while semantic result count stayed equal.

### Block 2 — rollback journal vs WAL under abrupt application-process exit

**CLAIM:** journal modes can use different physical mechanisms while both preserving the bounded committed/uncommitted transaction distinction across an abrupt application-process exit.

**SPEC/PROPERTY:** after reopening, B must be absent if the child process exited after INSERT but before COMMIT; B must be present if COMMIT completed before the same abrupt exit. Baseline A must remain and `PRAGMA integrity_check` must report `ok`.

**TARGET:** SQLite 3.46.1 using `journal_mode=DELETE` and `journal_mode=WAL`, both with `synchronous=FULL`.

**INPUT/STATE:** database begins with `A=60`; child begins `BEGIN IMMEDIATE`, inserts `B=90`, optionally commits, then terminates with `os._exit(99)` without normal connection cleanup.

**ORACLE:** exact reopened row set + `PRAGMA integrity_check`.

**OBSERVATION:**
- DELETE / uncommitted exit → only A, integrity `ok`;
- DELETE / committed exit → A+B, integrity `ok`;
- WAL / uncommitted exit → only A, integrity `ok`;
- WAL / committed exit → A+B, integrity `ok`.

**VERDICT:** bounded application-process-exit property reproduced for both journal modes.

**DEBUG / ROOT CAUSE:** the meaningful boundary in this experiment is COMMIT, not graceful connection close. Abrupt process exit after an uncommitted INSERT did not promote B into recovered committed state; completing COMMIT before the same abrupt exit did. The experiment deliberately does not infer identical physical recovery paths between DELETE and WAL.

**EVIDENCE LIMIT:** this is not OS-crash, power-loss, fsync-failure, torn-write, storage-controller, filesystem, Android/iOS, or benchmark evidence. `synchronous=FULL` was selected to avoid intentionally weakening the tested durability policy, but this Linux process-exit experiment cannot establish SQLite's documented power-loss guarantees.

## CONTRADICTIONS / INVALID SHORTCUTS

- `valid serialization format` ≠ `atomic update protocol`.
- `database used` ≠ `correct transaction boundary`.
- `journal_mode=WAL` ≠ `durability specification`.
- `COMMIT returned` ≠ `every failure-domain durability claim`.
- `application-process crash survived` ≠ `OS/power-loss survived`.
- `WAL and rollback passed the same oracle` ≠ `same physical mechanism/cost/concurrency behavior`.
- `index exists` ≠ `index is semantic source of truth`.
- `staging + replacement` ≠ `power-loss-safe durable publication` without target filesystem evidence.

## ENGINEERING JUDGMENT

Configuration names should not substitute for guarantees. A product decision should state at least the semantic transaction boundary, journal/recovery mechanism, synchronous/durability expectation, target failure domains, and recovery oracle. WAL may be attractive for concurrency/performance, but that is a separate measured decision rather than a correctness synonym.

## TRANSFER VALIDATION — LogMate relevance

Retained evidence identity:

`yhappcom/logmate → main commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-16`

That ref establishes Flutter/Dart context but not a local-ledger storage implementation. No PROJECT DECISION selects SQLite, WAL, JSON, Drift, Isar, or another technology.

TRANSFER: if LogMate later uses SQLite-family persistence, tests should distinguish semantic transaction correctness from journal-mode/durability configuration and should include the actual target platform failure boundary. Search/totals/export projections should remain non-authoritative unless explicitly designed otherwise.

## RELATED DOMAIN CHECK

- **Foundations:** F001 process boundary reused; direct Dart/Flutter execution remains OPEN after environment recheck 2026-09-17.
- **Architecture:** A002/A003 constrain mutation authority, invariant-aligned transaction boundaries, and compatibility.
- **Mobile:** target Android/iOS filesystem/database/process behavior remains OPEN; Linux evidence is not transferred as platform proof.
- **Data:** D001 durability/authority model directly reused; D002 now distinguishes journal/recovery and synchronous policy in addition to representation/transaction/index.
- **Quality:** Q002 evidence-boundary discipline applied: the real SQLite mechanism is exercised, and excluded failure domains are explicit.
- **Systems:** fsync/storage-stack behavior, performance, secure storage, release/config identity remain joint dependencies.
- **Design Studio:** no design contract changed; future saved/sync/error semantics must map to real commit/recovery states.
- **Web Manager:** browser/PWA storage is not inferred from SQLite evidence.
- **Marketing Manager:** not materially relevant.
- **Product:** no new product behavior claim was required; retained exact LogMate ref is only transfer context.

## OPEN / VALIDATION

1. Power-loss/OS-crash durability remains OPEN and requires a trustworthy failure environment; do not simulate it with `os._exit`.
2. Measure transaction grouping, WAL/checkpoint and index costs before performance conclusions.
3. Validate Android/iOS database/filesystem behavior before mobile durability claims.
4. D003: old/new reader-writer schema compatibility plus interrupted migration/rollback.
5. D005: prove backup by restore, not successful export alone.
6. No Data Foundation PASS yet.

## HANDOFFS

- **TO Architecture:** keep transaction boundaries aligned with domain invariants/authority, independent of journal mode.
- **TO Quality:** classify application-process exit separately from OS/power-loss failure; tests must name the actual failure domain.
- **TO Mobile:** reproduce commit/recovery semantics on exact Android/iOS storage/database stack before transfer.
- **TO Systems:** benchmark journal/synchronous/checkpoint choices and validate lower storage-stack durability assumptions under exact platform/artifact identity.

## Current judgment

D002 now has independent evidence that representation, publication, transaction, journal/recovery mode, durability policy and indexing are distinct. The reusable rule is: **state the semantic guarantee and failure domain first; configuration names such as JSON, SQLite, WAL or index do not themselves prove atomicity, durability, authority or performance.**
