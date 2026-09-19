# S004 — LogMate lockfile and toolchain identity transfer

Date: 2026-09-19
Lead: Systems
Status: IN STUDY — exact-ref product transfer; build execution OPEN

## Problem

S004 separates manifest intent, resolved dependency graph/content, toolchain identity, build identity, and artifact identity. This block transfer-tests that model against the current inspectable LogMate source without assuming that the default branch is production.

## Product identity

`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-19`.

Production identity is unknown. `main` is not treated as production.

## SOURCE

Current Dart documentation states that application packages should commit `pubspec.lock` so builds use the exact selected package versions. Current production guidance additionally recommends `dart pub get --enforce-lockfile`; that command fails when the lockfile is not an exact valid resolution of the manifest or a hosted package content hash has changed.

Current Dart pubspec documentation states that SDK constraints are version ranges. For Flutter constraints, the Flutter SDK currently enforces only the lower bound. A constraint therefore is not an exact Flutter toolchain identity.

Primary sources checked 2026-09-19:
- https://dart.dev/tools/pub/versioning
- https://dart.dev/tools/pub/packages
- https://dart.dev/tools/pub/pubspec
- https://dart.dev/tools/pub/cmd/pub-get

## Exact-ref observations

At the recorded LogMate ref:

- `pubspec.yaml` declares Dart SDK `^3.10.7` and app version `1.0.0+1`.
- Direct hosted dependencies are expressed as ranges, for example `cloud_functions: ^6.0.0`, `firebase_auth: ^6.6.1`, `firebase_core: ^4.14.0`, `cupertino_icons: ^1.0.8`.
- `pubspec.lock` is committed and records exact resolved hosted package versions and SHA-256 content hashes. Examples include `cloud_functions 6.4.0`, `firebase_auth 6.6.1`, `firebase_core 4.14.0`, `cupertino_icons 1.0.9`.
- The lockfile records SDK compatibility as Dart `>=3.10.7 <4.0.0` and Flutter `>=3.27.0`; it does not identify one exact Flutter SDK release/engine revision.
- Repository search found no `flutter-version` pin and no `fvm` evidence on the inspected default-branch index. `.github/workflows` was absent at the exact ref through the contents API. These negative observations are scoped to the inspected repository/ref/search surface; they do not prove that no external CI or operator-controlled toolchain pin exists.

## SYNTHESIS

The exact-ref product transfer confirms the S004 distinction:

`manifest constraints != resolved package graph/content != exact SDK/toolchain != build artifact`.

The committed lockfile materially strengthens dependency reproducibility because hosted package versions and content hashes are recorded. It does **not** by itself identify the exact Flutter SDK/engine/toolchain used to produce a release artifact.

`cloud_functions ^6.0.0 → locked 6.4.0` and `cupertino_icons ^1.0.8 → locked 1.0.9` are concrete examples of why manifest constraints alone are not resolved dependency identity. This is expected pub behavior, not a defect.

## ENGINEERING JUDGMENT

For a release-evidence chain intended to support reproducibility or provenance, LogMate should eventually bind at least:

`source commit → exact Flutter/Dart SDK identity → pubspec.lock → enforced lock resolution → build command/flags → post-build transforms → artifact digest → signing/attestation → delivered artifact identity`.

This is a reusable release-evidence requirement, not a project change order. The product repository remains authoritative for its release process.

## VALIDATION

No Flutter/Dart executable is available in the current execution environment, so the following were **not** executed and remain OPEN:

- `flutter --version` / exact engine identity;
- `dart pub get --enforce-lockfile` or Flutter equivalent against this ref;
- canonical LogMate build;
- dependency download/content-hash verification;
- two-host reproducibility comparison;
- artifact digest/signing/attestation comparison.

No PASS is awarded from the static audit.

## Failure model / acceptance boundary

A future release gate should reject or explicitly classify at least:

1. lockfile drift relative to `pubspec.yaml`;
2. hosted content-hash mismatch;
3. unrecorded SDK/toolchain drift;
4. canonical build vs ad-hoc build divergence;
5. post-build transform drift;
6. artifact digest mismatch after signing/attestation handoff.

The first two can be exercised with pub's lockfile enforcement when a trustworthy Dart/Flutter environment becomes available. The remaining cases require build/provenance evidence.

## RELATED DOMAIN CHECK

- Foundations: F001 direct Dart/Flutter execution remains the blocking runtime prerequisite.
- Architecture: build/toolchain identity becomes an externally relevant contract when release reproducibility/provenance is required.
- Mobile: exact Flutter SDK/engine and platform build target materially affect runtime/artifact identity.
- Data: migrations/backup compatibility should bind to exact release artifact when used as release gates.
- Quality: future regression oracle must distinguish dependency-lock validation from artifact reproducibility.
- Systems: S001/S004/S005 directly relevant; this note is an S004 product transfer and supplies an input to S005 release provenance.
- Design Studio: not materially relevant to this bounded dependency/toolchain identity audit.
- Web Manager: not materially relevant; no web deployment claim is made.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref inspected as recorded above.

## HANDOFFS

### Systems → Mobile / LogMate release engineering
Finding: committed package lock strengthens package identity, but exact Flutter SDK/engine and canonical build identity remain unbound in the inspected repository evidence.
Action when release tooling is defined: record/pin the exact supported build toolchain and execute lockfile enforcement as part of the canonical build/release evidence chain.
Status: OPEN.

### Systems → Quality
Future reproducibility tests should include a deliberate toolchain-drift negative case in addition to lockfile/content-hash drift; a green dependency resolution is not artifact reproducibility.
Status: OPEN.

## CHANGE WATCH / OPEN

Dart/pub lockfile and Flutter SDK-constraint behavior are tool/version sensitive. Recheck primary documentation and exact product build tooling before release-policy adoption. External CI/toolchain configuration may exist outside the inspected repository and remains unknown.
