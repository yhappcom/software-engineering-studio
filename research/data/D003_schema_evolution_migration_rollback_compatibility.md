# D003 — Schema Evolution, Migration, Rollback & Compatibility

Status: **IN STUDY — two integrated executable Foundation blocks complete**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem

A schema migration is not merely a new table shape. It is an evolution protocol across persisted representation, application readers/writers, migration metadata, transaction boundaries, validation constraints, and rollback/recovery expectations.

## SOURCE

Primary SQLite documentation checked 2026-09-17:

- `ALTER TABLE` documents arbitrary table redesign as a transaction-wrapped create/copy/drop/rename procedure and explicitly includes `foreign_key_check`/integrity validation before commit.
- `PRAGMA user_version` is application-controlled metadata; SQLite assigns it no schema meaning.
- transaction documentation distinguishes statement failure from transaction rollback: under the default ABORT conflict behavior a violating statement is backed out while earlier statements in the transaction can remain and the transaction stays active.
- foreign-key enforcement is connection configuration and should be set explicitly rather than assuming a default; `PRAGMA foreign_key_check` reports persisted violations.

## SYNTHESIS — migration is a protocol, not a shape

`old persisted contract → compatibility window → schema/data transform → invariant/FK validation → migration metadata → publication/commit → new persisted contract → old-contract retirement`

Compatibility is relational across at least:

`reader version × writer version × stored schema/data version × migration state`.

## EXECUTABLE VALIDATION — Block 1: compatibility/publication

Fixture: `research/data/fixtures/D003_schema_migration_compatibility.py`  
Environment: Python 3.13.5 / SQLite 3.46.1 / Linux.

- V2 expand + backfill + fallback-read + dual-write preserved the bounded old/new reader-writer contracts.
- Deliberately splitting physical schema mutation from `user_version` publication produced V2-shaped schema with `user_version=1`.
- Putting schema change, backfill and version update in one explicit transaction and injecting failure before COMMIT restored the V1 schema/data/version contract.
- V3 destructive retirement of `minutes` preserved migrated data for the new reader but caused the old reader to fail.

**CONTRADICTION:** migration success does not imply rollback-release/old-consumer compatibility.

## EXECUTABLE VALIDATION — Block 2: transform/constraint/FK failure

Fixture: `research/data/fixtures/D003_constraint_fk_migration_failure.py`  
Environment: Python 3.13.5 / SQLite 3.46.1 / Linux.

### 2A — catching a transform error and continuing can falsely publish a new version

The proposed V2 table strengthened the persisted invariant to `seconds >= 0`. Legacy input deliberately contained a row that mapped to negative seconds. `INSERT ... SELECT` into the V2 table failed with `CHECK constraint failed: seconds>=0`.

A deliberately weak migration caught that statement error, continued, set `user_version=2`, and COMMITted. Reopen/current observations were:

- `user_version=2`;
- both `flights` and empty `flights_v2` existed;
- the old table contained two rows, including the incompatible legacy row;
- the V2 copy contained zero rows.

**FAILURE CASE:** a statement-level constraint failure did not automatically make the application migration protocol fail. The application swallowed the error and published V2 metadata anyway.

**ROOT CAUSE:** SQLite's default ABORT behavior backs out the failing statement but does not necessarily roll back prior statements or end the explicit transaction. Migration success therefore requires an application-level success predicate and explicit error handling; `COMMIT succeeded` is not sufficient if required transform/validation steps failed earlier.

### 2B — fail-closed transaction alternative

The comparison protocol treated the same transform error as migration failure and explicitly rolled back the transaction. Observation:

- `user_version=1`;
- only original `flights` and `pilots` tables remained;
- the deliberately inserted incompatible row was also rolled back;
- original F1 remained.

**VALIDATION:** for this SQLite fixture and failure point, fail-closed handling plus transaction rollback preserved the complete V1 contract.

### 2C — foreign-key enforcement and validation are separate operational obligations

A separate case explicitly disabled FK enforcement, inserted an orphan `pilot_id='MISSING'`, committed it, then re-enabled enforcement. `PRAGMA foreign_key_check` returned the persisted violation.

**CONTRADICTION:** `foreign_keys=ON now` does not prove that already persisted data satisfies the FK invariant. Validation of migrated data is a separate step.

**ENGINEERING JUDGMENT:** when a migration procedure temporarily relaxes enforcement, acceptance should include explicit invariant/FK checks before publication. Do not treat configuration restoration as data validation.

