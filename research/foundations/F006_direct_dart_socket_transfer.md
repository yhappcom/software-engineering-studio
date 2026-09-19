# F006 — Direct Dart Socket Transfer

Status: **IN STUDY — HANG REPRODUCED; FIRST ROOT-CAUSE HYPOTHESIS FALSIFIED; OUTER CI CONTAINMENT VALIDATED**  
Evidence date: 2026-09-19

## Problem
F006 had executable Python/Linux stream-framing and connection-termination evidence, but direct Dart `dart:io` socket execution remained OPEN. With the hosted Dart path trustworthy for bounded Native execution, this block transfer-tests one central transport boundary rather than adding another Python model.

## SOURCE
Current Dart `dart:io` API documentation defines `Socket` as a TCP connection that is both a `Stream<Uint8List>` and an `IOSink`. `Socket.connect` completes with a socket or an error; its connect timeout bounds connection establishment and cancels ongoing connection attempts on timeout. `Socket.close()` closes the sink side; documentation warns buffered writes may require `flush()` before close. `dart:io` is not available to browser-based apps.

## SYNTHESIS
The prior F006 distinction remains the intended oracle: transport stream termination is not application-frame completion. A length-prefixed application frame must satisfy its own declared length; EOF after a partial body is not success. A connection-establishment failure is distinct from an established connection's application outcome.

## VALIDATION
Fixture: `research/foundations/fixtures/F006_dart_socket_boundary.dart`  
Workflow: `.github/workflows/f006-dart-socket-boundary.yml`  
Initial fixture head: `7f0680279a9afa753e9e0e5010f0a5a0c886f053`  
First close-order fix head: `6f78f6ee8ccda32143df55d2a7f3820a117cc5c7`  
Bounded-run workflow head: `835104ea9dac410b4f0a4d17f748882710f5921c`  
Requested runtime: Dart 3.13.3, GitHub-hosted Ubuntu 24.04.

### Claim / oracle
1. Loopback TCP client sends a frame declaring a five-byte body but transmits only `HE`, flushes, and terminates its send path. The server must reject frame completion because body length 2 is less than declared length 5.
2. A second probe releases a loopback listening port and requires a subsequent `Socket.connect` to fail rather than be classified as an established connection.

### Failure observation and reproduction
Run `35434862199`, job `105875694971`, exact head `7f0680279a9afa753e9e0e5010f0a5a0c886f053` reached the real fixture step and remained in progress rather than producing the expected bounded verdict.

The first causal hypothesis was that awaiting `client.close()` before allowing the peer EOF oracle to complete created an unnecessary wait cycle. Commit `6f78f6ee8ccda32143df55d2a7f3820a117cc5c7` changed the order: initiate close, await the server oracle with a five-second Future timeout, then await close completion with a five-second timeout.

**CONTRADICTION / FALSIFICATION:** regression run `35434895889`, job `105875778624`, exact head `6f78f6ee8ccda32143df55d2a7f3820a117cc5c7` again reached `Run F006 Dart socket boundary fixture` and remained `in_progress` for far longer than either five-second Future timeout. Therefore the original close-order hypothesis is not an adequate root cause. No Dart/runtime defect is assigned from this observation alone.

A partial running-job log could not be retrieved through the current GitHub evidence channel, so the exact internal await/resource retaining progress is still **OPEN**.

### Validation-governance correction and result
The workflow itself originally lacked a job/step timeout, allowing a faulty fixture to consume runner time without a bounded verdict. Commit `835104ea9dac410b4f0a4d17f748882710f5921c` added a three-minute job timeout, one-minute fixture-step timeout, and an F006 concurrency group with `cancel-in-progress: true`.

**VALIDATION:** bounded run `35437455712`, job `105882433731`, exact head `835104ea9dac410b4f0a4d17f748882710f5921c`, completed with `failure`. Setup, checkout, Dart setup, and environment recording all succeeded. The fixture step started at `2026-09-19T10:27:43Z` and ended as `failure` at `10:28:56Z`; the job completed at `10:28:58Z`. This validates the outer harness containment rung: the previously runaway fixture is now independently bounded by CI and yields a terminal failure rather than consuming an unbounded runner interval.

**EVIDENCE LIMIT:** the failed bounded step still does not expose command-level fixture output through the current evidence channel, so it does not identify which internal await/resource retained progress. It is not a socket-correctness verdict and not a root-cause proof.

**QUALITY / SYSTEMS SYNTHESIS:** application-level Future timeouts are not sufficient CI resource-governance controls. A validation harness that can itself hang needs an independent outer execution deadline. The outer deadline is now executable evidence, not merely a proposed safeguard.

A workflow-definition commit also triggered run `35434853921` before the fixture existed at that head. That run is not a valid fixture verdict and must not be used as F006 evidence.

## VALIDATION / OPEN
- Direct Dart socket correctness remains OPEN; do not award PASS from the bounded failure.
- Exact blocking/resource-retention phase remains OPEN because command-level fixture output is unavailable through the current evidence channel.
- Do not spend another runner cycle on close-order permutations. If F006 resumes, isolate phases into independently observable processes/steps or use an external process supervisor that can preserve phase-level output before termination.
- Balance Loop should now compare that debugging cost against higher-leverage independent evidence such as exact canonical LogMate toolchain/lock/build/artifact transfer or remaining F002/F003 prerequisites.
- Real remote timeout/partition, packet-level behavior, half-close/reset distinctions, TLS, Android/iOS connectivity/background state, browser/PWA networking and product protocol behavior remain OPEN.

## EVIDENCE LIMIT
Loopback TCP on hosted Linux cannot establish WAN behavior, radio/network transitions, mobile lifecycle behavior, browser semantics, peer durable commit, application ACK or exactly-once processing. The released-port probe is deliberately only a local connect-failure classification test. The reproduced hang plus bounded failure validates a harness failure mode, falsifies one causal hypothesis, and validates outer containment; it does not establish a Dart socket semantic defect.

## RELATED DOMAIN CHECK
- **Foundations:** F001/F004/F005 hosted Dart evidence enables this transfer; F006 base framing/termination model checked.
- **Architecture:** frame and terminal-state semantics are interface contracts when observable.
- **Mobile:** `dart:io` excludes browser apps; Android/iOS/browser transfer remains separate.
- **Data:** D006 operation identity/ACK/idempotency remains above transport and is not replaced by this fixture.
- **Quality:** oracle checks semantic frame completeness, not merely absence of exceptions; the hang and bounded failure demonstrate why the harness itself also needs an independent termination oracle/deadline.
- **Systems:** bounded CI execution is part of controlled evidence production; TLS, resource exhaustion, performance and release artifact identity remain separate.
- **Design Studio / Web Manager / Marketing Manager:** considered under the cross-repository contract; not materially relevant to this bounded transport/harness mechanism, so no canonical files were edited there.
- **Product:** no new product repository audit was required; no product implementation claim is made.

## HANDOFFS
- **Quality:** preserve run `35437455712` as executable evidence that the independent CI deadline terminates the runaway validation step. It is containment evidence, not socket correctness.
- **Systems:** CI evidence pipelines should independently bound target execution; application timeout logic is not a substitute for runner/job resource controls.
- **Data:** consume no new Dart transport correctness claim; application completion/ACK/durable-effect semantics remain above this unresolved transport fixture.
- **Mobile:** browser/PWA cannot inherit this `dart:io` result; use browser networking APIs and exact deployment context for transfer validation.
