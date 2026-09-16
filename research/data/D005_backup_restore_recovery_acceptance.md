# D005 — Backup, Restore & Recovery Acceptance

Status: **IN STUDY — two integrated executable Foundation blocks complete**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem
A backup is useful only if a declared recovery procedure can turn it into state accepted by the intended application/data contract without destroying the last known-good state on a failed restore. File existence, copy completion, physical integrity, application acceptance, and safe publication are distinct claims.

## SOURCE
Primary documentation checked 2026-09-17:
- SQLite Online Backup API: https://www.sqlite.org/backup.html and https://sqlite.org/c3ref/backup_finish.html
- SQLite `VACUUM INTO`: https://www.sqlite.org/lang_vacuum.html
- SQLite WAL: https://www.sqlite.org/wal.html — a WAL file can be part of persistent database state; separating a database from required WAL state can lose committed transactions or corrupt the database.
- Python 3.13 `os.replace`: https://docs.python.org/3.13/library/os.html#os.replace — successful replacement is atomic under POSIX, but can fail across filesystems.

## SYNTHESIS — recovery is an acceptance and publication pipeline
`source state → backup mechanism → backup artifact → storage/retention → isolated restore candidate → physical integrity → schema/version compatibility → domain/semantic validation → publication decision → live-state replacement → application acceptance`

A PASS at an earlier stage does not establish a later stage. Candidate validation should occur before destructive publication when preserving the last known-good state is a requirement.

## EXECUTABLE VALIDATION — Block 1: backup creation is not recovery proof
Fixture: `research/data/fixtures/D005_backup_restore_acceptance.py`  
Environment: Python 3.13.5 / SQLite 3.46.1 / Linux.

Independent acceptance oracle requires SQLite readability, `PRAGMA integrity_check=ok`, `user_version=2`, and exact independently specified rows `[(F1,60),(F2,90)]`.

Observed:
- actual SQLite backup restored the expected state after live semantic rows were deliberately destroyed;
- a non-empty artifact with a corrupted SQLite header existed but was rejected as `file is not a database`;
- a structurally valid database with `integrity_check=ok` but `user_version=99` failed the application/schema contract.

**CONTRADICTION:** backup-file existence, physical integrity, schema compatibility, semantic validity and application recovery are different claims.

## EXECUTABLE VALIDATION — Block 2: validate-before-publish preserves last known-good state at bounded failure points
Fixture: `research/data/fixtures/D005_restore_publication_safety.py`  
Environment: Python 3.13.5 / SQLite 3.46.1 / Linux/POSIX model.

### Claim / oracle
Bounded claim: if a restore candidate is validated in isolation before publication, an invalid candidate or a failure before publication need not destroy the last known-good live database. This is not a power-loss or mobile-filesystem claim.

The same independent oracle requires physical integrity, `user_version=2`, and exact expected semantic rows.

### Failure case — destructive publish before validation
An incompatible but structurally valid database (`integrity_check=ok`, `user_version=99`, wrong semantic row) was copied over the live path before validation.

Observed: subsequent acceptance failed and the prior known-good live state had already been replaced.

**CONTRADICTION:** `restore copy completed` does not mean the restore was safe; validation after destructive replacement can be too late to preserve the previous accepted state.

### Alternative — isolated candidate validation
The known-good live database was reset. The same incompatible artifact was restored to a separate candidate path and evaluated before publication.

Observed: candidate acceptance failed while the live database still passed the complete oracle.

### Injected failure after candidate acceptance but before publication
A valid candidate passed the oracle, then the fixture deliberately raised an exception before `os.replace`.

Observed: live state still passed the complete oracle.

### Successful bounded publication
A valid candidate was published with same-filesystem `os.replace`; live state then passed the complete oracle. Python documents successful POSIX replacement as atomic, while explicitly warning that cross-filesystem replacement may fail.

**VALIDATION:** within this bounded Linux/POSIX execution, validate-before-publish separates candidate acceptance from live-state replacement and preserves known-good state for invalid-candidate and pre-publication-failure cases.

## ROOT CAUSE / MODEL
Restore has at least two independently fallible phases: candidate construction/validation and publication. Publishing first collapses them and can destroy rollback material before compatibility/semantic checks run. Separating them provides a fail-closed boundary for failures that occur before publication.

This does not prove crash/power-loss durability of the rename itself. Directory-entry persistence, fsync ordering, filesystem guarantees, open handles, SQLite journal/WAL companion state, Android/iOS file-provider semantics, and cross-filesystem moves remain outside this fixture.

SQLite WAL is a specific caution: SQLite documents the `-wal` file as part of persistent database state when present; moving/copying only the main DB while required WAL state exists is not assumed safe. The fixture uses closed standalone database artifacts and therefore does not validate live WAL replacement.

