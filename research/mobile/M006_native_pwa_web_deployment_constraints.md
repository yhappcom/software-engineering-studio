# M006 — Native App vs PWA/Web Boundary & Deployment Constraints

Status: **IN STUDY — first integrated Foundation block + bounded acceptance evidence**  
Evidence date: 2026-09-18

## Problem / scope

A PWA, Home Screen web app and native application may present similar UI and may share domain code, but delivery mechanism, runtime lifetime, storage, background execution, update and installation semantics are not equivalent. The engineering question is not “can this look like an app?” but whether a concrete target satisfies the product's required semantic capability vector.

This block focuses on installability, offline/service-worker execution, background lifetime, storage/update boundaries and exact LogMate EFB transfer. It does not claim production acceptance.

## SOURCE

- WebKit, **WebKit Features in Safari 26.0** (2025-09-15): on iOS/iPadOS 26, every site added to Home Screen opens as a web app by default unless the user disables `Open as Web App`; a manifest is no longer required for that Home Screen web-app experience. Service Workers remain an optional enhancement, including for offline behavior.
- WebKit, **Web Push for Web Apps on iOS and iPadOS** (2023-02-16): iOS/iPadOS 16.4 added standards-based Web Push for Home Screen web apps; permission requires direct user interaction. This establishes event-driven background capability, not arbitrary continuous execution.
- MDN, **ServiceWorkerGlobalScope** / **Offline and background operation** (checked 2026-09-18): service workers can be terminated when idle and restarted for events; global state is not persisted across termination/restart. `waitUntil()` is not a guarantee against termination for excessively long work.
- MDN, **Background Synchronization API** (checked 2026-09-18): Background Sync is `Limited availability`, so it is not a portable baseline guarantee across major browsers.
- WebKit, **Updates to Storage Policy** (2023): web storage is origin-scoped and can be evicted under quota/storage-pressure/policy conditions; standalone Home Screen web apps participate in WebKit storage policy. Storage semantics therefore require separate durability/recovery validation.

## SYNTHESIS — delivery target model

Use:

`product semantic contract → capability vector → delivery/install path → runtime/lifetime mechanism → persistence/cache/update mechanism → unsupported/degraded state → acceptance oracle`

Do not collapse the following:

- `Home Screen installable` ≠ `offline-capable`;
- `offline-capable` ≠ `authoritative data is durable/recoverable`;
- `service worker can handle background events` ≠ `application code runs continuously in background`;
- `push/background event exists` ≠ `arbitrary immediate synchronization is guaranteed`;
- `same source/domain code` ≠ `same deployment/runtime semantics`;
- `new service worker downloaded` ≠ `every currently open client is immediately controlled by that version`;
- `browser accepted installation` ≠ `EFB/product acceptance`.

Service-worker lifecycle creates an additional release state machine: install, waiting, activate and client control can be temporally distinct. Acceptance therefore needs deployed artifact/origin/client-controller identity, not only source version.

## ENGINEERING JUDGMENT

For an EFB PWA, requirements should be expressed as user-visible semantics, not native analogies. Example: “the logbook opens and exposes previously committed local records without network after an accepted offline preparation step” is testable. “works like the native app offline” is underspecified.

Background guarantees should be fail-closed. If the platform cannot establish a required immediate/continuous background transfer guarantee, expose that capability as unsupported/degraded and design synchronization around foreground/resume/event-driven opportunities rather than silently promising native-like execution.

## PROJECT TRANSFER — LogMate exact ref

Repository → `yhappcom/logmate`  
Ref → branch `main`, commit `b551ce434ad72b1895033e0f3617c73b026d40ea`  
Declared version → `1.0.0+1` (retained from current Studio product audit)  
Evidence date → 2026-09-18  
Production identity → **UNKNOWN; default branch is not assumed to equal production**

At this exact ref, `MASTER.md` defines iOS/Android native and tablet/EFB PWA as first-class targets, requires equal domain semantic/calculation/projection results, permits platform-specific adapters/responsive UI, and explicitly does **not** guarantee immediate Sync while backgrounded/terminated without separate validation. It also states that canonical ledger/persistence/backup/server Sync are not yet implemented. Therefore M006 does not report a current product defect or PWA PASS.

This product contract is compatible with the source evidence above: an EFB PWA can be a valid target without pretending its lifecycle/background semantics equal native. The future acceptance plan must test offline data, update/client-control state, storage/recovery, foreground/resume sync and exact EFB browser/OS policy independently.

