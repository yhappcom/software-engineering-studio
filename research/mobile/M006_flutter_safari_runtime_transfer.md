# M006 — Flutter JavaScript runtime transfer to Safari

Status: **IN STUDY — HOSTED SAFARI WEBDRIVER ENABLEMENT BLOCKED; SEMANTIC SAFARI ORACLE NOT YET EXECUTED**  
Evidence date: 2026-09-22

## Problem and Balance Loop selection

The preceding M003 API-35 emulator permission/FGS causal boundary is closed at bounded transfer scope. Repeating emulator timing variants would add little evidence. Across current Stage-1 gaps, Safari is a materially different browser/runtime family and directly advances both F001 cross-runtime execution and M006 PWA/browser knowledge without requiring unavailable physical-device access or LogMate runner credentials.

This block therefore selects a bounded **Flutter JavaScript artifact → macOS Safari WebDriver → async runtime oracle**. It does not claim iOS/iPadOS/EFB, PWA offline/update behavior, or LogMate product equivalence.

## SOURCE

- Flutter current web FAQ states Flutter web apps can run on Safari (mobile and desktop): https://docs.flutter.dev/platform-integration/web/faq
- Flutter current supported-platform matrix lists Safari JavaScript support and is version-sensitive: https://docs.flutter.dev/reference/supported-platforms
- Apple documents `safaridriver --enable` as the Terminal path for enabling WebDriver on macOS; Apple notes `sudo` may be needed in some upgrade contexts: https://developer.apple.com/documentation/safari-developer-tools/macos-enabling-webdriver
- Apple documents Safari WebDriver as the supported browser-automation mechanism and the `Allow remote automation` setting: https://developer.apple.com/documentation/webkit/testing-with-webdriver-in-safari and https://developer.apple.com/documentation/safari-developer-tools/developer-settings

## SYNTHESIS

Framework documentation saying Safari is supported is not executable evidence that this Studio's Flutter artifact actually boots and executes asynchronous Dart-compiled JavaScript in Safari. A Safari-specific runtime oracle closes a different evidence class from the existing Chromium transfer.

## Executable validation contract

**CLAIM:** a release-mode Flutter web JavaScript artifact generated from the bounded Studio fixture can bootstrap in the Safari instance on the recorded macOS runner and execute a delayed Dart event-loop transition observable independently through WebDriver.

**TARGET:** `research/mobile/fixtures/m006_flutter_safari_runtime/`, generated web shell plus `flutter build web --release` output.

**INPUT/STATE:** local HTTP origin `http://127.0.0.1:8765/`; fixture sets document title to `M006_BOOT`, runs Flutter, then schedules a 750 ms Dart `Timer` that changes the title to `M006_ASYNC_READY`.

**ORACLE:** Safari WebDriver reads the browser-owned document title until `M006_ASYNC_READY` or a 30-second deadline. Browser capabilities plus Flutter/Dart/macOS/Safari/safaridriver identities are recorded. This oracle is deliberately outside Flutter widget-test machinery.

**VERDICT:** `SAFARI_FLUTTER_JS_ASYNC_READY` only when the Safari session loads the generated artifact and observes the delayed title transition. Timeout or harness/setup failure is not a platform contradiction until isolated.

**EVIDENCE LIMIT:** a pass would establish only bounded macOS Safari execution of this generated JavaScript fixture. It would not establish CanvasKit rendering correctness, accessibility, service-worker/PWA offline semantics, storage durability, iOS/iPadOS Safari, EFB policy, physical networking, LogMate artifact behavior, product release identity, or production behavior.

## Execution 1 — setup failure isolated from semantic target

Exact workflow head: `1335d4b2892c66f86ff9a6fab6883518316ec2a0`. GitHub Actions run `35705327847`, job `106672739308`, runner `macos-15`, terminal **failure**. Checkout, Flutter installation, environment capture and release web build completed; `Enable Safari WebDriver` failed and the semantic Safari oracle was skipped.

Artifact `10684121767`, digest `sha256:091321fa9c99574cbff21b5354b68e26e4a856af1f2d6c77d5b1d8392076e5b2`, recorded Flutter 3.47.5 / Dart 3.13.4 / macOS 15.7.9 build 24G830 / Safari 26.6.1 / safaridriver 20624.5.1.18.3. Exact enable failure details were not preserved, so ROOT CAUSE remained OPEN.

## Execution 2 — interactive enablement failure isolated

Exact workflow head `ebd7030de8efb04cec71e3c888d202232cab6a70`; run `35710948055`, job `106691136838`, `macos-15`, terminal **failure**. Artifact `10686147472`, digest `sha256:c4d2baf7c21c0833467889ac59491b20a4aff445334daf914e4d040027128549`.

