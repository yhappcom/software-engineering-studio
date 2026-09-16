# D001 — State, Persistence, Durability & Source of Truth

Status: **IN STUDY — SOURCE/MODEL + PROCESS-CRASH EXECUTABLE EVIDENCE**  
Date: 2026-09-16  
Lead: Data, Persistence & Distributed Systems

## Problem

Engineering discussions often collapse different guarantees into the word “saved”. That causes bugs in offline-first, backup, synchronization and recovery systems.

The Studio needs a precise model separating:

`state → mutation → persistence mechanism → commit/acknowledgement → durability scope → authoritative source → derived/cached projections`.

The key question is not merely “where is the data stored?” but **which state is authoritative, which failure boundary it survives, and which invariants must remain true when execution is interrupted**.

## SOURCE

Primary sources checked on 2026-09-16:

- SQLite Transactions — https://www.sqlite.org/lang_transaction.html
- SQLite Atomic Commit — https://www.sqlite.org/atomiccommit.html
- SQLite Is Transactional — https://www.sqlite.org/transactional.html
- SQLite WAL — https://www.sqlite.org/wal.html
- SQLite PRAGMA / synchronous semantics — https://www.sqlite.org/pragma.html
- Flutter App Architecture Guide — https://docs.flutter.dev/app-architecture/guide
- Flutter Common Architecture Concepts — https://docs.flutter.dev/app-architecture/concepts
- Flutter Offline-first support — https://docs.flutter.dev/app-architecture/design-patterns/offline-first
- Android Offline-first architecture — https://developer.android.com/topic/architecture/data-layer/offline-first

## First-principles model

### 1. State is broader than persistent data

State is information describing the system at a point in time. It can exist at different lifetimes and authority levels:

- local variables / stack state;
- in-memory object or view-model state;
- repository/session cache;
- durable local storage;
- remote authoritative storage;
- replicated copies;
- derived projections/indexes/caches;
- backups or archival copies.

A value being observable in memory proves only that the current execution context contains it. It does **not** prove persistence or durability.

### 2. Persistence and durability are not synonyms

**Persistence** answers where/how state is retained beyond a narrower lifetime, such as beyond a function call or process lifetime.

**Durability** is a guarantee relative to a failure boundary. Useful scopes include:

1. survives a function return;
2. survives navigation/widget reconstruction;
3. survives application process termination;
4. survives application restart;
5. survives operating-system crash;
6. survives power loss;
7. survives device loss/reinstall;
8. survives loss of one replica/server/device.

A statement such as “the write succeeded” is incomplete unless the acknowledgement boundary and required durability scope are known.

### 3. Transaction commit is a semantic boundary

SQLite documents that explicit transactions continue until COMMIT or ROLLBACK and are rolled back if the database connection closes before commit. SQLite's atomic-commit design aims to make a transaction appear all-or-nothing even when interrupted.

This gives a useful distinction:

`mutation executed` ≠ `transaction committed` ≠ `durable under every possible failure`.

The final term depends on database mode, synchronization settings, filesystem/device behavior and the failure being considered.

### 4. “Source of truth” is an authority rule, not merely a file location

Flutter's architecture guidance describes repositories as sources of truth for application data and recommends that the source of truth be the only place allowed to mutate a given data type. Its offline-first guidance allows a repository to coordinate local and remote services behind one authoritative application-facing access point.

Therefore a source of truth should be modeled as:

> the component/state contract that owns authoritative reads and valid mutation semantics for a data domain.

It does **not** necessarily mean:

- there is only one physical copy;
- the authoritative component itself must store bytes directly;
- remote storage is always authoritative;
- the UI's most recent value is authoritative.

A repository can be the application-level source of truth while coordinating a local database, a remote service and caches, provided mutation/consistency rules remain explicit.

### 5. Offline-first systems require an explicit authority policy

