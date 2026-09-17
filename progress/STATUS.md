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
| Systems | Stage 1 IN STUDY — S001 two + S002 first + S003 first + S004 first executable dependency/build block complete |

No specialist has passed Foundation.

## Meaningful new evidence

### S004 — dependency, supply-chain and build-system foundations
Canonical: `research/systems/S004_dependency_supply_chain_build_system_foundations.md`  
Fixture: `research/systems/fixtures/S004_dependency_resolution_integrity.py`

Systems' untouched dependency/build Foundation gap now has first executable evidence. The model separates manifest constraints, resolved dependency graph, dependency content/integrity, toolchain/build inputs, build execution/platform, output artifact and provenance/deployment.

Current Dart/pub primary documentation establishes that application packages should commit `pubspec.lock`; `pub get` normally respects locked versions when possible; `pub upgrade` intentionally re-resolves; and `pub get --enforce-lockfile` can fail when the lock is invalid or hosted-package content hashes differ.

Python 3.13.5/Linux bounded execution modeled an allowed dependency set where the same manifest resolved `1.0.0` before a compatible `1.1.0` existed and `1.1.0` afterward. A recorded lock retained `1.0.0`. Replacing the locked version's bytes while retaining its version label failed an independent SHA-256 digest oracle.

The evidence does not establish Dart pub runtime behavior, malicious-package detection, registry/maintainer security, native package-manager behavior, build reproducibility, CI isolation or product safety. A lockfile stabilizes a resolution boundary; it does not prove dependency safety. Provenance identifies production context; it does not prove functional correctness.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **A001-A003/A005:** change pressure, ownership/dependency, semantic contracts, refactoring/debt boundaries retained.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **D001-D006:** persistence/migration/cache/restore/sync evidence retained.
- **Q001-Q006:** all Quality Foundation topics have professional boundaries; Q004 includes executable generated counterexample/shrinking.
- **S001-S004:** artifact trust/provenance, authority/security, resource measurement, and dependency/build identity now have executable evidence.

## Cross-track handoffs
- **Architecture:** dependency choice creates API/change-pressure/runtime coupling; version labels do not establish semantic compatibility.
- **Mobile:** direct `pub get --enforce-lockfile`, dependency graph and native build dependency transfer remains OPEN until a trustworthy Dart/Flutter/mobile environment exists.
- **Data:** migration/persistence regressions must be bound to exact resolved dependencies/artifact before causal attribution.
- **Quality:** dependency/lock/toolchain changes are test-relevant artifact changes; successful resolution/build is not a correctness oracle.
- **Systems/S005:** release evidence should compose `manifest → resolution → content → build inputs/platform → artifact → provenance/deployment`.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision in those repositories is changed by this bounded Systems block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables were rechecked 2026-09-18 and remain unavailable; Python 3.13.5 is available.

S004 removes the untouched dependency/build Foundation gap at first executable level. Current strongest independent candidates are:
1. `S005` CI/CD, signing, versioning, reproducibility and release evidence — directly composes S001-S004 and closes another high-risk untouched Systems prerequisite;
2. `M003` sandbox/files/permissions/secure storage/platform APIs — high live-mobile/security transfer value, but platform execution limitations remain;
3. `A006` ADR/evidence-preserving decisions — useful governance prerequisite after principal Architecture concepts;
4. `Q004` mutation sensitivity/exhaustive-vs-generated comparison — useful method depth but lower prerequisite urgency than untouched release foundations;
5. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Dart/pub lockfile/content-hash/advisory behavior and GitHub dependency-review capabilities are version/service sensitive.
- SLSA 1.2 is the current specification family checked 2026-09-18; recheck for release-governance work.
- Android/iOS/Flutter/browser build, signing and dependency tooling are platform/version sensitive.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
