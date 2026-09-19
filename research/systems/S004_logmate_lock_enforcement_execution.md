# S004 — LogMate lock enforcement execution transfer

Date: 2026-09-19
Lead: Systems
Status: VALIDATION IN PROGRESS — exact-ref dependency metadata transferred to exact Flutter release fixture

## Problem / Balance Loop selection

After F006 outer containment was validated, the highest-leverage independent evidence gap is the S004/Mobile/Quality product-release chain: exact toolchain identity → committed-lock enforcement → canonical build → artifact identity. This block advances the first executable product-derived rung without modifying the LogMate repository or pretending Studio execution is the product's canonical release pipeline.

## Product identity

`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-19`.

Production identity is unknown. The default branch is not assumed production.

## SOURCE

Checked 2026-09-19:

- Dart `pub get` documentation: `--enforce-lockfile` fails when the lockfile does not exactly specify a valid resolution of the manifest or when a hosted package content hash changed: https://dart.dev/tools/pub/cmd/pub-get
- Dart glossary: hosted dependency content hashes are stored in the lockfile and `--enforce-lockfile` converts a discrepancy into an error: https://dart.dev/resources/glossary
- Flutter SDK archive: releases expose version, architecture, exact ref, release date, bundled Dart version and provenance; a moving channel label is not an exact toolchain identity: https://docs.flutter.dev/install/archive
- Flutter current release documentation records Flutter 3.47 as released 2026-08-12: https://docs.flutter.dev/release/whats-new

## Product-derived fixture

Canonical fixture directory: `research/systems/fixtures/s004_logmate_lock_enforcement/`.

The fixture copies the dependency-relevant manifest semantics and the complete `pubspec.lock` from the exact LogMate ref above. The product lockfile records exact hosted package versions/content hashes and SDK compatibility ranges (`dart >=3.10.7 <4.0.0`, `flutter >=3.27.0`). The fixture is evidence input, not a LogMate source checkout or application build.

## VALIDATION design

Workflow: `.github/workflows/s004-logmate-lock-enforcement.yml`
Workflow head: `d093377358944937edf9333842f0a8ee46a72b82`
Run: `35443174123`
Job: `105897460229`
Environment requested: GitHub-hosted `ubuntu-latest`; Flutter exact release tag `3.47.0` cloned from `flutter/flutter`.

Claim A: the exact-ref LogMate dependency manifest/lock pair is accepted by pub lock enforcement under the selected exact Flutter release.

Oracle A:
1. `flutter pub get --enforce-lockfile` exits zero;
2. `cmp` confirms the lockfile is not rewritten.

Claim B: a deliberate hosted-package content-hash mutation is rejected fail-closed.

Oracle B:
1. mutate exactly one nibble of the locked `cupertino_icons 1.0.9` SHA-256;
2. `flutter pub get --enforce-lockfile` must exit non-zero;
3. failure output must identify a hash/content/lock condition.

This negative case is required because a green resolution alone would not establish that the enforcement control is sensitive to the integrity failure class it claims to catch.

## Current observation

At the evidence checkpoint, run `35443174123` is `in_progress`. Checkout completed successfully and the exact Flutter-release installation step is running. Toolchain recording, positive lock enforcement and the deliberate hash-mutation negative case have not yet produced verdicts.

**VERDICT:** INCONCLUSIVE / IN PROGRESS. No PASS is awarded.

## SYNTHESIS

The prior static conclusion remains: `manifest constraint != resolved dependency/content identity != exact SDK/toolchain != build artifact`. This workflow adds an executable bridge between the first three identities, but even a successful result will not be a canonical LogMate build because the private product source is not being built in this Studio workflow.

## ENGINEERING JUDGMENT

An exact Flutter release chosen by the Studio is a controlled validation environment, not evidence that LogMate was or should be released with that toolchain. A future canonical product release needs its own declared/pinned toolchain identity before reproducibility/provenance claims are defensible.

## RELATED DOMAIN CHECK

- Foundations: trustworthy hosted Dart/Flutter execution now exists; F001 no longer blocks this bounded transfer.
- Architecture: toolchain/dependency identity is an externally relevant release contract only when release/reproducibility policy makes it so.
- Mobile: exact Flutter release identity matters, but this is dependency resolution rather than Android/iOS/browser runtime evidence.
- Data: no persistence semantics are exercised.
- Quality: deliberate hash mutation provides oracle-sensitivity/failure evidence rather than relying on a green dependency resolution alone.
- Systems: lead track; S004 directly advanced and S005 consumes resulting build/artifact identity later.
- Design Studio: not materially relevant.
- Web Manager: not materially relevant; no web deployment/runtime claim.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref inspected; no product repository files edited.

## HANDOFFS

### Systems → Quality
If the run succeeds, retain the positive lock resolution and deliberate content-hash rejection as separate oracles. Do not relabel either as artifact reproducibility.

### Systems → Mobile / LogMate release engineering
This fixture can show that a selected exact Flutter release can enforce the recorded product lock metadata. It cannot choose the canonical LogMate release toolchain. Product/release tooling must supply that identity before canonical build evidence.

## OPEN / CHANGE WATCH

- Final result of run `35443174123`.
- Exact Flutter git/Dart/engine identity observed by the run.
- Canonical LogMate toolchain identity remains unknown from inspected product repository evidence.
- Canonical LogMate source build, tests, target artifact digest, signing/attestation and independent-host reproducibility remain OPEN.
- Flutter/pub behavior is version-sensitive; preserve exact release/ref for every future verdict.