**OBSERVATION:** `safaridriver-enable.txt` contains `ATTEMPT=unprivileged` followed by `Password:Password is not valid, please try again.` It contains no return-code or fallback marker. The unprivileged command entered an interactive authorization path before the intended diagnostic/fallback sequence.

**ROOT CAUSE (bounded harness failure):** an interactive-first prerequisite probe was incompatible with unattended hosted CI. This is setup orchestration, not Flutter/Safari semantic evidence.

**FIX:** workflow commit `e4c68d1418eb5cda6193dbbb98b1171031053153` removes interactive-first enablement and uses `sudo -n /usr/bin/safaridriver --enable`, preserving return codes and failing closed.

## Execution 3 — non-interactive regression result

Exact workflow head: `e4c68d1418eb5cda6193dbbb98b1171031053153`.  
GitHub Actions run: `35716201875`; job `106708178990`; runner label `macos-15`; terminal conclusion **failure**.  
Run-bound artifact: `10690100321`, digest `sha256:def6b87ba8d1bab89eb3bd749eb0cdf277a45f36a7d243291141e2edf369ef47`.

**OBSERVATION:** checkout, Flutter installation, environment identity capture and release JavaScript build all completed successfully. `Enable Safari WebDriver with diagnostics` failed after approximately two seconds. `Execute Safari runtime oracle` was skipped. Artifact preservation succeeded.

**VALIDATION:** the run-2 fix eliminated the prior long interactive prompt path sufficiently for the workflow to terminate promptly and preserve a run-bound diagnostic artifact. It did **not** validate Safari runtime semantics and it did **not** establish that hosted-runner WebDriver enablement is possible.

**OPEN / EVIDENCE LIMIT:** the current GitHub connector can establish the step boundary and artifact identity but cannot retrieve the artifact archive contents or job log payload for this run. Therefore the exact `ENABLE_RC`/stderr cannot be truthfully asserted here. Do not infer that `sudo -n` failed for a particular authorization reason until those preserved diagnostics are read in an environment that can access the artifact payload.

**DEPENDENCY:** semantic Safari validation now depends on either (a) readable run-3 diagnostic payload followed by a justified enablement repair, or (b) a trustworthy Safari execution environment where WebDriver/remote automation is already enabled. Repeating privilege/flag permutations without those diagnostics would violate the failure-isolation standard.

## Alternative comparison

Existing F001/M006 Chromium evidence remains the comparison context. Safari uses WebKit/Safari WebDriver rather than the prior Chrome execution path, so a successful run would be a materially different browser-engine transfer. It is not independent product replication because the fixture and hosted CI context remain Studio-controlled.

## RELATED DOMAIN CHECK

- Foundations: directly advances F001 browser/runtime transfer beyond Chromium; executions 1–3 add no Safari semantic runtime PASS.
- Architecture: no architecture decision changed; browser support remains an external runtime boundary.
- Mobile: owner; M006 Safari execution is blocked at hosted WebDriver enablement, before semantic execution.
- Data: not materially tested; no persistence/durability claim.
- Quality: run 2 exposed interactive prerequisite-probe failure; run 3 confirms fail-closed prompt-free orchestration but exact diagnostic payload remains unread through the current connector.
- Systems: exact run/head/artifact identity is preserved; hosted-runner authorization and artifact-access capability are execution-environment dependencies.
- Design Studio: no visual/interaction semantic contract evaluated.
- Web Manager: PWA/browser overlap considered; no website operational decision changed.
- Marketing Manager: not materially relevant.
- Product: no product runtime audit in this block. Existing context remains `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence previously captured 2026-09-20`; production identity unknown and default branch is not assumed production.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** exact run-3 WebDriver-enable stderr/return code requires artifact/log payload access; do not guess it.
- **VALIDATION:** Safari transfer requires actual WebDriver session plus `M006_ASYNC_READY` semantic observation.
- **OPEN:** iOS/iPadOS Safari/EFB, physical device, offline/service-worker/update lifecycle, product-owned LogMate build, release/production artifact.
- **CHANGE WATCH:** Flutter Safari support matrix, Safari/WebDriver behavior, hosted macOS image and browser version.
- **OPEN:** fixture uses `dart:html`, a legacy/deprecated API surface; retain only as a narrow browser-observable probe, not product guidance.

## HANDOFFS

- Foundations: Safari semantic runtime remains OPEN; do not convert hosted setup evidence into F001 runtime evidence.
- Quality: a fail-closed diagnostic probe is useful only if the diagnostic payload is retrievable; preserve observability as part of the validation harness contract.
- Systems: hosted Safari automation enablement and artifact/log retrieval are environment capabilities; exact run/head/artifact identity is preserved but semantic execution is absent.
- LogMate/Web Manager: no canonical files edited. A later product transfer must use the product-owned PWA build/post-build path and exact product ref rather than this fixture.
