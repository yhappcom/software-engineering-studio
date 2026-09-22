# M006 — Flutter JavaScript runtime transfer to Safari

Status: **IN STUDY — EXECUTABLE TARGET QUEUED; NO PASS YET**  
Evidence date: 2026-09-22

## Problem and Balance Loop selection

The preceding M003 API-35 emulator permission/FGS causal boundary is closed at bounded transfer scope. Repeating emulator timing variants would add little evidence. Across current Stage-1 gaps, Safari is a materially different browser/runtime family and directly advances both F001 cross-runtime execution and M006 PWA/browser knowledge without requiring unavailable physical-device access or LogMate runner credentials.

This block therefore selects a bounded **Flutter JavaScript artifact → macOS Safari WebDriver → async runtime oracle**. It does not claim iOS/iPadOS/EFB, PWA offline/update behavior, or LogMate product equivalence.

## SOURCE

- Flutter current web FAQ states Flutter web apps can run on Safari (mobile and desktop): https://docs.flutter.dev/platform-integration/web/faq
- Flutter current supported-platform matrix lists Safari JavaScript support at 15.6+ and identifies a CI-tested Safari version; this is version-sensitive and therefore CHANGE WATCH: https://docs.flutter.dev/reference/supported-platforms
- Flutter web setup documents that non-Chrome/Edge browsers can be exercised through a web-server path, with more limited debugging support: https://docs.flutter.dev/platform-integration/web/setup
- Apple documents Safari WebDriver/remote automation as the supported browser-automation mechanism and exposes an Allow remote automation setting: https://developer.apple.com/documentation/safari-developer-tools/developer-settings
- Apple Developer documentation describes WebDriver as a mechanism for robust automated tests against Safari: https://developer.apple.com/documentation/safari-developer-tools/develop-menu

## SYNTHESIS

Framework documentation saying Safari is supported is not executable evidence that this Studio's Flutter artifact actually boots and executes asynchronous Dart-compiled JavaScript in Safari. A Safari-specific runtime oracle closes a different evidence class from the existing Chromium transfer.

## Executable validation contract

**CLAIM:** a release-mode Flutter web JavaScript artifact generated from the bounded Studio fixture can bootstrap in the Safari instance on the recorded macOS runner and execute a delayed Dart event-loop transition observable independently through WebDriver.

**TARGET:** `research/mobile/fixtures/m006_flutter_safari_runtime/`, generated web shell plus `flutter build web --release` output.

**INPUT/STATE:** local HTTP origin `http://127.0.0.1:8765/`; fixture sets document title to `M006_BOOT`, runs Flutter, then schedules a 750 ms Dart `Timer` that changes the title to `M006_ASYNC_READY`.

**ORACLE:** Safari WebDriver reads the browser-owned document title until `M006_ASYNC_READY` or a 30-second deadline. Browser capabilities plus Flutter/Dart/macOS/Safari/safaridriver identities are recorded. This oracle is deliberately outside Flutter widget-test machinery.

**VERDICT:** `SAFARI_FLUTTER_JS_ASYNC_READY` only when the Safari session loads the generated artifact and observes the delayed title transition. Timeout or harness/setup failure is not a platform contradiction until isolated.

**REPRODUCTION DATA:** workflow `.github/workflows/m006-flutter-safari-runtime-validation.yml`; exact workflow head and run identity; recorded toolchain/browser files; semantic evidence artifact.

**EVIDENCE LIMIT:** a pass would establish only bounded macOS Safari execution of this generated JavaScript fixture. It would not establish CanvasKit rendering correctness, accessibility, service-worker/PWA offline semantics, storage durability, iOS/iPadOS Safari, EFB policy, physical networking, LogMate artifact behavior, product release identity, or production behavior.

## Current execution

Exact workflow head: `1335d4b2892c66f86ff9a6fab6883518316ec2a0`.  
GitHub Actions run: `35705327847`.  
Observed state at note creation: **queued**. No executable verdict is awarded from the workflow definition alone.

## Alternative comparison

Existing F001/M006 Chromium evidence remains the comparison context. Safari uses WebKit/Safari WebDriver rather than the prior Chrome execution path, so a successful run would be a materially different browser-engine transfer. It is not independent product replication because the fixture and hosted CI context remain Studio-controlled.

## RELATED DOMAIN CHECK

- Foundations: directly advances F001 browser/runtime transfer beyond Chromium.
- Architecture: no architecture decision changed; browser support remains an external runtime boundary.
- Mobile: owner; advances M006 browser-family coverage.
- Data: not materially tested; no persistence/durability claim.
- Quality: independent browser-owned title oracle, timeout, environment identity and run-bound evidence are required.
- Systems: build/runtime provenance is captured, but this is not a product/release artifact.
- Design Studio: no visual/interaction semantic contract is being evaluated in this bounded runtime probe.
- Web Manager: PWA/browser overlap considered; no website operational decision is being made.
- Marketing Manager: not materially relevant.
- Product: LogMate remains relevant motivation, but this fixture is intentionally not a LogMate artifact. Existing exact product context remains `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence previously captured 2026-09-20`; production identity unknown and default branch is not assumed production.

## OPEN / VALIDATION / CHANGE WATCH

- **VALIDATION:** await terminal run and inspect semantic artifact before any transfer verdict.
- **OPEN:** iOS/iPadOS Safari/EFB, physical device, offline/service-worker/update lifecycle, product-owned LogMate build, release/production artifact.
- **CHANGE WATCH:** Flutter Safari support matrix, Safari/WebDriver behavior, hosted macOS image and browser version.
- **OPEN:** the fixture currently uses `dart:html`, which is legacy/deprecated API surface; it is acceptable only as a narrow browser-observable probe and should not be promoted as product implementation guidance.

## HANDOFFS

- Foundations: if terminal evidence is valid, classify only the bounded Safari JavaScript runtime transfer under F001; do not infer native Apple runtime behavior.
- Quality: preserve setup/harness failures separately from Safari semantic failures.
- Systems: preserve exact generated-artifact/toolchain/browser identity; do not equate this Studio build with LogMate's canonical PWA path.
- LogMate/Web Manager: no canonical files edited. A later product transfer must use the product-owned PWA build/post-build path and exact product ref rather than this fixture.