Android's official offline-first guidance demonstrates one common policy: higher layers read from a local data source, while a repository synchronizes local and network sources. Flutter's offline-first guidance similarly places coordination in repositories.

This is a **design pattern**, not a universal law. A product must still state:

- authoritative read source while offline/online;
- where writes are first accepted;
- what “saved” means to the user;
- how pending remote synchronization is represented;
- conflict semantics;
- failure/retry semantics;
- whether remote or local state wins in each class of conflict.

### 6. Derived data should not become an accidental second truth

If a value can be deterministically recomputed from canonical records, storing and independently mutating both the source and the derived value creates synchronization risk.

Examples:

- flight records vs monthly totals;
- transactions vs portfolio aggregate;
- canonical timestamp vs separately editable formatted date;
- ledger records vs search index/cache.

Derived data may be persisted for performance, but then it needs an invalidation/rebuild contract rather than independent semantic authority.

### 7. Invariants define valid states across failure boundaries

An invariant is a condition that must remain true for every valid committed state.

Examples suitable for later project validation include:

- one canonical record ID maps to at most one authoritative record version under the chosen identity policy;
- an aggregate equals the canonical records it claims to summarize;
- a transaction that is reported as committed is recoverable within its declared durability scope;
- a cache may be stale, but cannot silently redefine canonical data;
- synchronization metadata cannot make an uncommitted local mutation appear remotely confirmed.

The invariant is more important than the storage API used to implement it.

## EXECUTABLE VALIDATION 1 — application process termination

Fixture: `research/data/fixtures/D001_sqlite_durability.py`

Environment:

- Python 3.13.5
- SQLite 3.46.1
- Linux
- SQLite `journal_mode=DELETE`
- SQLite `synchronous=FULL`

Procedure:

1. create a database and commit a `baseline` row;
2. start a child process;
3. child opens `BEGIN IMMEDIATE`, inserts `uncommitted`, but does not COMMIT;
4. confirm a rollback-journal file exists;
5. kill the child process with SIGKILL;
6. reopen the database;
7. run a second child that inserts `committed` and explicitly COMMITs;
8. reopen again.

Observed result:

```text
before = [(1, 'baseline')]
child_ready = READY
journal_exists_before_kill = true
killed_returncode = -9
after_kill_reopen = [(1, 'baseline')]
commit_child_stdout = COMMITTED
after_committed_reopen = [(1, 'baseline'), (2, 'committed')]
```

### What this establishes

Within this bounded environment:

- executing the INSERT was insufficient for the uncommitted mutation to become authoritative durable state;
- an abrupt application-process termination did not expose the uncommitted row after reopening;
- the explicitly committed row remained visible after the writer process exited and a new connection reopened the database;
- the transaction/commit boundary materially changes recovery semantics.

### What this does **not** establish

This fixture does not prove:

- power-loss durability;
- OS-crash durability;
- flash-storage controller behavior;
- Android/iOS filesystem semantics;
- WAL-mode behavior;
- Flutter plugin behavior;
- distributed sync correctness;
- backup correctness.

SQLite documentation makes broader atomicity/durability claims under documented modes/settings, but those claims must not be confused with what this specific executable fixture measured.

## FAILURE / MISCONCEPTION ANALYSIS

### Misconception: “The write function returned, so the data is safe”

A storage API returning may mean anything from “accepted in memory” to “transaction committed” to “synced to nonvolatile storage”, depending on its contract. The required failure scope must be explicit.

### Misconception: “Local database = source of truth”

A database is a storage mechanism. Source-of-truth status is an application ownership/authority decision. A product can use multiple databases or replicas while keeping one logical mutation authority.

### Misconception: “Single source of truth means one copy”

Replication, caches and indexes are compatible with a single logical authority. The risk is not multiple copies by itself; it is multiple independent mutation authorities without reconciliation semantics.

### Misconception: “Cloud is always more authoritative than local”

