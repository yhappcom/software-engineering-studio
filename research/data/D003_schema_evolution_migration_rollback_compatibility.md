# D003 — Schema Evolution, Migration, Rollback & Compatibility

Status: **IN STUDY — first integrated executable Foundation block complete**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem

A schema migration is not merely a new table shape. It is an evolution protocol across persisted representation, application readers/writers, migration metadata, transaction boundaries, and rollback/recovery expectations. D003 asks which combinations remain compatible and what happens when migration publication is interrupted.

## SOURCE

Primary SQLite documentation checked 2026-09-17:

- SQLite `ALTER TABLE` documents supported schema changes and, for arbitrary table redesign, a transaction-wrapped create/copy/drop/rename procedure with integrity/foreign-key checks before commit.
- SQLite `PRAGMA user_version` exposes an application-controlled integer in the database header; SQLite itself assigns no semantics to it.
- SQLite atomic-commit documentation defines transaction atomicity as all changes in a transaction occurring or none occurring, subject to the documented mechanism/failure assumptions.

## SYNTHESIS — migration is a protocol, not a shape

Useful model:

`old persisted contract → compatibility window → schema/data transform → migration metadata → publication/commit → new persisted contract → old-contract retirement`

Compatibility is relational across at least:

`reader version × writer version × stored schema/data version × migration state`.

A schema can be structurally valid and still be operationally incompatible with a retained reader/writer. Likewise, application migration metadata can be stale even when the physical schema change succeeded if those publications are split.

## EXECUTABLE VALIDATION

Fixture: `research/data/fixtures/D003_schema_migration_compatibility.py`

Environment:
- Python 3.13.5
- SQLite 3.46.1
- Linux

### Block 1A — expand compatibility window

V1 stores `flights(id, minutes)`. V2 adds nullable `duration_seconds`, backfills it, lets the new reader fall back to `minutes*60`, and lets the new writer dual-write both representations.

After migration:
- old writer inserted `B=90 minutes`;
- new writer inserted `C=7200 seconds` while also retaining `minutes=120`;
- old reader observed A=60, B=90, C=120;
- new reader observed A=3600, B=5400, C=7200;
- `user_version=2`.

**VALIDATION:** the bounded expand/dual-read/dual-write protocol preserved both retained reader contracts for these operations.

**EVIDENCE LIMIT:** this does not prove every expand/contract migration safe. Concurrent processes, large datasets, triggers/FKs, app downgrade, replication, mobile packaging and production rollout are outside this fixture.

### Block 1B — split publication failure

A deliberately weak migration committed `ALTER TABLE ... ADD COLUMN duration_seconds` and then simulated interruption before updating `PRAGMA user_version`.

Reopen observation:
- physical columns: `id`, `minutes`, `duration_seconds`;
- application migration metadata: `user_version=1`.

**FAILURE CASE:** schema shape and application version metadata disagreed because they were published in separate commit boundaries.

**ROOT CAUSE:** `user_version` is application-managed metadata, not an automatically synchronized description of schema shape. Splitting schema mutation and metadata update allows an intermediate state that either side alone cannot rule out.

### Block 1C — transactional migration rollback alternative

Schema addition, backfill and `user_version=2` were placed in one explicit transaction. A deliberate exception was injected before COMMIT and the transaction rolled back.

Reopen/current-connection observation after rollback:
- columns returned to `id`, `minutes`;
- `user_version=1`;
- baseline A=60 remained readable by the old contract.

**VALIDATION:** for this SQLite operation set and failure point, the explicit transaction preserved the old schema/data/version contract rather than exposing the partially migrated state.

### Block 1D — contract phase / destructive retirement

A V3 rebuild retained only `duration_seconds` and removed `minutes`. Migrated data remained valid for the V3 reader, but the old reader failed with `no such column: minutes`.

**CONTRADICTION:** `migration succeeded` does not imply `old application remains compatible`.

The compatibility break was caused by retiring a representation still required by the old consumer contract, not by corrupt data.

## Compatibility matrix from the bounded fixture

| Stored contract | Old reader | Old writer | New reader | New writer |
| --- | --- | --- | --- | --- |
| V1 minutes-only | PASS | PASS | not claimed without migration-aware handling | not claimed |
| V2 expanded + backfilled | PASS | PASS | PASS via fallback | PASS via dual-write |
| V3 seconds-only | FAIL | FAIL/not applicable to removed column contract | PASS | PASS |

