# M006 — Flutter JavaScript runtime transfer to Safari

Status: **IN STUDY — FIRST EXECUTION FAILED AT WEBDRIVER ENABLEMENT; SEMANTIC SAFARI ORACLE NOT EXECUTED**  
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

**SOURCE comparison:** Apple's current documentation confirms `safaridriver --enable` is the supported Terminal operation, with `sudo` only conditionally needed. This supports treating enablement as a harness/environment prerequisite, not as the target Flutter runtime verdict.

## FIX / regression target

Commit `ebd7030de8efb04cec71e3c888d202232cab6a70` changes the workflow so the enable boundary becomes diagnosable rather than opaque:

1. attempt `/usr/bin/safaridriver --enable` unprivileged and preserve stdout/stderr + return code;
2. only if that fails, attempt `sudo -n /usr/bin/safaridriver --enable` and preserve stdout/stderr + return code;
3. preserve Selenium installation return code;
4. emit a classified setup verdict;
5. include `safaridriver-enable.txt` in the always-uploaded run-bound artifact.

This does not weaken the gate. If both enable attempts fail, the job still fails and the Safari semantic oracle remains unexecuted. The purpose is failure isolation and reproducible diagnostics, not forcing green CI.

## Alternative comparison

Existing F001/M006 Chromium evidence remains the comparison context. Safari uses WebKit/Safari WebDriver rather than the prior Chrome execution path, so a successful run would be a materially different browser-engine transfer. It is not independent product replication because the fixture and hosted CI context remain Studio-controlled.

## RELATED DOMAIN CHECK

- Foundations: directly advances F001 browser/runtime transfer beyond Chromium; no new F001 PASS from execution 1.
- Architecture: no architecture decision changed; browser support remains an external runtime boundary.
- Mobile: owner; advances M006 browser-family coverage and now has a concrete setup failure boundary.
- Data: not materially tested; no persistence/durability claim.
- Quality: execution 1 demonstrates why setup/harness failure must remain separate from semantic target failure; missing stderr prevented root-cause assignment, and the regression target now preserves it.
- Systems: exact run/head/artifact/toolchain/browser identity is preserved; hosted runner configuration is part of the execution environment.
- Design Studio: no visual/interaction semantic contract evaluated.
- Web Manager: PWA/browser overlap considered; no website operational decision changed.
- Marketing Manager: not materially relevant.
- Product: no product runtime audit in this block. Existing motivation context remains `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence previously captured 2026-09-20`; production identity unknown and default branch is not assumed production.

## OPEN / VALIDATION / CHANGE WATCH

- **VALIDATION:** inspect the regression execution at exact commit `ebd7030d...`; only award Safari runtime transfer if the semantic title oracle actually executes and passes.
- **OPEN:** exact execution-1 WebDriver-enable root cause because stderr was not preserved.
- **OPEN:** iOS/iPadOS Safari/EFB, physical device, offline/service-worker/update lifecycle, product-owned LogMate build, release/production artifact.
- **CHANGE WATCH:** Flutter Safari support matrix, Safari/WebDriver behavior, hosted macOS image and browser version.
- **OPEN:** fixture uses `dart:html`, a legacy/deprecated API surface; retain only as a narrow browser-observable probe, not product guidance.

## HANDOFFS

- Foundations: execution 1 adds no Safari runtime verdict; retain F001 Safari as OPEN pending semantic execution.
- Quality: preserve prerequisite/setup stderr and return codes before classifying browser/runtime contradictions.
- Systems: runner-level Safari automation enablement is an environment prerequisite; preserve exact hosted-image/browser identity and do not conflate it with artifact semantics.
- LogMate/Web Manager: no canonical files edited. A later product transfer must use the product-owned PWA build/post-build path and exact product ref rather than this fixture.
