# S004 — LogMate lock enforcement and baseline build transfer

Date: 2026-09-20
Lead: Systems
Status: IN STUDY — product-owned Flutter project baseline and dependency-lock transfer validated; product-owned PWA build path recovered; baseline source-build execution pending after first harness/source-fetch failure

## Product identity
`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-20`. Production identity is unknown; default branch is not assumed production.

## SOURCE — product-owned metadata identity
At the exact LogMate ref, version-controlled `.metadata` records `version.revision: 3b62efc2a3da49882f43c372e0bc53daef7295a6`, channel `stable`, and the same create/base migration revision across root/android/ios/linux/macos/web/windows. Official `flutter/flutter` tag `3.38.7` resolves to that revision. This establishes a product-owned project-generation/migration baseline, not an operational release-toolchain declaration.

**CONTRADICTION / correction:** prior wording that no exact Flutter identity existed in product-repository evidence was too broad. Exact project metadata identity exists; explicit operational/release-toolchain identity still does not.

## VALIDATION — dependency-lock transfer
Workflow head `7815772bc11f8902dee2816165195c56ad45fef9`; hosted run `35449021735`; Ubuntu hosted runners.

- Flutter 3.38.7 job `105912825103`: success. Exact product-derived manifest/lock passed `flutter pub get --enforce-lockfile` unchanged; deliberate one-nibble hosted-package content-hash mutation was rejected.
- Flutter 3.38.10 job `105912825084`: replication success.
- Flutter 3.47.0 job `105912824971`: controlled unchanged-lock failure, reproducing later-toolchain incompatibility.

**TRANSFER VALIDATION:** `product .metadata exact revision → official Flutter 3.38.7 tag → exact product-derived lock accepted unchanged + deliberate hash corruption rejected` is demonstrated. This closes the product-baseline dependency-lock rung only.

## SOURCE — product-owned PWA build path recovered
The exact LogMate ref contains a version-controlled `Makefile` target `build-pwa`:

1. `flutter build web --no-web-resources-cdn --no-wasm-dry-run`
2. `dart run tool/precache_flutter_web.dart`

The second command is not cosmetic. The exact-ref post-build tool requires the generated `build/web/flutter_service_worker.js`, changes the service worker core from a generated array to `Object.keys(RESOURCES)`, broadens query stripping from only `?v=` to any query string, and adds `{ignoreSearch: true}` to matching paths. The product README names native iOS/Android and tablet/EFB PWA as first-class targets and requires equivalent semantic/calculation/projection results across platforms.

**SYNTHESIS:** a direct `flutter build web` is not equivalent to the product-owned PWA build path at this ref. The post-build service-worker transformation is part of artifact provenance for PWA/offline acceptance. This is exactly the class guarded by `coordination/CROSS_REPO_COLLABORATION.md`: acceptance must bind source ref → canonical/product-owned build path → toolchain/lock → post-build transform → artifact identity.

## VALIDATION — first exact-ref baseline source-build attempt
Studio workflow `.github/workflows/s004-logmate-baseline-pwa-build.yml` was added at head `c0d5ed1b8e662733aae9386b79c3f9d64c624e52` to execute:

`LogMate exact ref b551ce4... → Flutter 3.38.7 exact revision assertion → committed lock enforcement → make build-pwa → service-worker post-transform oracles → build/web SHA-256 manifest`.

Hosted run `35452259148`, job `105921347918`, completed failure. Flutter 3.38.7 installation and exact-toolchain identity recording succeeded. The next combined `Fetch exact LogMate source ref` step failed immediately; lock enforcement, PWA build and artifact-identity steps were therefore skipped.

**VALIDATION VERDICT:** inconclusive for product build correctness. This run is evidence only that the first validation harness/source-acquisition step failed after toolchain setup. It is invalid to attribute the failure to LogMate source, Flutter web compilation, the PWA post-build transform, dependency resolution, or runtime behavior because none of those stages executed.

**DEBUG / ROOT-CAUSE STATUS:** OPEN. The current evidence channel exposes step-level verdicts but not command stderr for that combined step. Commit `3f599b88a40224071512f29ade35591e61807acf` splits repository clone, exact-ref checkout/product identity, and build-contract assertions into independent steps so the next execution can isolate the failing phase without guessing.

## ENGINEERING JUDGMENT
The product-owned `build-pwa` target is materially stronger build-path evidence than an ad hoc framework command. Flutter 3.38.7 remains a project-baseline toolchain, not proven release provenance. A successful execution of this workflow would establish a **baseline-labeled source build** and artifact identity for this exact ref; it would still not establish that the artifact was shipped, signed, deployed to production, independently reproduced, or accepted on the company EFB/browser/device.

## RELATED DOMAIN CHECK
- Foundations: hosted Dart/Flutter execution is available; no new language/runtime semantic claim.
- Architecture: post-build transformation is part of the externally relevant artifact contract when offline behavior depends on it.
- Mobile: PWA is a first-class LogMate target at the exact ref; build success would not equal browser/EFB runtime acceptance.
- Data: no persistence semantics are inferred from build output.
- Quality: first build attempt is preserved as failure evidence; skipped stages are not verdicts. Artifact checks include independent existence/content markers and SHA-256 identity if build reaches that stage.
- Systems: lead track; source/build/artifact provenance is the primary block.
- Design Studio: considered; no visual/interaction contract changed.
- Web Manager: considered; company-site ownership is not implicated by this product PWA artifact validation.
- Marketing Manager: considered; no measurement/monetization decision changed.
- Product: exact LogMate ref, README, Makefile and post-build tool checked; no product files edited.

## HANDOFFS
### Systems → Mobile / Quality / LogMate release engineering
- Treat `make build-pwa`, not raw `flutter build web`, as the product-owned PWA build path at `b551ce4...` unless later product evidence supersedes it.
- Flutter 3.38.7 is an exact project baseline and has dependency-lock execution evidence; it is not proven release policy.
- Do not treat run `35452259148` as a product-build failure: execution stopped in source acquisition before dependency/build stages.
- Once a baseline build succeeds, Mobile still needs actual browser/EFB offline/update/runtime transfer and Systems still needs release/deployment provenance.

## OPEN / CHANGE WATCH
- Split diagnostic workflow at `3f599b88a40224071512f29ade35591e61807acf` awaits execution/result.
- Explicit operational/release Flutter SDK/engine and external CI/operator pin remain unknown.
- Baseline PWA source build, artifact digest, signing/attestation, independent-host reproducibility, deployment identity and production identity remain OPEN.
- PWA service-worker generation is Flutter-version-sensitive; the product post-build tool intentionally fails closed on unexpected generated formats.
- `main` is not assumed production.
