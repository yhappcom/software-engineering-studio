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
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 two + Q004 first executable counterexample/shrinking + Q005 first + Q006 first |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### Q004 — executable generated counterexample and reduction
Canonical: `research/quality/Q004_property_model_based_testing_invariants.md`  
Fixture: `research/quality/fixtures/Q004_model_property_sequence_shrinking.py`

The prior infrastructure-only execution gap is resolved for the stdlib Python fixture. Python 3.13.5 execution with fixed seed `20260917` found a violation in the first generated case: `delete_v3, update_v2, update_v2`. The deliberately naive arrival-order replica ended at `B`, while the independent version-aware model ended at deleted state `None`.

Greedy command deletion reduced the reproducer to `delete_v3 → update_v2`; the fixture verified that removing either remaining command eliminates the violation, so the case is 1-minimal under single-command deletion. This reduced case is now retained as a deterministic model-level regression reproducer.

Evidence remains bounded: one seed does not establish search coverage, greedy deletion is not global minimization, reduction is not root-cause proof, and this is not Dart/Flutter/backend/product evidence. Deliberate mutation sensitivity of a version-aware SUT and generated-vs-exhaustive search comparison remain OPEN.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck.
- **F002/F003:** alias/lifetime and representation/workload/complexity first executable blocks.
- **F004-F006:** concurrency, async and network/termination failure mechanics.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **D001-D006:** persistence/migration/cache/restore/sync evidence retained.
- **Q001-Q006:** all Quality Foundation topics now have professional boundaries; Q004 now includes first executable evidence.
- **A001-A003, S001:** prior evidence retained.

## Cross-track handoffs
- **Data:** Q004 independently re-exposed D006's stale-update-after-newer-delete class; `delete_v3 → update_v2` is the reduced deterministic transfer case. Data still owns actual delete/recreate/tombstone semantics.
- **Architecture:** A003 contracts/invariants can become property sources, but test models should avoid duplicating implementation representation.
- **Mobile:** generated lifecycle/process-death state machines still require exact platform fault controls and durable-state oracles.
- **Systems:** CI use of generated campaigns must bind framework/seed/artifact/environment and resource budgets.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical semantic decision in those repositories is changed by this bounded testing-method block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables were rechecked and remain unavailable; Python 3.13.5 is available.

Q004's immediate executable-rung dependency is now closed, so source-only continuation has lower marginal value. Current strongest independent candidates are:
1. Architecture Foundation closure on architecture-vs-design-vs-implementation and refactoring/technical-debt boundaries — prerequisite/gate leverage;
2. `S002` threat modeling/least privilege/secrets — untouched, high security/reuse/risk leverage;
3. `S003` CPU/memory/I/O/network cost models and profiling — high cross-track leverage;
4. return to Q004 for deliberate mutant sensitivity and generated-vs-exhaustive comparison when that outranks the untouched gaps;
5. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.