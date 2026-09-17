# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F004 two synchronization + F005 two async + F006 two network blocks complete |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated Foundation block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two + D003 two + D004 first + D005 two + D006 two blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 two + Q005 first + Q006 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### Q006 — fault injection, recovery verification and regression governance
Canonical: `research/quality/Q006_fault_injection_recovery_regression_governance.md`  
Fixture: `research/quality/fixtures/Q006_fault_injection_recovery_regression.py`

The first Q006 block converts prior F005/F006/D006/Q003 failure mechanics into a Quality-owned recovery campaign method.
- explicit fault points: `before_apply`, `after_apply_before_ack`, `after_ack`;
- recovery replays the same logical operation identity because the injected failure does not by itself establish terminal operation state;
- independent terminal oracle requires balance 110 plus one applied/acknowledged logical operation;
- robust idempotent comparison passed 3/3 injected points;
- a deliberate regression mutant that records operation identity but no longer guards the effect failed both post-apply points with balance 120 while the before-apply point still passed;
- therefore fault observation, successful retry and verified recovery are distinct claims;
- killing the bounded mutant demonstrates sensitivity to that duplicated-effect regression, not completeness against all possible regressions.

Evidence limit: Python 3.13.5 / Linux 6.18.44 deterministic single-process model. No Dart/Flutter, real process death/restart, durable storage, real network/backend, combined-fault, mobile or production release-gate claim.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **F004:** lock-order/circular-wait plus condition predicate/signaling.
- **F005:** timeout-vs-underlying-work/cancellation plus ordering/error/cleanup.
- **F006:** stream framing plus termination/partial-delivery ambiguity.
- **Q003:** shared-memory schedule failure plus explicit 24-order async event matrix.
- **D006:** retry/idempotency/conflict plus reordered stale-update/delete/tombstone model.
- **Q005:** identical-symptom fault-isolation/observability block.
- **Q006:** explicit fault-point campaign + semantic recovery oracle + regression-mutant sensitivity.
- **D001-D005, Q001-Q002, A001-A003, M001, S001:** prior evidence retained.

## Cross-track handoffs
- **Foundations:** F005/F006 now have a reusable Quality campaign consumer; direct Dart/Flutter execution remains blocked.
- **Architecture:** consumer-visible recovery/terminal-state behavior should be represented as contracts/invariants where applicable.
- **Mobile:** M002 should inject exact process/lifecycle failure points and judge durable/recovered state rather than lifecycle callback observation alone.
- **Data:** D005/D006 can reuse the Q006 campaign structure while retaining Data-owned restore/sync semantic oracles.
- **Quality:** Q006 removes the previously untouched fault-injection/recovery/regression Foundation gap at bounded executable level; real crash/restart/network/runtime transfer remains OPEN.
- **Systems:** production/release recovery gates must bind tests to exact artifact/build/environment; security fault injection remains separate.
- **Design Studio / Web Manager / Marketing Manager:** no current canonical evidence materially changes this bounded Quality method.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

Q006 now supplies a reusable method for `fault point → recovery action → independent terminal-state oracle → regression sensitivity`. Quality Foundation breadth is materially stronger, but real process/storage/network/runtime transfer is still missing.

Strong next candidates:
1. `M002` Android/iOS process lifecycle, termination and background execution, now using Q006 to shape failure/recovery evidence rather than lifecycle-reading alone;
2. untouched `F002` memory/lifetime or `F003` data structures/complexity if prerequisite severity wins;
3. `Q004` property/model-based testing once a richer state machine can materially improve state-space coverage;
4. return immediately to direct F001/F005/F006 Dart/Flutter execution when a trustworthy SDK environment exists.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
