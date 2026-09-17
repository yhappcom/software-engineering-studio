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
| Systems | Stage 1 IN STUDY — S001 two + S002-S006 first executable/professional blocks; all S001-S006 now initiated with evidence |

No specialist has passed Foundation.

## Meaningful new evidence

### S006 — Rollback, incident evidence, production change safety and release governance
Canonical: `research/systems/S006_rollback_incident_change_safety_governance.md`  
Fixture: `research/systems/fixtures/S006_rollback_state_compatibility.py`

Systems' last untouched Stage-1 block now has first executable evidence. The model treats deployed state as a vector across artifact, configuration, durable data/schema, infrastructure, routing, external dependencies and control state rather than treating rollback as the inverse of deployment.

Current Google SRE canary guidance supports staged/time-limited exposure with evaluation before wider rollout and rollback/pause when a candidate is bad. Current AWS CodeDeploy documentation explicitly states that rollback redeploys a previous revision as a new deployment rather than restoring an old deployment event, reinforcing the distinction between selecting an old revision and restoring whole-system state.

Python 3.13.5/Linux bounded execution modeled a v1 artifact supporting schema 1 and a faulty v2 that had already advanced durable state to schema 2. Binary-only rollback to v1 failed against current state. A separately modeled compatible schema-1 restore allowed the exact old artifact to satisfy the recovery oracle. This demonstrates the bounded failure of assuming `previously known-good artifact => safe against current state`.

The evidence does not establish safe database reversal, snapshot consistency, data-loss acceptability, real deployment rollback, mobile/store downgrade, distributed recovery or production incident behavior.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **A001-A003/A005:** change pressure, ownership/dependency, semantic contracts, refactoring/debt boundaries retained.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **D001-D006:** persistence/migration/cache/restore/sync evidence retained.
- **Q001-Q006:** all Quality Foundation topics have professional boundaries; Q004 includes executable generated counterexample/shrinking.
- **S001-S006:** trust/provenance, authority/security, resource measurement, dependency/build identity, release evidence and rollback/change-safety now all have first professional evidence.

## Cross-track handoffs
- **Architecture:** rollback safety consumes A003 compatibility contracts; old artifact identity alone does not establish current-state compatibility.
- **Mobile:** canonical Flutter build/sign/install/update/downgrade/store transfer remains OPEN until a trustworthy mobile toolchain/platform exists.
- **Data:** D003/D005 schema compatibility and restore acceptance are prerequisites to stateful rollback readiness; data reversal must not be assumed.
- **Quality:** post-rollback acceptance requires independent semantic/data-integrity oracles, not deployment-command success or process liveness.
- **Systems:** preserve exact previously accepted artifact identity from S005 and evaluate current configuration/data/external-state compatibility before using it as a rollback target.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision in those repositories is changed by this bounded Systems block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables were rechecked 2026-09-18 and remain unavailable; Python 3.13.5 is available.

S006 removes the final untouched Systems Stage-1 block at first professional/executable level. Current strongest independent candidates are:
1. `M003` sandbox/files/permissions/secure storage/platform APIs — strongest live mobile/security gap, though real platform execution remains constrained;
2. `A006` ADR/evidence-preserving decisions — closes a remaining Architecture professional boundary with broad governance/release leverage;
3. `Q004` deliberate mutation sensitivity plus exhaustive-vs-generated comparison — deepens test-method evidence;
4. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- Deployment-platform rollback semantics and app-store/browser delivery policies are service/version sensitive.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- SLSA 1.2 is current as checked 2026-09-18.
- Product/mobile versioning schemes may not use SemVer; do not impose SemVer without a declared contract.
- Dart/pub lockfile/content-hash/advisory behavior and Android/iOS/Flutter signing/build tooling are version sensitive.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
