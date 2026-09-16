# D005 — Backup, Restore & Recovery Acceptance

Status: **IN STUDY — first integrated executable Foundation block complete**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem

A backup is useful only if a declared recovery procedure can turn it into state accepted by the intended application/data contract. File existence, copy completion, database physical integrity, and application recovery are distinct claims.

## SOURCE

Primary SQLite documentation checked 2026-09-17:

- SQLite Online Backup API: a completed backup operation copies database content into a destination snapshot; incremental backup can reduce source lock duration, and the API has explicit BUSY/LOCKED/IO/read-only failure behavior.
- `VACUUM INTO`: creates a consistent snapshot alternative to the backup API, but SQLite explicitly warns that interruption/power loss during generation can leave the output incomplete/corrupt; completion with appropriate synchronous settings has stronger post-completion durability semantics subject to OS/filesystem/hardware assumptions.

Primary references:
- https://www.sqlite.org/backup.html
- https://sqlite.org/c3ref/backup_finish.html
- https://www.sqlite.org/lang_vacuum.html

## SYNTHESIS — recovery is an acceptance pipeline

For a local database, distinguish:

`source state → backup mechanism → backup artifact → artifact storage/retention → restore mechanism → restored physical database → integrity validation → schema/version compatibility → domain/semantic validation → application acceptance`

A green result at an earlier stage does not automatically establish a later stage.

## EXECUTABLE VALIDATION — Block 1: backup creation is not recovery proof

Fixture: `research/data/fixtures/D005_backup_restore_acceptance.py`  
Environment: Python 3.13.5 / SQLite 3.46.1 / Linux.

### Claim / oracle

Bounded claim: a trustworthy recovery test must exercise restore and acceptance, not merely observe that a backup file exists.

Independent acceptance oracle for the fixture requires all of:
1. SQLite can open/read the restored artifact;
2. `PRAGMA integrity_check` returns `ok`;
3. declared schema contract `user_version=2` is present;
4. semantic rows equal independently specified `[(F1,60),(F2,90)]`.

### Positive restore path

The fixture created a V2 source database, used Python's SQLite backup binding to create a backup, then deliberately deleted the live rows. It restored from the backup into a separate path and evaluated the restored database with the acceptance oracle.

Observed: restored database passed physical integrity, schema contract, and semantic-row checks.

**VALIDATION:** within this SQLite/Python environment, the backup artifact could actually restore the declared bounded application state after the live copy had been semantically destroyed.

### Failure case A — existing/non-empty backup artifact can still be unusable

The fixture copied the valid backup and deliberately corrupted its SQLite header while retaining a real non-empty file.

Observed: the file existed and had non-zero size, but SQLite rejected it as `file is not a database`.

**CONTRADICTION:** `backup file exists` and `backup file has bytes` are not recovery or integrity proofs.

### Failure case B — physical integrity can pass while application compatibility fails

A second copy retained valid SQLite structure/data but changed application-managed `user_version` from 2 to 99.

Observed: `PRAGMA integrity_check` still returned `ok`, while the declared application-contract oracle rejected the artifact because the schema contract did not match.

**CONTRADICTION:** `integrity_check=ok` does not establish application/schema compatibility or semantic recoverability.

## ROOT CAUSE / MODEL

These failures arise because different validators answer different questions:

- filesystem existence/size: is there an artifact at this path?
- SQLite structural/integrity validation: is the database structurally consistent under SQLite's checks?
- schema/version contract: can the intended reader interpret this representation under its declared compatibility policy?
- semantic/domain oracle: does the restored state preserve required business meaning/invariants?
- application acceptance: can the intended application actually resume from the restored state?

Conflating these layers creates false confidence even when every individual check is behaving correctly.

## ALTERNATIVES / TRADE-OFFS

SQLite exposes multiple consistent-copy mechanisms. Online Backup API supports incremental copying and explicit operational error handling; `VACUUM INTO` produces a compact consistent snapshot but has different CPU/I/O and interruption properties. Mechanism choice is a PROJECT DECISION based on dataset size, concurrency, storage budget, platform APIs and recovery requirements. D005 does not choose a LogMate/MintTap implementation.

A plain filesystem copy of a live database is not assumed safe here. WAL/journal side files, locks, open transactions and platform/filesystem behavior can make that a materially different protocol.

## ENGINEERING JUDGMENT — minimum backup acceptance contract

