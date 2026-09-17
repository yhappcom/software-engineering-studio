# M005 — Cross-Platform Architecture, Portability & Platform Divergence

Status: **IN STUDY — first integrated Foundation block + bounded executable capability evidence**  
Date: 2026-09-18  
Lead: Mobile

## Problem
A shared Flutter/Dart codebase does not make Android, iOS and browser/PWA execution environments semantically identical. Portability must be defined against required application capabilities and guarantees, not source-code reuse percentage or matching API names.

## SOURCE
Primary/current sources checked 2026-09-18:

1. Flutter Web FAQ — https://docs.flutter.dev/platform-integration/web/faq
   - Flutter web supports major browsers, but browser constraints remain platform constraints.
   - `dart:io` filesystem access is not available to a web app; web-specific implementations may require conditional imports.
   - `Platform.is` is not a valid web portability mechanism; Flutter recommends `kIsWeb` for app-level distinction.
   - Dart isolate concurrency is not currently supported in Flutter web; web workers are a distinct browser mechanism and are not built into Flutter's isolate support.
2. Flutter custom platform-specific code — https://docs.flutter.dev/platform-integration/platform-channels
   - native platforms can use platform channels/Pigeon/native implementations; web platform-specific code generally uses JS interoperability instead.
3. Dart package guidance — https://dart.dev/tools/pub/create-packages and https://dart.dev/interop/js-interop/package-web
   - conditional imports/exports select implementations based on available platform libraries; all selected implementations should expose the same API surface.
   - current web interop guidance uses `dart.library.js_interop`; legacy `dart:html` is deprecated and does not support Wasm compilation.
4. MDN PWA guidance — https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/What_is_a_progressive_web_app and installability guidance.
   - PWA capability varies by browser/platform; progressive enhancement requires feature detection and acceptable fallbacks for unsupported advanced APIs.
   - installation behavior is browser/platform dependent; installability and offline behavior are separate concerns.

## SYNTHESIS — portability model
Model a cross-platform feature as:

`user/domain semantic contract → required capability vector → platform mechanism → platform-specific failure modes → fallback/degradation policy → acceptance oracle`

Useful capability dimensions include:
- storage namespace, durability, quota and user-mediated file access;
- process/lifecycle/background execution;
- concurrency primitive availability;
- network/browser security policy;
- secure-key/credential facilities;
- plugin/native/JS integration path;
- install/update/cache behavior;
- sharing/export/import mechanisms;
- performance/resource budgets.

A shared interface is useful only when each implementation either satisfies the same semantic contract or explicitly exposes an unsupported/degraded state. A common method name does not make guarantees equivalent.

## CONTRADICTION / invalid shortcuts
Reject:
- `same Dart source => same platform behavior`;
- `same API shape => same semantics`;
- `conditional import => portability proven`;
- `PWA installed => native app guarantees`;
- `browser fallback exists => original guarantee preserved`;
- `code reuse percentage => architecture quality`.

Conditional imports solve implementation selection. They do not prove semantic equivalence of the selected implementations.

## EXECUTABLE VALIDATION
Fixture: `research/mobile/fixtures/M005_capability_contract_matrix.py`

### Test Evidence Contract
- **CLAIM:** portability requires capability-aware implementation/fallback; silently assuming a native capability on web violates the modeled contract.
- **SPEC/PROPERTY:** (1) unsupported capability must not be reported as successful; (2) a platform-specific mechanism may satisfy the same higher-level export intent when the product contract allows it; (3) a required guarantee without an equivalent fallback must remain explicitly unsupported.
- **TARGET:** bounded native-mobile vs browser-web capability model.
- **INPUT/STATE:** arbitrary-filesystem export and required background-retry operations.
- **ORACLE:** explicit capability predicates and expected semantic outcomes independent of the implementation branch.
- **ENVIRONMENT:** Python 3.13.5 / Linux; executed 2026-09-18.
- **OBSERVATION:** native modeled filesystem path succeeded; unsafe shared implementation rejected the web capability set; export contract used a web download fallback; required background retry remained explicitly unsupported rather than silently succeeding.
- **VERDICT:** PASS for the bounded model.
- **FAILURE MODEL:** shared implementation assumes unavailable capability; fallback incorrectly claims preservation of a stronger guarantee.
- **EVIDENCE LIMIT:** not Flutter, Android, iOS, Safari, browser, service-worker or device execution evidence. The capability values are deliberately simplified model inputs, not a platform support matrix.

