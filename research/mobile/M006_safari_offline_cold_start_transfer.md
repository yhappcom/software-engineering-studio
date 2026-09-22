# M006 — Safari offline fetch/cache/cold-start transfer

Status: **IN STUDY — FIRST RUN INVALID / FAIL-CLOSED REGRESSION PENDING**  
Evidence date: 2026-09-23

## Problem / Balance Loop selection
The preceding macOS Safari block closed registration/update/controller/restart at bounded fixture scope, but explicitly left offline fetch/cache/cold-start OPEN. Across the six tracks this is the strongest currently executable independent boundary: it has direct LogMate PWA leverage, crosses Mobile/Quality/Systems/Data concerns, and does not require unavailable physical devices or LogMate runner credentials.

## SOURCE
- Service-worker `fetch` events can intercept navigation/subresource requests and `respondWith()` a cached response; CacheStorage stores Request/Response pairs for this purpose (MDN Service Worker/Cache documentation, checked 2026-09-23).
- WebKit Safari 26.6 release notes dated 2026-07-27 include Service Worker fixes, so operational behavior remains **CHANGE WATCH**.

## SYNTHESIS
Registration/control persistence is not evidence that a controlled application can actually boot when its origin is unreachable. A stronger offline claim requires: an online cache precondition, independent proof that the origin is unavailable, a fresh browser session, navigation while the origin remains unavailable, and a semantic app/controller oracle.

## Executable validation contract
**CLAIM:** on the recorded hosted macOS Safari environment, a same-origin service worker can precache the fixture shell, then after Safari is quit and the origin server is terminated, a newly created Safari WebDriver session can cold-navigate to the unavailable origin and execute the cached app under a service-worker controller.

**TARGET:** `research/mobile/fixtures/m006_safari_offline_cold_start/`; workflow `.github/workflows/m006-safari-offline-cold-start-validation.yml`.

**INPUT/STATE:** localhost origin `127.0.0.1:8770`; cache `m006-offline-v1`; assets `/`, `/index.html`, `/app.js`; online registration/control first; browser quit; origin process terminated; fresh Safari session; query-varied cold navigation.

**ORACLE:** fail-closed `validate.py` requires online app execution, online service-worker control, independent CacheStorage matches for shell + script, server-process termination plus an external Python HTTP probe that confirms the origin is unreachable, fresh `webdriver.Safari()`, offline navigation reaching `M006_APP_READY`, and a non-null service-worker controller. Any missing stage raises/nonzero. Workflow must propagate the Python exit status through `tee`, require non-empty oracle evidence, and require the explicit PASS verdict.

**FAILURE MODEL:** cache population failure, control failure, false offline condition, browser-session-only state, navigation bypassing service worker, missing cached shell/script, cached document without controlled execution, WebDriver/setup failure, and CI shell pipeline masking the oracle exit status. It does not simulate OS-wide network loss; it proves origin unreachability for the target origin by terminating its only server and independently probing failure.

## VALIDATION
Initial target head `ad49f26ddae6cf547e13375f18987523661dfe18`; run `35754546136`; job `106836891047`; workflow conclusion `success`.

**CONTRADICTION / ROOT CAUSE:** the run-bound artifact `10706289606` (`sha256:187a9abc72aa2967873dcec11a0cd8292101ea22e4e89e09d3ea2659fdb6972d`) contains environment and WebDriver-enable evidence but a zero-byte `oracle.json`. Environment: macOS 15.7.9 build 24G830, Safari/safaridriver 26.6.1; `ENABLE_RC=0`. The workflow executed `python validate.py | tee oracle.json` without `pipefail`; therefore a non-zero Python semantic failure could be masked by successful `tee`. The green workflow is **INVALID evidence** and awards no PASS/TRANSFER VALIDATION.

**VALIDATION repair:** commit `18633c1410e59ece075f6aa4b6bc24f83d8be15c` adds `set -o pipefail`, captures stderr with stdout, requires a non-empty oracle file, and requires the explicit `SAFARI_OFFLINE_COLD_START_PASS` verdict. The regression triggered by that exact repair must determine the semantic result; no verdict is inferred before it completes.

## ENGINEERING JUDGMENT
Origin-down cold start is materially stronger than toggling an application flag or returning HTTP 503 because a real network connection to the origin cannot be established. It is still narrower than physical airplane-mode/radio loss, DNS failure, captive portal, partial connectivity, cache eviction, machine restart, or iOS/iPadOS lifecycle.

## EVIDENCE LIMIT
This fixture is not Flutter-generated and is not the LogMate post-build service worker. It does not validate product artifact provenance, cache eviction, quota pressure, physical networking/storage, iOS/iPadOS/EFB, installation as a Home Screen web app, release identity, or production.

## RELATED DOMAIN CHECK
- Foundations: relies on browser/network/process boundaries; no new native-runtime claim.
- Architecture: offline boot is an externally observable lifecycle contract; no architecture decision changed.
- Mobile: owner; Safari offline boundary remains OPEN pending repaired regression.
- Data: CacheStorage availability is tested only as an app-shell prerequisite, not application-data correctness/durability.
- Quality: **handoff materialized** — shell pipeline semantics produced a false-green risk; executable evidence must propagate the primary oracle exit code and assert evidence presence/verdict.
- Systems: exact head/run/environment/artifact retained; localhost fixture is not product provenance.
- Design Studio: considered; no visual/interaction semantic contract changes the runtime claim.
- Web Manager: PWA/browser overlap considered; engineering evidence only, no website operational decision edited.
- Marketing Manager: not materially relevant.
- Product: retained context `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → prior evidence 2026-09-20`; production identity unknown and default branch is not assumed production. Exact product execution is not claimed.

## OPEN / CHANGE WATCH
- OPEN: repaired executable regression verdict and the first actual semantic failure stage if red.
- OPEN: exact LogMate `make build-pwa` artifact/runtime due source-acquisition authorization dependency.
- OPEN: physical/iOS/iPadOS/EFB offline behavior, eviction, storage/network failure diversity.
- CHANGE WATCH: Safari/WebKit Service Worker/CacheStorage behavior and hosted macOS runner image.

## HANDOFFS
- Quality: treat pipeline exit propagation and non-empty/verdict-bearing evidence as part of the validation oracle; audit analogous `| tee` executable workflows before trusting green status.
- Systems: a later product transfer must use LogMate's product-owned `make build-pwa` path and bind source→toolchain→post-build transform→artifact→Safari environment.
- Data: do not infer application-data offline correctness from app-shell CacheStorage success.
