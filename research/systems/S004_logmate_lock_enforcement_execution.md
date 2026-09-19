# S004 — LogMate lock enforcement execution transfer

Date: 2026-09-19
Lead: Systems
Status: IN STUDY — first exact-toolchain execution failed positive lock oracle; controlled alternative comparison in progress

## Problem / Balance Loop selection

After F006 outer containment was validated, the highest-leverage independent evidence gap is the S004/Mobile/Quality product-release chain: exact toolchain identity → committed-lock enforcement → canonical build → artifact identity. This block advances the first executable product-derived rung without modifying the LogMate repository or pretending Studio execution is the product's canonical release pipeline.

## Product identity

`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-19`.

Production identity is unknown. The default branch is not assumed production.

## SOURCE

Checked 2026-09-19:
- Dart `pub get`: `--enforce-lockfile` fails when the lockfile does not exactly specify a valid resolution of the manifest or a hosted package content hash changed: https://dart.dev/tools/pub/cmd/pub-get
- Dart glossary: hosted dependency content hashes are recorded in the lockfile and enforcement converts mismatch into failure: https://dart.dev/resources/glossary
- Flutter SDK archive exposes release version, architecture, exact ref, release date, bundled Dart version and provenance: https://docs.flutter.dev/install/archive
- Flutter current release documentation records Flutter 3.47 released 2026-08-12: https://docs.flutter.dev/release/whats-new

## Product-derived fixture

`research/systems/fixtures/s004_logmate_lock_enforcement/` copies the dependency-relevant manifest semantics and complete `pubspec.lock` from the exact LogMate ref. The product lockfile records exact hosted package versions/content hashes and SDK compatibility ranges (`dart >=3.10.7 <4.0.0`, `flutter >=3.27.0`). It is evidence input, not a LogMate source checkout/application build.

## VALIDATION design

Workflow: `.github/workflows/s004-logmate-lock-enforcement.yml`.

Positive oracle: `flutter pub get --enforce-lockfile` exits zero and `cmp` proves the lockfile was not rewritten.

Negative oracle: mutate exactly one nibble of locked `cupertino_icons 1.0.9` SHA-256; enforcement must exit non-zero and output must identify a hash/content/lock condition.

A negative case is mandatory because green dependency resolution alone does not establish control sensitivity to integrity drift.

## First execution — Flutter 3.47.0

Workflow head `d093377358944937edf9333842f0a8ee46a72b82`; run `35443174123`; job `105897460229`.

Observed step evidence:
- checkout: success;
- exact Flutter 3.47.0 install: success;
- toolchain identity recording: success;
- positive LogMate lock enforcement: **failure**;
- deliberate hash-mutation negative case: skipped because the prior step failed;
- overall job: failure, completed 2026-09-19T12:33:41Z.

**VALIDATION:** the copied exact-ref dependency metadata is not accepted by `--enforce-lockfile` under this selected exact Flutter 3.47.0 environment.

**OPEN / ROOT CAUSE:** current GitHub evidence access exposes step verdicts but not command-level stdout/stderr, so the precise incompatibility is not assigned. Possible dependency-resolution/toolchain causes are hypotheses only and are not recorded as root cause.

**EVIDENCE LIMIT:** this is not evidence that the product is broken, because Flutter 3.47.0 is Studio-selected and was never established as LogMate's canonical toolchain.

## ALTERNATIVE comparison

Workflow revision `0426836a14866f00dd9de4811c7083bb1f1c0675` changes the validation into a fail-fast-disabled matrix over exact Flutter `3.38.10` and `3.47.0`. Flutter 3.38.10 is a materially relevant alternative because it satisfies the product lockfile's Dart lower bound via Dart 3.10.x-era tooling while remaining an exact release rather than a moving channel. The comparison is intended to test toolchain sensitivity, not to infer which version the product historically used.

The matrix preserves the positive unchanged-lock oracle and deliberate content-hash mutation negative oracle independently for each exact release. Final matrix verdict is pending.

## SYNTHESIS

The first execution already strengthens the static model: a lockfile that records package versions/hashes plus broad SDK compatibility ranges is not equivalent to demonstrated acceptance under an arbitrary later SDK inside those broad conceptual constraints. Exact toolchain identity remains operationally relevant.

It does **not** yet establish why 3.47.0 rejected the lock, which alternative accepts it, or what LogMate's canonical toolchain should be.

## ENGINEERING JUDGMENT

A Studio-selected exact Flutter release is a controlled validation environment, not release-policy authority. A future canonical product release needs a product-owned declared/pinned toolchain before reproducibility/provenance claims are defensible.

## RELATED DOMAIN CHECK
- Foundations: trustworthy hosted Dart/Flutter execution exists; F001 no longer blocks this bounded transfer.
- Architecture: toolchain/dependency identity becomes an externally relevant release contract when reproducibility/provenance is required.
- Mobile: exact Flutter release identity matters; this is dependency resolution, not Android/iOS/browser runtime evidence.
- Data: no persistence semantics exercised.
- Quality: positive/negative oracles plus exact-version alternative comparison directly relevant.
- Systems: lead track; S004 advanced; S005 consumes build/artifact identity later.
- Design Studio: not materially relevant.
- Web Manager: not materially relevant; no web deployment/runtime claim.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref inspected; no product repository files edited.

## HANDOFFS

### Systems → Quality
Preserve the 3.47.0 positive-oracle failure as evidence rather than tuning it away. Compare exact toolchains under the same fixture/oracle; only a successful positive case should proceed to the deliberate hash-mutation sensitivity case.

### Systems → Mobile / LogMate release engineering
The failure demonstrates why a broad SDK range and committed lockfile do not identify a canonical release environment. Do not select 3.38.10 or 3.47.0 as product policy from this experiment; product/release tooling must own that decision.

## OPEN / CHANGE WATCH
- Final result of the `3.38.10` vs `3.47.0` matrix at workflow revision `0426836a...`.
- Command-level cause of the 3.47.0 positive-oracle failure.
- Canonical LogMate toolchain identity remains unknown from inspected product repository evidence.
- Canonical LogMate source build, tests, target artifact digest, signing/attestation and independent-host reproducibility remain OPEN.
- Flutter/pub behavior is version-sensitive; preserve exact release/ref for every verdict.
