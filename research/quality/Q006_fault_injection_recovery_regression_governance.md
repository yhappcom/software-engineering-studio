# Q006 — Fault Injection, Recovery Verification & Regression Governance

Status: **IN STUDY — first integrated Foundation block complete**  
Evidence date: 2026-09-17

## Problem and scope

Reliability testing is weaker than ordinary happy-path testing when it only proves that an injected failure was observed. The professional question is whether the system reaches an acceptable semantic state after the failure and whether a later regression reintroducing the same failure mechanism is detected.

This block studies a bounded operation with three explicit fault points:

`before apply → apply → acknowledgement`

and asks what a recovery retry may safely infer.

## SOURCE

- The Studio `methods/VALIDATION_STANDARD.md` requires failure-first evidence for persistence/sync/concurrency/recovery work and preserves the chain `failure observation → reproduction → isolation → causal hypothesis → check/falsification → root cause → fix → regression evidence`.
- Python `unittest` documentation defines a test fixture as setup plus associated cleanup and states that test cases should be self-contained/independent. This supports the harness-isolation discipline used here; it does **not** define the application recovery semantics.

## SYNTHESIS — recovery evidence model

A useful recovery campaign separates:

1. **fault model** — what can fail and at which semantic boundary;
2. **injection point** — exact location where the fault is forced;
3. **observable symptom** — exception/timeout/reset/etc.;
4. **recovery action** — retry, replay, rollback, restart, restore, reconcile;
5. **recovery oracle** — independent semantic terminal-state property;
6. **regression guard** — evidence that reintroducing the defect makes the test fail;
7. **scope limit** — failure classes and environments not represented.

`fault observed` is therefore not equivalent to `recovery verified`.

## EXECUTABLE VALIDATION

Fixture: `research/quality/fixtures/Q006_fault_injection_recovery_regression.py`

Environment executed before persistence:
- Python 3.13.5
- Linux 6.18.44 x86_64
- deterministic single-process state model

### CLAIM

If a caller retries after an ambiguous operation failure, the recovery test must judge the final semantic state rather than treating retry completion as the oracle. Stable logical-operation identity can make the bounded replay idempotent; removing the identity guard should be detected as a regression.

### PROPERTY / ORACLE

Initial balance is 100. One logical operation `op-1` adds 10 exactly once. After recovery:

- `balance == 110`;
- `applied == {'op-1'}`;
- `acked == {'op-1'}`.

The oracle is intentionally independent of whether an exception was raised.

### FAULT CAMPAIGN

Injected points:
- `before_apply`;
- `after_apply_before_ack`;
- `after_ack`.

After each injected failure, the harness replays the **same logical operation ID** once, modeling a caller that cannot infer terminal operation state from the failure symptom alone.

### OBSERVATION

Robust comparison:

`before_apply → 110 PASS`  
`after_apply_before_ack → 110 PASS`  
`after_ack → 110 PASS`

Regression mutant with the idempotency guard removed:

`before_apply → 110 PASS`  
`after_apply_before_ack → 120 FAIL`  
`after_ack → 120 FAIL`

### DEBUG / ROOT CAUSE

The failing mutant still records the operation identity but no longer uses it to guard the effect. A failure after application leaves the first effect present; recovery replay applies the same logical operation again. The final balance of 120 is therefore a duplicated semantic effect, not merely an exception-handling difference.

The `before_apply` case still passes because no first effect occurred before recovery. This is useful discrimination: the campaign is sensitive to **where** the failure occurs, not just to the existence of a fault.

## CONTRADICTION

The following shortcut is falsified in this bounded model:

> If the recovery retry returns successfully, the operation has recovered correctly.

Both mutant post-apply schedules complete the recovery call, yet violate the terminal-state oracle.

## REGRESSION GOVERNANCE

A recovery regression test is materially stronger when it can demonstrate that a plausible reintroduced defect is detected. Here, disabling the operation-ID guard is a deliberate bounded mutant. The campaign kills that mutant at the two post-apply fault points.

This is **not** a mutation-testing completeness claim. One killed mutant does not establish sensitivity to every regression class. It establishes that this specific recovery oracle is not vacuous with respect to the duplicated-effect defect it is intended to prevent.

## ENGINEERING JUDGMENT

For high-risk recovery paths, organize tests around semantic boundaries rather than generic exception categories. A useful matrix is:

`prestate × fault point × recovery action × terminal-state oracle × restart/retry count`

where the dimensions are bounded according to the actual system contract. The campaign should preserve first failing state/trace and distinguish harness failure from SUT failure.

## TRANSFER VALIDATION

This block transfers prior Q003/D006/F006 findings into a Quality-owned method:
- Q003 contributes explicit event/fault-space enumeration rather than repeated sleeps;
- D006 contributes stable logical-operation identity and apply-vs-ack separation;
- F006 contributes the reason transport failure can leave application state ambiguous.

The transfer is **VALIDATED only at deterministic model level**. It is not Dart/Flutter, Firestore, mobile process-death, real network, filesystem crash, or production evidence.

## RELATED DOMAIN CHECK

- **Foundations:** F005 timeout/cancellation and F006 transport termination ambiguity directly motivate ambiguous terminal state.
- **Architecture:** A003 contracts/invariants provide candidate recovery oracles; recovery behavior is part of consumer-visible semantics when exposed.
- **Mobile:** M001 shows lifecycle callbacks may be skipped; M002 process-death/background recovery remains OPEN.
- **Data:** D005/D006 supply restore and sync failure classes; this note does not redefine their data semantics.
- **Quality:** Q001 oracle discipline, Q003 bounded ordering, and Q005 root-cause separation are direct prerequisites.
- **Systems:** artifact/environment identity must bind any release-gate recovery evidence; security fault injection remains separate.
- **Design Studio:** not materially relevant to this bounded method until recovery/conflict states become user-visible interaction contracts.
- **Web Manager:** not materially relevant to this bounded model; future PWA/service-worker recovery is a transfer target, not current evidence.
- **Marketing Manager:** not materially relevant.
- **Product source:** no product repository was required to establish this reusable method; no product defect claim is made.

## HANDOFFS

- **TO Data:** use Q006 campaign structure when extending D005/D006 into process death, restart, duplicate delivery, delete/recreate, or tombstone-GC tests. Preserve Data-owned semantic oracle.
- **TO Mobile:** M002 should include exact lifecycle/process-kill injection point plus durable/recovered-state oracle, not callback observation alone.
- **TO Systems:** release gates can reuse the regression-sensitivity requirement, but must bind evidence to exact artifact/build/environment identity.
- **TO Foundations:** no change to F006 transport semantics; this confirms their value as fault-model inputs.

## OPEN / VALIDATION

- Direct Dart/Flutter execution remains unavailable in the current environment.
- Real process kill/restart and durable-storage recovery campaign.
- Network/backend fault proxy or equivalent real transport injection.
- Harness-vs-SUT failure discrimination under asynchronous execution.
- Fault combinations rather than one injected fault at a time.
- Resource leak/cleanup oracle after recovery.
- Cross-platform/mobile transfer and production release-gate evidence.

## Gate effect

Q006 now has a first executable Foundation block with explicit fault points, semantic recovery oracle, failure discrimination, root cause, robust alternative, and a deliberate regression mutant. Quality Stage 1 remains **NOT PASS** because real crash/restart/durable/network/runtime transfer and broader error/recovery evidence remain open.