## ENGINEERING JUDGMENT
Prefer a shared domain/application contract with platform adapters when the semantic contract is genuinely common. Keep platform divergence explicit where guarantees differ materially. Do not force a lowest-common-denominator abstraction if it hides security, durability, background, lifecycle or recovery differences that the product must reason about.

Feature detection is preferable to platform-name branching when the decision truly depends on a runtime capability. Platform identity remains appropriate when the platform itself is part of the contract or implementation selection.

## TRANSFER VALIDATION — LogMate
Evidence identity:

`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-18`

Default branch is **not** assumed to equal production.

At this exact ref, `MASTER.md` explicitly excludes a guarantee of automatic PWA P2P transfer without a common LAN and immediate transfer while the PWA is backgrounded/terminated. It also states that current product persistence/sync is not implemented and that the current Makefile's canonical target is `build-pwa`. `Makefile` builds Flutter web with `--no-web-resources-cdn --no-wasm-dry-run` and then runs a project precache tool.

**TRANSFER:** this is direct evidence that LogMate already has product requirements whose PWA/native semantics cannot be collapsed into one assumed execution model. M005 does **not** claim the current build is production, offline-complete, installable, or accepted on the company EFB. Those require exact artifact/deployment/browser/device validation under the cross-repo artifact provenance gate.

## Alternatives
1. **Uniform implementation assumption** — lowest code branching, but invalid when capabilities differ; rejected as a correctness model.
2. **Lowest-common-denominator contract** — simple, but may discard useful native capability and can weaken product guarantees silently.
3. **Shared semantic contract + platform adapters/fallbacks** — preferred when semantics can be preserved; requires explicit acceptance tests per implementation.
4. **Separate feature/product path per platform** — justified when semantics, lifecycle or operational constraints are materially different; higher maintenance cost but can be more truthful.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F005/F006 checked conceptually; execution, async and OS/network boundaries explain why source reuse cannot erase runtime differences. Direct Dart/Flutter execution remains OPEN.
- **Architecture:** A003 contract semantics and A006 evidence-preserving decisions apply; platform adapters must preserve semantic contracts rather than API shape only.
- **Mobile:** M001-M004 are direct prerequisites for lifecycle/storage/plugin divergence.
- **Data:** offline/persistence/sync guarantees must be platform-transfer tested rather than inferred from shared repository code.
- **Quality:** each platform implementation needs independent oracle/failure evidence; one platform PASS does not transfer automatically.
- **Systems:** artifact/build/deployment identity matters for PWA/native acceptance.
- **Design Studio:** searched for materially relevant PWA/mobile-web evidence; no canonical result found in this run. Interaction semantics must still expose unsupported/degraded states truthfully.
- **Web Manager:** searched for materially relevant LogMate/PWA evidence; no canonical result found in this run. Browser/PWA operational decisions remain Web-owned where applicable.
- **Marketing Manager:** searched for PWA evidence; no materially relevant canonical result found.
- **Product:** exact LogMate ref inspected as above.

## OPEN / VALIDATION / CHANGE WATCH
- **OPEN:** direct Dart/Flutter execution remains unavailable in the current environment (`dart`/`flutter` executables absent; Python 3.13.5 available).
- **TRANSFER VALIDATION:** real Flutter native vs web implementations, browser feature detection, storage/quota, service worker/update/offline behavior, background behavior and EFB device acceptance.
- **CHANGE WATCH:** Flutter web isolate/Wasm/import guidance, browser/PWA API support, iOS/iPadOS PWA behavior and install/update policies are version-sensitive.
- **DEPENDENCY:** exact LogMate production/deployment ref and EFB browser/OS policy are required before production portability claims.

## HANDOFFS
- **TO Architecture:** use capability vectors and semantic acceptance, not shared API shape, when deciding adapter boundaries.
- **TO Data:** define offline/sync/durability requirements separately from implementation mechanism and transfer-test on web/native.
- **TO Quality:** build cross-platform contract suites with platform-specific failure injection; unsupported must be a valid explicit outcome where the product contract allows it.
- **TO Systems:** bind PWA/native validation to exact source/build/post-build/artifact/deployment/runtime identity.
- **TO Web Manager:** when LogMate PWA operational work becomes active, validate browser/service-worker/install/update constraints against current requirements rather than importing native assumptions.

## Gate effect
M005 closes the previously untouched cross-platform portability/divergence boundary at a first professional/model level. It does not close Mobile Stage 1 because direct Flutter/native/web execution and M006 native-vs-PWA deployment constraints remain OPEN.
