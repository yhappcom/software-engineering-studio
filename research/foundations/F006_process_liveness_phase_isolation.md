# F006 — Process Liveness / Socket Directionality Phase Isolation

Status: **IN STUDY — CLOSE-vs-DESTROY CAUSAL DISCRIMINATOR CONFIRMED; COMBINED REGRESSION PENDING**  
Evidence date: 2026-09-20

## Problem
F006 transport semantic oracles passed while accepted connected-socket fixtures remained alive. Listener ownership had already been falsified. This block isolates whether send-side `Socket.close()` versus bidirectional `Socket.destroy()` explains the retained process liveness.

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
- `accepted-close` — FAIL: `F006_AB_BODY_DONE` at 04:29:28Z, then remained alive until the one-minute timeout; runner cleanup terminated the orphan Dart process.
- `accepted-destroy` — PASS: `F006_AB_BODY_DONE` at 04:29:30Z and the job proceeded immediately to cleanup with no orphan process.
- controls `server-close` and `refused-connect` — PASS / natural exit.
- `truncated-eof` — retained close-path failure.

**ROOT CAUSE at this bounded target:** the fixture treated completion of send-side `Socket.close()` as if it were complete connected-socket teardown. The receive side remained capable of retaining Dart process liveness. Replacing that lifecycle operation with explicit bidirectional `destroy()` removes the retained-liveness symptom in the structurally matched accepted-socket case.

This does not mean every `Socket.close()` use is a leak. It means the tested fixture's ownership contract required bidirectional teardown, while `close()` only satisfied its send-side contract.

## CONTRADICTIONS retained
- Replacing open-ended `ServerSocket.listen` with `server.first` did not restore natural exit: listener ownership is not the sole cause.
- Semantic PASS/BODY_DONE did not imply executable completion: application-level assertions alone were insufficient.

## FIX / regression
Commit `5aa89aa5c11c4baf68233a412566e891a855506a` changes the combined `F006_dart_socket_boundary.dart` fixture to flush the intentionally truncated frame and then explicitly `destroy()` the client, while retaining peer teardown, truncated-EOF rejection, and refused-connect oracles.

**VALIDATION pending:** the combined fixture must still demonstrate both semantic PASS and natural process exit in hosted execution. Do not call F006 closed until that regression is terminal-success evidence.

## Evidence dimensions
1. transport semantic oracle: PASS at bounded Dart/Linux loopback target;
2. server-only/refused-connect liveness: PASS;
3. accepted socket + send-side close: replicated FAIL natural exit;
4. structurally matched accepted socket + bidirectional destroy: PASS natural exit;
5. bounded retained-liveness root cause: established;
6. repaired combined semantic + natural-exit regression: PENDING.

## EVIDENCE LIMIT
Dart 3.13.3/Linux loopback only. This does not establish WAN/TLS/mobile/browser behavior, general TCP half-close semantics, application ACK/durability, product protocol correctness, or a universal rule that `Socket.close()` is wrong. `destroy()` is appropriate here because this fixture owns both endpoints and requires teardown after its flushed test payload; graceful application protocols may require different shutdown semantics.

## RELATED DOMAIN CHECK
- Foundations: F006 owns socket/process-liveness mechanism; F001/F004/F005 execution/async boundaries considered.
- Architecture: send-side completion and full resource-lifecycle completion are distinct contracts.
- Mobile: `dart:io` Linux loopback is not Android/iOS/browser/PWA evidence.
- Data: transport/process termination is not durable application completion.
- Quality: preserve natural process exit as an independent oracle and retain falsified listener hypothesis.
- Systems: CI timeout provided containment/liveness evidence; runner cleanup is not application cleanup.
- Design Studio / Web Manager / Marketing Manager: considered, not materially relevant.
- Product: no MintTap/LogMate behavior claimed or modified.

## HANDOFFS
- Quality/Systems: require executable-completion/resource-lifecycle oracles separately from internal semantic PASS markers where retained resources can keep a process alive.
- Architecture: API completion must be interpreted at its documented contract boundary; send-side completion is not bidirectional teardown.
- Mobile/Data: transfer only the contract/oracle lesson, not Linux socket behavior.

## OPEN / VALIDATION
- Recover/run the combined fixture at commit `5aa89aa5...` and require semantic PASS + natural exit.
- Cross-platform/native/product transfer remains OPEN.
- No Foundations PASS from this block alone.
