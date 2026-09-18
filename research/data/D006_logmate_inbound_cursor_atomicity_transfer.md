# D006 — LogMate inbound cursor/apply atomicity transfer

Date: 2026-09-18  
Lead: Data  
Status: **TRANSFER VALIDATION — bounded executable failure evidence; product implementation remains OPEN**

## Problem

LogMate's current data contract already states that a local entity mutation and its outbound `Operation` enqueue belong in one transaction. The same exact-ref contract defines `SyncState.lastAppliedCursor`, `Receipt`, `RevisionHistory`, tombstones and restore operations, but does not yet freeze the inbound server-change publication transaction. This matters because advancing a pull cursor is itself durable protocol state: if it becomes visible before the corresponding entity/revision/tombstone state, a crash can make an unapplied server change unreachable on the next cursor-based pull.

## Product evidence

`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-18`.

Production identity is unknown; default branch is **not** treated as production.

At this ref:
- `MASTER.md` confirms one canonical ledger, offline use, structured backup/recovery direction and owner-based multi-device Sync, while implementation status remains incomplete.
- `docs/specs/data-schema-spec.md` defines `Operation`, `Receipt`, immutable `RevisionHistory`, and `SyncState.lastAppliedCursor`; local entity update + outbound Operation enqueue are explicitly one transaction.
- deletion is a tombstone operation; restore is a new operation on the same entity ID.
- the same spec explicitly says canonical repository/persistence/Sync are not implemented and DATA-001 remains OPEN.

Therefore this note does **not** report a LogMate bug. It identifies and executable-tests a protocol invariant that should be decided before implementation.

## SOURCE

SQLite transaction documentation states that explicit transactions persist until COMMIT/ROLLBACK and that an uncommitted transaction rolls back when the database is closed. SQLite's atomic-commit documentation defines a transaction as all-or-none publication of its database changes. These are storage mechanisms, not a definition of LogMate's synchronization semantics.

## SYNTHESIS

For a cursor-based inbound replication protocol, the durable cursor is an acknowledgement by the client to itself: "all effects through this position are safely represented locally." Therefore cursor advancement must not become durable before every local state transition required by that cursor position is durably accepted, unless the protocol has another independent replay/reconciliation mechanism that proves equivalent recovery.

Candidate invariant:

`durable lastAppliedCursor = C  =>  every required accepted effect <= C is durably represented or independently recoverable`

This includes, depending on final DATA-001 design, entity state, tombstone/restore state, revision/history metadata, and any receipt/reconciliation state whose absence would change later behavior.

## Executable validation

Fixture: `research/data/fixtures/D006_inbound_cursor_atomicity.py`

Environment actually executed before persistence: Python 3.13.5 / Linux / stdlib SQLite.

### CLAIM
A split inbound publication that durably advances the cursor before applying the corresponding entity change can lose reachability of that change after process death; placing entity apply and cursor advancement in one local transaction prevents that specific split state.

### SPEC/PROPERTY
Bounded model: server change `(cursor=1, entity=f1, value=120, revision=2)` is returned only when the client's durable cursor is `<1`.

### PRESTATE
Entity `f1=(value=100, revision=1)`, cursor `0`.

### FAILURE CASE A — unsafe split publication
1. write cursor `1`;
2. COMMIT cursor;
3. terminate child with `os._exit(77)` before entity apply;
4. reopen in a fresh process context;
5. ask bounded server model for changes after durable cursor.

Observed: entity remained `(100,1)`, cursor was `1`, `integrity_check=ok`, and the server model returned no remaining change. Storage integrity therefore did not imply synchronization correctness.

### ALTERNATIVE B — one local transaction
1. `BEGIN IMMEDIATE`;
2. update entity to `(120,2)`;
3. update cursor to `1`;
4. terminate child with `os._exit(78)` before COMMIT;
5. reopen.

Observed: SQLite rolled back both writes: entity `(100,1)`, cursor `0`, `integrity_check=ok`; the server model still exposed change `1` for replay.

Fixture verdict: `D006 inbound cursor/apply crash boundary: PASS`.

## DEBUG / ROOT CAUSE

The unsafe failure is not database corruption. Each individual committed state is structurally valid. The defect is a **protocol publication-order violation**: cursor durability asserted progress beyond the durable semantic state. A database integrity check cannot detect this class because both tables are individually valid.

The safe comparison works in this bounded case because one transaction couples semantic apply and progress publication. It does not by itself solve duplicate delivery, concurrent writers, conflict resolution, server-side atomicity, external side effects, or multi-entity batches.

## ENGINEERING JUDGMENT

Before DATA-001 freezes Sync persistence, LogMate should define the atomic acceptance unit for inbound changes. The default candidate should be: apply the server change's required local semantic effects and advance `lastAppliedCursor` in one durable local transaction. If batching is used, the cursor may advance only to the greatest prefix whose required effects are all accepted in that same durable publication boundary.

`Receipt` handling requires a separate explicit decision: if a receipt changes local operation status, revision, or conflict behavior, its publication relationship with those state changes must be specified rather than assumed from the existence of `operationId`.

## OPEN / VALIDATION

- Actual LogMate local persistence technology/schema is not implemented at the audited ref.
- Exact server cursor semantics, batch semantics, ordering, transaction boundaries and version negotiation are OPEN.
- Receipt/application atomicity is OPEN.
- Multi-entity change sets, concurrent local edits, tombstone/restore races and dedup retention remain OPEN.
- No Dart/Flutter/Firebase execution occurred.
- No production/backend evidence exists.

## RELATED DOMAIN CHECK

- **Foundations:** F006 apply/commit/ACK distinctions directly support treating cursor advancement as a separate durable protocol event.
- **Architecture:** state ownership and externally relevant publication boundaries apply; protocol progress is not mere implementation detail.
- **Mobile:** process death can occur between asynchronous persistence steps; exact Android/iOS/Flutter transfer remains required.
- **Data:** D003 split-publication migration evidence and D006 retry evidence are directly reusable mechanisms.
- **Quality:** recovery oracle must inspect semantic state plus cursor/progress state; `integrity_check=ok` is insufficient.
- **Systems:** artifact/runtime identity and storage durability assumptions remain separate from protocol atomicity.
- **Design Studio:** not materially decision-changing for this storage/protocol invariant; future recovery/conflict UI must not hide unresolved state.
- **Web Manager:** not materially relevant to this product-local Sync invariant.
- **Marketing Manager:** not materially relevant.
- **Product:** exact LogMate ref audited as recorded above.

## HANDOFFS

### TO LogMate product team — OPEN
Before implementing Sync persistence, freeze and test the inbound acceptance transaction: entity/tombstone/revision effects and cursor advancement must have an explicit crash-recovery contract. Add crash points before apply, between semantic writes, before cursor update, and after commit; verify fresh-process replay and terminal semantic state.

### TO Quality
Use a cross-table/protocol oracle: `cursor C` is valid only when the required local effects through C are present or independently replayable. Database structural integrity alone is not the oracle.

### TO Mobile
Transfer-test the same crash schedule on the exact Flutter/local-database stack once available; do not infer Android/iOS behavior from Python/SQLite.

## Evidence limit

This is **TRANSFER VALIDATION of a protocol invariant against an exact product specification plus a bounded comparison fixture**, not product implementation validation and not production evidence. It must not be reported as a current LogMate defect or PASS.
