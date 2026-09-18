# Q006 — Real Process-Crash Recovery Oracle Transfer

Status: **IN STUDY — real crash/restart transfer added**  
Evidence date: 2026-09-18

## Problem
Q006 previously validated recovery governance only in a deterministic single-process model. D006 later produced a real child-process termination boundary where replication progress can outrun durable semantic state. This block transfer-tests the Quality method against that stronger failure mechanism and asks whether a structurally healthy database is a sufficient recovery oracle.

## SOURCE
- Studio `methods/VALIDATION_STANDARD.md`: recovery evidence must bind a claim to an oracle and deliberately exercise failure paths; structural success is not automatically semantic recovery.
- SQLite transaction/atomicity semantics are Data-owned evidence already exercised by D005/D006. This Quality note does not generalize those semantics beyond the executed SQLite boundary.

## SYNTHESIS
Recovery verification requires an oracle over the product/protocol semantics that can fail even when storage is structurally healthy. For replication progress, `integrity_check=ok` and successful reopen are insufficient if a durable cursor claims that a semantic effect was consumed when that effect is absent and no replay path remains.

## EXECUTABLE VALIDATION
Fixture: `research/quality/fixtures/Q006_real_crash_recovery_oracle.py`.

Environment: Python 3.13.5 / Linux x86_64 / stdlib SQLite; executed 2026-09-18.

### CLAIM
A structural database oracle can falsely accept a recovery state that violates replication semantics; a semantic recovery oracle must compare durable progress with durable effect/replayability.

### TARGET / STATE
Initial state: entity `(value=100, revision=1)`, cursor `0`. Modeled server change 1 means entity `(120,2)`; the bounded server returns change 1 only while local cursor `<1`.

### FAILURE CASES
- `unsafe`: child commits cursor `1`, then terminates via `os._exit(71)` before entity apply.
- `safe`: child starts one transaction, applies entity and cursor, then terminates via `os._exit(72)` before COMMIT.

Fresh parent-process reopen supplies the observation.

### ORACLES
Structural oracle: `PRAGMA integrity_check == ok`.

Semantic oracle: if cursor is at least 1, the semantic effect through change 1 must be present; if the old entity remains, change 1 must still be replayable. This oracle is independent of SQLite structural integrity.

### OBSERVATION
`unsafe`: entity `(100,1)`, cursor `1`, server remaining `[]`, integrity `ok`; structural oracle **PASS**, semantic oracle **FAIL**.

`safe`: entity `(100,1)`, cursor `0`, server remaining contains change 1, integrity `ok`; structural oracle **PASS**, semantic oracle **PASS**.

Fixture verdict: `Q006 real crash recovery-oracle discrimination: PASS`.

## DEBUG / ROOT CAUSE
The unsafe case is not database corruption. The failure is protocol publication ordering: durable progress advanced independently of the semantic effect it summarizes. Because the bounded server trusts cursor 1, recovery cannot replay the omitted effect. The structural oracle is therefore insensitive to the defect class. The safe comparison keeps progress and effect in one transaction, so pre-COMMIT process death leaves both unpublished and replay remains available.

## CONTRADICTION
`database reopened + integrity_check=ok` does **not** imply semantic recovery. The unsafe case falsifies that shortcut while remaining structurally healthy.

## REPLICATION / TRANSFER VALIDATION
This is a transfer from Q006's single-process model into a real OS child-process termination + persistent SQLite restart boundary, reusing the D006 invariant with a Quality-owned oracle-discrimination question. It strengthens Q006's evidence ladder from model fault injection to real process crash/restart for this bounded failure class.

It is not Dart/Flutter, mobile process death, Firestore/backend, power loss, filesystem/device crash, production LogMate, or a general SQLite durability proof.

## RELATED DOMAIN CHECK
- Foundations: F001/F006 process and apply/commit/ACK distinctions support the failure boundary; direct Dart/Flutter remains OPEN.
- Architecture: progress publication is externally meaningful protocol state; contract ownership remains Architecture/Data concern.
- Mobile: exact Android/iOS/Flutter process-death transfer remains OPEN.
- Data: D006 owns the cursor/effect invariant and supplied the stronger crash boundary; this note does not redefine it.
- Quality: Q001 oracle discipline and Q006 recovery governance are directly advanced.
- Systems: artifact/environment identity matters for release-gate use; power/device durability is outside this fixture.
- Design Studio / Web Manager / Marketing Manager: considered; no canonical evidence there changes this recovery-oracle mechanism.
- Product source: no new product audit was required; this fixture transfer-tests the already recorded LogMate-derived invariant, not product implementation.

## HANDOFFS
- Mobile: reproduce the same structural-vs-semantic oracle discrimination on the exact Flutter persistence stack after process death.
- Data: retain semantic-state + progress-state recovery oracles in D006 implementation validation.
- Systems: release recovery gates should not substitute storage health/process liveness for semantic recovery acceptance.

## OPEN / VALIDATION
Direct Dart/Flutter execution; actual Android/iOS process death; real backend/cursor batches; concurrent local edits; combined network+process faults; power/filesystem/device faults; production release-gate evidence.

## Gate effect
Q006's named real process kill/restart + durable-storage recovery gap is now closed at a bounded Python/Linux/SQLite transfer level. Quality Stage 1 remains **NOT PASS** because direct Dart/Flutter/mobile/runtime transfer and broader real recovery evidence remain open.
