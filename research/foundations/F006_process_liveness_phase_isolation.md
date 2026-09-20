# F006 — Process Liveness / Socket Directionality Phase Isolation

Status: **IN STUDY — SEMANTIC ORACLES PASS; ACCEPTED SOCKET CASES RETAIN PROCESS; CLOSE-vs-DESTROY CAUSAL TEST PENDING**  
Evidence date: 2026-09-20

## Problem
The original and one-shot-listener F006 fixtures emitted their semantic PASS markers but did not naturally terminate. Listener ownership was already falsified as the sole cause. The next block recovers the four-way isolated run and uses the smallest failing case to form a source-backed causal discriminator.

## VALIDATION — four-way isolation
Exact target: `yhappcom/software-engineering-studio → 75ba5067f8b173cc2ce8e7fdf7a7effb2e9dcefe → run 35486660067 → Dart 3.13.3 stable/linux_x64 → Ubuntu 24.04.5, runner image 20260907.300.1 → evidence 2026-09-20`.

Per-case terminal results:
- `server-close` — PASS / natural exit.
- `refused-connect` — PASS / natural exit.
- `accepted-close` — FAIL: body completed, then process remained alive until the independent one-minute timeout.
- `truncated-eof` — FAIL: body completed, then process remained alive until the independent one-minute timeout.

Decoded logs for both failing cases contain `F006_AB_BODY_DONE ... natural_exit_expected=true` before timeout; runner cleanup terminates the orphan Dart process. The common boundary is therefore creation of an accepted connected `Socket`, not server bind/close alone or a refused connection alone.

## SOURCE
Current official Dart `Socket.destroy()` documentation states that `destroy()` destroys the socket in both directions, while `close()` inherited from `IOSink` only closes the socket for sending data. `Socket` is simultaneously a receive `Stream<Uint8List>` and send `IOSink`.

## SYNTHESIS / causal hypothesis
The smallest failure (`accepted-close`) calls `client.close()` and destroys the accepted peer. Because `Socket.close()` is a send-side sink close rather than a documented bidirectional destruction primitive, successful completion of its returned future is not sufficient evidence that the receive side no longer retains process liveness. This is a hypothesis, not yet ROOT CAUSE.

## DEBUG — close vs destroy discriminator
Fixture `research/foundations/fixtures/F006_liveness_ab.dart` now adds `accepted-destroy`, structurally identical to `accepted-close` except both connected endpoints use `destroy()` after server close. Workflow `.github/workflows/f006-liveness-ab.yml` runs both cases alongside the retained controls.

Exact fixture commit `18447ee486b24eade05a5e3478957bf5c804958c`; exact workflow head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4`. A terminal run was not yet available when this record was written. Do not promote the directionality hypothesis to root cause until `accepted-close` fails again while `accepted-destroy` naturally exits under the same matrix environment.

## CONTRADICTION retained
Replacing open-ended `ServerSocket.listen` with `server.first`, awaiting `server.close`, and bounding operations did not restore natural exit. Listener ownership is not the sole cause at this target.

## Evidence dimensions
1. transport semantic oracle: PASS at bounded Dart/Linux loopback target;
2. server-only and refused-connect natural process liveness: PASS;
3. accepted-connected-socket cases using send-side `close()`: FAIL natural exit;
4. bidirectional-destroy causal discriminator: PENDING;
5. exact retained-resource root cause: OPEN.

## EVIDENCE LIMIT
Bounded Dart 3.13.3/Linux loopback evidence only. It does not establish WAN/TLS/mobile/browser behavior, general TCP half-close semantics, application ACK/durability, product protocol correctness, or that every use of `Socket.close()` leaks resources. A future close-vs-destroy A/B result applies only to the tested lifecycle unless transferred.

## RELATED DOMAIN CHECK
- Foundations: F006 owns the socket/process-liveness mechanism; F001/F004/F005 execution/async boundaries considered.
- Architecture: send-side completion and bidirectional resource lifecycle are distinct observable contracts.
- Mobile: `dart:io` loopback is not Android/iOS or browser/PWA networking evidence.
- Data: transport/process termination is not durable application completion.
- Quality: preserve independent process-exit oracle and the failed listener hypothesis; do not infer cause from correlation alone.
- Systems: CI timeout remains containment and liveness evidence, not semantic transport failure.
- Design Studio / Web Manager / Marketing Manager: considered, not materially relevant.
- Product: no MintTap/LogMate behavior claimed or modified.

## HANDOFFS
- Quality/Systems: an internal PASS marker can coexist with a retained native resource that prevents executable completion; process exit must remain an independent oracle.
- Mobile/Data: consume only the bounded socket semantic/liveness distinction; no platform or durability transfer is implied.

## OPEN / VALIDATION
- Recover the workflow triggered by exact head `d57d5531d9a5d96d21685d31e75bc2aaed051dd4` when available.
- Root-cause criterion: replicate `accepted-close` failure and observe `accepted-destroy` natural exit in the same environment; otherwise falsify/refine the directionality hypothesis.
- If confirmed, repair the combined semantic fixture with explicit bidirectional teardown and require both semantic oracle PASS and natural process exit as regression evidence.
- No Foundations PASS from this block.