This matrix is intentionally operation-specific. A PASS cell is not a universal guarantee for arbitrary queries, constraints or writes.

## ENGINEERING JUDGMENT

For local persistent applications, prefer treating migration as a release protocol with explicit compatibility and recovery states rather than a startup SQL script. Before destructive retirement, identify whether older binaries, rollback releases, backups, imports, sync peers, extensions, or background processes can still emit/read the old contract.

`expand → backfill → compatible read/write window → validate → contract` is a useful pattern when coexistence is required, but it is not mandatory when the deployment model proves single-version exclusivity and rollback is unnecessary. The deployment/release model determines how much compatibility window is needed.

## INVALID SHORTCUTS

- `schema changed successfully` ≠ `migration protocol succeeded`.
- `user_version=N` ≠ `SQLite verified schema N`.
- `new reader works` ≠ `old reader still works`.
- `additive schema change` ≠ universal reader/writer compatibility.
- `transactional migration rollback worked here` ≠ every engine/DDL/failure domain has identical transactional DDL semantics.
- `backup exists` ≠ rollback is safe; restore compatibility still requires validation.

## TRANSFER VALIDATION — LogMate relevance

Evidence identity rechecked 2026-09-17:

`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`.

Current exact ref describes configuration persistence, local ledger, Sync and Backup/Export as not implemented in the inspected product evidence. Therefore D003 is a **TRANSFER CANDIDATE**, not an audit finding about an existing LogMate migration.

Reusable constraint: when LogMate introduces a durable FlightRecord/configuration schema, migration acceptance should name retained app/backup/import/sync compatibility and interruption recovery before destructive field retirement.

MintTap repository identity was not resolved from the accessible GitHub repository search in this run, so no MintTap implementation claim is made.

## RELATED DOMAIN CHECK

- **Foundations:** F001 process boundary remains relevant; direct Dart/Flutter execution is still OPEN because no `dart`/`flutter` executable was available in the current environment.
- **Architecture:** A003 semantic compatibility model directly supplies retained consumer contracts; schema shape alone is insufficient.
- **Mobile:** startup migration, process death, app upgrade/downgrade and platform storage behavior remain platform validation dependencies.
- **Data:** D001 authority/durability and D002 transaction/journal distinctions are prerequisites.
- **Quality:** migration tests need old/new reader-writer oracles plus injected interruption and recovery verification.
- **Systems:** release rollback and artifact identity determine whether an older binary can encounter a newer schema.
- **Design Studio:** no design semantics changed; future migration/recovery UI must reflect real recoverability states.
- **Web Manager:** not materially relevant to this local SQLite fixture.
- **Marketing Manager:** not materially relevant.
- **Product:** LogMate exact ref checked; MintTap repo unresolved, therefore no product inference.

## OPEN / VALIDATION

1. Add downgrade/rollback-release evidence where old binary meets newer persisted state.
2. Add failed data-transform/constraint and foreign-key migration cases.
3. Add backup-before-migration + restore validation; successful backup creation alone is insufficient.
4. Validate migration interruption on the actual Android/iOS persistence stack before mobile claims.
5. Later distributed/offline work must include mixed-version peers and replication during schema evolution.
6. No Data Foundation PASS yet.

## HANDOFFS

- **TO Architecture:** A003 compatibility contracts transfer directly to persisted schemas; retain reader/writer behavior, not merely shape.
- **TO Quality:** build migration matrices around reader/writer/schema/migration-state combinations and inject failures before/after publication boundaries.
- **TO Mobile:** reproduce upgrade/startup/process-death migration behavior on exact Android/iOS stack before product acceptance.
- **TO Systems:** release rollback policy must declare whether old artifacts may open new schemas; artifact version and schema version are separate identities.
- **TO LogMate:** before durable ledger/configuration implementation, define migration/version metadata, compatibility window, destructive-retirement criteria and recovery oracle in the product repository. No product files edited.

## Current judgment

The first D003 block establishes that **schema evolution is a compatibility-and-publication protocol, not merely a DDL transformation**. Transactional migration can remove some partial-publication states, while expand/contract can preserve mixed reader/writer compatibility when the deployment model requires it. Neither mechanism proves rollback or cross-version safety without an explicit compatibility matrix and failure validation.
