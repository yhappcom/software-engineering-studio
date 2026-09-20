# F006 — Process Liveness / Socket Directionality Phase Isolation

Status: **BOUNDED PROFESSIONAL BOUNDARY CLOSED — ROOT CAUSE + FIX + REGRESSION VALIDATED**  
Evidence date: 2026-09-20

## Problem
F006 transport semantic oracles passed while accepted connected-socket fixtures remained alive. Listener ownership was falsified, then close-vs-destroy isolation identified the lifecycle boundary. This block now includes terminal regression evidence for the repaired combined fixture.

## SOURCE
Official Dart `Socket` API distinguishes the receive `Stream<Uint8List>` and send `IOSink` roles. `Socket.close()` is the IOSink/send-side close; `Socket.destroy()` destroys the socket in both directions.

## VALIDATION — four-way isolation retained
Exact target: `yhappcom/software-engineering-studio → 75ba5067f8b173cc2ce8e7fdf7a7effb2e9dcefe → run 35486660067 → Dart 3.13.3 stable/linux_x64 → Ubuntu 24.04.5, runner image 20260907.300.1 → evidence 2026-09-20`.

- `server-close` — natural exit.
- `refused-connect` — natural exit.
- `accepted-close` — BODY_DONE then timeout/orphan termination.
- `truncated-eof` — BODY_DONE then timeout/orphan termination.

This isolated the failing family to an accepted connected `Socket` using send-side close.

## DEBUG / ROOT CAUSE — close vs destroy discriminator
Exact target: `yhappcom/software-engineering-studio → d57d5531d9a5d96d21685d31e75bc2aaed051dd4 → run 35489259464 → Dart 3.13.3 stable/linux_x64 → Ubuntu 24.04.5, runner image 20260907.300.1 → evidence 2026-09-20`.

Same-run matrix result:
- `accepted-close` — FAIL: `F006_AB_BODY_DONE`, then remained alive until timeout; runner cleanup terminated the orphan Dart process.
- `accepted-destroy` — PASS: `F006_AB_BODY_DONE` and natural exit.
- controls `server-close` and `refused-connect` — PASS / natural exit.
- `truncated-eof` — retained close-path failure.

**ROOT CAUSE at this bounded target:** the fixture treated completion of send-side `Socket.close()` as if it were complete connected-socket teardown. The receive side remained capable of retaining Dart process liveness. Explicit bidirectional `destroy()` removed the retained-liveness symptom in the structurally matched accepted-socket case.

This does not mean every `Socket.close()` use is a leak. The tested fixture owned both endpoints and required complete teardown after its flushed test payload; graceful application protocols can require different shutdown semantics.

## FIX + REGRESSION
Commit `5aa89aa5c11c4baf68233a412566e891a855506a` changes the combined `research/foundations/fixtures/F006_dart_socket_boundary.dart` fixture to flush the intentionally truncated payload and explicitly `destroy()` the client while retaining peer teardown, truncated-EOF rejection and refused-connect oracles.

**VALIDATION:** exact workflow run `35491928998`, job `106028240397`, checkout `5aa89aa5c11c4baf68233a412566e891a855506a`, Dart SDK `3.13.3 stable/linux_x64`, Ubuntu `24.04.5`, runner image `ubuntu-24.04 20260907.300.1`, completed success. The combined fixture emitted all phases through `connect_failure_probe`, then `F006_DART_SOCKET_PASS truncated_eof_rejected=true connect_failure_observed=true bidirectional_teardown=true`, then `natural_process_exit_expected`; the Dart step completed successfully and the workflow immediately proceeded to post-job cleanup without the prior timeout/orphan termination.

**VERDICT:** the repaired combined target simultaneously preserves the two transport semantic oracles and natural process exit. This closes the named bounded F006 failure→isolation→root-cause→fix→regression chain.

## CONTRADICTIONS retained
- Replacing open-ended `ServerSocket.listen` with `server.first` did not restore natural exit: listener ownership was not the sole cause.
- Semantic PASS/BODY_DONE did not imply executable completion: application-level assertions alone were insufficient.

## Evidence dimensions
1. transport semantic oracle: PASS at bounded Dart/Linux loopback target;
2. server-only/refused-connect liveness: PASS;
3. accepted socket + send-side close: replicated FAIL natural exit;
4. structurally matched accepted socket + bidirectional destroy: PASS natural exit;
5. bounded retained-liveness root cause: established;
6. repaired combined semantic + natural-exit regression: PASS, run `35491928998`.

## EVIDENCE LIMIT
Dart 3.13.3/Linux loopback only. This does not establish WAN/TLS/mobile/browser behavior, general TCP half-close semantics, application ACK/durability, product protocol correctness, Android/iOS/Safari/PWA behavior, or a universal rule that `Socket.close()` is wrong. It is also Studio fixture evidence, not MintTap/LogMate production evidence.

## RELATED DOMAIN CHECK
- Foundations: F006 owns socket/process-liveness mechanism; F001/F004/F005 execution/async boundaries considered.
- Architecture: send-side completion and full resource-lifecycle completion are distinct contracts.
- Mobile: `dart:io` Linux loopback is not Android/iOS/browser/PWA evidence.
- Data: transport/process termination is not durable application completion.
- Quality: preserve natural process exit as an independent oracle and retain falsified listener hypothesis.
- Systems: CI timeout supplied containment/liveness evidence; successful regression now proves application exit at this target rather than runner cleanup.
- Design Studio / Web Manager / Marketing Manager: considered, not materially relevant to this bounded mechanism.
- Product: no MintTap/LogMate behavior claimed or modified.

## HANDOFFS
- Quality/Systems: require executable-completion/resource-lifecycle oracles separately from internal semantic PASS markers where retained resources can keep a process alive.
- Architecture: API completion must be interpreted at its documented contract boundary; send-side completion is not bidirectional teardown.
- Mobile/Data: transfer only the contract/oracle lesson, not Linux socket behavior.

## OPEN / VALIDATION
- Cross-platform/native/product transfer remains OPEN.
- WAN/TLS, protocol-level graceful shutdown and application acknowledgement/durability remain separate professional boundaries.
- No Foundations Stage 1 PASS is awarded from this block alone; return to Balance Loop for the next independent evidence gap.
