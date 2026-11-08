# D006 — Durable receipt retry and atomic applied-cursor failure-first canary

**Date:** 2026-11-08 Asia/Seoul. **Lead:** Data D006; **support:** Quality, Architecture, Foundations, Systems, Mobile. **Classification:** INDEPENDENT EXECUTABLE MODEL / OBSERVATION / SYNTHESIS / ENGINEERING JUDGMENT / OPEN / DEPENDENCY / TRANSFER VALIDATION NOT YET ESTABLISHED.

## Scope and source identity

- Public Studio latest checked before this study: `yhappcom/software-engineering-studio → main@b3d08c9656a1db2ad97d43f00c76b1489dbed7b7 → 2026-11-08`.
- Private product read-only current `main@f4bcd2f7b7e77039e29653baa1cc93797673885b`, declared `pubspec.yaml 1.0.0+1`, 2026-11-08. **Not assumed deployed.** Current W013 product Draft PR51 `docs/w013-ios-boundary-adoption-20261108@62d7295da6b447ba45dd3f0196c81ec449f2cdf9` on PR50 `verify/w013-android-runtime-20261108@c08feb25517c32a6104f4cc1ef49e7a4a9f33ddd`; 66 branches and 17 open PRs. Product Sync policy authority is unmerged Draft PR42 `docs/w013-policy-execution-alignment-20261106@71d8a1d4c3650fce0200677fa0db2345e444712d`, `docs/specs/local-first-manual-delta-sync-contract.md` blob `1b7441bf6bf06bcd8953ff87c7660de159e2c19e`. Owner-approved Automatic+Manual Delta is not proof of implemented authenticated Push/Pull, Receipt or Cursor. `main` retains older Manual-only copy; do not promote it over the approved Draft contract.
- No private product source, credentials, user data or proprietary test fixture was copied or executed. No product repo write, CI dispatch, PR or release operation.

## Independent executable experiment — Python stdlib SQLite, not Dart/Sembast

**Environment:** local Python **3.13.5**, standard-library `sqlite3`, temporary private directory, three independent file-backed SQLite databases (replica A, replica B, server) plus one deliberately unsafe client; WAL enabled. Executed command `python /mnt/data/studio_validation/D006_sqlite_delta_receipt_canary.py`. The script is a disposable local synthetic experiment, not a committed product implementation. Exit code 0; stdout:

`D006_SQLITE_CANARY_PASS 6/6: lost-ACK retry, receipt uniqueness, collision reject, atomic rollback, replay convergence, cursor-first loss counterexample`

**Synthetic schema:** local `operations(opid PRIMARY KEY,digest,payload,acked)`, `records(k PRIMARY KEY,v)`, `cursor_state(id=1,cursor)`; server `events(seq AUTOINCREMENT PRIMARY KEY,opid UNIQUE,digest,payload)`. Operation payloads use canonical sorted JSON and SHA-256. Each local record+cursor apply is enclosed in one SQLite transaction. Server duplicate OpID returns the previously committed sequence only when digest matches; mismatched digest raises. All fixture identities and values are invented (`op-1`, `flight-1`, `1:20`).

| Failure-first control | Expected oracle | Observed |
| --- | --- | --- |
| ACK loss after server commit | Client remains pending; same ID/digest retry returns original receipt, one server event | PASS |
| Duplicate receipt | `COUNT(events)=1` despite retry | PASS |
| Same OpID, different digest | Reject, no event mutation | PASS |
| Crash injected after local record apply but before cursor update | Transaction rollback removes both record and cursor advance | PASS |
| Close/reopen B and replay twice | A/B record states equal; B cursor equals server sequence; exactly one local operation | PASS |
| Deliberately unsafe cursor-first commit then interruption | Subsequent pull skips the record forever while cursor claims applied | **COUNTEREXAMPLE REPRODUCED** |

This is a *mechanism* demonstration: **downloaded/acknowledged is not durably applied**, and **cursor-first commit can silently lose data**. It is not a proof of the product's implementation, cross-process race safety, Firebase authentication, operation ACL, causal ordering, tombstone/LWW, multi-generation restore, server sequencing under concurrency, encryption or physical-device crash durability.

## Causal explanation, alternatives and falsifiable next gate

The safe implementation couples the **semantic local Apply** and **contiguous applied Cursor** in the *same atomic transaction*, with the OpID/digest receipt protecting ACK-loss retries. On interruption before commit, both remain unapplied and are replayable. After commit, both are durable to the modeled transaction boundary. The negative implementation commits the cursor before the record: the cursor's claim is ahead of reality, so replay skips a missing operation.

Alternative A: persist cursor after each record in the same transaction (**preferred for this minimal model**). Alternative B: use an explicit durable inbox/pending-event journal with independent replay recovery; it may be required if product Apply spans multiple stores, transactions or backends, but its recovery/ordering invariants must be independently tested. Alternative C: cursor-first shortcut (**rejected by executed counterexample**). These are engineering alternatives, **not product decisions**.

**Next independent test gate:** extend to two concurrently committing writers and a durable event journal; inject termination at pre-server-commit, post-server-commit/pre-ACK, pre-local-commit, post-local-commit/pre-response and retry-after-restart, verify contiguous sequence with a gap, identical/mismatched OpID, owner/generation mismatches, tombstone conflict and old-client mutation. For LogMate transfer, exact-head authorized Dart/Sembast file-backed tests and authenticated Firebase Emulator tests remain separate mandatory gates; no product code/test changes authorized here.

## RELATED DOMAIN CHECK / HANDOFFS

- **Foundations:** SQLite transaction atomicity and crash interruption; Python model is not Dart runtime transfer.
- **Architecture:** receipt (remote acceptance) and applied cursor (local durable progress) are different authorities. API must not conflate them.
- **Mobile:** background suspension/restart and offline catch-up require replay from durable local progress, not network response.
- **Data:** D006 owns OpID immutability, idempotency, durable cursor, event order and convergence; this experiment strengthens one prerequisite only.
- **Quality:** injected failure and deliberately unsafe counterexample are mandatory; a happy-path replay alone would not discriminate cursor ordering.
- **Systems:** server-side authentication/authorization, generation, receipt storage and concurrency remain OPEN; local SQLite cannot substitute for Firebase.
- **Design Studio / Web Manager / Marketing Manager:** no material dependency or write needed in this bounded study.

**Gate:** D006 Stage 1 remains **NOT PASS**. **New independent evidence:** file-backed SQLite transaction/ACK/cursor counterexample executed 6/6. **OPEN:** exact reproduction script is currently local to the study environment (not yet public Studio fixture), independent runner transfer, Dart/Sembast, backend auth, real cross-device sync and release.
