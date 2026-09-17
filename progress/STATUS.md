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
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks + S002 first executable least-privilege/security block complete |

No specialist has passed Foundation.

## Meaningful new evidence

### S002 — threat modeling, least privilege, secrets and secure storage
Canonical: `research/systems/S002_threat_model_least_privilege_secrets_secure_storage.md`  
Fixture: `research/systems/fixtures/S002_least_privilege_capability_boundary.py`

Systems' largest untouched security Foundation gap now has first executable evidence. Current NIST AC-6 evidence grounds least privilege in only the authority needed by users/processes for assigned tasks. NIST SP 800-154 is explicitly treated as an Initial Public Draft with a 2025 plan-to-finalize note, not final normative authority. Current Android Keystore documentation establishes key-material extraction/use restrictions when applicable, while also preserving the important limit that a compromised authorized app process may still be able to use a non-exportable key.

Python 3.13.5/Linux execution compared ambient read authority with a resource-scoped capability. The intentionally overprivileged component read unrelated `tax` state; the scoped capability rejected that access while preserving the declared `profile` operation. This is bounded authority-model evidence, not Android/iOS/Flutter/product security evidence.

The reusable security reasoning chain is now: `asset/security property → principal → entry/data flow → trust boundary → authority → threat/failure → control → residual risk → validation`. Secrets are modeled across purpose, authority, storage, exposure, lifetime, rotation/revocation, logging and compromise response rather than as merely encrypted values.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **A001-A003/A005:** change pressure, ownership/dependency, semantic contracts, refactoring/debt boundaries retained.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **D001-D006:** persistence/migration/cache/restore/sync evidence retained.
- **Q001-Q006:** all Quality Foundation topics have professional boundaries; Q004 includes executable generated counterexample/shrinking.
- **S001/S002:** artifact trust/provenance plus runtime authority/threat/secrets first executable boundaries.

## Cross-track handoffs
- **Mobile/M003:** validate sandbox, permission, Keystore/Keychain and key invalidation with exact platform evidence; secure-storage API presence is not a complete security claim.
- **Architecture:** security-relevant interfaces should minimize authority width as part of ownership/dependency design.
- **Quality:** recovery/fault campaigns should include overprivilege, revocation and expired-secret paths with independent authorization oracles.
- **Data:** classify sensitive assets and required authority before accepting backup/sync/export paths.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision in those repositories is changed by this bounded Systems block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables were rechecked 2026-09-18 and remain unavailable; Python 3.13.5 is available.

S002 removes the largest untouched security Foundation gap at first executable level. Current strongest independent candidates are:
1. `S003` CPU/memory/I/O/network cost models and profiling — untouched, high cross-track/performance leverage;
2. `M003` sandbox/files/permissions/secure storage/platform APIs — high live-mobile/security transfer value, but platform execution limitations remain;
3. `S004` dependency/supply-chain/build-system fundamentals — untouched release/security prerequisite;
4. `A006` ADR/evidence-preserving decisions — useful governance prerequisite after principal Architecture concepts;
5. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.
- Android Keystore/attestation guarantees are API/device/version sensitive.
- ISO/IEC/IEEE 42010:2022 remains current from prior check; DIS 42024 remains draft work.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.