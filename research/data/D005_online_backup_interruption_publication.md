# D005 — Online Backup interruption and publication boundary

Status: **IN STUDY — executable process-interruption evidence**  
Evidence date: 2026-09-19  
Fixture: `research/data/fixtures/D005_online_backup_interruption_publication.py`

## Problem

The prior D005 block established that SQLite Online Backup is database-aware under live WAL writes, but completion and safe publication remained separate OPEN properties. This block asks what a consumer may infer if the backup-producing process dies after copying has begun but before the backup operation reaches completion.

## SOURCE

SQLite's Online Backup C API states that the destination is held in a write transaction for the backup operation. `sqlite3_backup_step()` returns `SQLITE_DONE` only when all pages have been copied. If `sqlite3_backup_finish()` is called before `SQLITE_DONE`, the active destination write transaction is rolled back. SQLite's backup documentation also warns that OS/power failure during ordinary file copying can leave a backup corrupted and presents the Online Backup API as a database-aware mechanism.

Primary sources checked 2026-09-19:
- https://www.sqlite.org/c3ref/backup_finish.html
- https://www.sqlite.org/backup.html

## CLAIM / PROPERTY

A backup candidate must not be considered an accepted/published backup merely because its destination pathname exists or because progress has been reported. Acceptance requires an explicit successful-completion oracle plus semantic validation appropriate to product risk. Publication of a replacement artifact is a separate state transition from generation.

## EXECUTABLE VALIDATION

Environment observed in this run:
- Linux execution environment;
- Python 3.13.5;
- SQLite 3.46.1 as reported by Python's `sqlite3` module.

Source setup:
- WAL-mode SQLite source;
- 1,500 rows, each with a 3,000-byte payload;
- observed source size: 1,505 SQLite pages.

### Failure case — final/public-looking path exists before completion

A child process opened an Online Backup destination using the final-looking path `unsafe-final.db`. The backup copied one page per step. The progress callback created a marker after progress began and slept briefly; the parent then killed the child process.

Observed progress marker: `0,1504,1505` — one page of progress had been reported. The child exited by kill. The destination pathname existed, but in the observed run the file size was 0 bytes and reopening it did not contain the expected `ledger` table (`OperationalError: no such table`).

**VALIDATION:** pathname existence and progress are invalid backup-completion oracles.

### Alternative — private candidate while retaining last accepted publication

A previously accepted `published.db` containing 10 rows and `integrity_check=ok` was created. A replacement backup was generated at a separate private `candidate.tmp` path. The child was killed after the same first-progress boundary.

Observed:
- candidate existed but did not contain the complete source state;
- SHA-256 of the previously published artifact was unchanged across the interrupted attempt;
- reopening the published artifact still returned 10 rows and `integrity_check=ok`.

**VALIDATION:** separating candidate generation from publication prevents this bounded interrupted generation attempt from replacing the last accepted artifact.

## DEBUG / ROOT-CAUSE CONNECTION

The observation matches the documented destination transaction boundary: progress during `backup_step` is not equivalent to `SQLITE_DONE`, and the destination write transaction is not a completed backup merely because bytes/path state are externally observable. A process kill also prevents normal application-level completion handling, so a producer that exposes the candidate path as though it were accepted can create a false-success artifact boundary even when SQLite's internal transaction mechanism is behaving correctly.

## SYNTHESIS

Backup correctness has at least four distinct transitions/oracles:

`generate candidate → reach database-aware completion → validate candidate → publish/accept candidate`

For replacement backup workflows, preserving the last accepted artifact until the new candidate has reached the required completion/validation boundary is stronger than writing directly to a name that consumers interpret as accepted. This is an engineering protocol conclusion, not a claim that pathname replacement alone is durable across hard power loss.

## ENGINEERING JUDGMENT

A reusable backup protocol should normally distinguish:
1. private/in-progress candidate identity;
2. successful database-copy completion;
3. structural and semantic acceptance checks;
4. publication of the accepted candidate;
5. retention/cleanup policy for the prior accepted artifact and abandoned candidates.

The exact publication primitive, fsync ordering, directory durability, encryption, retention and user-visible semantics are platform/product decisions and require their own evidence.

## CONTRADICTION / REFINEMENT

A common weak model is `backup file exists ⇒ backup succeeded`. The executable failure case directly contradicts that model. Likewise, a progress callback is an observability signal, not a commit/publication oracle.

## EVIDENCE LIMIT

This is **process-interruption evidence**, not physical power-loss evidence. It does not establish:
- crash-durable atomic rename/replacement;
- directory fsync semantics;
- lying-successful fsync behavior;
- filesystem/controller/device guarantees;
- Windows/Android/iOS behavior;
- Flutter wrapper behavior;
- encryption/export/share pipeline behavior;
- production LogMate backup behavior.

No PASS is awarded from this block.

## RELATED DOMAIN CHECK

- **Foundations:** process termination and file/I/O boundaries apply; direct Dart/Flutter execution remains OPEN.
- **Architecture:** candidate vs accepted artifact is an ownership/state-transition contract; consumers must not infer acceptance from path existence.
- **Mobile:** exact Android/iOS/Flutter file replacement, app process-death and backup/export behavior require transfer validation.
- **Data:** owning track; extends D005 from live-copy consistency into interruption/publication semantics.
- **Quality:** requires separate completion, structural integrity, semantic completeness and publication-state oracles; a progress callback is not sufficient.
- **Systems:** publication durability, fsync/directory semantics, temporary-file lifecycle, encryption and artifact retention are operational inputs.
- **Design Studio:** not materially relevant to the low-level mechanism; user-visible backup status must nevertheless not label an in-progress candidate as completed.
- **Web Manager:** not materially relevant to this local SQLite mechanism.
- **Marketing Manager:** not materially relevant.
- **Product:** no claim that current LogMate uses SQLite Online Backup; product implementation transfer remains OPEN.

## HANDOFFS

### Data → Quality
Add a reusable recovery/backup test rule: existence/progress cannot satisfy completion. Test interrupted candidate generation and assert the last accepted backup remains semantically usable.

### Data → Systems
Validate the next publication rung separately: same-filesystem replacement semantics, file+directory synchronization ordering, and hard-power-loss scope must not be inferred from this process-kill result.

### Data → Mobile / LogMate
When the persistence stack is implemented, define the backup state machine and transfer-test process death between candidate generation, completion, validation and publication on the exact Flutter/platform stack.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** hard-power-loss-safe publication and directory durability;
- **OPEN:** interrupted replacement after candidate completion but during publication;
- **OPEN:** Android/iOS/Flutter transfer;
- **OPEN:** production backup retention/encryption/share semantics;
- **VALIDATION:** exact platform filesystem and wrapper behavior;
- **CHANGE WATCH:** SQLite/wrapper/platform filesystem behavior by version and configuration.
