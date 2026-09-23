# M006 — Safari service-worker lifecycle transfer

Status: **IN STUDY — FALSE-GREEN CORRECTED; FAIL-CLOSED REGRESSION EXPOSED INITIAL-CONTROL ORACLE DEFECT; REPAIRED REGRESSION PENDING**  
Evidence date: 2026-09-23

## Problem / Balance Loop selection
The bounded macOS Safari Flutter-JavaScript runtime transfer was already closed, while Safari PWA/service-worker lifecycle remained explicitly OPEN. This is a materially different evidence class from existing Chromium offline/restart/update/cold-start evidence and has direct LogMate PWA leverage. Physical iOS/iPadOS/EFB and exact-product PWA artifact remain separate boundaries.

## SOURCE
- WebKit Safari 26.6 release notes include Service Worker fixes, so this remains version-sensitive: https://webkit.org/blog/18178/webkit-features-for-safari-26-6/
- Service Worker lifecycle surfaces used by the fixture are `ServiceWorkerRegistration.update()`, `ServiceWorkerContainer.controller`, and `controllerchange`; update discovery, acquisition of control, and controller replacement are distinct states.

## SYNTHESIS
A successful generic Safari page/runtime probe does not establish Safari service-worker registration, activation, update, controller replacement, or persistence across a fresh WebDriver browser session. Existing Chromium lifecycle evidence therefore requires an independent WebKit transfer.

## Executable validation contract
**CLAIM:** on the recorded macOS Safari environment, a same-origin localhost fixture can register and become controlled by V1, detect a byte-different V2 through explicit `registration.update()`, transition control to V2, and retain V2 registration/control across a fresh Safari WebDriver session.

**TARGET:** `research/mobile/fixtures/m006_safari_service_worker/`; workflow `.github/workflows/m006-safari-service-worker-validation.yml`.

**INPUT/STATE:** local server on `127.0.0.1:8769`; dynamic `/sw.js` served from fixture state; run begins V1, mutates worker body to V2, then quits and recreates Safari WebDriver.

**ORACLE:** exact committed `validate.py` uses browser-owned `navigator.serviceWorker.controller` for the first post-registration control boundary, then independently queries V1 in the controlled document, requires `controllerchange`, confirms V2, and confirms V2 after WebDriver recreation. Timeout/exception emits a structured FAIL payload and exits nonzero; success emits `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS`.

## CONTRADICTION 1 — historical false green
The prior record treated exact head `d31cc310f7444a3b1880b1faae7901314a801a34`, run `35741047017`, job `106790579808`, terminal workflow success as bounded TRANSFER VALIDATION. That verdict is withdrawn.

Run-bound artifact `10698973958`, digest `sha256:3b103c6d08afcaf4dfae79add9fc56f292bf8c7b01797a78a7ddb85c634bcbb4`, contained **`oracle.json` at 0 bytes**. The exact workflow used `python validate.py | tee ...` without `pipefail` or an independent semantic verdict assertion. Q006 therefore transferred naturally: the historical green was INVALID evidence.

## Repair 1 — fail-closed workflow
Commit `6daa9781cc884aab601744a5decf7a7459d06906` added `set -o pipefail`, a non-empty oracle assertion, and explicit `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS` enforcement.

### VALIDATION / failure observation
Fail-closed regression run `35802543585`, job `106995919837`, exact head `6daa9781cc884aab601744a5decf7a7459d06906`, completed **failure** on `macos-15`. Setup, Safari WebDriver enablement and evidence upload succeeded; only `Execute Safari service-worker lifecycle oracle` failed. Artifact `10726377605`, digest `sha256:67483e7b00559f54792f606f5f906ed55b82b8703c2ce63cc6c22326ca63cdcd`, was directly inspected: `enable.txt` records `ENABLE_RC=0`, `oracle.json` is 0 bytes, and `server.log` shows the initial page plus `/sw.js` requests. This is now a trustworthy red gate, but the empty stdout artifact alone does not identify Safari as the cause.

