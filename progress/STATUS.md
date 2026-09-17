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
| Systems | Stage 1 IN STUDY — S001 two + S002 first + S003 first + S004 first + S005 first executable release-evidence block complete |

No specialist has passed Foundation.

## Meaningful new evidence

### S005 — CI/CD, signing, versioning, reproducibility and release evidence
Canonical: `research/systems/S005_ci_signing_versioning_release_evidence.md`  
Fixture: `research/systems/fixtures/S005_release_identity_gate.py`

Systems' untouched CI/signing/versioning/release-evidence Foundation gap now has first executable evidence. The model separates intended source/ref, resolved inputs/toolchain, CI workflow/run, output bytes/digest, signature/attestation subject, verification policy, release/version record, deployment target and runtime acceptance.

Current GitHub artifact-attestation documentation establishes cryptographically signed provenance claims and explicitly warns that an attestation is not a guarantee that an artifact is secure; verification and policy evaluation remain required. SemVer 2.0.0 establishes public-API version semantics when adopted and forbids silently changing released version contents; it is not artifact identity.

Python 3.13.5/Linux bounded execution accepted the intended `source=abc123`, `build=42`, expected-digest artifact. It rejected a stale-source artifact that retained the same build label and rejected changed bytes that retained the same source/build labels. This demonstrates the bounded failure caused by collapsing source/build/artifact identities.

The evidence does not establish real signing, key custody, GitHub Actions/OIDC behavior, attestation verification, mobile signing/store delivery, reproducible builds, deployment correctness or product safety.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN after environment recheck 2026-09-18.
- **F002-F006:** alias/lifetime, complexity, concurrency, async and network/termination failure mechanics retained.
- **A001-A003/A005:** change pressure, ownership/dependency, semantic contracts, refactoring/debt boundaries retained.
- **M001/M002:** Flutter/platform lifecycle/process/background conceptual boundaries; real runtime transfer OPEN.
- **D001-D006:** persistence/migration/cache/restore/sync evidence retained.
- **Q001-Q006:** all Quality Foundation topics have professional boundaries; Q004 includes executable generated counterexample/shrinking.
- **S001-S005:** artifact trust/provenance, authority/security, resource measurement, dependency/build identity and first release-evidence composition now have executable evidence.

## Cross-track handoffs
- **Architecture:** version semantics depend on declared compatibility contracts; version labels are not artifact or semantic-compatibility proof.
- **Mobile:** canonical Flutter build → signing → artifact digest/package identity → install/store delivery transfer remains OPEN until a trustworthy mobile toolchain exists.
- **Data:** migration/recovery evidence must bind the exact accepted artifact before causal attribution.
- **Quality:** green CI/test evidence attaches to the tested artifact; a later rebuild under the same source/version label is not automatically equivalent.
- **Systems/S006:** rollback should preserve/select previously accepted artifact identity and provenance rather than assume rebuilding old source recreates it.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision in those repositories is changed by this bounded Systems block.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and is not simulated. `dart` and `flutter` executables were rechecked 2026-09-18 and remain unavailable; Python 3.13.5 is available.

S005 removes the untouched CI/signing/versioning/release-evidence Foundation gap at first executable level. Current strongest independent candidates are:
1. `S006` rollback, incident evidence, production change safety and release governance — completes the Systems Stage-1 delivery chain and directly composes S001-S005;
2. `M003` sandbox/files/permissions/secure storage/platform APIs — high live-mobile/security transfer value, but platform execution limitations remain;
3. `A006` ADR/evidence-preserving decisions — useful governance prerequisite after principal Architecture concepts;
4. `Q004` mutation sensitivity/exhaustive-vs-generated comparison — useful method depth but lower prerequisite urgency than untouched release/rollback foundations;
5. return immediately to direct Dart/Flutter/mobile execution when a trustworthy SDK/device environment becomes available.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## CHANGE WATCH
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- SLSA 1.2 is current as checked 2026-09-18.
- Product/mobile versioning schemes may not use SemVer; do not impose SemVer without a declared contract.
- Dart/pub lockfile/content-hash/advisory behavior and Android/iOS/Flutter signing/build tooling are version sensitive.
- NIST SP 800-154 remains draft/planned for finalization; recheck before treating it as final.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