## VALIDATION — bounded executable acceptance model

Fixture: `research/mobile/fixtures/M006_native_pwa_acceptance_matrix.py`

Environment: Python 3.13.5 on Linux, 2026-09-18.

Claim: installability/offline capability alone must not satisfy a stronger contract that requires guaranteed continuously running background application code.

Oracle: independent conjunction over declared required capabilities. The fixture contains deliberately bounded `pwa-model` and `native-model` targets; it is not a platform emulator.

Observation: `M006 bounded acceptance matrix: PASS`.

Failure case: a naive installability-only gate accepts the modeled PWA even after the product contract is strengthened to require continuous background execution; the capability-aware oracle rejects it.

Verdict: **PASS only for the acceptance-model logic.**

Evidence limit: no Flutter/browser/iPad/EFB/native execution; no service-worker, IndexedDB, CacheStorage, install, update, eviction, background event, app-store or device-policy behavior was executed here.

## ALTERNATIVES / trade-offs

- Native-only can provide different OS integration/background/storage mechanisms but conflicts with a product environment that cannot use the required installation channel.
- PWA can avoid app-store installation and provide offline/event-driven capabilities, but browser/OS support and lifecycle constraints are part of the product architecture.
- Server-mediated sync can reduce peer-discovery constraints but introduces network/service/account/security dependencies.
- Foreground/resume synchronization avoids claiming unsupported continuous background execution but changes freshness semantics and UX expectations.

No alternative is universally superior; select against the product capability vector and evidence.

## RELATED DOMAIN CHECK

- Foundations: F001/F005/F006 checked; execution, async and network completion boundaries remain relevant. Direct Dart/Flutter execution still OPEN.
- Architecture: A003/M005 semantic-contract discipline reused; adapter/API equality is not semantic equivalence.
- Mobile: M001-M005 reused; M006 adds delivery/install/update/browser lifetime boundary.
- Data: D001/D004-D006 relevant to authoritative local state, offline ownership, sync and recovery. PWA storage durability remains TRANSFER VALIDATION.
- Quality: Q001/Q002/Q006 require per-platform acceptance and failure injection; service-worker update/storage/network failure cases belong in future runtime campaigns.
- Systems: S001/S004-S006 require exact source/build/post-build/deploy/origin/runtime identity and rollback/update evidence.
- Design Studio: repository search for PWA/mobile-web evidence returned no materially relevant result this run. Unsupported/degraded states must still be handed back rather than hidden.
- Web Manager: repository search for LogMate/PWA evidence returned no materially relevant result this run. Website/PWA operational decisions remain Web-owned where applicable.
- Marketing Manager: repository search returned no materially relevant PWA evidence this run.
- Product: exact LogMate ref checked as above.

## HANDOFFS

### Mobile → Data / Quality
Future LogMate PWA acceptance should explicitly test: authoritative-record persistence across close/reopen and device/browser storage conditions; offline launch after accepted preparation; queued operation behavior across termination/restart; duplicate/retry semantics; recovery/export/backup. Do not infer durability from CacheStorage/IndexedDB presence.

### Mobile → Systems / Web Manager
Bind PWA acceptance to canonical build, post-build service-worker transforms, artifact identity, deployment origin, browser/OS/EFB version and active service-worker/client-control state. A source commit alone is insufficient release identity.

### Mobile → Design Studio
If background/immediate sync is unsupported or degraded, interaction/content semantics must represent pending/stale/manual-resume states rather than imply completion.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN:** direct Dart JIT/AOT and Flutter runtime validation; no `dart`/`flutter` executable available on 2026-09-18 environment recheck.
- **TRANSFER VALIDATION:** iPad/EFB Home Screen installation, offline launch, service-worker install/update/control, IndexedDB/storage persistence/eviction, foreground/background/termination, push/event behavior, and actual LogMate canonical build.
- **DEPENDENCY:** exact company EFB iPadOS/Safari policy/version and allowed installation/network behavior are required before production acceptance.
- **CHANGE WATCH:** iOS/iPadOS/Safari/WebKit Home Screen behavior, installability, storage policy and background APIs; Chrome/other browser PWA/background API support; Flutter web service-worker/build behavior.
- **OPEN:** production ref/deployment identity for LogMate remains unknown.

## Gate effect

M006 closes the previously untouched Mobile Foundation native-vs-PWA/deployment boundary at first professional/model level. Mobile Stage 1 remains **NOT PASS** because direct Flutter/native/browser/EFB execution and platform transfer evidence are still absent.
