# D005 — Dart candidate/publication process-interruption transfer

Status: **BOUNDED TRANSFER VALIDATION**  
Evidence date: 2026-09-25  
Fixture: `research/data/fixtures/D005_dart_candidate_publication_transfer.dart`  
Workflow: `.github/workflows/d005-dart-candidate-publication-transfer.yml`

## Problem

Prior D005 Python/SQLite evidence established that candidate generation, database-aware completion, validation and publication are distinct states. Data status still carried a stale statement that direct Dart/Flutter execution was unavailable. F001 now has direct Dart evidence, so this block transfer-tests the reusable candidate/publication protocol at the Dart `dart:io` file/process boundary rather than repeating SQLite semantics.

## SOURCE

Dart's `File.rename` is the API used for the bounded publication transition in this fixture. The claim here is deliberately narrower than crash durability: successful rename is used only as the observed namespace transition after a validated private candidate. No claim is made that Dart `flush: true` or rename alone supplies hard-power-loss durability, directory durability, or cross-platform atomic replacement guarantees.

Toolchain acquisition is pinned: `dart-lang/setup-dart@65eb853c7ba17dde3be364c3d2858773e7144260` (v1.7.2 tag target checked 2026-09-25), installing Dart 3.13.4. Checkout is pinned to `actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683` (v4.2.2 tag target checked 2026-09-25).

## CLAIM / PROPERTY

At this bounded Dart/Linux target, keeping replacement state in a private candidate until an explicit publication transition prevents process termination before publication from overwriting the last accepted artifact. Candidate existence/completeness and accepted publication remain separate states.

## EXECUTABLE TEST / FAILURE CASE

Exact workflow head: `9c52779c0e69f10557e8e36da97db55aa24325f2`  
Hosted run: `36020700051`  
Job: `107704539236`  
Environment: GitHub-hosted `ubuntu-24.04`, Dart 3.13.4  
Result: `completed / success`.

Fixture protocol:
1. create accepted `published.json` with semantic state generation=1, rows=10;
2. child writes and flushes private `candidate.tmp` with generation=2, rows=200, then emits a separate ready marker and waits;
3. parent independently reads and validates candidate semantic state;
4. parent injects process failure with SIGKILL before publication and requires a nonzero child exit;
5. parent rereads the accepted artifact and requires it to remain byte-identical and semantically generation=1, rows=10;
6. only after that failure oracle, parent renames the private candidate onto the publication path and requires generation=2, rows=200;
7. workflow independently greps the fail-closed terminal verdict and all old/new semantic observations.

All setup, environment-recording and fail-closed validation steps completed successfully in job `107704539236`.

## VALIDATION

This is **TRANSFER VALIDATION** from the prior Python/SQLite candidate/publication state-machine conclusion into direct Dart process/file execution. It demonstrates the protocol property under an injected process death before publication without treating file existence, flush completion, or workflow green alone as the oracle.

## SYNTHESIS

The reusable state model survives the language/runtime transfer:

`private candidate → semantic validation → publication transition → accepted artifact`

A process can die after producing a complete candidate without invalidating the previous accepted artifact when the candidate has not yet been published. This supports keeping backup/export replacement candidates private until validation completes.

## CONTRADICTION / REFINEMENT

`progress/file exists/write completed ⇒ accepted backup/export` remains invalid. The Dart transfer also removes the stale Data-track execution dependency that claimed trustworthy direct Dart execution was unavailable. It does **not** close mobile filesystem or durability questions.

## EVIDENCE LIMIT

This run does not establish:
- hard-power-loss durability;
- file or parent-directory fsync ordering;
- atomic replacement guarantees on Android/iOS/Windows/macOS filesystems;
- behavior when source/destination cross filesystems;
- Flutter plugin/wrapper behavior;
- SQLite backup correctness in Dart;
- encryption/export/share pipeline behavior;
- LogMate product behavior or production behavior.

No Data Stage-1 PASS is awarded.

## RELATED DOMAIN CHECK

- **Foundations:** F001 direct Dart execution is already validated; the stale SDK blocker is removed.
- **Architecture:** candidate and accepted artifact remain distinct state/ownership contracts.
- **Mobile:** exact Android/iOS process-death and filesystem transfer remains OPEN.
- **Data:** owning track; extends D005 with direct Dart language/runtime transfer.
- **Quality:** failure injection precedes PASS; independent semantic old/new-state oracles and nonzero child exit are required.
- **Systems:** hard-power-loss, filesystem durability, publication primitive and artifact retention remain separate operational evidence.
- **Design Studio:** not materially relevant to this low-level transfer.
- **Web Manager:** not materially relevant.
- **Marketing Manager:** not materially relevant.
- **Product:** latest LogMate implementation ref remains `7551e1ca9e07df0b99e88aa03c8a56be03d8b2d3`, declared `1.0.0+1`, evidence date 2026-09-25; production identity unknown. No claim that LogMate implements this protocol.

## HANDOFFS

### Data → Mobile
Transfer the same candidate-before-publication process-death oracle to the exact Android/iOS/Flutter persistence/export stack when that implementation exists. Do not infer mobile filesystem guarantees from Linux.

### Data → Systems
The next materially stronger publication rung is durability across abrupt system/power loss with explicit file/directory synchronization and platform filesystem semantics; Dart `flush`/rename evidence here is insufficient.

### Data → LogMate
When backup/export is implemented, preserve private candidate, validation and publication as separate states and test process death between them on the exact product ref/build.

## OPEN / CHANGE WATCH

- **OPEN:** Android/iOS/physical-device transfer;
- **OPEN:** hard-power-loss and directory durability;
- **OPEN:** exact LogMate persistence/backup/export transfer;
- **CHANGE WATCH:** Dart/platform file semantics and mobile filesystem behavior by SDK/OS/filesystem version.
