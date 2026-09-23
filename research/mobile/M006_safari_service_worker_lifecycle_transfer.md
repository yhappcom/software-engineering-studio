# M006 — Safari service-worker lifecycle transfer

Status: **IN STUDY — PRIOR TRANSFER VERDICT INVALIDATED BY RUN-BOUND ARTIFACT; FAIL-CLOSED REGRESSION PENDING**  
Evidence date: 2026-09-23

## Problem / Balance Loop selection
The bounded macOS Safari Flutter-JavaScript runtime transfer was already closed, while Safari PWA/service-worker lifecycle remained explicitly OPEN. This is a materially different evidence class from existing Chromium offline/restart/update/cold-start evidence and has direct LogMate PWA leverage. Physical iOS/iPadOS/EFB and exact-product PWA artifact remain separate boundaries.

## SOURCE
- WebKit Safari 26.6 release notes include Service Worker fixes, so this remains version-sensitive: https://webkit.org/blog/18178/webkit-features-for-safari-26-6/
- Service Worker lifecycle surfaces used by the fixture are `ServiceWorkerRegistration.update()` and `ServiceWorkerContainer.controllerchange`; these distinguish update discovery from acquisition of a new controller.

## SYNTHESIS
A successful generic Safari page/runtime probe does not establish Safari service-worker registration, activation, update, controller replacement, or persistence across a fresh WebDriver browser session. Existing Chromium lifecycle evidence therefore requires an independent WebKit transfer.

## Executable validation contract
**CLAIM:** on the recorded macOS Safari environment, a same-origin localhost fixture can register and become controlled by V1, detect a byte-different V2 through explicit `registration.update()`, transition control to V2, and retain the V2 registration/control across a fresh Safari WebDriver session.

**TARGET:** `research/mobile/fixtures/m006_safari_service_worker/`; workflow `.github/workflows/m006-safari-service-worker-validation.yml`.

**INPUT/STATE:** local server on `127.0.0.1:8769`; dynamic `/sw.js` served from fixture state; run begins V1, mutates worker body to V2, then quits and recreates Safari WebDriver.

**ORACLE:** exact committed `validate.py` requires V1 control, controller change, V2 control and V2 control after WebDriver recreation; timeout/exception exits nonzero and success emits `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS`.

## CONTRADICTION / evidence correction
The prior record treated exact head `d31cc310f7444a3b1880b1faae7901314a801a34`, run `35741047017`, job `106790579808`, terminal workflow success as bounded TRANSFER VALIDATION. That verdict is withdrawn.

The run-bound artifact `10698973958`, digest `sha256:3b103c6d08afcaf4dfae79add9fc56f292bf8c7b01797a78a7ddb85c634bcbb4`, was directly downloaded and inspected on 2026-09-23. It contains `enable.txt` (12 bytes), `server.log` (532 bytes), and **`oracle.json` (0 bytes)**. The server log shows initial page/service-worker requests but contains no semantic PASS evidence.

The workflow at that exact evidence lineage executed:

`python validate.py | tee "$RUNNER_TEMP/oracle.json"`

without `set -o pipefail`, without a non-empty artifact assertion, and without a semantic verdict assertion. Therefore a nonzero Python oracle could be masked by successful `tee`, exactly matching the Q006 false-green mechanism. A green job plus empty oracle is **INVALID evidence**, not PASS.

**CONTRADICTION:** the earlier claim that the semantic step was fail-closed was false at the workflow boundary. The Python process itself was fail-closed, but its exit status was not reliably propagated through the shell pipeline.

## Repair / VALIDATION
Commit `6daa9781cc884aab601744a5decf7a7459d06906` repairs the workflow with three independent controls:
1. `set -o pipefail` so Python failure propagates through `tee`;
2. `test -s "$RUNNER_TEMP/oracle.json"` so empty evidence cannot pass;
3. explicit grep for `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS` so a non-empty diagnostic payload cannot masquerade as semantic success.

The push-triggered regression for this exact repaired head must complete before any Safari service-worker lifecycle PASS/TRANSFER VALIDATION is restored. If it fails, preserve the failure stage and debug causally rather than weakening the oracle.

## ENGINEERING JUDGMENT
This correction has higher Quality/Systems value than preserving a convenient browser conclusion. Workflow success is not semantic evidence when verdict propagation is defective. Run-bound artifacts can invalidate a historical green result and must be treated as part of the evidence contract.

## EVIDENCE LIMIT
No current Safari service-worker registration/update/restart transfer claim is awarded from run `35741047017`. Chromium evidence and the separately validated Safari generic runtime/same-session offline observations are unaffected because they have separate evidence lineages. Even a future repaired PASS would not establish offline navigation/cache correctness, Flutter-generated service-worker compatibility, LogMate post-build service-worker semantics, iOS/iPadOS/EFB, physical networking/storage, eviction policy, release identity, or production behavior.

## RELATED DOMAIN CHECK
- Foundations: no native/iOS claim; historical browser evidence must preserve verdict lineage.
- Architecture: externally observable update/control states remain lifecycle contracts; no product architecture decision changed.
- Mobile: owner; Safari service-worker lifecycle transfer reopened.
- Data: no cache-data correctness or durability claim.
- Quality: Q006 verdict-propagation mechanism directly invalidated the historical green evidence.
- Systems: exact workflow head/run/job/artifact/digest retained; artifact inspection is provenance/evidence-integrity relevant.
- Design Studio: not materially relevant.
- Web Manager: PWA/browser overlap considered; no external canonical file edited.
- Marketing Manager: not materially relevant.
- Product: retained context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → prior evidence 2026-09-20`; production identity unknown and default branch is not assumed production. This fixture does not audit that product artifact.

## OPEN / CHANGE WATCH
- VALIDATION: repaired fail-closed Safari service-worker lifecycle regression at exact head `6daa9781...`.
- OPEN: Safari offline fetch/cache and cold-start-under-offline conditions beyond separately bounded same-session evidence.
- OPEN: exact LogMate `make build-pwa` artifact/runtime due existing source-acquisition dependency.
- OPEN: iOS/iPadOS/EFB and physical-device behavior.
- CHANGE WATCH: Safari/WebKit service-worker behavior and hosted macOS image.

## HANDOFFS
- Quality: historical green CI evidence can require reclassification when artifact inspection reveals missing semantic verdict; audit verdict propagation separately from log preservation.
- Systems: preserve run-bound artifact integrity as part of release/validation evidence; green metadata alone is insufficient.
- Web Manager / LogMate: no canonical files edited; no Safari service-worker lifecycle transfer should be consumed until repaired regression evidence exists.
