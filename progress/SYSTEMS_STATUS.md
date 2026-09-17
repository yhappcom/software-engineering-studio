# Systems Specialist Status

Track: Systems, Security, Performance & Delivery  
Prefix: `S###`  
State: **Stage 1 — IN STUDY / NOT YET PASSED**  
Last sync: 2026-09-18

## Current evidence

### S001 — Trust boundaries, artifact identity and build provenance foundations
**IN STUDY — two integrated executable trust-boundary blocks complete.** Canonical: `research/systems/S001_trust_artifact_provenance_foundations.md`. Source/build/artifact/deployment/runtime identity plus integrity/authenticity/authorization/provenance separation established. Public-key/key lifecycle, CI trust boundary and mobile signing remain OPEN.

### S002 — Threat modeling, least privilege, secrets and secure storage
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S002_threat_model_least_privilege_secrets_secure_storage.md`. Principal × resource × operation × context/lifetime authority scoping, ambient-authority failure/scoped-capability alternative, secrets lifecycle and Android Keystore guarantee limits established. Real platform/product transfer OPEN.

### S003 — CPU, memory, I/O, network cost models and profiling
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S003_resource_cost_models_profiling_foundations.md`. Wall latency/CPU/allocation/I/O/network observables separated; bounded Python CPU-vs-wait-vs-allocation fixture complete. Variance, profiler alternatives, real I/O/network and Dart/Flutter/device transfer OPEN.

### S004 — Dependency, supply-chain and build-system fundamentals
**IN STUDY — first integrated executable Foundation block complete.** Canonical: `research/systems/S004_dependency_supply_chain_build_system_foundations.md`. Manifest/resolved graph/content/toolchain/build/artifact/provenance identities separated; bounded resolution-drift and same-version integrity failure evidence complete. Direct Dart/pub/build transfer OPEN.

### S005 — CI/CD, signing, versioning, reproducibility and release evidence
**IN STUDY — first integrated executable Foundation block complete.**  
Canonical: `research/systems/S005_ci_signing_versioning_release_evidence.md`  
Fixture: `research/systems/fixtures/S005_release_identity_gate.py`

Established:
- CI verdict, version label, source identity, artifact digest, signature/attestation, verification policy and deployment identity are separate claims;
- current GitHub artifact-attestation docs expose cryptographically signed provenance claims including repository/commit/workflow/environment context and explicitly warn that attestations do not guarantee artifact security;
- SemVer communicates a public-API change contract when adopted; it is not artifact identity and released contents must not be silently replaced under the same version;
- Python 3.13.5/Linux bounded execution accepted the intended `source=abc123/build=42/digest` tuple while rejecting a stale-source artifact with the same build label and changed bytes under the same source/build labels;
- signature/attestation presence, green CI and version matching are not release correctness or authorization by themselves;
- reproducible-build, real CI/OIDC/attestation, key lifecycle, mobile signing/store delivery and deployment evidence remain OPEN.

## Queue
- `S001` — IN STUDY; public-key/key lifecycle/CI/mobile signing OPEN.
- `S002` — IN STUDY; real platform/product threat/secure-storage transfer OPEN.
- `S003` — IN STUDY; variance/profiler/real I/O-network/runtime transfer OPEN.
- `S004` — IN STUDY; Dart/pub, malicious dependency, native package managers, build scripts/cache/reproducibility OPEN.
- `S005` — **IN STUDY / first executable release-identity block complete**; real CI/signing/attestation/reproducibility/mobile deployment OPEN.
- `S006` — Rollback, incident evidence, production change safety and release governance.

## Gate assessment
Systems Stage 1 remains **NOT PASS**. S001-S005 now cover trust/provenance, authority/security, resource measurement, dependency/build identity and first release-evidence composition with bounded executable evidence. Direct Dart/mobile/build-pipeline transfer plus real signing/attestation/reproducibility and rollback/production evidence remain open.

## HANDOFFS
- **Foundations:** release/build execution remains an external process/artifact boundary; comparison-runtime evidence does not transfer to Dart/Flutter.
- **Architecture:** A003 compatibility contracts determine version semantics; a version label is not proof of semantic compatibility.
- **Mobile:** transfer-test canonical Flutter build → package signing → artifact digest/package identity → install/delivery on exact Android/iOS toolchains.
- **Data:** bind migration/recovery evidence to the exact accepted release artifact before causal attribution.
- **Quality:** test evidence must remain attached to the tested artifact/digest or a proven-equivalent build; green CI does not authorize a later rebuild automatically.
- **S006:** rollback should select a previously accepted artifact/provenance record rather than assume rebuilding an old source/version recreates the same artifact.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there is changed by this bounded release mechanism block.

## CHANGE WATCH / OPEN
- Direct Dart/Flutter execution remains unavailable as rechecked 2026-09-18; Python 3.13.5 is available.
- GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive.
- SLSA 1.2 is current as checked 2026-09-18.
- Product/mobile versioning schemes may not use SemVer; do not impose it without a declared public-API/version contract.
- Real CI/OIDC/workflow permissions, key compromise/revocation, Android/iOS signing, app-store delivery, reproducible-build comparison and deployment rollback remain OPEN.

## Next work
Return to Balance Loop. S005 removes the untouched CI/signing/versioning/release-evidence Foundation gap at first executable level. Strong next candidates are `S006` rollback/incident/change safety because it completes the Systems Stage-1 delivery chain, `M003` sandbox/files/permissions/secure storage for high mobile/security leverage, and `A006` ADR/evidence-preserving decisions. Direct Dart/Flutter/mobile execution remains first-attempt work whenever a trustworthy SDK/device environment becomes available.
