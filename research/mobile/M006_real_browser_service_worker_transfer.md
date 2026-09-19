# M006 — Real-browser Service Worker Offline Transfer

Status: **IN STUDY — executable browser transfer pending hosted verdict**  
Evidence date: 2026-09-20

## Why this block
Balance Loop comparison favored Mobile M006 over another Dart-only Foundation variant: Foundations F001-F005 already have bounded direct execution; S004 exact LogMate source build is blocked by authorized cross-private-repository acquisition; F006 needs a better phase-isolating harness. Browser/PWA execution is a named Mobile, Data, Quality and Systems evidence gap and directly supports LogMate's EFB/PWA direction.

## SOURCE
- W3C Service Workers Candidate Recommendation Draft, 12 Aug 2026: service workers are event-driven workers that can wake to receive events; the specification defines registration, lifecycle, fetch interception and client-control machinery.
- Existing canonical M006 source/model remains applicable for WebKit-specific Home Screen/background/storage limits. This fixture does not transfer Chromium behavior to Safari/iPadOS.

## CLAIM / VALIDATION CONTRACT
**CLAIM:** in one concrete Chromium runtime, a controlled page can receive a deliberately precached resource through a service-worker fetch handler after browser network emulation is switched offline, while an uncached resource fails. This is stronger than the prior Python capability model but narrower than LogMate/EFB acceptance.

**TARGET:** `research/mobile/fixtures/m006_browser_service_worker/` at workflow head `754ed4f86be25ffd32c85665d42a78c88988452e`.

**INPUT/STATE:** loopback HTTP origin; service worker install/activate with `skipWaiting()` + `clients.claim()`; CacheStorage entry `/payload.txt`; controlled page; then Playwright browser context offline mode.

**ORACLE:** (1) online payload equals independent literal `M006-CACHED-PAYLOAD-v1`; (2) page has a non-null `navigator.serviceWorker.controller`; (3) after offline transition, query-varied `/payload.txt?offline=1` returns the same cached literal because the handler intentionally matches by pathname and serves the canonical cache key; (4) `/never-cached.txt` rejects while offline. The negative uncached case prevents a false PASS caused by network still being available.

**ENVIRONMENT:** GitHub Actions `ubuntu-24.04`; Node/Python identities recorded by workflow; Playwright package pinned to 1.55.0 and its Chromium installed by Playwright. Exact browser build must be recovered from execution evidence before a completed verdict is recorded.

**FAILURE MODEL:** registration/control failure, cache population failure, fetch-handler mismatch, offline emulation not preventing network access, or accidental broad offline fallback.

**EVIDENCE LIMIT:** this is generic Chromium service-worker execution, not Flutter web, LogMate source, product post-build transform, deployed HTTPS origin, real network loss, browser restart, storage eviction, Safari/WebKit/iPadOS, Home Screen installation, EFB policy, release artifact, or production evidence. Playwright offline emulation is not physical connectivity loss.

## EXECUTION STATE
Workflow: `.github/workflows/m006-browser-service-worker-validation.yml`. Run `35461424265`, job `105945868263`, head `754ed4f86be25ffd32c85665d42a78c88988452e` was **in progress** when this note was persisted. Checkout and environment-recording steps had succeeded; pinned Playwright Chromium installation was still running. No PASS/FAIL is awarded until the browser oracle reaches a terminal verdict.

## RELATED DOMAIN CHECK
- Foundations: F005 async/event distinction and F006 network-boundary discipline apply; this does not resolve F006.
- Architecture: service-worker/cache behavior is an externally observable deployment contract, not merely implementation detail.
- Mobile: lead track; advances M006 from model-only toward real browser execution.
- Data: CacheStorage delivery is not authoritative-record durability, backup or recovery evidence.
- Quality: independent positive/negative oracles and bounded workflow timeout are required; terminal result pending.
- Systems: browser/runtime/artifact/origin identity must be bound before product/release claims.
- Design Studio: no design contract is changed; degraded/offline state semantics remain a future handoff if product behavior is validated.
- Web Manager: no website/PWA operational decision is changed by a local generic fixture.
- Marketing Manager: not materially relevant to this browser-mechanism claim.
- Product: LogMate exact product evidence retained from canonical M006/S004; no product files edited and this fixture is not a LogMate build.

## HANDOFFS
- **Mobile → Quality:** if terminal execution succeeds, reuse the positive controlled-cache + negative uncached oracle shape for deployed-browser acceptance, but add restart/update/storage/network failure classes.
- **Mobile → Systems:** bind future product transfer to exact browser version, LogMate build/post-build artifact digest, deployment origin and active service-worker/controller identity.
- **Mobile → Data:** do not treat successful CacheStorage offline fetch as proof of canonical logbook-record persistence or recoverability.

## OPEN / CHANGE WATCH
- Hosted browser verdict and exact Chromium build identity pending.
- Safari/iPadOS/EFB, Flutter web, LogMate canonical artifact, service-worker update/client-control transitions, storage eviction/restart and deployed-origin behavior remain OPEN.
- W3C Service Workers and browser implementations remain CHANGE WATCH.
