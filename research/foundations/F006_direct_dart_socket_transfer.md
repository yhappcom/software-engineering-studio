# F006 — Direct Dart Socket Transfer

Status: **IN STUDY — HOSTED VALIDATION IN PROGRESS**  
Evidence date: 2026-09-19

## Problem
F006 had executable Python/Linux stream-framing and connection-termination evidence, but direct Dart `dart:io` socket execution remained OPEN. With the hosted Dart path now trustworthy for bounded Native execution, this block transfer-tests one central transport boundary rather than adding another Python model.

## SOURCE
Current Dart `dart:io` API documentation defines `Socket` as a TCP connection that is both a `Stream<Uint8List>` and an `IOSink`. `Socket.connect` completes with a socket or an error; its connect timeout bounds connection establishment and cancels ongoing connection attempts on timeout. `Socket.close()` closes the sink side; documentation warns buffered writes may require `flush()` before close. `dart:io` is not available to browser-based apps.

## SYNTHESIS
The prior F006 distinction survives as the intended oracle: transport stream termination is not application-frame completion. A length-prefixed application frame must satisfy its own declared length; EOF after a partial body is not success. A connection-establishment failure is a distinct observation from an established connection's application outcome.

## VALIDATION
Fixture: `research/foundations/fixtures/F006_dart_socket_boundary.dart`  
Workflow: `.github/workflows/f006-dart-socket-boundary.yml`  
Exact fixture head: `7f0680279a9afa753e9e0e5010f0a5a0c886f053`  
Requested runtime: Dart 3.13.3, GitHub-hosted Ubuntu 24.04.

### Claim / oracle
1. Loopback TCP client sends a frame declaring a five-byte body but transmits only `HE`, flushes, and closes its send side. The server must observe the four bytes `00 05 48 45` and reject frame completion because body length 2 is less than declared length 5.
2. A second probe releases a loopback listening port and requires a subsequent `Socket.connect` to fail rather than be classified as an established connection.

### Current observation
Run `35434862199`, job `105875694971`, exact head `7f0680279a9afa753e9e0e5010f0a5a0c886f053` entered real GitHub-hosted execution. At the evidence cutoff the job remained `in_progress`; no PASS/FAIL is awarded yet.

A workflow-definition commit also triggered run `35434853921` before the fixture existed at that head. That run is not a valid fixture verdict and must not be used as F006 evidence.

## VALIDATION / OPEN
- Await exact run `35434862199` completion and step verdict before changing F006's direct-Dart gap.
- Add no PASS from queue/start evidence.
- Real remote timeout/partition, packet-level behavior, half-close/reset distinctions, TLS, Android/iOS connectivity/background state, browser/PWA networking and product protocol behavior remain OPEN.

## EVIDENCE LIMIT
Loopback TCP on hosted Linux cannot establish WAN behavior, radio/network transitions, mobile lifecycle behavior, browser semantics, peer durable commit, application ACK or exactly-once processing. The released-port probe is deliberately only a local connect-failure classification test.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F004/F005 hosted Dart evidence enables this transfer; F006 base framing/termination model checked.
- **Architecture:** frame and terminal-state semantics are interface contracts when observable.
- **Mobile:** `dart:io` excludes browser apps; Android/iOS/browser transfer remains separate.
- **Data:** D006 operation identity/ACK/idempotency remains above transport and is not replaced by this fixture.
- **Quality:** oracle checks semantic frame completeness, not merely absence of exceptions.
- **Systems:** TLS, resource exhaustion, performance and release artifact identity remain separate.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this bounded transport mechanism.
- **Product:** no new product repository audit was required; no product implementation claim is made.

## HANDOFFS
- **Data / Quality:** if the direct Dart regression succeeds, consume it only as evidence that Dart TCP EOF/connection failure must remain distinct from application completion; preserve explicit operation/ACK/recovery oracles.
- **Mobile:** browser/PWA cannot inherit this `dart:io` result; use browser networking APIs and exact deployment context for transfer validation.