For user-owned durable data, a backup feature should define at minimum:

`what is backed up → consistency point → artifact identity/version → completion criterion → retention/location → restore procedure → destructive-restore safeguards → integrity checks → schema compatibility → semantic invariants → success/failure UX → rollback/retry path`.

Periodic restore drills or automated restore tests are stronger evidence than backup-job success counters alone.

## INVALID SHORTCUTS

- `backup command returned success` ≠ recovery proven.
- `backup file exists` ≠ artifact is valid.
- `non-zero file size` ≠ artifact is valid.
- `integrity_check=ok` ≠ intended application can read the schema.
- `schema is readable` ≠ domain semantics are correct.
- `restore completed` ≠ application acceptance passed.
- one Linux/Python/SQLite restore ≠ Android/iOS/filesystem/cloud-backup behavior.

## TRANSFER VALIDATION — LogMate relevance

Product evidence rechecked 2026-09-17:

`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 (retained prior exact-ref evidence) → evidence date 2026-09-17`.

The repository head remained `b551ce434ad72b1895033e0f3617c73b026d40ea`. Prior exact-ref inspection recorded Backup/Export and durable ledger/configuration as not implemented. Therefore this study is a **TRANSFER CANDIDATE**, not a product defect finding and not an implementation decision.

Reusable requirement candidate for future LogMate work: a user-facing backup feature should not be accepted from file creation alone; validation should restore into an isolated target and verify schema plus FlightRecord/domain invariants before claiming recoverability.

MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## RELATED DOMAIN CHECK

- **Foundations:** F001 process/runtime distinction retained. Direct Dart/Flutter execution rechecked 2026-09-17; neither executable is available, so the gap remains OPEN.
- **Architecture:** A003 compatibility model applies to restored artifact ↔ reader contract.
- **Mobile:** actual Android/iOS sandbox, file-provider, process-death and user-file restore behavior remains a DEPENDENCY for product acceptance.
- **Data:** D001 authority/durability, D002 transaction/journal, and D003 schema compatibility are direct prerequisites.
- **Quality:** Q001 independent oracle and Q002 evidence-boundary rules shape restore acceptance; the test must cross the actual storage/restore mechanism when making recovery claims.
- **Systems:** artifact integrity/authenticity/authorization/provenance are separate from recoverability. Backup confidentiality/key management and release-artifact compatibility remain future S002/S005 dependencies.
- **Design Studio:** search found no materially applicable backup/restore canonical evidence in the checked repository; future recovery UX must reflect actual states rather than optimistic copy completion.
- **Web Manager:** no materially applicable backup/restore evidence found for this local SQLite block.
- **Marketing Manager:** no materially applicable backup/restore evidence found; no marketing metric changes the recovery oracle.
- **Product:** LogMate exact head rechecked; no product repository edited.

## OPEN / VALIDATION

1. Corruption detection beyond header damage: page-level corruption, truncation, missing companion state where applicable.
2. Restore interruption and atomic publication: avoid replacing the only good live copy with an unvalidated restore.
3. Version matrix: older/newer application artifacts against backup schema versions.
4. Backup authenticity/confidentiality/key-loss semantics for sensitive data.
5. Android/iOS Files/document-provider/cloud-location behavior and storage-full/permission-revocation failures.
6. Retention/version rotation and user-error recovery semantics.
7. No Data Foundation PASS yet.

## HANDOFFS

- **TO Quality:** define recovery acceptance tests as restore-through-real-mechanism + independent physical/schema/domain oracles; backup-job success alone is insufficient.
- **TO Architecture:** backup schema/version is an externalized compatibility contract; readers must declare accepted versions.
- **TO Mobile:** reproduce restore interruption, permission/storage-full and file-provider behavior on exact Android/iOS stack.
- **TO Systems:** add confidentiality/authenticity/key lifecycle and artifact identity without confusing those claims with recoverability.
- **TO LogMate:** before implementing Backup/Export, define a recoverability acceptance contract and isolated restore validation. No product files edited.

## Current judgment

D005's first block establishes an important boundary with executable evidence: **backup creation, physical integrity, schema compatibility, semantic validity and application recovery are separate claims**. The next high-value D005 block is restore publication/interruption safety: prove that a failed or incompatible restore cannot destroy the last known-good local state before moving toward mobile-specific backup behavior.
