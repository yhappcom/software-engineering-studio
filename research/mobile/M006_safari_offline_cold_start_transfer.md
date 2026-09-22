# M006 — Safari offline fetch/cache/cold-start transfer

Status: **IN STUDY — FAIL-CLOSED REGRESSION RED / FAILURE-STAGE DIAGNOSTIC RUN PENDING**  
Evidence date: 2026-09-23

## Problem / Balance Loop selection
The preceding macOS Safari block closed registration/update/controller/restart at bounded fixture scope, but explicitly left offline fetch/cache/cold-start OPEN. Across the six tracks this remains the strongest currently executable independent boundary: it has direct LogMate PWA leverage, crosses Mobile/Quality/Systems/Data concerns, and does not require unavailable physical devices or LogMate runner credentials.

## SOURCE
- Service-worker `fetch` events can intercept navigation/subresource requests and `respondWith()` a cached response; CacheStorage stores Request/Response pairs for this purpose (primary browser-platform evidence retained from the prior study, checked 2026-09-23).
- Safari/WebKit Service Worker behavior remains **CHANGE WATCH** because current Safari releases continue to ship Service Worker fixes.

## SYNTHESIS
Registration/control persistence is not evidence that a controlled application can actually boot when its origin is unreachable. A stronger offline claim requires: an online cache precondition, independent proof that the origin is unavailable, a fresh browser session, navigation while the origin remains unavailable, and a semantic app/controller oracle.

## Executable validation contract
**CLAIM:** on the recorded hosted macOS Safari environment, a same-origin service worker can precache the fixture shell, then after Safari is quit and the origin server is terminated, a newly created Safari WebDriver session can cold-navigate to the unavailable origin and execute the cached app under a service-worker controller.

**TARGET:** `research/mobile/fixtures/m006_safari_offline_cold_start/`; workflow `.github/workflows/m006-safari-offline-cold-start-validation.yml`.

**INPUT/STATE:** localhost origin `127.0.0.1:8770`; cache `m006-offline-v1`; assets `/`, `/index.html`, `/app.js`; online registration/control first; browser quit; origin process terminated; fresh Safari session; query-varied cold navigation.

**ORACLE:** fail-closed `validate.py` requires online app execution, online service-worker control, independent CacheStorage matches for shell + script, server-process termination plus an external Python HTTP probe that confirms the origin is unreachable, fresh `webdriver.Safari()`, offline navigation reaching `M006_APP_READY`, and a non-null service-worker controller. Workflow propagates the Python exit status through `tee`, requires non-empty oracle evidence, and requires the explicit PASS verdict.

**FAILURE MODEL:** cache population failure, control failure, false offline condition, browser-session-only state, navigation bypassing service worker, missing cached shell/script, cached document without controlled execution, WebDriver/setup failure, CI shell pipeline masking the oracle exit status, and diagnostic loss before the final verdict.

## VALIDATION
### Run 1 — invalid false-green
Initial target head `ad49f26ddae6cf547e13375f18987523661dfe18`; run `35754546136`; job `106836891047`; workflow conclusion `success`.

**CONTRADICTION / ROOT CAUSE:** run-bound artifact `10706289606` (`sha256:187a9abc72aa2967873dcec11a0cd8292101ea22e4e89e09d3ea2659fdb6972d`) contained environment and WebDriver-enable evidence but a zero-byte `oracle.json`. Environment: macOS 15.7.9 build 24G830, Safari/safaridriver 26.6.1; `ENABLE_RC=0`. The workflow executed `python validate.py | tee oracle.json` without `pipefail`; a non-zero Python semantic failure could therefore be masked by successful `tee`. The green workflow is **INVALID evidence** and awards no PASS/TRANSFER VALIDATION.

### Run 2 — fail-closed regression exposes a real unresolved semantic failure
Repair commit `18633c1410e59ece075f6aa4b6bc24f83d8be15c` added `set -o pipefail`, stderr capture, non-empty evidence assertion, and explicit PASS-verdict assertion. Exact-head run `35761385843`, job `106859999178`, runner `macos-15`, completed **failure**. Checkout, environment recording, Safari WebDriver enablement/Selenium provisioning and evidence upload all succeeded; the `Execute Safari offline cold-start oracle` step alone failed after about 76 seconds. Artifact `10709888786`, digest `sha256:74b4bb8ad8f7e83d719072a904f46528a11422058b663d0f5e6aacc72b22354a`, was preserved.

**VALIDATION:** the fail-closed repair works: the semantic failure can no longer produce green CI. However, the currently accessible GitHub evidence channel exposes run/job/artifact metadata but not the artifact ZIP or job-log payload, so the exact failing semantic stage must not be guessed.

**OPEN / diagnostic defect:** the validator only emitted its observation array on final PASS. If an assertion/timeout occurred earlier, useful stage observations could be lost. Commit `65add7b1eb2259ed0090fb4d1a79e39ac2f4d851` repairs this evidence defect by emitting `SAFARI_OFFLINE_COLD_START_FAIL`, the exception and all accumulated observations before re-raising. The next exact-head run is diagnostic, not a behavior fix: it must identify the first semantic failure before any service-worker logic is changed.

## ENGINEERING JUDGMENT
Run 2 is stronger evidence than the earlier false-green because it demonstrates that the primary oracle now controls the CI verdict. It is not evidence that Safari cannot cold-start a service-worker-controlled cached app generally. Until the first failing stage is preserved, the result is a bounded unresolved failure of this exact fixture/environment.

## EVIDENCE LIMIT
This fixture is not Flutter-generated and is not the LogMate post-build service worker. It does not validate product artifact provenance, cache eviction, quota pressure, physical networking/storage, iOS/iPadOS/EFB, installation as a Home Screen web app, release identity, or production.

## RELATED DOMAIN CHECK
- Foundations: browser/network/process boundaries checked; no new native-runtime claim.
- Architecture: offline boot remains an externally observable lifecycle contract; no architecture decision changed.
- Mobile: owner; Safari offline boundary remains OPEN after a real fail-closed semantic red.
- Data: CacheStorage is only an app-shell prerequisite, not application-data correctness/durability.
- Quality: false-green masking is fixed; run 2 proves fail-closed propagation. Diagnostic evidence must now survive the failure path, not only PASS.
- Systems: exact head/run/job/artifact identity retained; localhost fixture is not product provenance.
- Design Studio: considered; no visual/interaction contract changes this runtime claim.
- Web Manager: PWA/browser overlap considered; no website canonical edit required.
- Marketing Manager: not materially relevant.
- Product: retained context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → prior evidence 2026-09-20`; production identity unknown and default branch is not assumed production. Exact product execution is not claimed.

## OPEN / CHANGE WATCH
- OPEN: first semantic failure stage from the diagnostic regression at exact head `65add7b1...`.
- OPEN: Safari origin-down offline cold-start verdict; no PASS/TRANSFER VALIDATION.
- OPEN: exact LogMate `make build-pwa` artifact/runtime due source-acquisition authorization dependency.
- OPEN: physical/iOS/iPadOS/EFB offline behavior, eviction, storage/network failure diversity.
- CHANGE WATCH: Safari/WebKit Service Worker/CacheStorage behavior and hosted macOS runner image.

## HANDOFFS
- Quality: pipeline exit propagation is now executable-regression validated; require failure-path diagnostic preservation as part of high-value oracle design.
- Systems: later product transfer must use LogMate's product-owned `make build-pwa` path and bind source→toolchain→post-build transform→artifact→Safari environment.
- Data: do not infer application-data offline correctness from app-shell CacheStorage behavior.
