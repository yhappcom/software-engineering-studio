# M006 — Flutter JavaScript runtime transfer to Safari

Status: **BOUNDED macOS SAFARI TRANSFER VALIDATED; iOS/iPadOS/EFB/PRODUCT REMAIN OPEN**  
Evidence date: 2026-09-22

## Problem and Balance Loop selection

The preceding M003 API-35 emulator permission/FGS causal boundary is closed at bounded transfer scope. Across remaining Stage-1 gaps, Safari is a materially different browser/runtime family and directly advances both F001 cross-runtime execution and M006 PWA/browser knowledge without pretending to provide physical iOS/iPadOS or product evidence.

This block therefore selected a bounded **Flutter JavaScript artifact → macOS Safari WebDriver → async runtime oracle**. It does not claim iOS/iPadOS/EFB, PWA offline/update behavior, or LogMate product equivalence.

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

**ORACLE:** Safari WebDriver reads the browser-owned document title until `M006_ASYNC_READY` or a 30-second deadline. Browser capabilities plus Flutter/Dart/macOS/Safari/safaridriver identities are recorded. This oracle is deliberately outside Flutter widget-test machinery. The workflow exits nonzero when the semantic verdict is not `SAFARI_FLUTTER_JS_ASYNC_READY`.

**EVIDENCE LIMIT:** a pass establishes only bounded macOS Safari execution of this generated JavaScript fixture. It does not establish CanvasKit rendering correctness, accessibility, service-worker/PWA offline semantics, storage durability, iOS/iPadOS Safari, EFB policy, physical networking, LogMate artifact behavior, product release identity, or production behavior.

## Failure → isolation → repair chain

### Execution 1
Exact workflow head `1335d4b2892c66f86ff9a6fab6883518316ec2a0`, run `35705327847`, terminal failure before semantic execution. Flutter installation, environment capture and release web build completed; WebDriver setup failed. Artifact `10684121767`, digest `sha256:091321fa9c99574cbff21b5354b68e26e4a856af1f2d6c77d5b1d8392076e5b2`, recorded Flutter 3.47.5 / Dart 3.13.4 / macOS 15.7.9 build 24G830 / Safari 26.6.1 / safaridriver 20624.5.1.18.3.

### Execution 2
Exact head `ebd7030de8efb04cec71e3c888d202232cab6a70`, run `35710948055`, artifact `10686147472`, digest `sha256:c4d2baf7c21c0833467889ac59491b20a4aff445334daf914e4d040027128549`. The unprivileged enable command entered an interactive authorization path (`Password is not valid`), so the unattended harness could not reach its intended fallback. **ROOT CAUSE (bounded harness failure):** interactive-first prerequisite probing was incompatible with hosted CI. Commit `e4c68d1418eb5cda6193dbbb98b1171031053153` changed the probe to noninteractive `sudo -n` and preserved diagnostics.

### Execution 3
Exact head `e4c68d1418eb5cda6193dbbb98b1171031053153`, run `35716201875`, artifact `10690100321`, digest `sha256:def6b87ba8d1bab89eb3bd749eb0cdf277a45f36a7d243291141e2edf369ef47`, terminal failure. Later artifact inspection established that `sudo -n /usr/bin/safaridriver --enable` actually returned `ENABLE_RC=0`; the failure was subsequent Selenium provisioning through system/Homebrew Python under PEP 668 externally-managed-environment policy. **ROOT CAUSE (bounded harness failure):** dependency provisioning strategy, not Safari enablement or Flutter/Safari semantics. Commit `44c8be44bb53f2b67c08f40a0738f29858018bdd` moved Selenium into an isolated `$RUNNER_TEMP/m006-venv` and kept setup fail-closed.

## Execution 4 — semantic regression PASS

Exact workflow head: `44c8be44bb53f2b67c08f40a0738f29858018bdd`.  
GitHub Actions run: `35727646652`; job `106745123287`; runner label `macos-15`; terminal conclusion **success**.  
Run-bound artifact: `10694445918`, digest `sha256:f1274228bdbfaf29b6eca507a6e490385dbf3756777ce7e130007ecbb75bdf35`.

