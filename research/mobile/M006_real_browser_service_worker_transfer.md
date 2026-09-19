# M006 — Real-browser Service Worker Offline Transfer

Status: **IN STUDY — Chromium offline + browser-restart persistence transfer VALIDATED**  
Evidence date: 2026-09-20

## Why this block
Balance Loop comparison favored Mobile M006 over another Dart-only Foundation variant: Foundations F001-F005 already have bounded direct execution; S004 exact LogMate source build is blocked by authorized cross-private-repository acquisition; F006 needs a better phase-isolating harness. Browser/PWA execution is a named Mobile, Data, Quality and Systems evidence gap and directly supports LogMate's EFB/PWA direction.

## SOURCE
- W3C Service Workers Candidate Recommendation Draft, 12 Aug 2026: service workers are event-driven workers that can wake to receive events; the specification defines registration, lifecycle, fetch interception and client-control machinery.
- Existing canonical M006 source/model remains applicable for WebKit-specific Home Screen/background/storage limits. This fixture does not transfer Chromium behavior to Safari/iPadOS.

## CLAIM / VALIDATION CONTRACT
**CLAIM:** in one concrete Chromium runtime, a controlled page can receive a deliberately precached resource through a service-worker fetch handler after browser network emulation is switched offline, while an uncached resource fails. A second materially different claim tests whether service-worker control and the cached payload survive closing the first persistent browser context/process and relaunching against the same profile.

**TARGET:** `research/mobile/fixtures/m006_browser_service_worker/`; restart fixture introduced at `74ce65f03023a95ad46028bc548775bc75f029ff`, executed at workflow head `c4d45429c45617f127a6502de4bc241371617c55`.

**INPUT/STATE:** loopback HTTP origin; service worker install/activate with `skipWaiting()` + `clients.claim()`; CacheStorage entry `/payload.txt`; controlled page; Playwright browser context offline mode. Restart variant uses a temporary persistent Chromium profile, closes the first context, relaunches a second persistent context against the same profile, performs the second navigation online, verifies controller presence, then switches offline.

**ORACLE:** same-session: cached literal `M006-CACHED-PAYLOAD-v1`, non-null controller, offline query-varied cached fetch succeeds, never-cached fetch rejects. Restart: first session establishes literal + controller; after relaunch controller must be non-null; offline `/payload.txt?after-restart=1` must return the same literal; `/never-cached-after-restart.txt` must reject. Negative uncached cases prevent false PASS from an accidentally live network.

**ENVIRONMENT:** GitHub Actions `ubuntu-24.04`; Playwright package pinned to 1.55.0 and its Chromium installed by Playwright. The fixture records `browser.version()` to stdout, but the current connector evidence channel exposes step verdicts rather than command stdout; exact Chromium build identity therefore remains OPEN rather than fabricated.

**FAILURE MODEL:** registration/control failure, cache population failure, fetch-handler mismatch, offline emulation not preventing network access, accidental broad offline fallback, loss of service-worker registration/control across process restart/profile reuse, or loss of the cached payload across restart.

**EVIDENCE LIMIT:** generic Chromium + loopback + emulated offline. The restart navigation is intentionally online, so this does not establish offline cold-start shell availability. It is not Flutter web, LogMate source, product post-build transform, deployed HTTPS origin, real network loss, storage eviction, service-worker update/waiting/activation transition, Safari/WebKit/iPadOS, Home Screen installation, EFB policy, release artifact, authoritative-record durability, backup/recovery, or production evidence.

## VALIDATION / TRANSFER VALIDATION
### Same-session offline
Workflow run `35461424265`, job `105945868263`, head `754ed4f86be25ffd32c85665d42a78c88988452e` completed **success**. Checkout, environment recording, pinned Playwright Chromium installation and browser service-worker offline oracle all succeeded.

**VALIDATION:** real Chromium accepted service-worker registration/control, served the explicit cached payload under emulated offline state, and satisfied the negative uncached-fetch failure oracle.

### Browser restart / persistent profile
Workflow run `35464672061`, job `105954736630`, exact head `c4d45429c45617f127a6502de4bc241371617c55` completed **success** on `ubuntu-24.04`. Both the existing same-session oracle and the distinct `Execute browser restart persistence oracle` step succeeded; the restart step ran after pinned Chromium installation and completed independently.

**VALIDATION:** under the fixture contract, service-worker control and the explicitly cached payload survived closure of the first persistent browser context/process and relaunch against the same profile; after the relaunch and an intentionally online navigation, switching the second context offline still served the cached payload, while the never-cached resource failed.

**TRANSFER VALIDATION:** M006 now survives two browser lifecycle contexts: same-session offline and process/context restart with persistent-profile reuse. This is materially stronger than the prior Python capability model and the first browser run, but it is specifically a persistence-across-restart result—not an offline-cold-start, eviction-resilience, Safari/EFB, or product-artifact result.

No Mobile Stage 1 PASS is awarded.

## RELATED DOMAIN CHECK
- Foundations: F005 async/event distinction and F006 network-boundary discipline apply; this does not resolve F006.
- Architecture: service-worker/cache behavior is an externally observable deployment contract, not merely implementation detail.
- Mobile: lead track; advances M006 with a distinct browser lifecycle failure boundary.
- Data: CacheStorage persistence across this restart is not authoritative-record durability, backup or recovery evidence.
- Quality: positive/negative oracles plus a process/context restart boundary were exercised; update/storage-eviction/real-network failure classes remain open.
- Systems: browser/runtime/artifact/origin identity must be bound before product/release claims; exact Chromium build remains unrecovered through the connector.
- Design Studio: no design contract changed; degraded/offline state semantics remain a future handoff if product behavior is validated.
- Web Manager: no website/PWA operational decision changed by a local generic fixture.
- Marketing Manager: not materially relevant to this browser-mechanism claim.
- Product: LogMate exact product evidence remains `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`; production identity unknown. No product files were edited and this fixture is not a LogMate build.

## HANDOFFS
- **Mobile → Quality:** retain both negative uncached oracles; next browser lifecycle validation should change the failure class (update/activation, eviction, offline cold start, real connectivity loss) rather than repeat restart/profile reuse.
- **Mobile → Systems:** future product transfer must bind exact browser version, LogMate build/post-build artifact digest, deployment origin and active service-worker/controller identity.
- **Mobile → Data:** do not treat CacheStorage restart persistence as proof of canonical logbook-record persistence or recoverability.

## OPEN / CHANGE WATCH
- Exact Chromium build identity was emitted by the fixture but is not exposed by the current connector evidence channel and remains OPEN.
- Safari/iPadOS/EFB, Flutter web, LogMate canonical artifact, service-worker update/client-control transitions, offline cold start, storage eviction and deployed-origin behavior remain OPEN.
- W3C Service Workers and browser implementations remain CHANGE WATCH.