## ALTERNATIVES / TRADE-OFFS
- validate isolated candidate then publish: preserves live state for invalid candidates and failures before publication, at cost of temporary storage and publication protocol complexity;
- destructive overwrite then validate: simpler but can destroy the last accepted state before discovering incompatibility;
- Online Backup API / `VACUUM INTO`: consistent-copy mechanisms with different locking, I/O and interruption properties; mechanism choice remains a PROJECT DECISION;
- same-filesystem atomic rename/replace can narrow publication visibility failures under applicable filesystem guarantees, but atomic namespace replacement is not identical to power-loss durability.

## ENGINEERING JUDGMENT — minimum recovery acceptance contract
For user-owned durable data, define:
`what is backed up → consistency point → artifact identity/version → completion criterion → retention/location → isolated restore procedure → physical/schema/domain validation → publication protocol → destructive-restore safeguard → success/failure UX → rollback/retry path`.

## INVALID SHORTCUTS
- `backup command returned success` ≠ recovery proven.
- `backup file exists/non-zero` ≠ artifact valid.
- `integrity_check=ok` ≠ intended reader accepts the schema.
- `restore copy completed` ≠ safe publication.
- `atomic rename` ≠ power-loss durability.
- `main SQLite file copied` ≠ complete WAL-mode persistent state.
- one Linux/Python/SQLite result ≠ Android/iOS/filesystem/cloud behavior.

## TRANSFER VALIDATION — LogMate relevance
Retained exact-ref context rechecked in the preceding D005 block: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. Prior exact-ref inspection recorded Backup/Export and durable ledger/configuration as not implemented. Therefore D005 remains a **TRANSFER CANDIDATE**, not a product defect finding or SQLite implementation decision.

Reusable requirement candidate: future LogMate recovery should validate a candidate independently before destructive live publication when feasible, and acceptance must include schema plus FlightRecord/domain invariants. Platform-specific implementation requires Mobile validation.

MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## RELATED DOMAIN CHECK
- **Foundations:** F001 process/runtime distinction retained. Direct Dart/Flutter execution rechecked 2026-09-17; neither executable is available, so OPEN remains.
- **Architecture:** A003 compatibility applies to backup schema/version ↔ intended reader and to rollback expectations.
- **Mobile:** Android/iOS sandbox, document-provider, cross-volume, open-handle, process-death and storage-full behavior remain dependencies.
- **Data:** D001 authority/durability, D002 transaction/journal/WAL, D003 schema compatibility directly constrain restore safety.
- **Quality:** Q001 independent oracle and Q002 evidence-boundary rules used; failure was deliberately injected before publication.
- **Systems:** atomic namespace replacement, durability, backup authenticity/confidentiality/key lifecycle are distinct. No cryptographic claim here.
- **Design Studio:** recovery UX must not present candidate-copy completion as recovery success; no external canonical file edited.
- **Web Manager:** not materially relevant to this local SQLite publication fixture.
- **Marketing Manager:** not materially relevant to the recovery oracle.
- **Product:** retained LogMate exact-ref context only; no product repository edited.

## OPEN / VALIDATION
1. Failure during/after publication, including process crash and actual power loss.
2. Filesystem durability/fsync and cross-filesystem publication semantics.
3. WAL/open-database restore protocol; do not replace only the main DB while companion state is active.
4. Corruption breadth: page corruption/truncation and storage-full failures.
5. Version matrix: older/newer application artifacts against backup schema versions.
6. Backup authenticity/confidentiality/key-loss semantics.
7. Android/iOS Files/document-provider/cloud-location behavior and permission revocation.
8. Retention/version rotation and user-error recovery semantics.
9. No Data Foundation PASS yet.

## HANDOFFS
- **TO Quality:** recovery tests need explicit candidate-validation and publication failure points, not only restore completion.
- **TO Architecture:** define rollback/reader compatibility before allowing destructive publication of a restored schema.
- **TO Mobile:** reproduce publication interruption, cross-volume/document-provider, storage-full and process-death behavior on exact Android/iOS stack.
- **TO Systems:** distinguish atomic namespace replacement from durable publication; add authenticity/confidentiality/key lifecycle separately.
- **TO LogMate:** before Backup/Export implementation, define candidate validation and last-known-good preservation. No product files edited.

## Current judgment
D005 now has two executable blocks. It establishes that recovery requires both acceptance and safe publication discipline, and demonstrates a bounded fail-closed validate-before-publish alternative. The professional boundary remains incomplete because crash/power-loss, WAL/open-handle and mobile storage semantics are not validated. Balance Loop should now compare whether those dependencies are obtainable; otherwise advance to the highest-value independent prerequisite rather than simulating them.
