# S004 — Dependency, Supply-Chain & Build-System Foundations

Status: **IN STUDY — first integrated executable Foundation block complete**  
Evidence date: 2026-09-18

## Problem / scope

A source ref does not uniquely determine a runnable artifact unless dependency resolution, build inputs, toolchain/build platform and post-build steps are also controlled or recorded. This block separates dependency constraints, resolved dependency identity, integrity, vulnerability knowledge, build provenance and artifact identity.

## SOURCE

### Dart/pub
Current Dart documentation establishes:
- `dart pub get` resolves direct and transitive dependencies and writes `pubspec.lock`;
- application packages should commit `pubspec.lock` so developers/deployment use the same resolved versions;
- `dart pub upgrade` intentionally ignores the existing lockfile when selecting newer compatible versions;
- `dart pub get --enforce-lockfile` fails if the lockfile is not a valid exact resolution or hosted-package content hashes changed;
- `dart pub deps` exposes the direct/transitive dependency graph;
- pub surfaces known security advisories during dependency resolution.

Primary sources:
- https://dart.dev/tools/pub/cmd/pub-get
- https://dart.dev/tools/pub/cmd/pub-upgrade
- https://dart.dev/tools/pub/dependencies
- https://dart.dev/tools/pub/security-advisories

### SLSA
SLSA 1.2 distinguishes build inputs/dependencies, build platform, output artifact and provenance. Build provenance records how an artifact was produced; stronger build levels add provenance authenticity and build-platform hardening. Provenance is evidence about production of an artifact, not proof that the source/dependencies are non-malicious or functionally correct.

Primary sources:
- https://slsa.dev/spec/v1.2/build-track-basics
- https://slsa.dev/spec/v1.2/terminology

### GitHub dependency review
GitHub dependency review compares dependency changes between revisions and can surface newly introduced vulnerable dependencies. This is vulnerability/policy evidence, not a complete supply-chain correctness oracle.

Primary source:
- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review

## SYNTHESIS — dependency/build identity model

Use these separate identities:

`manifest constraints → resolved dependency graph → dependency content/integrity → toolchain/build inputs → build execution/platform → output artifact → provenance/deployment`

A version constraint expresses an allowed set. A lockfile records one resolution. A content digest can detect content mismatch for the recorded object. A vulnerability database adds known-risk knowledge. Build provenance connects an output to recorded build inputs/platform. None of these alone proves the others.

Invalid shortcuts:
- `same pubspec.yaml => same dependency graph`;
- `same version string => same bytes`;
- `lockfile present => dependency is safe`;
- `no known advisory => dependency is secure`;
- `build succeeded => artifact is trustworthy/correct`;
- `same source commit => validation-equivalent artifact`;
- `provenance exists => artifact behavior is correct`.

## VALIDATION — bounded executable dependency-resolution/integrity fixture

Canonical fixture: `research/systems/fixtures/S004_dependency_resolution_integrity.py`

### Test Evidence Contract
- **CLAIM:** an allowed version range can resolve differently as the available registry changes; recording a resolution stabilizes this bounded dependency identity; checking recorded content digest detects same-version byte substitution.
- **SPEC/PROPERTY:** unlocked resolution may choose another compatible version; locked resolution must preserve the recorded version in this model; content accepted for a locked version must match its recorded digest.
- **TARGET:** deterministic Python dependency-resolution/integrity model, not Dart pub.
- **INPUT/STATE:** registry A exposes only `1.0.0`; later registry B exposes compatible `1.0.0` and `1.1.0`; lock records `1.0.0` and its SHA-256; tampered bytes retain the `1.0.0` label.
- **ORACLE:** explicit version equality assertions plus independent `hashlib.sha256` comparison.
- **ENVIRONMENT:** Python 3.13.5, Linux, 2026-09-18.
- **OBSERVATION:** manifest-only resolution changed `1.0.0 → 1.1.0`; locked resolution remained `1.0.0`; tampered same-version bytes failed the digest comparison.
- **VERDICT:** PASS for the bounded model.
- **FAILURE MODEL:** dependency drift from unresolved compatible versions and same-version content substitution.
- **REPRODUCTION:** run the canonical fixture with Python 3.13.5.
- **EVIDENCE LIMIT:** this is not Dart pub execution, package-signature verification, registry compromise testing, transitive resolver completeness, malicious-package detection, reproducible-build proof, CI isolation, or product evidence.

