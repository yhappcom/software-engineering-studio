# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002/F003 first blocks + F004 two + F005 two + F006 two blocks complete |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial + A005 first executable refactoring/debt boundary block complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated block + M002 first process/background source/failure-model block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two + D003 two + D004 first + D005 two + D006 two blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 two + Q004 first executable counterexample/shrinking + Q005 first + Q006 first |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### A005 — architecture/refactoring/technical-debt boundaries
Canonical: `research/architecture/A005_refactoring_technical_debt_evolutionary_boundaries.md`  
Fixture: `research/architecture/fixtures/A005_refactoring_behavior_boundary.py`

The principal Architecture Stage-1 conceptual gap is now materially covered at first executable level. Current ISO/IEEE/SEI evidence distinguishes architecture from its description and frames architecture around significant structures/relations/properties/decisions used to reason about system qualities. Fowler's precise refactoring boundary is retained: internal restructuring must preserve the relevant observable behavior.

Python 3.13.5/Linux execution compared a legacy quote function, a split-calculation restructuring, and a deliberate clamp mutant against an independently declared three-case oracle. Legacy and refactored implementations preserved `USD 110.00`, `USD 0.00`, and `ERROR:negative principal`; the tidy-looking mutant changed the negative-input contract to `USD 0.00` and was detected. This establishes bounded behavior-preservation evidence plus mutation sensitivity; it is not Dart/Flutter/product evidence.

Technical debt is now modeled as a concrete contingent future-change liability: artifact/decision → short-term context/benefit → plausible future change → extra cost/risk → remediation → uncertainty. Bug, code smell, age, and aesthetic dislike are not sufficient debt classifications by themselves.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck.
- **F002/F003:** alias/lifetime and representation/workload/complexity first executable blocks.
- **F004-F006:** concurrency, async and network/termination failure mechanics.
- **A001-A003:** change pressure/information hiding, ownership/dependency direction, semantic contracts/invariants.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **D001-D006:** persistence/migration/cache/restore/sync evidence retained.
- **Q001-Q006:** all Quality Foundation topics have professional boundaries; Q004 includes executable generated counterexample/shrinking.
- **S001:** artifact identity/authenticity/authorization/provenance evidence retained.

## Cross-track handoffs
- **Quality:** refactoring validation should declare the observer set and use independent contract oracles; green tests alone do not prove behavior preservation.
- **Data:** persisted schema/data evolution is not ordinary internal refactoring when old readers/writers/data are part of observable compatibility.
- **Systems:** performance/security/artifact properties can be architectural observables; technical debt can exist in build/release infrastructure.
- **Mobile:** lifecycle/plugin/platform behavior can enlarge the observer set beyond Dart-level nominal outputs.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision in those repositories is changed by this bounded Architecture block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables were rechecked 2026-09-17 and remain unavailable; Python 3.13.5 is available.

A005 materially closes the roadmap's Architecture-vs-design-vs-implementation and refactoring/technical-debt Foundation gap, so further source-only Architecture expansion has lower marginal value. Current strongest independent candidates are:
1. `S002` threat modeling, least privilege, secrets and secure-storage fundamentals — untouched, high security/risk/reuse leverage;
2. `S003` CPU/memory/I/O/network cost models and profiling — untouched, high cross-track leverage;
3. `M003` sandbox/files/permissions/secure-storage/platform APIs — live mobile relevance but platform execution limitations remain;
4. return to Q004 for deliberate mutant sensitivity/search comparison when it outranks untouched gaps;
5. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
ISO/IEC/IEEE 42010:2022 is current as checked 2026-09-17. ISO/IEC/IEEE DIS 42024 architecture fundamentals is under development; do not adopt draft terminology as stable without recheck.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.