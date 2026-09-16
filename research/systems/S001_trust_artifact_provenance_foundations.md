# S001 — Trust Boundaries, Artifact Identity & Build Provenance Foundations

Status: **IN STUDY — first integrated source/model + executable artifact-identity failure evidence**  
Date: 2026-09-16  
Lead: Systems

## Problem
A source commit, a build invocation, a produced artifact, and a deployed/running artifact are related but not identical objects. Security and release reasoning fails when trust is granted merely because two artifacts claim the same source ref, or when user-controlled build metadata is treated as self-authenticating evidence.

## SOURCE
### NIST SP 800-207 — Zero Trust Architecture
NIST states that zero trust grants no implicit trust solely from network location or asset ownership and focuses protection on resources rather than network segments. S001 transfers the underlying trust-boundary discipline cautiously: identity/location/ownership metadata is an input to authorization or verification, not proof by itself.

Primary: https://csrc.nist.gov/pubs/sp/800/207/final

### NIST SP 800-218 — Secure Software Development Framework 1.1
The final SSDF provides secure-development practices intended to reduce released vulnerabilities and address software supply-chain risk. NIST currently also lists SP 800-218 Rev.1 / SSDF 1.2 as a 2025 public draft, so 1.1 remains the final baseline checked for this study.

Primary: https://csrc.nist.gov/pubs/sp/800/218/final

### SLSA v1.2 — Provenance
Current SLSA v1.2 defines provenance as verifiable information describing where, when, and how an artifact was produced. Build provenance links output artifacts back to source/build inputs. SLSA explicitly distinguishes builder identity, build definition/parameters, resolved dependencies, and artifact subjects/digests; the trusted builder is part of the trust base.

Primary: https://slsa.dev/spec/v1.2/provenance

## SYNTHESIS
A release claim should preserve a chain such as:

`source ref → build definition/parameters → resolved dependencies/toolchain → builder/trust boundary → post-build transforms → artifact digest/identity → deployment target → runtime observation`

The exact fields depend on risk and platform. The chain is not a demand for SLSA adoption in every yhappcom project; it is a reasoning model for avoiding identity collapse.

### Distinctions
- **source identity**: which revision was intended as input;
- **build identity**: which build definition, parameters, dependencies, environment/builder produced output;
- **artifact identity**: the actual output bytes, preferably bound by a cryptographic digest where practical;
- **deployment identity**: which artifact was placed at which origin/store/device/environment;
- **runtime evidence**: what that deployed artifact actually did in a specified environment.

A source ref does not uniquely identify an artifact when build flags, dependencies, generated assets, environment, or post-build transforms can change bytes/behavior.

## VALIDATION — source ref alone is a weak artifact oracle
Fixture: `research/systems/fixtures/S001_artifact_identity.py`

### Test Evidence Contract
- **CLAIM:** equal declared source ref is insufficient to establish artifact equality when a post-build transform can change output bytes.
- **SPEC/PROPERTY:** accepted artifact identity for this bounded test is the SHA-256 digest of the expected canonical artifact bytes.
- **TARGET:** canonical output versus the same output after a deterministic post-build transform.
- **INPUT/STATE:** identical declared source ref `abc123`; one artifact receives `POST_BUILD_PATCH=offline` after canonical construction.
- **ORACLE:** independently hash observed bytes and compare to the expected canonical digest.
- **ENVIRONMENT:** Python 3.13.5; Linux 6.18.44 x86_64; glibc 2.41.
- **OBSERVATION:** both artifacts passed the weak `source_ref == abc123` check. Canonical SHA-256 was `f8acaec1d75f06db55d7804ce24007d6829ab5cd1a3ab97af1cd89860fa74743`; transformed SHA-256 was `fb59fee4330f9c46628166ab7bb00896d5e8bd073b4b6b90bbb22fd7fbfe2aa8`.
- **VERDICT:** weak source-ref verifier accepted two byte-distinct artifacts; digest comparison distinguished them.
- **FAILURE MODEL:** source-equivalent but artifact-distinct build/post-build path.
- **REPRODUCTION DATA:** fixture is deterministic and contains complete bytes and source ref.
- **EVIDENCE LIMIT:** does not establish cryptographic authenticity, signed provenance, reproducible builds, Flutter build behavior, malicious-build resistance, or production release integrity. SHA-256 equality here is an artifact-byte identity check, not proof that the artifact is safe or correctly built.