**OBSERVATION:** every material step completed successfully: toolchain/Safari identity capture, release JavaScript build, noninteractive Safari WebDriver enablement plus isolated Selenium provisioning, `Execute Safari runtime oracle`, and run-bound evidence preservation. The exact committed oracle creates a real `webdriver.Safari` session, loads the local release artifact, polls browser-owned `driver.title`, and exits nonzero unless the final semantic verdict is `SAFARI_FLUTTER_JS_ASYNC_READY`. Therefore the terminal-success semantic step is executable evidence that this bounded Safari session observed the delayed Dart transition.

**VALIDATION:** the run-3 PEP 668 provisioning repair has regression evidence, and the named macOS Safari runtime claim receives bounded **TRANSFER VALIDATION** relative to the prior Chromium execution path. Safari/WebKit is a materially different browser engine/context, while the fixture remains Studio-controlled. This is not independent product REPLICATION and not production evidence.

**EVIDENCE ACCESS LIMIT:** the GitHub API exposed exact run/job/step status and artifact identity/digest, but the connector could not download the artifact ZIP in this run. Do not invent the per-poll observation sequence or browser capability payload. The semantic verdict is nevertheless mechanically bound to the successful oracle step by the committed fail-closed workflow.

## Alternative comparison

Existing F001/M006 Chromium evidence is the comparison context. Safari uses WebKit/Safari WebDriver rather than the prior Chrome execution path. The successful run therefore adds a materially different browser-engine transfer, not a second claim that all PWA semantics are equivalent across browsers.

## RELATED DOMAIN CHECK

- Foundations: directly advances F001 browser/runtime transfer beyond Chromium; direct Dart JIT/AOT and host→Chrome evidence remain retained.
- Architecture: no architecture decision changed; browser support remains an external runtime boundary.
- Mobile: owner; bounded macOS Safari semantic execution is now validated.
- Data: not materially tested; no persistence/durability claim.
- Quality: failure→isolation→repair→regression chain now includes both interactive prerequisite and PEP 668 provisioning defects plus a green semantic oracle.
- Systems: exact run/head/job/artifact/digest identity is preserved; hosted runner and browser/toolchain remain environment-specific.
- Design Studio: no visual/interaction semantic contract evaluated.
- Web Manager: PWA/browser overlap considered; no website operational decision changed.
- Marketing Manager: not materially relevant.
- Product: no product runtime audit in this block. Existing context remains `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence previously captured 2026-09-20`; production identity unknown and default branch is not assumed production.

## OPEN / VALIDATION / CHANGE WATCH

- **VALIDATION CLOSED at bounded scope:** macOS Safari WebDriver session + Flutter release-JavaScript async semantic transition.
- **OPEN:** iOS/iPadOS Safari/EFB and physical-device browser behavior.
- **OPEN:** service-worker/offline/update lifecycle in Safari; the existing Chromium PWA evidence does not transfer automatically.
- **OPEN:** product-owned LogMate `make build-pwa` artifact/runtime, release/production artifact and production identity.
- **OPEN:** physical networking/storage behavior and Safari accessibility/rendering semantics.
- **CHANGE WATCH:** Flutter Safari support matrix, Safari/WebDriver behavior, hosted macOS image and browser version.
- **OPEN:** fixture uses `dart:html`, a legacy/deprecated API surface; retain only as a narrow browser-observable probe, not product guidance.

## HANDOFFS

- Foundations: record macOS Safari as a bounded F001 browser/runtime TRANSFER VALIDATION; do not infer iOS/iPadOS/native/product execution.
- Quality: retain the full setup-failure chain; a green final run is meaningful because the semantic step is fail-closed, not merely because the workflow is green.
- Systems: artifact/run provenance is sufficient to bind the bounded Studio claim, but product artifact provenance still requires the product-owned build path and exact source authorization.
- LogMate/Web Manager: no canonical files edited. A later product transfer must use the product-owned PWA build/post-build path and exact product ref rather than this fixture.
