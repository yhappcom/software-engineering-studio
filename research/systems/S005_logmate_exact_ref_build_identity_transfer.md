# S005 — LogMate Exact-Ref Build Identity Transfer

Status: **IN STUDY — exact-ref product transfer / no build execution**  
Evidence date: 2026-09-18

## Problem / scope

Transfer S004/S005 build-identity and reproducibility findings to a natural current Flutter application repository without pretending that source inspection is build evidence.

Product evidence identity:

`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared app version 1.0.0+1 → evidence date 2026-09-18`

`main` is the inspected ref only. It is **not assumed to be production**.

## SOURCE

Current Dart pub documentation states that application packages should commit `pubspec.lock`; the lockfile records selected package versions and content hashes. `dart pub get --enforce-lockfile` fails if the lockfile is not an exact valid resolution or hosted-package content hashes have changed, and Dart documents it as useful for CI/deployment.

Current Flutter documentation exposes each SDK release with both a Flutter version and a unique source ref/commit and documents switching to a specific Flutter version. `flutter --version` reports the current SDK framework/engine/tools identity.

Primary sources:
- https://dart.dev/tools/pub/versioning
- https://dart.dev/tools/pub/cmd/pub-get
- https://docs.flutter.dev/install/archive
- https://docs.flutter.dev/install/upgrade
- https://docs.flutter.dev/reference/flutter-cli

## PRODUCT OBSERVATION

At the exact LogMate ref:

- `pubspec.yaml` declares app version `1.0.0+1` and Dart SDK constraint `^3.10.7`.
- `pubspec.lock` is present and records exact hosted dependency versions and SHA-256 content hashes; its SDK section permits Dart `>=3.10.7 <4.0.0` and Flutter `>=3.27.0`.
- Android Gradle wrapper is fixed to Gradle `8.14`.
- Android settings pin Android Gradle Plugin `8.11.1`, Google Services plugin `4.3.15`, and Kotlin Android plugin `2.2.20`.
- Android settings obtain Flutter from `local.properties` via `flutter.sdk`; the inspected repository evidence does not itself identify one exact Flutter SDK version/ref.
- Repository search found no `flutter-version` or `fvm` evidence on the indexed default branch. This is negative search evidence, not proof that no external CI/toolchain pin exists.

## SYNTHESIS

The exact source commit plus `pubspec.lock` materially narrows dependency identity, but it does **not** fully determine canonical Flutter build identity.

For this product ref, the repository-visible build-input relation is approximately:

`source commit + pubspec.lock hosted package identities + local Flutter SDK selected by local.properties + pinned Android Gradle/plugin versions + platform/JDK/other environment + build flags/post-build transforms → artifact bytes`

Therefore these claims must remain separate:

- `same LogMate commit`;
- `same Dart/hosted dependency resolution`;
- `same Flutter framework/engine/tooling`;
- `same Android build toolchain`;
- `same build configuration`;
- `same artifact bytes`.

A lockfile cannot substitute for exact Flutter SDK identity because Flutter itself is an SDK dependency and the lockfile only expresses a compatible SDK range here. Conversely, pinning Flutter alone would not pin hosted dependency content, Gradle/JDK/platform inputs, signing, or post-build processing.

## FAILURE / ALTERNATIVE COMPARISON

### Weak release reconstruction

`checkout commit b551ce... → use any compatible installed Flutter → flutter pub get → build`

This can satisfy repository constraints while still changing framework/engine/tool versions or other build inputs. It is therefore insufficient as an oracle for reproducing the previously accepted artifact.

### Stronger acceptance contract

For evidence-critical CI/release builds, preserve at minimum:

1. exact source commit;
2. exact Flutter SDK version/ref and Dart version reported by that SDK;
3. committed lockfile and lockfile-enforced dependency retrieval where operationally appropriate;
4. relevant platform build-tool identities (for Android: Gradle wrapper, AGP, Kotlin plugin, JDK/SDK inputs as applicable);
5. build mode/flags and version overrides;
6. post-build/signing transforms;
7. final artifact digest and signer/package identity where applicable;
8. CI/workflow/run identity or equivalent execution provenance.

This is an engineering evidence contract, not a project mandate to adopt a particular version manager.

## VALIDATION / evidence boundary

No Flutter/Dart executable exists in the current Studio execution environment on 2026-09-18, so the exact LogMate ref was **not built**. No reproducibility, dependency-resolution, Android packaging, signing, test, or runtime PASS is awarded.

This run provides **TRANSFER VALIDATION of the identity model against natural product configuration**, not executable product validation. It establishes that the current repository-visible evidence contains several pinned inputs while exact Flutter SDK identity remains externally supplied/unknown from the inspected files.

A trustworthy future executable test should build the same exact ref twice under a declared exact Flutter SDK/ref and lockfile policy, compare artifact bytes/digests, deliberately vary one toolchain input, and preserve the resulting failure signature. A second independent environment would strengthen the evidence further.

## ENGINEERING JUDGMENT

The highest-leverage immediate release-engineering improvement is not to infer reproducibility from the committed lockfile. It is to make the canonical build toolchain identity explicit wherever the product's release process is defined, then bind release evidence to the artifact actually produced. Whether that is stored in the product repository, CI configuration, a version manager, or another controlled release record is a product/release-governance decision.

## RELATED DOMAIN CHECK

- **Foundations:** F001 direct Dart/Flutter execution remains OPEN; this transfer must not be used as runtime evidence.
- **Architecture:** A006 evidence-preservation applies: build decisions need exact evidence/ref and reconsideration triggers when toolchains change.
- **Mobile:** direct Flutter/Android build and installed-package transfer remain OPEN; Mobile should consume the exact toolchain/artifact identity when that environment exists.
- **Data:** migration/restore acceptance should bind to an authorized exact artifact, not only source/version labels.
- **Quality:** future reproducibility tests need byte/digest oracles plus deliberate toolchain/input-drift negatives.
- **Systems:** S004 lock/dependency identity and S005 build/release identity are the direct owners.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical evidence from those repositories materially changes this build-input identity question.
- **Product:** exact LogMate ref above inspected. No product canonical file edited.

## HANDOFFS

### TO LogMate / release engineering
When release/build automation is defined, record the exact Flutter SDK identity and release artifact identity in addition to source ref and lockfile. Consider lockfile-enforced dependency retrieval for CI/deployment where compatible with the chosen Flutter/Dart workflow. This is a handoff only; Studio does not edit product canonical files.

### TO Mobile
When a trustworthy Flutter environment is available, transfer-test this exact-ref contract through `flutter --version`, dependency resolution, canonical build, artifact digest, and platform package/signing identity.

### TO Quality
Design the future product reproducibility oracle so that changing Flutter/toolchain identity can be detected independently of source/lockfile equality.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** exact Flutter SDK/ref used by any real LogMate release is unknown from this inspected repository evidence.
- **OPEN:** production/release identity is unknown; default branch is not treated as production.
- **VALIDATION:** no Dart/Flutter build executed in this run.
- **VALIDATION:** canonical CI/release workflow, JDK/Android SDK inputs, signing, post-build transforms and artifact digests require exact release evidence when they exist.
- **CHANGE WATCH:** Flutter/Dart SDK and package-resolution behavior are version-sensitive; recheck primary docs and product release configuration before operational adoption.

## Gate effect

S005 gains a natural exact-ref Flutter-product transfer of its build-identity model and exposes a concrete missing release-evidence dimension: exact Flutter SDK identity. This does not close Systems Foundation because executable Flutter/mobile build, CI/provenance, signing authorization and production evidence remain OPEN.
