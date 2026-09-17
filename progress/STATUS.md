# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002/F003 first blocks + F004 two + F005 two + F006 two blocks complete |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated block + M002 first process/background source/failure-model block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two + D003 two + D004 first + D005 two + D006 two blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 two + Q004 source/model + prepared fixture (execution OPEN) + Q005 first + Q006 first |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### Q004 — property/model-based testing and invariant checking
Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`  
Fixture: `research/quality/fixtures/Q004_model_property_sequence_shrinking.py`

Q004 closes the last completely untouched Quality Foundation topic at the SOURCE/MODEL level. Current QuickCheck/model-based-testing literature and Hypothesis stateful-testing documentation support generated properties/action sequences, reference-model comparison, invariants and reduced reproducing programs.

The Studio now explicitly separates property/invariant, generator/model transition system, search strategy and counterexample reduction. Generated passing samples are counterexample-search evidence rather than proof; a reduced failure is not automatically root cause or globally minimal; and bounded exhaustive enumeration remains preferable when the complete relevant state space is genuinely tractable.

A stdlib-only executable fixture was prepared using D006's stale-update/newer-delete failure class. It generates versioned delivery histories from a fixed seed, compares a deliberately naive arrival-order replica with an independent version-aware model, and greedily removes commands while preserving a violation. **No execution result is claimed:** available execution tools failed with infrastructure `GatewaySelectionError`. The fixture is therefore executable material awaiting VALIDATION, not executable evidence.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN.
- **F002:** binding/object/identity/mutation/alias/reachability/resource-lifetime model + first alias/shallow-copy failure/alternative evidence.
- **F003:** first representation/workload/complexity block with queue semantic oracle and CPython size sweep.
- **F004:** lock-order/circular-wait plus condition predicate/signaling.
- **F005:** timeout-vs-underlying-work/cancellation plus ordering/error/cleanup.
- **F006:** stream framing plus termination/partial-delivery ambiguity.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **Q003/Q005/Q006:** schedule matrix, fault isolation and recovery/regression methods.
- **D001-D006, Q001-Q002, A001-A003, S001:** prior evidence retained.

## Cross-track handoffs
- **Data:** D006 future delete/recreate/tombstone-GC or operation-vs-state work should define Data-owned invariants first; Q004 can generate histories and reduce counterexamples.
- **Architecture:** A003 contracts/invariants can become property sources, but test models should avoid duplicating implementation representation.
- **Mobile:** generated lifecycle/process-death state machines require exact platform fault controls and durable-state oracles before transfer.
- **Systems:** CI use of generated campaigns must bind framework/seed/artifact/environment and resource budgets.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical semantic decision in those repositories is changed by this bounded testing-method block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. During this run the available local execution facility itself failed with infrastructure `GatewaySelectionError`, so Q004 execution was also preserved as OPEN rather than fabricated.

Q004 removes the last untouched Quality Foundation topic conceptually, but its executable rung is incomplete. First retry execution/mutation validation when trustworthy execution is available. If infrastructure remains blocked, source-only Q004 has lower marginal value.

Strong independent next candidates:
1. Architecture Foundation closure on architecture-vs-design-vs-implementation and refactoring/technical-debt boundaries;
2. `S002` threat modeling/least privilege/secrets — high security/reuse value and currently untouched;
3. `S003` CPU/memory/I/O/network cost models and profiling — high cross-track leverage, but meaningful execution should wait for working runtime tooling;
4. `M003` sandbox/files/permissions only if platform evidence can advance beyond reading;
5. return immediately to Q004 execution and direct Dart/Flutter/mobile execution when trustworthy environments become available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
