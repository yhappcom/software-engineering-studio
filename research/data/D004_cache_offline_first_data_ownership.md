# D004 — Cache Semantics & Offline-First Data Ownership

Status: **IN STUDY — SOURCE/MODEL + FIRST EXECUTABLE FAILURE/ALTERNATIVE**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem
A cache is a copy selected for reuse/performance/availability. Offline-first adds a harder problem: local observations and mutations may exist while the remote system is unreachable. Treating every locally visible value as either merely disposable cache or globally authoritative state causes data-loss and correctness failures.

The working model is:

`logical authority → confirmed base → cache/projection → pending local mutation → synchronization acknowledgement → conflict/reconciliation → visible state`

These roles may share one physical database but remain different semantic states.

## SOURCE
Primary sources checked 2026-09-17:
- Firebase, **Access data offline / Firestore**: offline persistence caches actively used data; offline reads/writes/listens/queries are supported; local changes synchronize when connectivity returns; `SnapshotMetadata.fromCache` identifies cache-origin snapshots that may be stale or incomplete; multiple changes to one document use last-write-wins in the documented Firestore offline behavior.
- Firebase, **Get data with Cloud Firestore**: SDK APIs can explicitly select CACHE, SERVER or DEFAULT sources.
- Firebase JavaScript Firestore API: disabling network makes reads/listeners use cache and queues writes; `waitForPendingWrites` distinguishes local issuance from backend acknowledgement; `snapshots-in-sync` does not mean server synchronization.
- Android/Flutter offline-first guidance was already indexed in D001 and remains relevant to repository/local-source coordination.

## SYNTHESIS
### Cache is not an authority classification
A physical local store can contain at least three semantically different classes:
1. confirmed replicated data that may be stale;
2. derived/query/index cache that is disposable/rebuildable;
3. locally accepted pending mutations that must not be discarded as ordinary cache if the product promises offline writes.

Therefore `local == cache` and `remote == source of truth` are both insufficient universal models.

### Freshness, completeness and authority are separate
A cached value may be valid but stale. A cache miss may mean "not cached" rather than "does not exist". A server-origin observation may be fresher than a cached base while still not incorporating a pending local mutation that has not yet been acknowledged.

### Offline-first requires an explicit mutation state machine
At minimum distinguish:
- confirmed/acknowledged state;
- pending local mutation;
- rejected/failed mutation;
- conflict or superseded state when the synchronization policy can produce it;
- cache freshness/completeness metadata where reads depend on it.

A refresh operation must state which layer it replaces. Blindly replacing visible local state with a fetched remote snapshot can erase or hide an accepted offline mutation.

## EXECUTABLE VALIDATION 1
Fixture: `research/data/fixtures/D004_cache_offline_ownership.py`

Environment executed: Python 3.13.5 / Linux container, 2026-09-17.

### CLAIM
A destructive refresh that conflates confirmed remote base with pending local mutation can lose the user's visible offline edit; separating pending mutation from confirmed base preserves it across a stale refresh. Cache absence also does not establish authoritative absence.

### PROPERTY / ORACLE
- after an accepted local edit to 90 and a stale server refresh containing 60, pending-aware visible state remains 90;
- confirmed base may update independently to 60;
- an object absent from an unpopulated cache may still exist remotely.

### OBSERVATION
```text
unsafe_after_refresh=60
safe_visible=90 base=60 pending=90
cache_says_absent=True authoritative_absent=False
VERDICT=PASS
```

### FAILURE / ROOT CAUSE
The unsafe policy stores both remote-confirmed base and local pending mutation in one replaceable slot. Refresh therefore has no semantic boundary telling it what may be invalidated and overwrites the pending edit.

### ALTERNATIVE
The comparison keeps `base_cache` and `pending` distinct. Refresh replaces only the confirmed base; the pending overlay remains the visible value until synchronization policy resolves it.

### EVIDENCE LIMIT
This is a deterministic language-neutral model, not Firestore SDK execution, SQLite implementation, multi-device synchronization, network reordering, durable queue, conflict-resolution, Android/iOS process-death, or production evidence. It establishes the ownership failure mechanism only.

## FIRESTORE TRANSFER BOUNDARY
**SOURCE:** Current Firebase docs explicitly expose cache/server source distinctions and cache metadata; cached results can be stale or incomplete. Offline writes are synchronized later, and pending-write acknowledgement has distinct APIs/metadata semantics.

**ENGINEERING JUDGMENT:** An application using Firestore must not infer global confirmation merely because a latency-compensated/local snapshot shows the mutation. UI/domain semantics such as `saved locally`, `sync pending`, and `synced` require product-specific contracts above SDK cache visibility.

**CHANGE WATCH:** Firestore offline behavior, cache APIs and platform defaults are SDK/platform-sensitive; recheck exact FlutterFire/Firebase versions before product release advice.

## PRODUCT TRANSFER
Retained product evidence only: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17` from prior exact-ref audit. The durable ledger/sync implementation was not present in that evidence, so this is a **TRANSFER CANDIDATE**, not a defect finding or technology decision.

For LogMate, future local ledger + optional sync should define whether an entered FlightRecord is locally committed before remote acknowledgement and prevent refresh/sync from treating pending records as disposable cache.

MintTap repository identity remains unresolved in Studio status, so no implementation claim is made.

## RELATED DOMAIN CHECK
- **Foundations:** F001 process/runtime distinction retained; direct Dart/Flutter execution remains OPEN.
- **Architecture:** D004 extends A002 state ownership: confirmed base, pending mutation and projection need explicit owners/contracts even if colocated physically.
- **Mobile:** process death/background/offline transitions can affect pending-state persistence; real Android/iOS evidence remains required.
- **Data:** D001 authority/durability model is reused; D006 will own replication/conflict/idempotency depth.
- **Quality:** tests must include stale refresh, cache miss, pending write, rejection and reconnect; fake cache-only tests cannot establish server acknowledgement.
- **Systems:** confidentiality of persistent caches and resource/eviction behavior are separate claims.
- **Design Studio:** recovery/sync UI semantics must reflect real confirmed/pending/failed states; no design canonical file edited.
- **Web Manager:** persistent web cache has different trust/session implications; no transfer assumed.
- **Marketing Manager:** not materially relevant to this mechanism block.

## HANDOFFS
- **Data → Architecture:** model confirmed base, pending mutation and derived cache as separate semantic ownership roles.
- **Data → Quality:** add stale-refresh/cache-miss/pending-ack failure cases and assert server acknowledgement separately from local visibility.
- **Data → Mobile:** later reproduce offline write + process death + reconnect on exact FlutterFire/Android/iOS stack.
- **Data → Design Studio:** `saved`, `pending`, `synced`, `failed` wording must be driven by the engineering state contract.

## OPEN / VALIDATION
1. Execute equivalent pending-write/cache-source behavior on a trustworthy Firestore/FlutterFire emulator or real SDK environment.
2. Add durable pending-queue/process-death evidence before claiming offline-write survival.
3. D006 must test concurrent/multi-device conflict, retry/idempotency and acknowledgement ordering; do not smuggle those claims into cache semantics.
4. Cache eviction/completeness and query semantics need concrete implementation evidence when a product storage stack is selected.

## Current judgment
D004 has a first coherent Foundation block with source evidence, a failure mechanism, executable counterexample and safer alternative. It is **not PASS** and does not establish a production offline-first design.