Observed output:
```text
manifest_only_A= 1.0.0
manifest_only_B= 1.1.0
locked_B= 1.0.0
tampered_integrity_ok= False
PASS: lock stabilizes this resolution; content hash detects same-version content change
```

## DEBUG / ROOT CAUSE

The drift is not caused by nondeterministic arithmetic in the fixture. The manifest deliberately denotes a set of acceptable versions, while the available candidate set changed between resolution events. The lock converts that open choice into a recorded concrete resolution for this model. The integrity failure is separate: the version identity stayed fixed while bytes changed, and the digest oracle exposed the mismatch.

## ALTERNATIVES / trade-offs

- **Manifest constraints only:** flexible resolution; useful for reusable packages, but insufficient to identify one application build dependency graph.
- **Committed application lockfile:** stronger resolution repeatability and explicit transitive diffs; does not establish safety, provenance or full build reproducibility.
- **Lockfile + integrity enforcement:** additionally detects mismatched recorded package contents where the ecosystem provides content hashes; still does not detect malicious-but-authentic packages.
- **Dependency review/advisory scanning:** adds known-vulnerability/policy evidence; coverage is limited by inventory and advisory knowledge.
- **Build provenance:** adds source/build-input/platform/output traceability; correctness and benign dependency behavior remain separate claims.

## ENGINEERING JUDGMENT

For application repositories, dependency change should be treated as code/build change even when application source files are untouched. Review should include direct and transitive resolution changes, integrity/provenance evidence where available, and tests appropriate to the affected behavior. A lockfile is necessary evidence for many application build paths but is not sufficient evidence for artifact reproducibility or supply-chain security.

## RELATED DOMAIN CHECK

- **Foundations:** F003 supports graph/complexity vocabulary; F006 reinforces that external retrieval is an OS/network boundary.
- **Architecture:** dependency choice can create runtime/API/change-pressure coupling; A003 semantic compatibility remains independent of version numbering.
- **Mobile:** Flutter/Dart applications depend on pub resolution plus Android/iOS native/build-tool dependencies; real toolchain transfer remains OPEN.
- **Data:** dependency/toolchain upgrades can change persistence/migration behavior; exact artifact identity is required before attributing data failures.
- **Quality:** dependency/build changes require exact artifact/environment binding and regression oracles; successful resolution/build is not correctness evidence.
- **Systems:** S001 artifact/provenance identity and S002 trust/security boundaries directly support this block; S005 should later operationalize CI/signing/release enforcement.
- **Design Studio:** not materially relevant to this bounded mechanism block.
- **Web Manager:** future PWA/build/deployment dependency governance is a transfer candidate, but no Web Manager canonical decision is changed here.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no product implementation audit was required for this reusable mechanism block; no MintTap/LogMate behavior claim is made.

## HANDOFFS

### TO Quality
Treat dependency/lock/build-tool changes as test-relevant artifact changes. Preserve exact resolved graph/toolchain/artifact identity in release evidence where risk warrants it.

### TO Mobile
When a trustworthy Dart/Flutter environment exists, transfer-test `pub get --enforce-lockfile`, direct/transitive graph inspection and build behavior using an exact Flutter application fixture. Do not infer Dart behavior from the Python model.

### TO Systems S005
Use this identity chain as a prerequisite for CI/CD/release evidence: manifest is not resolved graph; resolved graph is not artifact; artifact is not provenance/deployment.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN / VALIDATION:** direct Dart `pub get`, `pub upgrade`, `pub deps`, `--enforce-lockfile` execution; current environment has no `dart`/`flutter` executable.
- **OPEN:** malicious-but-authentic dependency, compromised registry/maintainer, git/path dependencies, native Gradle/CocoaPods/SwiftPM dependency boundaries, build-script execution and cache poisoning.
- **OPEN:** reproducible-build experiment proving byte-identical output under controlled inputs.
- **CHANGE WATCH:** Dart/pub lockfile/content-hash/advisory behavior and GitHub dependency-review capabilities are tool/service-version sensitive.
- **CHANGE WATCH:** SLSA 1.2 is the current specification family checked 2026-09-18; use approved/current pages for operational claims and recheck before release governance work.

## Gate effect

S004 now has SOURCE → MODEL → EXECUTABLE FAILURE/ALTERNATIVE evidence at a bounded comparison-runtime level. Systems Stage 1 remains **NOT PASS** because direct Dart/mobile/build-pipeline transfer, dependency attack cases, signing/release/rollback and production evidence remain open.