## FAILURE / ROOT CAUSE
The deliberate weak verifier collapses two identities: it assumes `same source ref ⇒ same artifact`. That implication is false in the fixture because an allowed transformation occurs after the source identity is fixed. The failure is therefore not a hash failure; it is an incomplete verification model.

## CONTRADICTION
Shortcut falsified:

`same source ref = same validated artifact`

A source ref is provenance input, not sufficient artifact identity.

## ENGINEERING JUDGMENT
Artifact hashes improve identity precision but do not establish provenance authenticity by themselves. If the same untrusted actor can alter both artifact and expected hash/metadata, comparison may be internally consistent while proving little. Higher-risk delivery chains therefore need a trustworthy provenance/signing/control-plane model proportionate to the threat model; SLSA explicitly models the builder as part of the trust base.

## CROSS-REPOSITORY TRANSFER
### Web Manager
`yhappcom/web-manager/STATUS.md`, checked 2026-09-16, already records the operational guard `same source ref ≠ same accepted PWA artifact when build/post-build/origin differs` and leaves production/device acceptance OPEN. S001 supplies reusable engineering evidence for that guard without taking ownership of web operations.

Classification: **TRANSFER VALIDATION** — the Web Manager operational concern survives a language-independent executable artifact-identity fixture.

No Web Manager canonical file was edited.

### Design Studio / Marketing Manager
Not materially relevant to this bounded artifact-identity mechanism. Design semantics and marketing measurement do not determine artifact provenance.

### Product repositories
No MintTap or LogMate implementation claim was required for this generic first block. No product repository was audited; production refs remain unknown for this study.

## RELATED DOMAIN CHECK
- **Foundations:** F001 separates source/runtime/process layers; S001 adds build/artifact/deployment identity and must not collapse them.
- **Architecture:** A001-A003 show semantic boundaries/contracts; artifact provenance is orthogonal and can invalidate runtime evidence even when source architecture is unchanged.
- **Mobile:** M001 remains untouched; Android/iOS/Flutter packaging/signing/runtime transfer is OPEN.
- **Data:** persisted data migrations/backups need artifact/version identity when recovery depends on release version.
- **Quality:** Q001 Test Evidence Contract directly used; executable evidence must identify the target artifact/environment.
- **Systems:** owning track.
- **Web Manager:** exact current status checked; finding transfer-validates its artifact-provenance guard.

## HANDOFFS
- **TO Mobile:** future Flutter/device validation should record source ref, canonical build target/command, toolchain/dependency lock, post-build transforms, artifact identity, install/deploy target, build mode and device/OS.
- **TO Quality:** release/e2e evidence should reject source-ref-only target identity when materially different artifacts can be produced.
- **TO Data:** migration/rollback evidence should bind results to the exact application/schema artifact/version under test.
- **TO Web Manager:** existing PWA provenance guard is supported by reusable S001 executable evidence; browser/origin/service-worker acceptance remains web/product-specific.

## OPEN / VALIDATION
- distinguish integrity, authenticity, authorization and provenance with executable signed/unsigned metadata examples;
- least-privilege/trust-boundary failure case beyond artifact identity;
- build dependency/toolchain identity and reproducibility versus provenance;
- mobile signing/package/store delivery chain transfer;
- CI/CD trust boundaries, secret exposure and builder isolation;
- resource boundaries and measurement fundamentals remain separate S001/S003 work.

## CHANGE WATCH
- SLSA current version checked as v1.2 on 2026-09-16; recheck before operational adoption.
- NIST lists SSDF 1.2 as a public draft while SSDF 1.1 remains final; recheck final status before policy adoption.

## Current conclusion
The first Systems Foundation rule is: **validation attaches to a concrete artifact and environment, not to source code in the abstract.** Source revision is necessary provenance, but artifact identity, build path, trust base, deployment context and runtime observation are separate claims. Trust should be earned by evidence appropriate to the resource and threat model, not inherited from location, ownership, naming, or source-ref equality alone.
