# M006 — Safari service-worker lifecycle transfer

Status: **BOUNDED TRANSFER VALIDATION COMPLETE — OFFLINE FETCH/COLD-START STILL OPEN**  
Evidence date: 2026-09-23

## Problem / Balance Loop selection
The bounded macOS Safari Flutter-JavaScript runtime transfer was already closed, while Safari PWA/service-worker lifecycle remained explicitly OPEN. This is a materially different evidence class from existing Chromium offline/restart/update/cold-start evidence and has direct LogMate PWA leverage. Physical iOS/iPadOS/EFB and exact-product PWA artifact remain separate boundaries.

## SOURCE
- WebKit Safari 26.6 release notes include Service Worker fixes, so this remains version-sensitive: https://webkit.org/blog/18178/webkit-features-for-safari-26-6/
- Service Worker lifecycle surfaces used by the fixture are `ServiceWorkerRegistration.update()` and `ServiceWorkerContainer.controllerchange`; these distinguish update discovery from acquisition of a new controller.

## SYNTHESIS
A successful generic Safari page/runtime probe does not establish Safari service-worker registration, activation, update, controller replacement, or persistence across a fresh WebDriver browser session. Existing Chromium lifecycle evidence therefore required an independent WebKit transfer.

## Executable validation contract
**CLAIM:** on the recorded macOS Safari environment, a same-origin localhost fixture can register and become controlled by V1, detect a byte-different V2 through explicit `registration.update()`, transition control to V2, and retain the V2 registration/control across a fresh Safari WebDriver session.

**TARGET:** `research/mobile/fixtures/m006_safari_service_worker/`; workflow `.github/workflows/m006-safari-service-worker-validation.yml`.

**INPUT/STATE:** local server on `127.0.0.1:8769`; dynamic `/sw.js` served from fixture state; run begins V1, mutates worker body to V2, then quits and recreates Safari WebDriver.

**ORACLE:** browser-owned Service Worker APIs drive document-title states. Exact committed `validate.py` requires `M006_SW_READY_V1`, an actual `M006_SW_CONTROLLER_CHANGED`, `M006_SW_READY_V2`, then `M006_SW_READY_V2` again after quitting and recreating Safari WebDriver. Timeout/exception exits nonzero. This is stronger than workflow-green alone because the semantic step is fail-closed.

**FAILURE MODEL:** registration unsupported/failure, activation/control failure, update not discovered, controller not replaced, V2 not controlling after refresh, registration/control unavailable in the fresh browser session, WebDriver/setup failure. Offline fetch/cold-start is intentionally not claimed.

## VALIDATION / TRANSFER VALIDATION
Exact head `d31cc310f7444a3b1880b1faae7901314a801a34`; GitHub Actions run `35741047017`; job `106790579808`; runner label `macos-15`; terminal **success** on 2026-09-22 UTC / 2026-09-23 KST. The job records Safari environment, successfully enables WebDriver/provisions isolated Selenium, executes the Safari service-worker lifecycle oracle for about 80 seconds, and preserves evidence.

Run-bound artifact: `10698973958`, name `m006-safari-service-worker-35741047017`, digest `sha256:3b103c6d08afcaf4dfae79add9fc56f292bf8c7b01797a78a7ddb85c634bcbb4`, bound by GitHub to the same run/head.

**VERDICT — TRANSFER VALIDATION:** the bounded lifecycle claim passes on this macOS Safari/WebKit execution context. This transfers registration/control, byte-different explicit update, controller replacement, and fresh-WebDriver-session registration/control persistence from the previously validated Chromium class to Safari/WebKit at fixture scope.

The current connector exposed run/job/artifact metadata and the exact fail-closed oracle, but not the artifact ZIP payload in this run. Therefore individual polling observations and exact Safari version emitted by the environment step are not invented here; the semantic step's success is evidence only for the assertions encoded in the committed oracle.

## ENGINEERING JUDGMENT
The fresh WebDriver session is useful browser-session lifecycle evidence, but it is not a machine restart, storage eviction, physical-device lifecycle, or offline-network test. Service-worker registration/control persistence must remain distinct from cached-resource correctness and offline navigation.

## EVIDENCE LIMIT
This PASS does not establish offline navigation/cache correctness, Flutter-generated service-worker compatibility, LogMate post-build service-worker semantics, iOS/iPadOS/EFB, physical networking/storage, eviction policy, release identity, or production behavior. It is not independent REPLICATION because it uses the same Studio fixture family and hosted macOS execution class as the preceding Safari runtime work.

## RELATED DOMAIN CHECK
- Foundations: materially extends browser runtime/lifecycle transfer; no native/iOS claim.
- Architecture: externally observable update/control states are lifecycle contracts; no architecture decision changed.
- Mobile: owner; named Safari registration/update/restart lifecycle gap closed at bounded transfer scope.
- Data: no cache-data correctness or durability claim.
- Quality: fail-closed multi-stage semantic oracle completed; workflow success is interpreted only through exact committed assertions.
- Systems: exact workflow head/run/job/artifact/digest retained; localhost fixture is not product artifact provenance.
- Design Studio: not materially relevant; no visual/interaction contract tested.
- Web Manager: PWA/browser overlap is relevant; result is an engineering constraint, not a website operational decision. No external repo edited.
- Marketing Manager: not materially relevant.
- Product: retained context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → prior evidence 2026-09-20`; production identity unknown and default branch is not assumed production. This fixture does not audit that product artifact.

## OPEN / CHANGE WATCH
- OPEN: Safari offline fetch/cache and cold-start-under-offline conditions.
- OPEN: exact LogMate `make build-pwa` artifact/runtime due existing source-acquisition dependency.
- OPEN: iOS/iPadOS/EFB and physical-device behavior.
- CHANGE WATCH: Safari/WebKit service-worker behavior and hosted macOS image.

## HANDOFFS
- Quality: preserve the exact semantic stages; do not reduce this to workflow-green evidence.
- Systems: product transfer still requires product-owned `make build-pwa` path and artifact provenance.
- Web Manager / LogMate: no canonical files edited; later product transfer should treat Safari update/control behavior as an implementation constraint, not a web/product decision made here.
