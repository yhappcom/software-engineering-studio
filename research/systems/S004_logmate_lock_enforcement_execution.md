# S004 — LogMate lock enforcement execution transfer

Date: 2026-09-19
Lead: Systems
Status: IN STUDY — exact-toolchain sensitivity demonstrated; dependency-lock execution rung validated under Flutter 3.38.10; canonical product toolchain/build still OPEN

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

## Product-derived fixture

`research/systems/fixtures/s004_logmate_lock_enforcement/` copies the dependency-relevant manifest semantics and complete `pubspec.lock` from the exact LogMate ref. The product lockfile records exact hosted package versions/content hashes and SDK compatibility ranges (`dart >=3.10.7 <4.0.0`, `flutter >=3.27.0`). It is evidence input, not a LogMate source checkout/application build.

## VALIDATION design

Workflow: `.github/workflows/s004-logmate-lock-enforcement.yml`.

Positive oracle: `flutter pub get --enforce-lockfile` exits zero and `cmp` proves the lockfile was not rewritten.

Negative oracle: mutate exactly one nibble of locked `cupertino_icons 1.0.9` SHA-256; enforcement must exit non-zero and output must identify a hash/content/lock condition.

A negative case is mandatory because green dependency resolution alone does not establish control sensitivity to integrity drift.

## Exact-toolchain alternative comparison — completed

Workflow head `0426836a14866f00dd9de4811c7083bb1f1c0675`; run `35443257511`; Ubuntu 24.04.5 hosted runners.

### Flutter 3.38.10 — VALIDATION success
Job `105897690809` completed success.

Recorded identity:
- Flutter `3.38.10`
- framework revision `c6f67dede3d4aa1aa7a69dd56a3494a5cde6cc80`
- engine revision `cafcda5721a78a7884db92f13c5e89f7643d52dd`
- engine content hash `3c25ef829c74f0f39fbb8df093d9a6b9f941ea6b`
- Dart SDK `3.10.9`

Positive oracle: `flutter pub get --enforce-lockfile` returned 0 and `cmp pubspec.lock.before pubspec.lock` succeeded. The exact copied lock resolution was accepted without rewrite.

Negative oracle: one nibble of the locked `cupertino_icons 1.0.9` SHA-256 was mutated. Enforcement returned exit code 65 and explicitly reported `The existing content-hash from pubspec.lock doesn't match contents`, identified `cupertino_icons-1.0.9`, reported that the lockfile could be corrupted/content changed, and refused the resolution. This demonstrates failure sensitivity to hosted-package integrity drift, not merely a green positive path.

### Flutter 3.47.0 — controlled failure
Job `105897690857` completed failure.

Recorded identity:
- Flutter `3.47.0`
- framework revision `4cf24164269a5ebf0c16a028a00727d0e77bbb05`
- engine revision `5f77625673248ee5846fbcaf5d3e1a3878386fd7`
- engine content hash `59d54a2b2896a6bbf356c94b7fac7b9e235bdacd`
- Dart SDK `3.13.0`

The unchanged-lock positive oracle returned exit code 65. Command output showed the resolver would change seven SDK-coupled/transitive packages: `characters 1.4.0→1.4.1`, `intl 0.20.2→0.20.3`, `matcher 0.12.17→0.12.20`, `material_color_utilities 0.11.1→0.13.0`, `meta 1.17.0→1.19.0`, `test_api 0.7.7→0.7.12`, and `vector_math 2.2.0→2.4.3`. Enforcement therefore refused the committed lock resolution. The deliberate hash negative case was correctly skipped because the positive prerequisite failed.

## CONTRADICTION / ROOT CAUSE boundary

The earlier unknown-cause 3.47.0 failure is now narrowed: it is not a hosted-package content-hash mismatch in the unchanged lock. The exact later Flutter/Dart SDK environment requires a different valid resolution for seven SDK-coupled/transitive packages, so `--enforce-lockfile` rejects the older committed graph.

This is a toolchain-sensitivity result, not evidence that LogMate is broken. Flutter 3.47.0 was Studio-selected and is not established as LogMate's canonical toolchain. Likewise, success under 3.38.10 does not prove 3.38.10 was historically or operationally the product toolchain.

## TRANSFER VALIDATION

For the exact product-derived manifest/lock pair, package-lock validity is demonstrably a function of exact Flutter/Dart toolchain identity:

`same manifest + same committed lock + Flutter 3.38.10/Dart 3.10.9 → accepted unchanged`

`same manifest + same committed lock + Flutter 3.47.0/Dart 3.13.0 → rejected; seven dependencies would change`

Under the accepting toolchain, deliberate hosted-package content-hash corruption fails closed. This closes only the Studio product-derived dependency-lock execution rung.

## SYNTHESIS

`SDK compatibility range ≠ exact toolchain identity ≠ demonstrated lock acceptance ≠ canonical product build ≠ artifact identity`.

A committed lockfile provides strong package graph/content identity, but its executable validity can still depend on the SDK's own package constraints. Reproducible release claims therefore require exact toolchain identity in addition to the lockfile.

## ENGINEERING JUDGMENT

Do not infer product policy from the first accepting historical-compatible toolchain. A canonical release path should be product-owned and explicitly pin/capture Flutter framework revision, engine revision/content identity and bundled Dart version before build/artifact reproducibility is claimed.

## RELATED DOMAIN CHECK
- Foundations: trustworthy hosted Dart/Flutter execution exists; F001 no longer blocks this bounded transfer.
- Architecture: toolchain/dependency identity is an externally relevant release contract when reproducibility/provenance is required.
- Mobile: exact Flutter release identity materially changes dependency resolution; no Android/iOS/browser runtime evidence was produced.
- Data: no persistence semantics exercised.
- Quality: positive unchanged-lock oracle, deliberate integrity mutation and exact-toolchain alternative comparison all executed.
- Systems: lead track; S004 dependency-lock execution rung advanced; S005 consumes build/artifact identity later.
- Design Studio / Web Manager / Marketing Manager: not materially relevant to this bounded mechanism; no canonical files edited.
- Product: exact LogMate ref audited; no product repository files edited.

## HANDOFFS

### Systems → Quality
Preserve both toolchains as a regression pair: 3.38.10 demonstrates a valid positive plus mutation-sensitive negative oracle; 3.47.0 demonstrates that an SDK upgrade can invalidate an otherwise committed graph. Do not normalize either result away.

### Systems → Mobile / LogMate release engineering
Product release tooling should declare/pin the exact Flutter/Dart/engine identity. Do not select 3.38.10 merely because this fixture accepts the lock. Before a canonical build, recover authoritative product/operator/CI toolchain identity if it exists.

## OPEN / CHANGE WATCH
- Canonical LogMate Flutter SDK/engine and any external CI/operator toolchain pin remain unknown from inspected product-repository evidence.
- Canonical LogMate source build, tests, target artifact digest, signing/attestation and independent-host reproducibility remain OPEN.
- No production identity is known; `main` is not assumed production.
- Flutter/pub behavior is version-sensitive; preserve exact release/ref/engine/Dart identity for every verdict.
