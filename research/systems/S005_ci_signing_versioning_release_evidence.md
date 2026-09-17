# S005 — CI/CD, Signing, Versioning, Reproducibility & Release Evidence

Status: **IN STUDY — first integrated executable Foundation block complete**  
Evidence date: 2026-09-18

## Problem / scope
A green CI run, a version label, a signature, and a deployed artifact are different claims. Release acceptance needs an evidence chain that binds the intended source and build process to the exact bytes accepted for deployment.

## SOURCE

### GitHub artifact attestations
Current GitHub documentation states that artifact attestations create cryptographically signed claims about build provenance and can include repository, environment, commit SHA, triggering event and workflow linkage. GitHub explicitly warns that an attestation is not a guarantee that an artifact is secure; verification and policy evaluation are required.

Primary sources:
- https://docs.github.com/en/actions/concepts/security/artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations

### SLSA
SLSA 1.2 treats provenance as verifiable information describing where, when and how an artifact was produced; stronger build levels strengthen provenance authenticity and build-platform integrity. Provenance does not establish application correctness.

Primary source:
- https://slsa.dev/spec/v1.2/build-provenance

### Semantic Versioning
SemVer 2.0.0 requires a declared public API for semantic-version claims and states that released version contents must not be modified. Build metadata does not affect version precedence. Versioning therefore communicates an API/change contract; it is not artifact identity or proof of byte equality.

Primary source:
- https://semver.org/spec/v2.0.0.html

## SYNTHESIS — release evidence chain
Use separate identities and verdicts:

`intended source/ref → resolved dependencies/toolchain → CI workflow/run → build output bytes/digest → signing/attestation subject → verification policy → release/version record → deployment target → runtime acceptance`

Invalid shortcuts:
- `CI green => releasable`;
- `version label matches => artifact bytes match`;
- `signature verifies => source/ref is intended`;
- `attestation exists => artifact is secure/correct`;
- `same source => reproducible bytes`;
- `deployed successfully => intended artifact was deployed`.

Signing authenticates a statement/object under a trust/key policy. It does not decide whether the signed object is the object the release intended. Version labels identify release semantics only under their declared versioning contract. Reproducibility is a separate property requiring controlled inputs and repeated build comparison.

## VALIDATION — bounded release identity gate
Canonical fixture: `research/systems/fixtures/S005_release_identity_gate.py`

### Test Evidence Contract
- **CLAIM:** release acceptance that checks only a build number or payload presence can accept the wrong source or changed bytes; binding source identity, build identity and artifact digest rejects those bounded substitutions.
- **SPEC/PROPERTY:** accepted artifact must simultaneously match expected source, expected build identity and expected digest.
- **TARGET:** deterministic Python release-gate model, not GitHub Actions, Flutter signing or an app-store pipeline.
- **INPUT/STATE:** intended `source=abc123`, `build=42`, known payload digest; variants preserve build number while substituting either source identity or payload bytes.
- **ORACLE:** direct equality of independently supplied expected source/build plus SHA-256 digest of artifact bytes.
- **ENVIRONMENT:** Python 3.13.5, Linux 6.18.44 x86_64, 2026-09-18.
- **OBSERVATION:** intended artifact accepted; stale-source artifact rejected; same-source/build but changed bytes rejected.
- **VERDICT:** PASS for the bounded identity property.
- **FAILURE MODEL:** stale/wrong-source release and post-build/rebuild byte substitution under a reused build label.
- **REPRODUCTION:** run canonical fixture with Python 3.13.5.
- **EVIDENCE LIMIT:** no real signature, key custody, GitHub Actions runner, OIDC, attestation verification, app signing, reproducible build, deployment or store evidence.

Observed output:
```text
good= True
stale_source= False
rebuilt_bytes= False
PASS: release acceptance binds source, build identity and artifact bytes
```

## DEBUG / ROOT CAUSE
The two mutants exploit identity collapse. In one, the build number is retained while the source changes; in the other, source/build labels are retained while bytes change. A release gate that treats any one label as the whole artifact identity cannot distinguish these states. The bounded alternative keeps the identities independent and requires all declared predicates.

## ALTERNATIVES / trade-offs
- **Green CI only:** useful test evidence, but not release/artifact identity.
- **Version/build label only:** human/product release identity; insufficient for byte identity.
- **Digest only:** strong byte identity for a known artifact; does not explain source/build provenance or authorization.
- **Signature only:** authenticity/integrity relative to key/trust policy; a correctly signed wrong artifact remains possible if release selection is wrong.
- **Attestation + verification policy:** binds richer provenance claims and permits policy enforcement; still requires correctness/security tests and trustworthy workflow/platform assumptions.
- **Reproducible build comparison:** can strengthen source/input→byte confidence; requires controlled toolchain/environment and is not demonstrated here.

## ENGINEERING JUDGMENT
A release pipeline should produce evidence, not merely execute commands. The acceptance record should make it possible to answer which source/ref, resolved inputs/toolchain, workflow/run and exact artifact were approved, how authenticity/provenance were verified, what tests applied to that artifact, and what deployment target received it. A release version should not substitute for these identities.

## RELATED DOMAIN CHECK
- **Foundations:** F001 execution/artifact boundaries and F006 external process/network boundaries support pipeline reasoning; direct Dart/Flutter execution remains unavailable.
- **Architecture:** A003 compatibility contracts determine what a version change means; A005 observer sets include release-visible behavior.
- **Mobile:** Android/iOS signing, package identity, store delivery and Flutter build transfer remain OPEN.
- **Data:** migration/recovery evidence must bind the exact release artifact and schema behavior.
- **Quality:** green tests are evidence for their declared oracle/target, not authorization to release a different artifact.
- **Systems:** S001 provenance/trust and S004 dependency/build identity are direct prerequisites.
- **Design Studio / Web Manager / Marketing Manager:** considered; this bounded release mechanism does not change their canonical decisions.
- **Product source/ref:** no product audit required; no MintTap/LogMate production claim is made.

## HANDOFFS
### TO Quality
Bind release-test evidence to the exact artifact/digest or proven-equivalent build path. A later rebuild under the same source/version label is a new artifact unless equivalence is established.

### TO Mobile
When a trustworthy Flutter/mobile environment is available, transfer-test source/ref→canonical build→package signing→artifact digest→installable package identity on exact Android/iOS toolchains.

### TO Systems S006
Rollback/release governance should preserve the accepted artifact identity and provenance so rollback means selecting a previously validated artifact, not rebuilding an old source label by default.

## OPEN / VALIDATION / CHANGE WATCH
- **OPEN / VALIDATION:** direct GitHub Actions attestation generation/verification, OIDC/workflow permission boundaries, key compromise/revocation, mobile signing, store delivery, reproducible-build comparison and deployment rollback.
- **OPEN:** distinguish build reproducibility from hermeticity and deterministic outputs with executable multi-build evidence.
- **CHANGE WATCH:** GitHub artifact-attestation availability/permissions and Sigstore behavior are service-sensitive; recheck before operational adoption.
- **CHANGE WATCH:** SLSA 1.2 is current as checked 2026-09-18.
- **CHANGE WATCH:** product/mobile versioning schemes may not be SemVer; do not impose SemVer unless the product declares that contract.

## Gate effect
S005 now has SOURCE → MODEL → EXECUTABLE FAILURE/ALTERNATIVE evidence at a bounded comparison-runtime level. Systems Stage 1 remains **NOT PASS** because real CI/signing/attestation/mobile/reproducibility/deployment evidence and S006 rollback/incident governance remain open.
