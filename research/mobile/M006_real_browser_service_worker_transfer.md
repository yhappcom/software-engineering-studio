# M006 — Real-browser Service Worker Offline Transfer

Status: **IN STUDY — Chromium offline + restart persistence + update/client-control + offline cold-start VALIDATED**  
Evidence date: 2026-09-20

## Why this block
Balance Loop favored M006 because LogMate's PWA/EFB direction gives browser lifecycle evidence high product and cross-track leverage, while S004 exact-ref build remains source-access blocked and F006 needs a better isolating harness. After same-session offline, restart persistence and update/client-control were validated, offline cold-start navigation was the next materially distinct failure class.

## SOURCE
- W3C Service Workers Candidate Recommendation Draft, 12 Aug 2026 remains the latest listed Service Workers publication as checked 2026-09-20. Service workers provide event-driven registration/lifecycle/fetch interception machinery; installing, waiting, active and client-control states are distinct.
- Existing canonical M006 source/model remains applicable for WebKit-specific Home Screen/background/storage limits. Chromium evidence does not transfer to Safari/iPadOS.

## CLAIM / VALIDATION CONTRACT
**CLAIM:** in one exact Chromium runtime, (1) a controlled page can receive a deliberately precached resource while browser networking is emulated offline and an uncached resource fails; (2) service-worker control and cached payload persist across browser restart/profile reuse; (3) a changed service worker can install into waiting without silently replacing an existing controller, then explicitly activate and cause controller transition; and (4) after an online warm/setup session is closed, a new browser process using the same persistent profile can be put offline *before navigation* and successfully navigate to a precached application shell under service-worker control while a never-cached resource still fails.

**TARGET:** `research/mobile/fixtures/m006_browser_service_worker/`. Offline cold-start fixture: `cold.html`, `cold-sw.js`, `validate_cold_start.mjs`; execution workflow head `3eef4e22b993018ea6b1787df0b82a819e545cdc`.

**ORACLE:** cold-start validation first establishes control and shell/payload cache state online, closes that browser context/process, launches a new persistent context against the same profile, calls browser-context offline emulation before any second-session navigation, then requires navigation response success, controller presence, exact cached shell marker, exact cached payload, and failure of a never-cached request. The negative request guards against accidental live-network success. Earlier update fixture independently distinguishes waiting from active controller identity through MessageChannel version responses and bounded `controllerchange`.

**ENVIRONMENT:** GitHub Actions `ubuntu-24.04` runner image `20260907.300.1`, Linux kernel `6.17.0-1022-azure`, Node `22.23.2`, Python `3.12.3`, Playwright `1.55.0`, exact downloaded Chromium **140.0.7339.16 / Playwright build v1187**. Run `35473544016`, job `105978759910`.

**FAILURE MODEL:** registration/control failure, cache population/fetch mismatch, accidentally live network, loss of registration/cache across restart, update lifecycle/controller errors, offline second-process navigation failing before a worker can serve the shell, shell cache mismatch, or a false-positive offline condition exposed by successful never-cached fetch.

**EVIDENCE LIMIT:** generic Chromium + loopback + Playwright offline emulation. The origin server remains running during the cold-start test, while the browser context is forced offline; this is not physical radio/link loss. The worker is synthetic Studio code, not Flutter-generated or LogMate post-processed. It is not Safari/WebKit/iPadOS/EFB, deployed HTTPS, storage eviction, authoritative-record durability, release artifact or production evidence.

## VALIDATION / TRANSFER VALIDATION
### Same-session offline
Run `35461424265`, job `105945868263`, head `754ed4f86be25ffd32c85665d42a78c88988452e` completed **success**: controlled cached fetch succeeded offline and never-cached fetch failed.

### Browser restart / persistent profile
Run `35464672061`, job `105954736630`, head `c4d45429c45617f127a6502de4bc241371617c55` completed **success**: after restart/profile reuse and intentionally online second navigation, controller presence persisted and the prior cache still served offline while an uncached resource failed.

### Service-worker update / client-control transition
Run `35470979806`, job `105971774906`, exact head `73e6aad0e59c27719652a0cc22c3a5b519edc917` completed **success**. v2 reached waiting while the existing client still identified v1; explicit `skipWaiting()` produced bounded `controllerchange`, then the controller independently identified v2.

### Offline cold-start navigation
Run `35473544016`, job `105978759910`, exact head `3eef4e22b993018ea6b1787df0b82a819e545cdc` completed **success**. All earlier regressions also passed. The new oracle warmed a dedicated shell/payload cache online, closed the first browser process, launched a second persistent context, set it offline before navigation, and successfully navigated to `/cold.html?offline-cold=1`. The page was service-worker controlled, body contained the exact `M006 cold shell` marker, cached payload equaled `M006-CACHED-PAYLOAD-v1`, and `/never-cached-cold.txt` failed. Job logs also close the prior browser-identity gap: Chromium `140.0.7339.16`, Playwright build `v1187`.

**TRANSFER VALIDATION:** M006 now survives four materially different browser lifecycle contexts: same-session offline fetch, browser restart/profile persistence, service-worker update/client-control transition, and second-process offline-before-navigation cold start. This supports the bounded engineering conclusion that a deliberately precached navigation shell can survive process restart and be served by a persisted worker/cache without network access in this exact Chromium environment.

No Mobile Stage 1 PASS is awarded.

## RELATED DOMAIN CHECK
- Foundations: F005 async/event boundaries apply; F006 transport root cause remains unrelated and OPEN.
- Architecture: service-worker version/control and offline shell availability are externally observable deployment states.
- Mobile: lead track; offline cold start was a named open failure class and is now boundedly validated in exact Chromium.
- Data: cache/shell persistence is not authoritative-record durability, backup, migration or eviction evidence.
- Quality: cold-start acceptance needs positive shell/payload/controller oracles plus an uncached negative oracle; online warm success alone is insufficient.
- Systems: artifact/origin/runtime/controller identity must all be bound for release claims; this run now binds exact Chromium identity but not a LogMate artifact.
- Design Studio: no canonical design contract changed; user-facing offline/update semantics remain a future handoff when product behavior is defined.
- Web Manager: no company-site operational decision changed; reusable browser mechanism only.
- Marketing Manager: not materially relevant.
- Product: LogMate identity retained as `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared 1.0.0+1 → evidence date 2026-09-20`; production identity unknown. No product files edited; this is not a LogMate build.

## HANDOFFS
- **Mobile → Quality:** PWA acceptance should separately test warm offline, restart persistence, update/controller transition and offline-before-navigation cold start; include an uncached negative oracle to detect accidental network availability.
- **Mobile → Systems:** exact Chromium identity is now known for this evidence (`140.0.7339.16`, Playwright build `v1187`). Future LogMate acceptance still needs product artifact digest + deployed origin + runtime + active worker/controller identity.
- **Mobile → Data:** do not infer canonical-record persistence or eviction resistance from service-worker/cache shell persistence.
- **Mobile → Design/Web:** if product offline/update UX is later specified, engineering can return concrete lifecycle constraints without redefining UX semantics.

## OPEN / CHANGE WATCH
- Safari/iPadOS/EFB, Android/iOS native lifecycle, Flutter web, canonical LogMate artifact, storage eviction, physical/real connectivity loss and deployed-origin behavior remain OPEN.
- Update/cold-start behavior for Flutter-generated/LogMate-postprocessed service workers remains OPEN until canonical artifact access exists.
- W3C Service Workers and browser implementations remain CHANGE WATCH.
