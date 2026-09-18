# D006 — Isolated Linux Network-Link Interruption During Ambiguous Retry

Status: **VALIDATION — real kernel network-namespace/link interruption + TCP + SQLite evidence**  
Date: 2026-09-18  
Lead: Data, Persistence & Distributed Systems

## Problem / scope
The previous D006 block killed the server after commit. This block asks a materially different question: if both application processes remain alive but the network device becomes unavailable after commit and before the client receives the application response, does retry ambiguity remain, and does durable logical-operation identity still prevent duplicate mutation?

## SOURCE
- Linux `network_namespaces(7)` documents that network namespaces isolate networking resources including network devices, protocol stacks, routing tables, firewall rules, `/proc/net`, and port/socket namespaces. Linux man-pages are published at `https://www.kernel.org/pub/linux/docs/man-pages/`.
- `ip-link(8)` documents `ip link set ... up|down` as network-device configuration: `https://man7.org/linux/man-pages/man8/ip-link.8.html`.
- The prior D006 source set remains applicable for retry semantics and commit boundaries: RFC 9110 §9.2.2 and SQLite WAL/transaction documentation.

## SYNTHESIS
A live process and live TCP socket do not eliminate response ambiguity. A network-device outage can occur after durable application commit but before response delivery. The application therefore still needs a protocol-level answer to `was this logical operation already committed?`; reconnecting after link recovery cannot infer that fact from transport state alone.

## EXECUTABLE VALIDATION
Fixture: `research/data/fixtures/D006_network_namespace_link_interruption.py`.

### Environment
Actually executed 2026-09-18: Linux container, Python 3.13.5, Python `sqlite3`, IPv4 loopback TCP, `unshare -Urn`, and `ip link`. `dart` and `flutter` were absent. A direct `unshare -n` attempt failed with `Operation not permitted`; a combined fresh user+network namespace (`unshare -Urn`) succeeded. This distinction is retained rather than treating executable presence as privilege evidence.

### CLAIM / PROPERTY
For one logical `op-1:+10`, after server commit and before ACK receipt, bringing the isolated namespace's loopback device down must make the first attempt inconclusive to the client. After restoring the device, retry with durable operation identity must preserve one effect; the no-dedup alternative must expose duplicate application.

### TARGET / FAULT
The fixture creates a fresh user+network namespace, enables only its loopback interface, and runs client/server TCP communication there. The server commits to SQLite and signals the fault window. The fixture executes `ip link set dev lo down` while client and server remain alive. The client times out, closes the ambiguous attempt, the fixture restores `lo`, and the client retries the same logical operation.

### ORACLE
Safe case: first observation is timeout; retry result = 10; final counter = 10; durable operation rows = 1. Unsafe comparison: same first timeout and fault schedule, but retry/final counter = 20 when no durable logical-operation deduplication exists.

### OBSERVATION
```text
safe (('timeout', None), 10, 10, 1)
unsafe (('timeout', None), 20, 20, None)
D006 network-namespace link interruption: PASS
```

## DEBUG / ROOT CAUSE
The fault does not kill either application process. It removes the transport path during the post-commit/pre-response interval. The client's timeout therefore carries no proof about committed server state. The unsafe alternative reinterprets the retry as a new mutation and reaches 20. The safe alternative stores operation identity/result transactionally with the mutation and returns the prior result after link recovery.

## ALTERNATIVE COMPARISON
This is stronger than repeating server-death/EOF because the failure mechanism is now kernel network-device unavailability while application processes remain alive. It still does not model every network failure. Durable deduplication is one bounded alternative, not a universal exactly-once protocol.

## EVIDENCE LIMIT
This is an isolated Linux loopback network namespace on one host. It is not a veth/two-host topology, WAN loss/reorder, router/NAT failure, mobile radio transition, DNS/TLS failure, OS/power crash, concurrent clients, Firestore, Flutter, Android/iOS, browser/PWA, or production evidence. Timeout duration is fixture-specific. The test establishes the declared post-commit link-interruption boundary only.

## TRANSFER VALIDATION
OPEN: reproduce on a veth/two-namespace or remote-host boundary if trustworthy infrastructure is available, then on the exact product sync stack. Preserve exact product ref/version/build/backend identity and terminal semantic oracle.

## RELATED DOMAIN CHECK
- **Foundations:** F006 transport/apply/commit/ACK separation survives a different real failure mechanism; direct Dart/Flutter remains OPEN.
- **Architecture:** logical operation identity and dedup retention remain protocol/state-ownership decisions.
- **Mobile:** lifecycle/radio/platform connectivity transfer remains OPEN; a timeout/reconnect UI must not imply non-application.
- **Data:** materially strengthens D006 from server-death ambiguity to live-process network-device interruption.
- **Quality:** fault campaigns should vary causal mechanisms; one ambiguous-response schedule is not representative of all network failures.
- **Systems:** user/network namespace capability verification is part of trustworthy fault-injection setup; correctness dedup remains separate from replay authorization.
- **Design Studio / Web Manager / Marketing Manager:** checked for material relevance; no canonical cross-repo decision is changed by this bounded kernel/data mechanism, so no foreign canonical files were edited.

## HANDOFFS
- **Data → Quality:** preserve `commit → link down → client timeout → link up → retry → semantic-state oracle` as a distinct regression/fault schedule from process death.
- **Data → Mobile:** reproduce with the actual platform network/lifecycle controls before inferring mobile behavior.
- **Data → Systems:** future network fault infrastructure should record namespace/capability setup and prove the intended fault was actually applied.

## OPEN / CHANGE WATCH
- Direct Dart JIT/AOT and Flutter runtime validation remain OPEN.
- veth/two-namespace, remote/multi-host, packet loss/reorder, concurrent retry and real product/backend transfer remain OPEN.
- D005 storage-full/I/O/power-loss boundaries remain OPEN.
