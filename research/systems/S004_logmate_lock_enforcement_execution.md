# S004 — LogMate lock enforcement and baseline build transfer

Date: 2026-09-20
Lead: Systems
Status: IN STUDY — product baseline/lock validated; product PWA build path recovered; hosted baseline build blocked at cross-repository source acquisition

## Product identity
`yhappcom/logmate → branch main → commit b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-20`. Production identity is unknown; default branch is not assumed production.

## SOURCE — product-owned metadata identity
At the exact LogMate ref, `.metadata` records Flutter revision `3b62efc2a3da49882f43c372e0bc53daef7295a6`, channel `stable`, and matching create/base migration revisions. Official `flutter/flutter` tag `3.38.7` resolves to that revision. This establishes a project-generation/migration baseline, not release-toolchain provenance.

**CONTRADICTION / correction:** prior wording that no exact Flutter identity existed in product evidence was too broad. Exact project metadata identity exists; explicit operational/release-toolchain identity still does not.

## VALIDATION — dependency-lock transfer
Workflow head `7815772bc11f8902dee2816165195c56ad45fef9`; run `35449021735`.
- Flutter 3.38.7 job `105912825103`: exact product-derived manifest/lock passed `flutter pub get --enforce-lockfile`; deliberate hosted content-hash mutation was rejected.
- Flutter 3.38.10 job `105912825084`: replication success.
- Flutter 3.47.0 job `105912824971`: controlled unchanged-lock failure, reproducing later-toolchain incompatibility.

**TRANSFER VALIDATION:** `product metadata revision → official Flutter 3.38.7 → exact lock accepted unchanged + deliberate integrity corruption rejected` is demonstrated. This closes only the product-baseline dependency-lock rung.

## SOURCE — product-owned PWA build path recovered
Exact-ref `Makefile` defines `build-pwa`:
1. `flutter build web --no-web-resources-cdn --no-wasm-dry-run`
2. `dart run tool/precache_flutter_web.dart`

The exact-ref post-build tool requires `build/web/flutter_service_worker.js`, changes service-worker core caching to `Object.keys(RESOURCES)`, broadens query stripping to any query string, and adds `{ignoreSearch: true}` to cache matching. The product README identifies tablet/EFB PWA as a first-class target alongside native iOS/Android.

**SYNTHESIS:** raw `flutter build web` is not artifact-equivalent to this product-owned PWA path. The post-build transform is part of artifact provenance for offline/PWA acceptance.

## VALIDATION — exact-ref baseline source-build attempts
Workflow `.github/workflows/s004-logmate-baseline-pwa-build.yml` targets:

`LogMate exact ref b551ce4... → Flutter 3.38.7 exact revision → committed lock → make build-pwa → service-worker oracles → build/web SHA-256 manifest`.

### Attempt 1
Head `c0d5ed1b8e662733aae9386b79c3f9d64c624e52`, run `35452259148`, job `105921347918`: Flutter 3.38.7 installation and identity succeeded. The combined source-fetch/assertion step failed; all dependency/build/artifact stages were skipped.

### Attempt 2 — causal isolation
Head `3f599b88a40224071512f29ade35591e61807acf`, run `35452482342`, job `105921932831`: Flutter installation and exact identity again succeeded. The newly isolated `Clone LogMate repository` step failed immediately. Exact-ref checkout, product-identity assertion, build-contract assertion, lock enforcement, PWA build and artifact hashing were all skipped.

**DEBUG / ROOT-CAUSE STATUS:** the failure phase is now isolated to unauthenticated hosted-runner acquisition of the LogMate repository, before any product source executes. Command stderr is not exposed in the current evidence channel, so the precise HTTP/authentication failure string is unavailable and must not be fabricated. The evidence is sufficient to reject product-code, dependency-resolution, Flutter web compiler and post-build-transform explanations for these runs.

**DEPENDENCY:** the Studio hosted workflow needs a source-acquisition path authorized to read the exact LogMate repository/ref (or another trustworthy execution environment where that exact ref is already available). Do not copy a partial product snapshot into Studio and call it an exact-ref source build.