That depends on product semantics. An offline-first personal logbook may intentionally accept durable local writes before remote sync. A server-centric financial or collaborative system may use different authority rules. The product contract decides.

### Misconception: “Durable means backed up”

A locally committed database can survive process death while still be lost with the device. Backup/restore and replication protect different failure domains and require separate evidence.

## PRODUCT TRANSFER CHECK — LogMate

Product evidence inspected:

`yhappcom/logmate → main commit b551ce434ad72b1895033e0f3617c73b026d40ea → evidence date 2026-09-16`.

The README states that core work is local/on-device, Firebase Auth and owner Sync are a cloud-minimal connectivity layer above local operation, and the planned implementation sequence puts the local ledger/on-device domain before optional backup/sync.

This makes D001 directly relevant, but **no storage technology or final authority algorithm is inferred from the README**.

Transfer requirements for later LogMate implementation:

- define exactly when a newly entered FlightRecord becomes durably committed;
- distinguish local durable commit from remote-sync acknowledgement;
- ensure Home/logbook/search/totals derive from the same canonical ledger semantics;
- define recovery after process termination during write/migration/import;
- keep backup and sync semantics distinct from ordinary persistence;
- specify conflict policy before claiming multi-device consistency.

## RELATED DOMAIN CHECK

### Foundations
Reuses F001's process boundary. D001 demonstrates why in-memory success and process-surviving state are separate evidence levels.

### Architecture
`A001` should treat source-of-truth and mutation authority as architectural boundaries rather than naming conventions. Repository patterns should not be adopted mechanically without product-specific ownership needs.

### Mobile
`M001/M002` must later validate Android/iOS lifecycle/process-death/storage behavior. This Linux SQLite fixture is not mobile evidence.

### Quality
`Q001/Q002` should classify process termination, failed commit, partial import, migration interruption and stale cache as explicit failure-model test cases.

### Systems
Durability has security/performance/delivery trade-offs. `synchronous`, journaling mode, filesystem behavior, storage encryption and release migrations require Systems evidence before production decisions.

### Design Studio
No canonical design claim changes. When a local write is durable but remote sync is pending/ambiguous, Interaction and Content should receive the actual state contract instead of inventing wording from storage implementation details.

### Web Manager / Marketing Manager
No canonical change in this block. Web/PWA storage and analytics durability semantics require separate runtime evidence when those projects need them.

## SYNTHESIS — Studio data-state contract

For any material persisted state, record these fields when relevant:

`data/domain → logical source of truth → physical sources/copies → mutation authority → commit acknowledgement → durability scope → consistency/freshness rule → invariants → recovery path → backup/sync relationship`.

This contract is now the preferred baseline for Data/Architecture/Quality discussions.

## OPEN / VALIDATION

1. `D002`: compare file write, SQLite rollback journal and SQLite WAL semantics with executable failure cases.
2. Validate mobile SQLite/database behavior on actual Android/iOS execution environments before product claims.
3. `D003`: intentionally interrupt schema migrations and verify recoverability.
4. `D004`: test stale cache/local-vs-remote authority policies rather than only describing them.
5. `D005`: distinguish persistence, export and backup by restore verification.
6. `D006`: add replication/idempotency/conflict experiments before any LogMate sync recommendation.

## HANDOFFS

- Data → Architecture: mutation authority and SSOT must be explicit architectural contracts.
- Data → Mobile: validate declared durability scope against mobile lifecycle/process/storage behavior.
- Data → Quality: process-kill and interruption belong in the baseline failure matrix.
- Data → Design Studio Interaction/Content: user-facing `saved`, `syncing`, `synced`, `failed`, and `unknown` states must reflect real commit/sync boundaries.

## Current judgment

`D001` establishes a reusable state/persistence/durability/authority model and includes executable process-crash evidence. It is **not a Data Foundation PASS**: mobile transfer, alternate persistence modes, migration/recovery, backup/restore and distributed-sync evidence remain future gates.