## ROOT CAUSE — initial-control oracle lifecycle mismatch
Exact fixture inspection isolates a harness defect before any Safari lifecycle conclusion. `registerSW()` registers the worker, waits for readiness, and if the current document is still uncontrolled executes `location.reload(); return;`. The Python validator invoked `registerSW()` once and then waited for the application-owned title `M006_SW_READY_V1`. That original JavaScript invocation cannot continue across the navigation, and the reloaded document does not automatically call `registerSW()` again. Therefore the expected V1 title is not a valid first-control oracle for this fixture.

This is the same class of lifecycle-oracle error previously exposed in the Safari offline study: a navigation destroys document-owned execution/presentation state. The first control boundary must be observed from browser-owned state that survives the navigation relationship, not from an invocation that was terminated by the reload.

## Repair 2 — lifecycle-aligned semantic oracle
Commit `4f7e376572a6fe8c6eddea40e4d95841c4ce2033` changes only the validation harness semantics:
1. invoke initial registration;
2. poll `Boolean(navigator.serviceWorker.controller)` to establish control after the possible reload;
3. invoke `registerSW()` again in the controlled document and require `M006_SW_READY_V1` to independently query V1;
4. retain the V2 explicit-update/controllerchange, refresh/V2, and fresh-WebDriver V2-persistence checks;
5. emit structured FAIL observations/traceback before re-raising so future red runs preserve the first semantic failure stage.

The push-triggered regression for this repaired exact head is pending. No Safari service-worker lifecycle PASS or TRANSFER VALIDATION is awarded until terminal status and run-bound semantic artifact agree.

## ENGINEERING JUDGMENT
Two independent validation defects were exposed in sequence: shell verdict propagation and a document-lifecycle-invalid oracle. Fixing the first correctly converted a convenient false green into a useful red result; the red result then exposed the second defect. This is stronger engineering evidence than weakening the oracle to recover green status.

## EVIDENCE LIMIT
No current Safari service-worker registration/update/restart transfer claim is awarded. Chromium evidence and separately validated Safari generic runtime/same-session origin-down offline observations are unaffected because they have separate evidence lineages. Even a future repaired PASS would not establish Flutter-generated service-worker compatibility, LogMate post-build service-worker semantics, iOS/iPadOS/EFB, physical networking/storage, eviction policy, release identity, or production behavior.

## RELATED DOMAIN CHECK
- Foundations: browser/document lifecycle invalidates presentation-state assumptions across navigation; no native claim.
- Architecture: registration, control, controller replacement and browser-session persistence are distinct lifecycle contracts.
- Mobile: owner; Safari service-worker lifecycle transfer remains OPEN.
- Data: no cache-data correctness or durability claim.
- Quality: Q006 verdict propagation transferred naturally; lifecycle-aligned oracle independence is now additionally required.
- Systems: exact workflow head/run/job/artifact/digest retained; artifact semantic content is part of provenance.
- Design Studio: not materially relevant.
- Web Manager: PWA/browser overlap considered; no external canonical file edited.
- Marketing Manager: not materially relevant.
- Product: retained context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → prior evidence 2026-09-20`; production identity unknown and default branch is not assumed production. This fixture does not audit that product artifact.

## OPEN / CHANGE WATCH
- VALIDATION: repaired lifecycle-aligned Safari service-worker regression at exact head `4f7e3765...`.
- OPEN: exact LogMate `make build-pwa` artifact/runtime due existing source-acquisition dependency.
- OPEN: ordinary Safari profile/relaunch, iOS/iPadOS/EFB and physical-device behavior.
- CHANGE WATCH: Safari/WebKit service-worker behavior and hosted macOS image.

## HANDOFFS
- Quality: navigation/reload-spanning tests must not use destroyed document-owned presentation state as the sole lifecycle oracle; preserve browser/runtime-owned state and structured failure observations.
- Systems: green metadata, subprocess status, and run-bound semantic artifact are separate evidence controls.
- Web Manager / LogMate: no canonical files edited; do not consume a Safari service-worker lifecycle transfer verdict until repaired regression evidence exists.
