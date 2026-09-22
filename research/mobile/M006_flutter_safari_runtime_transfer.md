# M006 — Flutter JavaScript runtime transfer to Safari

Status: **IN STUDY — RUN 2 ISOLATED INTERACTIVE WEBDRIVER ENABLEMENT FAILURE; SEMANTIC SAFARI ORACLE NOT YET EXECUTED**  
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

Exact workflow head: `1335d4b2892c66f86ff9a6fab6883518316ec2a0`.  
GitHub Actions run: `35705327847`; job `106672739308`; runner label `macos-15`.  
Terminal workflow conclusion: **failure**.

The run successfully completed checkout, Flutter installation, environment identity capture, and generation/build of the release-mode Flutter JavaScript artifact. It then failed specifically at `Enable Safari WebDriver`; `Execute Safari runtime oracle` was skipped. Therefore this run is **not** evidence that Safari accepted or rejected the Flutter artifact.

Run-bound artifact: `10684121767`, digest `sha256:091321fa9c99574cbff21b5354b68e26e4a856af1f2d6c77d5b1d8392076e5b2`.

Recorded environment:
- Flutter `3.47.5`, framework revision `6a19cca56475dbfba1478ee68d7bd0c2ef891da1`
- Dart `3.13.4`, `macos_arm64`
- macOS `15.7.9` build `24G830`
- Safari `26.6.1`
- safaridriver: `Included with Safari 26.6.1 (20624.5.1.18.3)`

### FAILURE / ROOT-CAUSE STATUS

**FAILURE OBSERVATION:** the setup step containing `sudo /usr/bin/safaridriver --enable` failed before Selenium installation and before the semantic Safari oracle.

**OPEN:** execution 1 did not preserve the enable command's stderr/exit details in its artifact. Therefore the exact root cause is not established. It would be invalid to label this a Safari/Flutter compatibility failure or to assert an authorization mechanism without the missing diagnostics.

## Execution 2 — interactive enablement failure isolated

Exact workflow head: `ebd7030de8efb04cec71e3c888d202232cab6a70`.  
GitHub Actions run: `35710948055`; job `106691136838`; runner label `macos-15`; terminal conclusion **failure**. The build stages completed and the semantic Safari runtime step was skipped after the WebDriver enablement step failed.

Run-bound artifact: `10686147472`, digest `sha256:c4d2baf7c21c0833467889ac59491b20a4aff445334daf914e4d040027128549`.

Recorded environment again identifies Flutter `3.47.5` / Dart `3.13.4` / macOS `15.7.9` build `24G830` / Safari `26.6.1` / safaridriver `20624.5.1.18.3`.

**OBSERVATION:** `safaridriver-enable.txt` contains `ATTEMPT=unprivileged` followed by `Password:Password is not valid, please try again.` It contains no `UNPRIVILEGED_RC`, no sudo-attempt marker, and no Selenium-install marker. The unprivileged command therefore entered an interactive authorization path before the scripted fallback and diagnostic sequence could run.

**ROOT CAUSE (bounded harness failure):** the run-2 workflow attempted unprivileged `safaridriver --enable` first in a non-interactive hosted CI context. That command requested interactive authorization, so the harness did not reach its intended return-code capture/fallback path. This is a setup-orchestration defect; it is not evidence about Flutter-on-Safari runtime semantics.

**FIX:** exact workflow commit `e4c68d1418eb5cda6193dbbb98b1171031053153` removes the interactive-first path and uses `sudo -n /usr/bin/safaridriver --enable` directly, preserving the enable return code and Selenium-install return code. A failed non-interactive privileged enable still fails closed; no green result is synthesized.

## Alternative comparison

Existing F001/M006 Chromium evidence remains the comparison context. Safari uses WebKit/Safari WebDriver rather than the prior Chrome execution path, so a successful run would be a materially different browser-engine transfer. It is not independent product replication because the fixture and hosted CI context remain Studio-controlled.

## RELATED DOMAIN CHECK

- Foundations: directly advances F001 browser/runtime transfer beyond Chromium; no new F001 PASS from executions 1–2.
- Architecture: no architecture decision changed; browser support remains an external runtime boundary.
- Mobile: owner; advances M006 browser-family coverage and now has a bounded setup-harness root cause plus regression target.
- Data: not materially tested; no persistence/durability claim.
- Quality: execution 2 demonstrates that diagnostic fallback logic is ineffective when the first command can block on interactive authorization; CI prerequisite probes must themselves be non-interactive and evidence-preserving.
- Systems: exact run/head/artifact/toolchain/browser identity is preserved; hosted runner authorization behavior is part of the execution environment.
- Design Studio: no visual/interaction semantic contract evaluated.
- Web Manager: PWA/browser overlap considered; no website operational decision changed.
- Marketing Manager: not materially relevant.
- Product: no product runtime audit in this block. Existing motivation context remains `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence previously captured 2026-09-20`; production identity unknown and default branch is not assumed production.

## OPEN / VALIDATION / CHANGE WATCH

- **VALIDATION:** inspect the regression execution from exact workflow commit `e4c68d1418eb5cda6193dbbb98b1171031053153`; only award Safari runtime transfer if the semantic title oracle actually executes and passes.
- **OPEN:** whether non-interactive privileged enablement is permitted on the hosted macOS runner and, if so, whether Safari can establish a WebDriver session.
- **OPEN:** iOS/iPadOS Safari/EFB, physical device, offline/service-worker/update lifecycle, product-owned LogMate build, release/production artifact.
- **CHANGE WATCH:** Flutter Safari support matrix, Safari/WebDriver behavior, hosted macOS image and browser version.
- **OPEN:** fixture uses `dart:html`, a legacy/deprecated API surface; retain only as a narrow browser-observable probe, not product guidance.

## HANDOFFS

- Foundations: executions 1–2 add no Safari semantic runtime verdict; retain F001 Safari as OPEN pending actual semantic execution.
- Quality: prerequisite probes that may request interactive authorization must not precede non-interactive fallback/diagnostic collection in unattended CI.
- Systems: runner-level Safari automation enablement is an environment prerequisite; preserve exact hosted-image/browser identity and do not conflate it with artifact semantics.
- LogMate/Web Manager: no canonical files edited. A later product transfer must use the product-owned PWA build/post-build path and exact product ref rather than this fixture.