## Compatibility matrix from bounded evidence

| Stored contract/state | Old reader | Old writer | New reader | New writer |
| --- | --- | --- | --- | --- |
| V1 minutes-only | PASS | PASS | migration-aware handling required | not claimed |
| V2 expanded/backfilled | PASS | PASS | PASS via fallback | PASS via dual-write |
| Weak failed-transform state labeled V2 | old table remains but publication is internally inconsistent | unsafe to infer | V2 copy incomplete | unsafe to infer |
| V3 seconds-only | FAIL | incompatible with removed representation | PASS | PASS |

Cells are operation-specific, not universal guarantees.

## ENGINEERING JUDGMENT

Treat migration as a release protocol with explicit compatibility, validation, publication and recovery states. `expand → backfill → compatible read/write → validate → contract` is useful when coexistence is required, but deployment/release constraints determine the needed compatibility window.

For migrations that strengthen invariants, legacy data is an input to the migration algorithm, not an assumption. A transform must define what happens to nonconforming historical rows: reject/rollback, repair with an independently justified rule, quarantine for review, or another explicit domain policy. Silent dropping or metadata publication after failure is not a valid default.

## INVALID SHORTCUTS

- `schema changed successfully` ≠ `migration protocol succeeded`.
- `user_version=N` ≠ `SQLite verified schema N`.
- `COMMIT succeeded` ≠ every required migration step succeeded if the application swallowed an earlier statement error.
- `foreign_keys=ON` ≠ existing data has no FK violations.
- `new reader works` ≠ `old reader still works`.
- `additive schema change` ≠ universal reader/writer compatibility.
- `backup exists` ≠ rollback is safe; restore compatibility still requires validation.

## TRANSFER VALIDATION — LogMate relevance

Retained evidence identity:

`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`.

At that exact ref, inspected product evidence described durable local ledger/configuration persistence/Sync/Backup-Export as not implemented. D003 remains a **TRANSFER CANDIDATE**, not an existing-product defect finding.

Reusable constraint: before LogMate introduces durable FlightRecord/configuration migrations, define migration success predicates, handling for historical rows that violate new invariants, compatibility window, version publication, validation, and recovery oracle.

MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## RELATED DOMAIN CHECK

- **Foundations:** F001 process boundary relevant; direct Dart/Flutter execution rechecked 2026-09-17 and remains OPEN because neither executable is available.
- **Architecture:** A003 semantic compatibility/invariant model supplies retained consumer properties.
- **Mobile:** Android/iOS startup/process-death/upgrade/downgrade migration remains a platform validation dependency.
- **Data:** D001 authority/durability and D002 transaction/journal distinctions are prerequisites.
- **Quality:** migration oracle must include required-step completion plus post-migration invariant/FK checks; injected errors must not be mistaken for automatic transaction rollback.
- **Systems:** release rollback determines whether old artifacts may encounter new state.
- **Design Studio:** future repair/quarantine/recovery UI must reflect real recoverability; no design semantics changed.
- **Web Manager / Marketing Manager:** not materially relevant to this local SQLite mechanism block.
- **Product:** retained LogMate exact-ref evidence used; no product repository edited.

## OPEN / VALIDATION

1. Add actual rollback-release evidence where an old binary meets newer persisted state, beyond the current old-reader fixture.
2. Add backup-before-migration + restore validation; successful backup creation alone is insufficient.
3. Validate migration interruption on actual Android/iOS persistence stack.
4. Later mixed-version sync/replication work must cover schema evolution across peers.
5. No Data Foundation PASS yet.

## HANDOFFS

- **TO Architecture:** strengthened persisted invariants are compatibility changes; historical-state handling is part of the contract.
- **TO Quality:** migration PASS oracle must include every required transform/validation step; add regression tests proving caught statement errors cannot publish the new version.
- **TO Mobile:** reproduce migration failure/restart behavior on exact Android/iOS stack before acceptance.
- **TO Systems:** release rollback policy must bind artifact identity to schema compatibility and migration success evidence.
- **TO LogMate:** define nonconforming-history policy and fail-closed migration publication before durable ledger/configuration implementation. No product files edited.

## Current judgment

D003 now establishes two independent failure classes: cross-version compatibility/publication failure and transform/invariant-validation failure. Transactions can bound atomic publication, but only when the application treats required-step failure as migration failure. Constraint enforcement configuration and persisted-data validation are distinct. Backup/restore and real mobile migration evidence remain prerequisites before stronger operational claims.