**VALIDATION VERDICT:** baseline PWA source build remains OPEN. Both failures are pre-build infrastructure/access evidence, not LogMate build failures.

## TRANSFER VALIDATION — credential context is part of source provenance
On 2026-09-20 the connected GitHub evidence channel successfully read the exact private product ref `b551ce434ad72b1895033e0f3617c73b026d40ea`, including `Makefile`, `pubspec.yaml`, and `.metadata`. The exact-ref `pubspec.yaml` independently confirms declared version `1.0.0+1`; `.metadata` confirms Flutter revision `3b62efc2a3da49882f43c372e0bc53daef7295a6`; `Makefile` confirms the two-stage product-owned `build-pwa` target.

This does **not** resolve the hosted build dependency. Attempt 2 proves that the GitHub Actions execution identity used by the Studio workflow could not acquire the LogMate repository, while the current connected evidence identity can read the same exact ref. Therefore repository authorization is scoped to the credential/execution context and must not be inferred to transfer between an interactive connector and a hosted runner.

**SYNTHESIS:** source provenance has at least two distinct questions: (1) can an evidence channel inspect the exact source identity, and (2) can the execution environment acquire that exact source under its own credentials and build it? Positive evidence for (1) does not establish (2). Copying connector-returned files into the Studio would also weaken the build claim because it would no longer demonstrate repository acquisition and complete exact-ref source identity inside the runner.

**VALIDATION:** exact-ref static product identity is revalidated through an authorized read channel; exact-ref hosted source acquisition and source build remain OPEN. No PASS is awarded for the build rung.

## ENGINEERING JUDGMENT
The product-owned `build-pwa` target is materially stronger build-path evidence than an ad hoc framework command. Flutter 3.38.7 remains a project-baseline toolchain, not proven release provenance. Once source access is trustworthy, a successful workflow can establish a **baseline-labeled source build** and artifact identity for the exact ref; it still cannot establish shipment, signing, deployment, independent-host reproducibility, or EFB/browser acceptance.

## RELATED DOMAIN CHECK
- Foundations: hosted Dart/Flutter execution available; no new runtime semantic claim.
- Architecture: post-build transformation is part of artifact contract when offline behavior depends on it.
- Mobile: PWA is first-class at the exact product ref; build success would not equal browser/EFB runtime acceptance.
- Data: no persistence semantics inferred.
- Quality: two failures preserve stage boundaries; skipped stages are not verdicts. Attempt 2 isolates source acquisition as the failing phase.
- Systems: lead track; source/build/artifact provenance and CI access boundary are primary.
- Design Studio: considered; no design contract changed.
- Web Manager: considered; company-site ownership not implicated.
- Marketing Manager: considered; no measurement/monetization decision changed.
- Product: exact LogMate ref, README, Makefile and post-build tool checked; no product files edited.

## HANDOFFS
### Systems → Mobile / Quality / LogMate release engineering
- Treat `make build-pwa`, not raw `flutter build web`, as product-owned PWA build path at `b551ce4...` unless superseded by later product evidence.
- Flutter 3.38.7 is an exact project baseline with lock evidence, not proven release policy.
- Runs `35452259148` and `35452482342` are source-acquisition/harness failures only; they do not test product compilation.
- The connected evidence identity can inspect the exact private ref, but that authorization does not transfer to the Studio GitHub Actions runner. A future exact-ref build needs runner-appropriate authorization or an equivalent trustworthy environment where the exact ref is already present.
- Once built, Mobile still needs browser/EFB offline/update/runtime transfer; Systems still needs release/deployment provenance.

## OPEN / CHANGE WATCH
- Authorized hosted source acquisition or an equivalent trustworthy exact-ref execution environment is required before baseline build validation can continue.
- Explicit operational/release Flutter SDK/engine and CI/operator pin remain unknown.
- Baseline PWA source build, artifact digest, signing/attestation, independent-host reproducibility, deployment identity and production identity remain OPEN.
- Service-worker generation is Flutter-version-sensitive; the product post-build tool intentionally fails closed on unexpected formats.
- `main` is not assumed production.
