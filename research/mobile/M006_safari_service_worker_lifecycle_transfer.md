# M006 — Safari service-worker lifecycle transfer

Status: **IN STUDY — FALSE-GREEN CORRECTED; INITIAL AND RESTART NAVIGATION ORACLES ISOLATED; REPAIRED REGRESSION PENDING**  
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

**ORACLE:** browser-owned `navigator.serviceWorker.controller` is the cross-navigation control oracle. Worker version is then queried by a fresh `registerSW()` invocation in the controlled document. Update additionally requires `controllerchange`; fresh-session persistence requires restored controller state followed by an independent V2 query. Timeout/exception emits structured FAIL evidence and exits nonzero; success emits `SAFARI_SW_REGISTER_UPDATE_RESTART_PASS`.

## CONTRADICTION 1 — historical false green
Historical exact head `d31cc310f7444a3b1880b1faae7901314a801a34`, run `35741047017`, job `106790579808` is INVALID evidence. Artifact `10698973958`, digest `sha256:3b103c6d08afcaf4dfae79add9fc56f292bf8c7b01797a78a7ddb85c634bcbb4`, contained a zero-byte `oracle.json`; the workflow piped the producer through `tee` without `pipefail` or an independent verdict assertion.

## Repair 1 — fail-closed workflow
Commit `6daa9781cc884aab601744a5decf7a7459d06906` added `set -o pipefail`, non-empty oracle enforcement, and explicit semantic verdict enforcement. Run `35802543585`, job `106995919837` then failed honestly. Artifact `10726377605`, digest `sha256:67483e7b00559f54792f606f5f906ed55b82b8703c2ce63cc6c22326ca63cdcd`, retained successful WebDriver enablement and initial page/worker requests but an empty stdout oracle.

## ROOT CAUSE 1 — initial-control oracle lifecycle mismatch
`registerSW()` can reload an initially uncontrolled document after readiness. The pre-navigation JavaScript invocation cannot continue afterward, so waiting for its later `M006_SW_READY_V1` title was lifecycle-invalid. Commit `4f7e376572a6fe8c6eddea40e4d95841c4ce2033` repaired the first boundary by polling browser-owned controller state across navigation, then re-invoking `registerSW()` in the controlled document to query V1. It also added structured failure observations.

## VALIDATION — run 3 isolates the restart boundary
Exact repaired head `4f7e376572a6fe8c6eddea40e4d95841c4ce2033`, run `35806396805`, completed **failure**. Run-bound artifact `10727414954`, digest `sha256:4fd3600dd74ed8eb80e5bebc1215d9c00fbf89f3ada7427a06a743a94d40d126`, was directly inspected.

The structured oracle proves substantial positive lifecycle behavior before the failure:
- initial controller changed `false → true`;
- an independent controlled-document query confirmed `M006_SW_READY_V1`;
- explicit update observed `controllerchange` and confirmed `M006_SW_READY_V2`;
- after quitting and recreating Safari WebDriver, the old validator repeatedly observed title `M006_SW_BOOT` and timed out waiting for `M006_SW_READY_V2`.

Server evidence also shows page and worker requests across the sequence. This red result therefore moves the first unresolved point to the fresh-session restart oracle; it does **not** invalidate the observed V1 registration/control or V2 update/controller-change evidence.

## ROOT CAUSE 2 — restart oracle repeats the same navigation-lifetime defect
Exact validator inspection shows the fresh-session branch executed `d.get(...); registerSW();` and then waited directly for `M006_SW_READY_V2`. A recreated WebDriver document can again begin uncontrolled while discovering the persisted registration; `registerSW()` can reload that document, destroying the invocation before it can set the V2 title. The repeated `M006_SW_BOOT` observation is consistent with the post-reload document and is not, by itself, evidence that registration/update state failed to persist.

This is a harness ROOT CAUSE for the run-3 timeout expectation. It is not yet a PASS for fresh-session persistence.

## Repair 3 — lifecycle-aligned restart persistence oracle
Commit `54bbd5283920aa3d82057cc2da8a14b0db4bacbf` applies the same lifecycle discipline to the recreated session:
1. navigate and invoke `registerSW()`;
2. poll browser-owned `navigator.serviceWorker.controller` as `restart-controller-persistence` across any reload;
3. invoke `registerSW()` again in the now-controlled document;
4. require `M006_SW_READY_V2` as an independent persisted-version query.

Push-triggered regression run `35810765603` is in progress. No Safari service-worker lifecycle PASS/TRANSFER VALIDATION is awarded until its terminal status and run-bound semantic artifact agree.

## ENGINEERING JUDGMENT
Three evidence defects were exposed sequentially: workflow verdict propagation, initial-document lifecycle, and restart-document lifecycle. The useful invariant is broader than Safari: when the target operation can navigate/reload, the test must separate browser/runtime-owned lifecycle state from application-owned presentation state tied to a destroyed document. A fresh session is not a justification for reverting to a pre-navigation title oracle.

## EVIDENCE LIMIT
Current evidence validates bounded V1 control and V2 update/controllerchange within run 3, but the combined registration/update/restart claim remains OPEN until run 4. Chromium evidence and separately validated Safari generic runtime/same-session origin-down offline evidence have separate lineages. No result here establishes Flutter-generated service-worker compatibility, LogMate post-build semantics, iOS/iPadOS/EFB, physical networking/storage, eviction, release identity, or production behavior.

## RELATED DOMAIN CHECK
- Foundations: navigation destroys document-owned execution/presentation state; direct Dart/Flutter evidence already exists and is not the blocker.
- Architecture: registration, control, update/controller replacement, and browser-session persistence are distinct lifecycle contracts.
- Mobile: owner; combined Safari lifecycle transfer remains OPEN.
- Data: no application-data durability/cache-correctness claim.
- Quality: Q006 verdict propagation transferred naturally; lifecycle-valid oracle state must match the owner/lifetime of the property.
- Systems: exact head/run/artifact/digest and semantic artifact content retained separately from workflow metadata.
- Design Studio: not materially relevant to this runtime oracle correction.
- Web Manager: PWA/browser overlap considered; no external canonical file edited.
- Marketing Manager: not materially relevant.
- Product: retained context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → prior evidence 2026-09-20`; production identity unknown and default branch is not assumed production. This fixture does not audit that product artifact.

## OPEN / CHANGE WATCH
- VALIDATION: restart-aligned regression run `35810765603`, exact head `54bbd528...`.
- OPEN: exact LogMate `make build-pwa` artifact/runtime due existing source-acquisition dependency.
- OPEN: ordinary Safari profile/relaunch, installed PWA, iOS/iPadOS/EFB and physical-device behavior.
- CHANGE WATCH: Safari/WebKit service-worker behavior and hosted macOS image.

## HANDOFFS
- Quality: navigation/reload-spanning tests need lifecycle-owner-aligned oracles at every navigation boundary, including restart/recreated-session branches; a repaired first navigation does not validate later ones.
- Systems: green metadata, subprocess status, semantic artifact content, and lifecycle validity remain separate evidence controls.
- Web Manager / LogMate: no canonical files edited; do not consume a combined Safari service-worker lifecycle transfer verdict until run 4 evidence is inspected.
