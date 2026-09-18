# D006 — Real TCP Ambiguous Retry Across Server Process Restart

Status: **VALIDATION — bounded real localhost TCP + OS process restart evidence**  
Date: 2026-09-18  
Lead: Data, Persistence & Distributed Systems

## Problem / claim
A client can lose the response after a server has committed a mutation. Transport EOF therefore does not establish non-application. Retrying the same logical mutation after the server process restarts duplicates the effect unless the application protocol preserves stable logical operation identity and durable deduplication state.

## SOURCE
- IETF RFC 9110 §9.2.2 defines idempotency by intended server effect and explicitly motivates retry after communication failure when the client cannot read the response. It does not make arbitrary non-idempotent application mutations safe to retry.
- SQLite WAL documentation states that WAL commit occurs when a commit record is appended to the WAL and that the WAL is part of persistent database state. SQLite transaction documentation separates transaction commit/rollback semantics from connection lifetime.

## SYNTHESIS
The relevant end-to-end state machine is:

`logical operation id → TCP delivery → server apply → DB commit → process failure / ACK loss → client ambiguity → server restart → retry → durable dedup lookup → ACK`.

`connection closed before response` is compatible with both `not applied` and `applied+committed but response lost`. Retry safety therefore depends on application semantics, not TCP reconnect alone.

## EXECUTABLE VALIDATION
Fixture: `research/data/fixtures/D006_real_tcp_ambiguous_retry_restart.py`

Environment actually executed before persistence: Python 3.13.5 / Linux container / IPv4 loopback TCP / Python sqlite3 runtime, 2026-09-18. Separate `multiprocessing` server processes were used. `dart` and `flutter` executables were absent on the same environment recheck.

### CLAIM
Stable operation identity plus durable deduplication survives an application-server process crash after commit but before ACK in this bounded protocol; attempt-only handling does not.

### SPEC / PROPERTY
One logical `op-1` with delta `+10` must have one logical effect even when delivery is retried after an ambiguous connection termination.

### TARGET / STATE
A localhost TCP server owns a SQLite database containing a counter and, in the safe alternative, an `ops(id PRIMARY KEY, result)` table. The first server commits and then calls `os._exit(33)` before sending application response bytes. A fresh server process opens the same DB and receives the retry.

### ORACLE
Independent terminal-state assertions require safe final counter `10`, exactly one durable operation record, and retry result `10`. The deliberately unsafe comparison must expose duplicate effect `20` under the same failure schedule.

### OBSERVATION
```text
safe b'' 33 b'{"result": 10}\n' 0 10 1
unsafe b'' 33 b'{"result": 20}\n' 0 20
D006 real TCP ambiguous-retry restart: PASS
```

The first client observed EOF (`b''`) while the first server exited 33 after commit. After restart, durable dedup returned 10 without a second mutation. Without operation identity/deduplication, retry applied the delta again and returned/finalized 20.

### ROOT CAUSE
The unsafe protocol identifies network attempts rather than logical operations. Once ACK bytes are absent, the client cannot infer whether the server committed. Reconnecting does not repair that epistemic gap. The safe bounded alternative moves operation identity and prior result into the same durable database transaction as the mutation, so the restarted process can distinguish a retry from a new logical operation.

### ALTERNATIVE
Durable operation-id/result deduplication is one valid bounded alternative for this single-database mutation. It is not a universal exactly-once protocol.

## EVIDENCE LIMIT
This is real socket communication and real application-process termination/restart, but only over localhost on one host. It is **not** WAN packet-loss, router failure, mobile radio transition, OS crash, power loss, multi-host partition, concurrent multi-writer, Firestore, Flutter, Android/iOS, browser/PWA, or production evidence. SQLite and operation state share one local transaction here; external side effects would require a different protocol. The test does not establish exactly-once end-to-end semantics.

## TRANSFER VALIDATION
OPEN: repeat the same ambiguous `commit-before-ACK` schedule against the exact LogMate/MintTap persistence/sync stack when implemented and against a real remote transport or controllable network namespace. Preserve backend/app version and artifact identity.

## RELATED DOMAIN CHECK
- **Foundations:** F006 delivery/frame/apply/commit/ACK separation is directly reproduced with real TCP plus process restart; F001 Dart/Flutter remains toolchain-blocked.
- **Architecture:** operation identity and dedup lifetime are protocol/state-ownership contracts, not retry-library details.
- **Mobile:** background/process death and reconnect can create this ambiguity; platform transfer remains OPEN.
- **Data:** extends D006 from deterministic modeled retry ambiguity to real socket/process/persistent-state evidence; consumes D005 process-crash persistence boundary.
- **Quality:** provides a reusable fault schedule: commit → kill-before-ACK → restart → retry → fresh semantic oracle.
- **Systems:** replay/security authorization are separate from correctness idempotency; localhost evidence does not validate hostile replay handling.
- **Design Studio / Web Manager / Marketing Manager:** considered; no canonical decision there changes this transport/data mechanism.
- **Product:** no product repository was audited in this block, so no new product implementation claim is made.

## HANDOFFS
- **Data → Quality:** reuse this out-of-process network ambiguity schedule in recovery/regression suites; require a terminal semantic oracle, not only successful reconnect.
- **Data → Mobile:** reproduce on the eventual exact Flutter/mobile persistence and sync implementation under process/background/network interruption.
- **Data → Architecture:** require stable logical operation identity and dedup retention semantics wherever retryable non-idempotent effects cross an ambiguous ACK boundary.
- **Data → Systems:** if operation IDs cross trust boundaries, separately threat-model replay, authorization and retention/privacy.

## OPEN / CHANGE WATCH
- Real remote/network-namespace interruption and multi-host partition remain OPEN.
- Concurrent retry, dedup retention/GC, crash during dedup transaction, external side effects and operation-id collision remain OPEN.
- Direct Dart/Flutter execution remains OPEN because no trustworthy executable is available in the current environment.
