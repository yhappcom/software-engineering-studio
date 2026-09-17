# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-18  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F002/F003 first blocks + F004 two + F005 two + F006 two blocks complete |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial + A005 first executable refactoring/debt boundary block complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated block + M002 first process/background source/failure-model block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two + D003 two + D004 first + D005 two + D006 two blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 two + Q004 first executable counterexample/shrinking + Q005 first + Q006 first |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks + S002 first executable security block + S003 first executable profiling/resource block complete |

No specialist has passed Foundation.

## Meaningful new evidence

### S003 — CPU/memory/I/O/network cost models and profiling
Canonical: `research/systems/S003_resource_cost_models_profiling_foundations.md`  
Fixture: `research/systems/fixtures/S003_resource_cost_profiling.py`

Systems' untouched performance/profiling Foundation gap now has first executable evidence. The resource model separates wall latency, process CPU time, allocation/retention/peak memory, I/O and network dimensions rather than collapsing performance into one timer.

Python 3.13.5/Linux execution compared three deliberately different workloads. CPU arithmetic observed 345.435 ms wall / 345.408 ms process CPU; an 80 ms wait observed 80.203 ms wall / only 0.098 ms process CPU; a short allocation workload observed 5319.660 KiB peak traced Python allocation. Broad workload-class assertions passed.

The failure lesson is bounded but reusable: wall time alone cannot identify CPU work. Low CPU can falsify a CPU-bound explanation for this controlled wait, but low CPU in production does not prove disk/network root cause without additional evidence. `tracemalloc` allocation is also explicitly not treated as total RSS/native/GPU/platform memory.

F003 complexity is now connected to S003 profiling without conflation: complexity predicts growth under a model; profiling observes a specific workload/runtime/environment. One benchmark run remains insufficient for performance truth or a regression threshold.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **A001-A003/A005:** change pressure, ownership/dependency, semantic contracts, refactoring/debt boundaries retained.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **D001-D006:** persistence/migration/cache/restore/sync evidence retained.
- **Q001-Q006:** all Quality Foundation topics have professional boundaries; Q004 includes executable generated counterexample/shrinking.
- **S001-S003:** artifact trust/provenance, runtime authority/security, and first resource/profiling boundaries now have executable evidence.

## Cross-track handoffs
- **Foundations/F003:** complexity is predictive model; measured profiling is bounded observation; neither substitutes for the other.
- **Mobile:** transfer CPU/wait/allocation distinctions to Flutter/Android/iOS frame/startup/memory-pressure tooling when a trustworthy environment exists.
- **Data:** index/cache/sync alternatives should state which resource dimension changes and what trade-off is introduced.
- **Quality:** future performance regression evidence needs exact artifact/environment/workload, distributions/noise and a product budget oracle rather than a single timing.
- **Architecture:** resource budgets become architectural when cross-boundary structure/ownership determines them.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision in those repositories is changed by this bounded Systems block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables were rechecked 2026-09-18 and remain unavailable; Python 3.13.5 is available.

S003 removes the untouched performance/profiling Foundation gap at first executable level. Current strongest independent candidates are:
1. `S004` dependency/supply-chain/build-system fundamentals — untouched release/security prerequisite with high reuse;
2. `M003` sandbox/files/permissions/secure storage/platform APIs — high live-mobile/security transfer value, but platform execution limitations remain;
3. `A006` ADR/evidence-preserving decisions — useful governance prerequisite after principal Architecture concepts;
4. `Q004` mutation sensitivity/exhaustive-vs-generated comparison — useful method depth but lower prerequisite urgency than untouched S004;
5. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Python profiling APIs support the bounded S003 fixture only; their semantics/constants are not transferred to Dart/mobile.
- Android/iOS/Flutter/browser performance tooling and budgets are platform/version sensitive.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.
- Android Keystore/attestation guarantees are API/device/version sensitive.
- ISO/IEC/IEEE 42010:2022 remains current from prior check; DIS 42024 remains draft work.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
