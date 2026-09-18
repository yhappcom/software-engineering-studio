# D005 — SQLite Online Backup API under live WAL concurrency

Status: **IN STUDY — EXECUTABLE LIVE-CONCURRENCY EVIDENCE**  
Evidence date: 2026-09-19

## Problem

Earlier D005 evidence established that in WAL mode committed state may exist outside the main database file and that active readers can prevent checkpoint completion/reset. The next distinct recovery boundary is whether SQLite's Online Backup API can produce a semantically complete database while the WAL-backed source remains live and another connection commits during an incremental backup.

This is not a claim about LogMate's current persistence implementation.

## SOURCE

SQLite's current Online Backup API documentation states that each `sqlite3_backup_step()` holds a shared lock on the source only for that step, so other source connections may modify the database between steps. If another connection/process modifies the source, the backup is automatically restarted by the next step. `SQLITE_BUSY`/`SQLITE_LOCKED` are non-permanent step outcomes. SQLite's backup documentation further states that, whether restarted or not, a completed backup is a consistent and up-to-date snapshot; sufficiently frequent source writes can prevent completion.

Primary sources checked 2026-09-19:
- https://www.sqlite.org/c3ref/backup_finish.html
- https://www.sqlite.org/backup.html

## CLAIM / PROPERTY

**CLAIM:** under this bounded WAL/live-writer fixture, a completed SQLite Online Backup operation must not silently publish the pre-write semantic state merely because copying began before a concurrent commit. External source modification should force restart/update behavior, and successful completion should yield a structurally valid destination containing the committed row.

**PROPERTY:** completed destination row set equals current source row set for the modeled ledger; the deliberately injected concurrent row is present; `PRAGMA integrity_check=ok`; progress reaches `SQLITE_DONE`. A rise in `remaining` pages after prior progress is used as a bounded restart/progress observation, not a portable API guarantee about exact counts.

## EXECUTABLE VALIDATION

Fixture: `research/data/fixtures/D005_online_backup_live_wal_concurrency.py`

Environment:
- Linux
- Python 3.13.5
- SQLite 3.46.1 via Python `sqlite3`
- source journal mode: WAL
- `wal_autocheckpoint=0`
- 500 initial rows with payload large enough to create 502 source pages
- incremental backup: 5 pages per step
- separate writer connection commits one additional `CONCURRENT` row after two progress callbacks

Observed canonical run before persistence:

```text
page_count before backup: 502
progress prefix: (0,497,502), (0,492,502), then (0,497,502), (0,492,502), (0,487,502)...
final progress: (...), (101,0,502)
source_count=501
backup_count=501
concurrent_rows=1
integrity_check=ok
```

`101` is `SQLITE_DONE` in this environment.

## VALIDATION

The external commit occurred after backup copying had already made progress. On the next observed backup progress, `remaining` rose from 492 to 497 pages. The completed destination contained all 501 rows including the injected concurrent row and passed `integrity_check`.

This executable result agrees with the documented restart behavior for modifications from a different source connection.

## SYNTHESIS

1. **Online Backup API is a database-aware consistency mechanism, not a raw main-file copy.** In WAL mode this matters because committed state can be outside the main DB file.
2. **Backup start time is not automatically the semantic cut represented by a completed incremental backup under concurrent external writes.** In this fixture, a commit made after copying started was included after restart.
3. **Completion and consistency are separate from bounded progress.** SQLite explicitly warns that frequent enough writes may repeatedly restart an incremental backup so that it never completes.
4. A backup acceptance contract therefore needs at least: source identity/state assumptions, completion oracle, semantic-content oracle, destination integrity/openability, concurrency policy, progress/timeout budget, and recovery behavior for abandoned/failed destination creation.

## CONTRADICTION / wording caution

