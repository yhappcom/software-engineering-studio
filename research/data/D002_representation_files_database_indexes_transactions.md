# D002 — Representation, Files, Databases, Indexes & Transaction Fundamentals

Status: **IN STUDY — first integrated executable Foundation block complete**  
Date: 2026-09-16  
Lead: Data, Persistence & Distributed Systems

## Problem

Application data work often collapses several different mechanisms into “storage”: serialization format, file publication, database transaction, index, and durability. D001 separated state/persistence/durability/authority. D002 asks what each concrete mechanism actually contributes and which guarantees it does not provide.

## SOURCE

Primary sources checked 2026-09-16:

- IETF RFC 8259, *The JavaScript Object Notation (JSON) Data Interchange Format*: JSON is a text serialization format for structured data. It defines representation grammar/interoperability, not transaction or durability semantics.
- SQLite, *Atomic Commit In SQLite*: a transaction is intended to appear all-or-nothing; the documented rollback-mode mechanism uses a rollback journal and storage flush/commit steps. The document explicitly scopes its mechanism and notes configuration/hardware assumptions.
- SQLite, *Query Planning*: an index is an auxiliary sorted structure that can change lookup strategy from table scan to indexed search. SQL remains declarative; the planner chooses an access strategy.

## SYNTHESIS — separate the mechanisms

A useful baseline is:

`semantic data → serialization/encoding → publication/update mechanism → transaction boundary → persistence/durability mechanism → indexes/projections → query/read contract`

These roles are not interchangeable.

### Serialization
Serialization maps semantic values to a representation such as JSON bytes/text. A representation being syntactically valid says nothing by itself about atomic replacement, durability, schema compatibility, or authority.

### File publication
Writing a serialized document into a canonical file is a mutation mechanism. A destructive overwrite can expose a partially written representation if execution is interrupted. Staging a replacement separately can keep publication distinct from construction, but this model alone does not establish filesystem crash/power-loss atomicity or durability.

### Database transaction
A transaction groups mutations under an all-or-nothing semantic boundary. SQLite provides concrete atomic-commit mechanisms; application code still must choose transaction boundaries that correspond to domain invariants.

### Index
An index is an access structure, not a second semantic authority. A correct index may change the physical query plan while preserving the same query result. If an application independently mutates an index/projection as if it were canonical state, that is an ownership problem rather than an inherent property of indexing.

## EXECUTABLE VALIDATION

Fixture: `research/data/fixtures/D002_representation_transaction_index.py`

Environment:
- Python 3.13.5
- SQLite 3.46.1 (Python stdlib binding)
- Linux 6.18.44 x86_64 / glibc 2.41

### Test Evidence Contract

**CLAIM A:** serialization validity does not provide atomic publication.  
**SPEC/PROPERTY:** the canonical ledger must remain parseable as one complete JSON value after an interrupted update.  
**TARGET:** destructive whole-file JSON overwrite.  
**FAILURE MODEL:** execution stops after only half of the replacement bytes are written.  
**ORACLE:** RFC-8259-compatible JSON parser accepts/rejects the canonical file.  
**OBSERVATION:** the canonical file became invalid JSON.  
**VERDICT:** failure reproduced.

**ALTERNATIVE A:** construct replacement bytes in a separate staging file and interrupt before publication. In the bounded process-level model, the old canonical JSON remained intact. This demonstrates separation of construction from publication; it does not prove `rename`/replacement durability under OS crash or power loss.

**CLAIM B:** transaction execution and transaction commit are distinct.  
**TARGET:** SQLite rollback-journal database.  
**FAILURE MODEL:** insert B inside a transaction, raise a simulated failure before commit, then rollback.  
**ORACLE:** committed rows after recovery remain exactly baseline A.  
**OBSERVATION:** rows were `[('A', 60)]`; B was absent.  
**VERDICT:** bounded transaction rollback property reproduced.

**CLAIM C:** an index can change access strategy without changing semantic query result.  
**TARGET:** `flights(minutes)` query before/after `idx_flights_minutes`.  
**ORACLE:** result count remains equal while `EXPLAIN QUERY PLAN` changes.  
**OBSERVATION:** without the index SQLite reported `SCAN flights`; with it SQLite reported `SEARCH flights USING INDEX idx_flights_minutes (minutes=?)`; result count was equal.  
**VERDICT:** index-as-access-structure distinction reproduced.

