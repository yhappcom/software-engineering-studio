# S004 — LogMate lock enforcement execution transfer

Date: 2026-09-19
Lead: Systems
Status: IN STUDY — product-owned Flutter project metadata identity recovered; exact 3.38.7 lock validation pending; canonical operational/release toolchain and build remain OPEN

## Problem / Balance Loop selection

The highest-leverage open S004/Mobile/Quality chain is exact toolchain identity → committed-lock enforcement → canonical build → artifact identity. Prior execution established toolchain-sensitive lock behavior but did not identify a product-owned toolchain clue. This continuation searches the exact product ref rather than promoting the first accepting Studio toolchain to product policy.

## Product identity

`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-19`.

Production identity is unknown. The default branch is not assumed production.

## SOURCE / product-owned metadata discovery

At the exact LogMate ref, version-controlled `.metadata` states that the Flutter project tracks:

- `version.revision: 3b62efc2a3da49882f43c372e0bc53daef7295a6`
- `version.channel: stable`
- root/android/ios/linux/macos/web/windows migration `create_revision` and `base_revision` equal the same revision.

The file itself says it tracks Flutter project properties and is used by the Flutter tool for capabilities/upgrades; it does **not** declare that this revision is the current CI/operator/release SDK.

Authoritative upstream GitHub evidence resolves `flutter/flutter` tag `3.38.7` directly to commit `3b62efc2a3da49882f43c372e0bc53daef7295a6`. The upstream commit message is `Update changelog for flutter 3.38.7 stable hotfix (#180931)` and is GitHub-signature verified.

**SYNTHESIS:** the product repository contains a product-owned Flutter **project-generation/migration baseline identity** that maps exactly to official Flutter 3.38.7. This materially narrows the prior statement that no exact Flutter identity existed anywhere in product evidence.

**CONTRADICTION / correction:** prior Studio wording that exact canonical Flutter SDK was wholly absent from product-repository evidence was too broad. An exact project metadata revision is present. What remains absent is evidence that this metadata revision is the operational build/release toolchain for the inspected product ref.

## Product-derived fixture

`research/systems/fixtures/s004_logmate_lock_enforcement/` copies the dependency-relevant manifest semantics and complete `pubspec.lock` from the exact LogMate ref. The product lockfile records exact hosted package versions/content hashes and SDK compatibility ranges (`dart >=3.10.7 <4.0.0`, `flutter >=3.27.0`). It is evidence input, not a LogMate source checkout/application build.

## VALIDATION design

Workflow: `.github/workflows/s004-logmate-lock-enforcement.yml`.

Positive oracle: `flutter pub get --enforce-lockfile` exits zero and `cmp` proves the lockfile was not rewritten.

Negative oracle: mutate exactly one nibble of locked `cupertino_icons 1.0.9` SHA-256; enforcement must exit non-zero and output must identify a hash/content/lock condition.

A negative case is mandatory because green dependency resolution alone does not establish control sensitivity to integrity drift.

The matrix now includes **3.38.7** specifically because exact product `.metadata` revision maps to that official tag, alongside the already-observed 3.38.10 accepting comparison and 3.47.0 resolver-rejection comparison. Workflow head `7815772bc11f8902dee2816165195c56ad45fef9` was committed on 2026-09-19. No 3.38.7 execution verdict is recorded until an actual hosted run completes.

## Exact-toolchain alternative comparison — retained

Workflow head `0426836a14866f00dd9de4811c7083bb1f1c0675`; run `35443257511`; Ubuntu 24.04.5 hosted runners.

### Flutter 3.38.10 — VALIDATION success
Job `105897690809` completed success.

Recorded identity:
- Flutter `3.38.10`
- framework revision `c6f67dede3d4aa1aa7a69dd56a3494a5cde6cc80`
- engine revision `cafcda5721a78a7884db92f13c5e89f7643d52dd`
- engine content hash `3c25ef829c74f0f39fbb8df093d9a6b9f941ea6b`
- Dart SDK `3.10.9`

Positive oracle accepted the unchanged lock. A one-nibble `cupertino_icons 1.0.9` SHA-256 mutation failed closed with exit 65 and explicit content-hash mismatch.

### Flutter 3.47.0 — controlled failure
Job `105897690857` completed failure.

Recorded identity:
- Flutter `3.47.0`
- framework revision `4cf24164269a5ebf0c16a028a00727d0e77bbb05`
- engine revision `5f77625673248ee5846fbcaf5d3e1a3878386fd7`
- engine content hash `59d54a2b2896a6bbf356c94b7fac7b9e235bdacd`
- Dart SDK `3.13.0`

The unchanged-lock positive oracle returned exit 65 because seven SDK-coupled/transitive packages would change: `characters`, `intl`, `matcher`, `material_color_utilities`, `meta`, `test_api`, and `vector_math`.

## TRANSFER VALIDATION

Retained demonstrated result:

`same manifest + same committed lock + Flutter 3.38.10/Dart 3.10.9 → accepted unchanged`

`same manifest + same committed lock + Flutter 3.47.0/Dart 3.13.0 → rejected; seven dependencies would change`

New product metadata supplies a non-guessed exact historical/project baseline, Flutter 3.38.7, for the next transfer. Its lock behavior remains **VALIDATION pending** until execution completes.

## ENGINEERING JUDGMENT

`.metadata` is stronger than an inferred SDK from dependency compatibility because it is product-owned exact revision evidence, but weaker than a release toolchain pin. Do not relabel it as canonical CI/operator/release identity without product build scripts, CI configuration, release records, or equivalent evidence. Conversely, do not ignore it when choosing a historically grounded validation toolchain.

## RELATED DOMAIN CHECK
- Foundations: hosted Dart/Flutter execution exists; no new Foundation semantic claim.
- Architecture: exact build/toolchain identity is an externally relevant release contract when reproducibility/provenance is required.
- Mobile: `.metadata` supplies an exact Flutter project baseline, not Android/iOS/browser runtime acceptance.
- Data: not materially changed by this block.
- Quality: the new 3.38.7 matrix is an evidence-grounded transfer target with positive and deliberate negative oracles.
- Systems: lead track; S004 identity chain materially narrowed.
- Design Studio / Web Manager / Marketing Manager: considered under cross-repo contract; no canonical decisions changed and no files edited.
- Product: exact LogMate ref and `.metadata` checked; no product files edited.

## HANDOFFS

### Systems → Mobile / Quality / LogMate release engineering
Product-owned `.metadata` at `b551ce4...` maps exactly to official Flutter 3.38.7. Treat this as project-generation/migration baseline evidence, not automatically as current release policy. Use it as a grounded validation target while seeking explicit CI/operator/release toolchain identity.

## OPEN / CHANGE WATCH
- 3.38.7 lock-enforcement execution is pending; do not award a verdict from metadata reading alone.
- Canonical operational/release Flutter SDK/engine and external CI/operator toolchain pin remain unknown.
- Canonical LogMate source build, tests, target artifact digest, signing/attestation and independent-host reproducibility remain OPEN.
- No production identity is known; `main` is not assumed production.
- Flutter/pub behavior is version-sensitive; preserve exact release/ref/engine/Dart identity for every verdict.
