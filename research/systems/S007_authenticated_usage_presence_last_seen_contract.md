# S007 — Authenticated usage presence and last-seen contract

Date: 2026-09-24
Owner: Systems
State: IN STUDY / implementation validation OPEN

## Scope

LogMate product decision: after established ownership/onboarding, a persisted authenticated session routes directly to Home without showing onboarding. Product operations nevertheless need a reliable indication of whether/when an authenticated account has recently used LogMate.

Exact product audit: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`; production identity unknown. The tree contains Firebase Auth/session code and tests but no product-specific server-authoritative authenticated app-activity receipt was identified in this audit.

## SOURCE

Firebase Admin user management exposes account creation and **last sign-in** metadata. Firebase Auth also persists current-user state across app/browser restart until sign-out. These semantics mean `lastSignInTime` is authentication activity, not a complete oracle for subsequent app use under a restored session.

Firebase ID tokens can be sent to a trusted backend and verified there; the verified token UID is the server-side identity authority for an authenticated request.

Google Analytics for Firebase can report app activity/events, but reporting is asynchronous/aggregated and is an analytics system rather than an authoritative per-account operational state record.

Primary sources checked 2026-09-24:
- https://firebase.google.com/docs/auth/admin/manage-users
- https://firebase.google.com/docs/auth/users
- https://firebase.google.com/docs/auth/admin/verify-id-tokens
- https://firebase.google.com/docs/analytics

## SYNTHESIS

Do not use Firebase Auth `lastSignInTime` as LogMate `lastSeenAt`. A user who remains signed in can open the app repeatedly and route directly to Home without a new sign-in, so Auth metadata can remain old while product use is current.

Separate three concepts:

1. `lastSignInAt` — Firebase authentication metadata; useful for auth/security context.
2. `lastSeenAt` — latest **server-observed authenticated LogMate foreground/start activity** for the UID.
3. analytics engagement/session metrics — aggregate product measurement, not authorization or account-state authority.

## PROJECT DECISION transfer

The owner requires recent-access visibility for authenticated users who normally bypass onboarding and enter Home directly.

Recommended V1 contract:

- After Firebase Auth initialization resolves an authenticated UID and the startup gate accepts that UID for the local owner, emit a best-effort authenticated presence receipt without delaying Home.
- Also emit on a meaningful foreground/resume after a bounded throttle interval; do not write continuously while the app is foregrounded.
- The trusted server verifies the Firebase ID token and derives UID from the verified token. Never trust a client-supplied UID as identity authority.
- Server writes its own timestamp, e.g. `users/{uid}/account_meta.lastSeenAt`, using a server timestamp. Client wall-clock time is diagnostic only and must not be the authoritative last-seen value.
- A compact companion field such as `lastSeenSurface = android|ios|web` may be retained if product operations genuinely needs cross-surface diagnosis. Avoid precise location, device fingerprint, flight/logbook content, IP-derived profile, or unnecessary hardware identifiers for this purpose.
- A failed presence write must not block Home or established offline-first local use. Queue/coalesce one pending receipt and retry when authenticated connectivity returns.
- Coalesce repeated opens/resumes so an offline queue cannot grow without bound. For a last-seen scalar, newest pending observation supersedes older pending observations.
- A successful receipt is operational evidence that the backend observed an authenticated app-use checkpoint; it is not proof that the user performed any particular logbook action.

## Deletion interaction

New owner decision: user-initiated account deletion permanently removes local access and deletes both server and local user data. Therefore the per-user `lastSeenAt` record is user-associated server data and belongs inside the deletion saga's server-erasure scope. It must not survive as a UID-addressable operational profile after account deletion unless a separate legally/operationally justified retention policy is explicitly adopted.

Deletion-pending/locked state takes precedence over presence reporting: once deletion is durably requested and local access is locked, normal Home entry and normal last-seen heartbeats stop. Deletion/recovery requests may have their own narrowly scoped audit evidence if required, but that is not the normal usage-presence record.

## Failure-first implementation contract

Codex/product tests should cover at minimum:

1. restored authenticated session + completed onboarding routes Home and schedules presence without showing Welcome;
2. presence network failure does not block Home/local ledger;
3. retry after reconnect records server-observed UID and timestamp;
4. client UID spoof input cannot alter another UID's lastSeen;
5. client clock skew cannot control authoritative `lastSeenAt`;
6. rapid foreground/resume is throttled/coalesced;
7. offline repeated resumes retain only bounded newest pending presence;
8. explicit sign-out stops authenticated presence writes;
9. owner UID mismatch does not emit a valid-owner presence receipt;
10. deletion-pending lock prevents Home and normal presence emission;
11. deletion server erasure removes the user-associated lastSeen record;
12. Android/iOS/PWA restored-session paths preserve the same semantic contract.

## VALIDATION

OPEN. No exact LogMate runtime, Firebase Auth Emulator/backend, native, or PWA execution evidence was produced in this research block. Reading/source synthesis is not PASS.

Required evidence escalation:

- exact Dart tests around startup/presence scheduling and non-blocking failure;
- Firebase Auth Emulator + backend/emulator test verifying token-derived UID and cross-UID denial;
- server-timestamp oracle independent of client clock;
- offline queue/coalescing/reconnect test;
- deletion-saga test proving presence data enters server erasure scope;
- Android/iOS/PWA transfer validation.

## Alternatives considered

### Firebase Auth `lastSignInTime` only
Rejected for the product-use requirement. It measures authentication/sign-in, not every later app access under persisted sessions.

### Google Analytics only
Useful for aggregate engagement/retention and marketing/product analysis, but not ideal as the canonical per-account operational `lastSeenAt` because reporting is analytics-oriented and asynchronous.

### Write on every screen/action
Rejected for V1. It creates unnecessary write volume/privacy surface and adds no value if the requirement is simply recent authenticated access.

## RELATED DOMAIN CHECK

- Foundations: no new prerequisite.
- Architecture: presence is a side effect of accepted authenticated startup/foreground, not a routing prerequisite; keep it behind a provider-neutral interface.
- Mobile: foreground/resume semantics and PWA visibility/restart differ; transfer validation required.
- Data: newest-value coalescing and deletion erasure scope are material.
- Quality: failure-first non-blocking, spoofing, clock-skew, retry and deletion tests required.
- Systems: owns token verification, identity authority and operational presence boundary.
- Design Studio: no user-visible screen is required for ordinary presence recording; privacy disclosure/content may become relevant.
- Web Manager/Marketing: aggregate engagement may use Analytics separately; do not make the operational lastSeen record a marketing event store.
- Product source/ref checked as recorded above.

## HANDOFFS

- **LogMate / Codex:** implement a provider-neutral authenticated-presence service after accepted startup ownership; backend derives UID from verified Firebase token and writes server timestamp; Home remains non-blocking/offline-first.
- **Data:** include user-associated presence metadata in account-deletion server erasure.
- **Quality:** require cross-UID spoof denial, client-clock independence, throttle/coalescing and offline retry tests.
- **Marketing/Web:** use Analytics for aggregate usage/retention if desired; do not reinterpret Auth `lastSignInTime` as product activity.
