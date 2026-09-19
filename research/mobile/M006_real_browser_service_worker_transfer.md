# M006 — Real-browser Service Worker Offline Transfer

Status: **IN STUDY — Chromium offline + restart persistence + update/client-control transition VALIDATED**  
Evidence date: 2026-09-20

## Why this block
Balance Loop favored M006 because LogMate's PWA/EFB direction gives browser lifecycle evidence high product and cross-track leverage, while S004 exact-ref build remains source-access blocked and F006 needs a better isolating harness. After same-session offline and restart persistence were validated, the next distinct failure class was service-worker update/waiting/activation/client-control transition.

## SOURCE
- W3C Service Workers Candidate Recommendation Draft, 12 Aug 2026: service workers have registration/lifecycle/update machinery and distinct installing, waiting and active workers; client control changes are lifecycle events rather than ordinary cache reads.
- Existing canonical M006 source/model remains applicable for WebKit-specific Home Screen/background/storage limits. Chromium evidence does not transfer to Safari/iPadOS.

## CLAIM / VALIDATION CONTRACT
**CLAIM:** in one concrete Chromium runtime, (1) a controlled page can receive a deliberately precached resource while browser networking is emulated offline and an uncached resource fails; (2) service-worker control and the cached payload can persist across browser restart/profile reuse; and (3) a changed service-worker script can install into `waiting` without silently replacing the controller of an existing v1 client, then explicitly `skipWaiting()` and cause `controllerchange` to v2.

**TARGET:** `research/mobile/fixtures/m006_browser_service_worker/`. Update fixture `validate_update.mjs` introduced at `c5e42a5173d4de1abbca598e9b2b5534690a9e4e`; workflow execution head `73e6aad0e59c27719652a0cc22c3a5b519edc917`.

**ORACLE:** update fixture first obtains a message-channel version response from the active v1 controller. The server then changes `/sw.js` to v2 and `registration.update()` is required to yield an installed waiting worker. Before promotion, the controller must still answer `v1`; after posting `SKIP_WAITING`, a bounded `controllerchange` must occur and the controller must answer `v2`. This separates script discovery/install from client takeover.

**ENVIRONMENT:** GitHub Actions `ubuntu-24.04`; Playwright package pinned to 1.55.0 and its Chromium installed by Playwright. Fixtures emit `browser.version()` but current connector evidence exposes step verdicts rather than command stdout; exact Chromium build identity remains OPEN.

**FAILURE MODEL:** registration/control failure, cache population/fetch mismatch, accidentally live network, loss of registration/cache across restart, update not discovered, v2 failing to reach waiting, premature controller replacement, `skipWaiting()`/activation not producing controller transition, or version oracle addressing the wrong worker.

**EVIDENCE LIMIT:** generic Chromium + loopback + emulated offline. The restart navigation is intentionally online, so offline cold-start is not established. Update validation uses a synthetic Studio worker, not Flutter-generated or LogMate post-processed service worker. It is not Safari/WebKit/iPadOS/EFB, deployed HTTPS, storage eviction, real connectivity loss, authoritative-record durability, release artifact or production evidence.

## VALIDATION / TRANSFER VALIDATION
### Same-session offline
Run `35461424265`, job `105945868263`, head `754ed4f86be25ffd32c85665d42a78c88988452e` completed **success**: controlled cached fetch succeeded offline and never-cached fetch failed.

### Browser restart / persistent profile
Run `35464672061`, job `105954736630`, head `c4d45429c45617f127a6502de4bc241371617c55` completed **success**: after restart/profile reuse and intentionally online second navigation, controller presence persisted and the prior cache still served offline while an uncached resource failed.

### Service-worker update / client-control transition
Run `35470979806`, job `105971774906`, exact head `73e6aad0e59c27719652a0cc22c3a5b519edc917` completed **success** on `ubuntu-24.04`. Checkout, environment capture, pinned Chromium installation, prior offline/restart regressions and the distinct update-transition oracle all succeeded.

**VALIDATION:** v2 installation reached the waiting state while the existing controlled client continued to identify its controller as v1. Explicit promotion via `skipWaiting()` produced a bounded `controllerchange`, after which the controller independently identified itself as v2.

**TRANSFER VALIDATION:** M006 now survives three materially different browser lifecycle contexts: same-session offline fetch, browser restart/profile persistence, and service-worker update/client-control transition. This validates the lifecycle distinction `installed update ≠ current client controller`; explicit activation/control transition is observable and must be part of PWA update acceptance.

No Mobile Stage 1 PASS is awarded.

## RELATED DOMAIN CHECK
- Foundations: F005 async/event boundaries apply; F006 transport root cause remains unrelated and OPEN.
- Architecture: service-worker version/control is externally observable deployment state, not merely source identity.
- Mobile: lead track; update/client-control was a named open failure class and is now boundedly validated in Chromium.
- Data: cache/update lifecycle evidence is not authoritative-record durability, backup or migration evidence.
- Quality: independent version responses plus waiting/controllerchange state provide a stronger oracle than successful registration alone.
- Systems: artifact/origin/runtime/controller identity must all be bound for release claims; source/build identity alone cannot establish which worker controls a client.
- Design Studio: no canonical design contract changed; user-facing stale/update semantics remain a future handoff when product behavior is defined.
- Web Manager: no company-site operational decision changed; reusable browser mechanism only.
- Marketing Manager: not materially relevant.
- Product: LogMate identity retained as `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`; production identity unknown. No product files edited; this is not a LogMate build.

## HANDOFFS
- **Mobile → Quality:** PWA update tests must distinguish update discovery/install, waiting state, activation and actual client-controller transition; registration success alone is insufficient.
- **Mobile → Systems:** future LogMate acceptance should bind artifact digest + deployed origin + exact browser/runtime + active service-worker/controller identity, especially across updates.
- **Mobile → Data:** do not infer canonical-record persistence from service-worker/cache lifecycle behavior.
- **Mobile → Design/Web:** if product update UX is later specified, engineering can return concrete waiting/activation/controller-transition constraints without redefining UX semantics.

## OPEN / CHANGE WATCH
- Exact Chromium build identity remains OPEN through the current connector evidence channel.
- Safari/iPadOS/EFB, Flutter web, canonical LogMate artifact, offline cold start, storage eviction, real network loss and deployed-origin behavior remain OPEN.
- Update behavior for Flutter-generated/LogMate-postprocessed service workers remains OPEN until canonical artifact access exists.
- W3C Service Workers and browser implementations remain CHANGE WATCH.
