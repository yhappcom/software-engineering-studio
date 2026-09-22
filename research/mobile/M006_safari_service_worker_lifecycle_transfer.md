# M006 — Safari service-worker lifecycle transfer

Status: **IN STUDY — EXECUTABLE RUN PENDING**  
Evidence date: 2026-09-22

## Problem / Balance Loop selection
The bounded macOS Safari Flutter-JavaScript runtime transfer is closed, while Safari PWA/service-worker lifecycle remains explicitly OPEN. This is a materially different evidence class from the existing Chromium offline/restart/update/cold-start evidence and has direct LogMate PWA leverage. Physical iOS/iPadOS/EFB and exact-product PWA artifact remain separate boundaries.

## SOURCE
- WebKit Safari 26.6 release notes (2026-07-27) include current Service Worker fixes, confirming this area remains version-sensitive: https://webkit.org/blog/18178/webkit-features-for-safari-26-6/
- Service Worker specification surface as summarized by MDN: `ServiceWorkerRegistration.update()` fetches/checks an updated worker and installs when the script differs; `updatefound`/worker state and `controllerchange` expose lifecycle transitions: https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/update and https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/controllerchange_event

## SYNTHESIS
A successful generic Safari page/runtime probe does not establish Safari service-worker registration, activation, update, controller replacement, or persistence across a fresh WebDriver browser session. Existing Chromium lifecycle evidence must not be silently transferred to WebKit.

## Executable validation contract
**CLAIM:** on the recorded macOS Safari environment, a same-origin localhost fixture can register and become controlled by V1, detect a byte-different V2 through explicit `registration.update()`, transition control to V2, and retain the V2 registration/control across a fresh Safari WebDriver session.

**TARGET:** `research/mobile/fixtures/m006_safari_service_worker/`; workflow `.github/workflows/m006-safari-service-worker-validation.yml`.

**INPUT/STATE:** local server on `127.0.0.1:8769`; dynamic `/sw.js` is served `no-store`; run begins V1, mutates server worker body to V2, then opens a fresh Safari WebDriver session.

**ORACLE:** browser-owned Service Worker APIs drive document-title states. The Python WebDriver oracle independently requires `M006_SW_READY_V1`, an actual `controllerchange`, then `M006_SW_READY_V2`, then `M006_SW_READY_V2` again after quitting and recreating Safari WebDriver. Any timeout/exception exits nonzero. Observation timeline is uploaded as a run-bound artifact.

**FAILURE MODEL:** registration unsupported/failure, activation/control failure, update not discovered, controller not replaced, V2 not controlling after refresh, registration/control not available in the fresh browser session, WebDriver/setup failure. Offline fetch/cold-start is intentionally not claimed by this first Safari lifecycle block.

**EVIDENCE LIMIT:** even a PASS will not establish offline navigation/cache correctness, Flutter-generated service-worker compatibility, LogMate post-build service worker semantics, iOS/iPadOS/EFB, physical networking/storage, eviction policy, release identity, or production behavior.

## Current execution
Exact workflow head `d31cc310f7444a3b1880b1faae7901314a801a34`; GitHub Actions run `35741047017` was **queued** when recorded. No PASS, TRANSFER VALIDATION, REPLICATION, or CONTRADICTION is awarded before semantic execution evidence is available.

## RELATED DOMAIN CHECK
- Foundations: service-worker/browser lifecycle is a runtime boundary; no new F001 claim yet.
- Architecture: externally observable update/control states are lifecycle contracts; no architecture decision changed.
- Mobile: owner; closes a named M006 Safari lifecycle gap if executable evidence succeeds.
- Data: no durability/cache-data correctness claim.
- Quality: fail-closed multi-stage semantic oracle; failure must be isolated before causal claims.
- Systems: exact workflow head/run and later artifact identity must be retained; localhost fixture is not product artifact provenance.
- Design Studio: not materially relevant; no visual/interaction contract tested.
- Web Manager: PWA/browser overlap is materially relevant, but no website operational decision is changed and no external repo is edited.
- Marketing Manager: not materially relevant.
- Product: existing exact LogMate context remains `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → prior evidence 2026-09-20`; production identity unknown. This fixture does not audit that product artifact.

## OPEN / CHANGE WATCH
- VALIDATION: run `35741047017` semantic result and artifact.
- OPEN: Safari offline fetch/cold-start/update-under-offline conditions.
- OPEN: exact LogMate `make build-pwa` artifact/runtime due existing source-acquisition dependency.
- OPEN: iOS/iPadOS/EFB and physical-device behavior.
- CHANGE WATCH: Safari/WebKit service-worker behavior and hosted macOS image.

## HANDOFFS
- Quality: preserve stage-specific observations; workflow green alone is insufficient if semantic oracle is weakened.
- Systems: if this fixture passes, product transfer still requires the product-owned `make build-pwa` path and artifact provenance.
- Web Manager / LogMate: no canonical files edited; later transfer should treat Safari update/control behavior as an implementation constraint, not a web/product decision made here.