The high-level backup page describes the destination as a snapshot of the source as copying commenced, while the same official backup documentation and C API describe external mid-backup writes causing restart and say the completed backup is consistent and up-to-date. The executable fixture demonstrates the latter behavior for this SQLite 3.46.1 incremental WAL case: a post-start external commit was present in the completed backup. Do not operationalize “backup start time” as a guaranteed point-in-time cut without a stronger mechanism/transaction contract and direct validation.

This is a documentation-semantics caution, not a claim that SQLite is internally inconsistent; the exact snapshot point depends on the backup execution/restart behavior.

## ALTERNATIVES

SQLite documents `VACUUM INTO` and `sqlite3_rsync` as other backup techniques. They have different mechanics and must not inherit this fixture's concurrency/progress claims without separate validation. A raw main-file copy is already known from prior D005 WAL evidence to be an unsafe completeness oracle when committed WAL state has not been consolidated.

## EVIDENCE LIMIT

This run does **not** establish:
- sustained-writer starvation thresholds or bounded completion latency;
- behavior when the backup process itself crashes or destination storage fails;
- Online Backup API behavior through a particular Flutter/Dart SQLite package;
- Android/iOS filesystem, lifecycle, process-death or backup policy behavior;
- physical power-loss durability;
- a fixed point-in-time snapshot at invocation time;
- production LogMate behavior.

No Data Foundation PASS is awarded.

## Product transfer context

Repository checked: `yhappcom/logmate`  
Ref: `main` → `b551ce434ad72b1895033e0f3617c73b026d40ea`  
Declared version: `1.0.0+1` from retained prior exact-ref evidence  
Evidence date: 2026-09-19  
Production identity: **unknown; default branch is not assumed production**.

No relevant `backup restore SQLite WAL` evidence was found by repository search in `yhappcom/design-studio`, `yhappcom/web-manager`, `yhappcom/marketing-manager`, or the inspected LogMate default-branch search. This does not prove absence outside indexed/default-branch search scope.

## RELATED DOMAIN CHECK

- **Foundations:** F001 direct Dart/Flutter remains OPEN; F004/F006 process/concurrency boundaries support connection/progress reasoning.
- **Architecture:** backup consistency point and publication/completion semantics are externally meaningful contracts, not storage implementation trivia.
- **Mobile:** exact plugin/native/filesystem/process-lifecycle transfer remains OPEN.
- **Data:** extends D005 from WAL checkpoint completeness to database-aware online backup under a live writer.
- **Quality:** backup tests require independent semantic-content and completion/progress oracles; `integrity_check=ok` alone is insufficient.
- **Systems:** backup latency/resource budget and destination artifact handling become operational concerns under frequent writes.
- **Design Studio:** considered; no materially relevant canonical evidence found in the bounded search.
- **Web Manager:** considered; no materially relevant canonical evidence found in the bounded search.
- **Marketing Manager:** considered; no materially relevant canonical evidence found in the bounded search.
- **Product:** exact LogMate ref checked as above; no claim of current SQLite/WAL implementation.

## HANDOFFS

- **Quality:** add a future failure campaign that distinguishes destination structural integrity, semantic completeness, backup completion and bounded progress/starvation.
- **Mobile:** when Flutter/native SQLite infrastructure exists, reproduce concurrent-write backup with exact package/version, app lifecycle and destination-file publication path.
- **Systems:** define timeout/resource/temporary-file/atomic-publication policy if a product uses online backup for user-visible backup/export.
- **LogMate:** before implementing backup, choose and document the consistency point and whether concurrent writes may be included; do not infer point-in-time-at-start semantics from API name alone.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** sustained write pressure and starvation/resource thresholds.
- **OPEN:** interruption/crash during Online Backup and safe destination publication.
- **OPEN:** Flutter/Android/iOS transfer and actual LogMate backup implementation.
- **VALIDATION:** materially different backup mechanisms (`VACUUM INTO`, platform/export pipeline) only when they become decision-relevant.
- **CHANGE WATCH:** SQLite backup/WAL behavior and wrapper APIs are version-sensitive; bind future evidence to exact SQLite/wrapper versions.