## DEBUG / ROOT CAUSE

The JSON failure was not caused by JSON being an unsuitable representation. The failure came from coupling **construction of the replacement representation** with **destructive publication to the authoritative path**. A syntactically valid serialization format cannot supply an atomic update protocol.

The SQLite failure path did not expose B because the transaction was explicitly rolled back before commit. This is a different mechanism from parsing/serialization and must be reasoned about separately.

The query-plan difference did not imply different business meaning: the index altered access mechanics while the retained SQL predicate/result oracle remained the same.

## CONTRADICTIONS / INVALID SHORTCUTS

- `valid serialization format` ≠ `atomic update protocol`.
- `file write completed partially` ≠ `valid persisted state`.
- `database used` ≠ `correct transaction boundary`.
- `transaction committed` ≠ `all possible durability scopes satisfied` (D001).
- `index exists` ≠ `index is semantic source of truth`.
- `index changed query plan` ≠ `semantic result may change`.
- `staging + replacement` ≠ `power-loss-safe durable commit` without filesystem/platform evidence.

## TRANSFER VALIDATION — LogMate relevance

Evidence identity:

`yhappcom/logmate → main commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-16`

The inspected `pubspec.yaml` establishes Flutter/Dart context but does not establish a local-ledger storage implementation. Therefore D002 makes **no PROJECT DECISION** selecting JSON, SQLite, Isar, Drift, or another technology.

**ENGINEERING JUDGMENT:** when LogMate implements its local ledger, transaction boundaries should follow FlightRecord/domain invariants; export/backup serialization should not automatically become the authoritative mutation mechanism; search/totals indexes or projections should remain rebuildable unless the product explicitly assigns them authority.

**LIMIT:** no current LogMate persistence defect or production behavior is claimed.

## RELATED DOMAIN CHECK

- **Foundations:** F001 process boundary retained; direct Dart/Flutter execution remains OPEN.
- **Architecture:** A002 authority/state ownership explains why indexes/projections should not become accidental writers; A003 semantic compatibility will matter when serialized/schema representations evolve.
- **Mobile:** M001 warns lifecycle callbacks are not guaranteed; durable mutation design cannot rely only on a final lifecycle callback. Actual Android/iOS filesystem/database semantics remain OPEN.
- **Data:** D001 supplies durability/authority distinctions; D002 adds concrete representation/transaction/index mechanisms.
- **Quality:** Q002 requires real storage mechanisms when storage semantics are the claim; this fixture does that with stdlib SQLite rather than a fake repository.
- **Systems:** filesystem flush, power-loss, storage security and performance trade-offs remain Systems/Data joint dependencies.
- **Design Studio:** not materially needed for this mechanism block; later saved/sync/error UX must reflect real commit states.
- **Web Manager:** PWA/browser storage semantics are not transferred from this native/local model.
- **Marketing Manager:** not materially relevant.
- **Product source:** exact LogMate ref/version checked; production ref remains unknown and default branch was not equated with production.

## OPEN / VALIDATION

1. Compare rollback-journal and WAL behavior with interruption/recovery evidence.
2. Measure transaction grouping and index cost rather than assuming indexes are free performance wins.
3. Validate file replacement/fsync semantics on target Android/iOS filesystems before durable-publication claims.
4. D003: old/new reader-writer schema compatibility and interrupted migration.
5. D005: prove backup by restore, not by successful export alone.
6. No Data Foundation PASS until migration/recovery/backup and mobile-relevant evidence mature.

## HANDOFFS

- **TO Architecture:** transaction boundary should align with invariants/authority, not storage API convenience.
- **TO Quality:** storage tests must cross the real representation/transaction/index mechanism relevant to the claim.
- **TO Mobile:** validate target-platform file/database publication and process-death semantics before transferring Linux evidence.
- **TO Systems:** later measure fsync/journaling/index costs and security implications under exact artifact/platform identity.

## Current judgment

D002's first block establishes that serialization, publication, transactions, durability and indexes solve different problems. The strongest reusable rule is: **name the mechanism and guarantee separately; do not infer atomicity, durability, authority or performance from the mere choice of representation/database/index.**
