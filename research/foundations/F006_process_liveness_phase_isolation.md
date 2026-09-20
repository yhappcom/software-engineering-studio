# F006 — Process Liveness / Listener Lifecycle Phase Isolation

Status: **IN STUDY — SEMANTIC SOCKET ORACLE OBSERVED PASS; NATURAL PROCESS EXIT FAILURE ISOLATED; ALTERNATIVE LISTENER-LIFECYCLE RUN PENDING**  
Evidence date: 2026-09-20

## Problem

The earlier F006 record correctly preserved run `35437455712` as a bounded CI failure because the Dart command exceeded its one-minute outer deadline. At that time the evidence channel had not exposed command stdout, so socket correctness and the internal blocking phase remained OPEN.

The GitHub job-log channel is now available. This block re-inspects the exact historical job before creating another hypothesis.

## VALIDATION — recovered historical evidence

Exact historical target:

- repository: `yhappcom/software-engineering-studio`
- exact head: `835104ea9dac410b4f0a4d17f748882710f5921c`
- workflow run: `35437455712`
- job: `105882433731`
- Dart: `3.13.3 stable`, `linux_x64`
- OS: Ubuntu 24.04.5 LTS; runner image `ubuntu-24.04` version `20260907.300.1`

The decoded job log shows the fixture emitted:

`F006_DART_SOCKET_PASS truncated_eof_rejected=true connect_failure_observed=true`

at `2026-09-19T10:27:44.1491166Z`, roughly 0.25 seconds after the fixture step began. The workflow then remained alive until the one-minute step timeout at `10:28:56Z`. Runner cleanup explicitly terminated orphan process `dart:F006_dart_`.

## SYNTHESIS

The prior combined label “socket verdict/root cause OPEN” was too coarse once stdout became observable.

The bounded application-level transport oracles **did complete successfully** in that exact run:

1. EOF after the truncated length-prefixed body was rejected as frame completion;
2. connection to a released loopback port was classified as failure.

What failed was **natural Dart process termination after those oracles had already passed**. Therefore semantic transport-oracle success and process/resource-lifecycle success must be separate verdict dimensions.

This is not yet proof of which resource kept the isolate/event loop alive. The previous fixture used `ServerSocket.listen(...)`; although `server.close()` and accepted-socket cleanup were invoked, assigning the retained liveness specifically to the listener subscription without a controlled alternative would overstate the evidence.

## DEBUG / ROOT-CAUSE PROGRESSION

- **failure observation:** fixture command exceeds outer deadline;
- **recovered phase evidence:** semantic PASS marker occurs before the hang;
- **isolation:** the failure is post-oracle process/resource liveness, not failure to reach the socket oracle;
- **prior hypothesis:** changing client close-await ordering did not remove the hang — falsified;
- **new causal hypothesis:** one-shot listener lifecycle may avoid the retained liveness seen with the prior `ServerSocket.listen` structure;
- **check:** exact head `3904ca9806d8e48bb90b5f6019acbdffc60feffb` replaces the open-ended listener structure with `server.first`, explicit phase markers, bounded server/peer/client cleanup, and preserves the same semantic transport oracles;
- **current verdict:** workflow run `35484021836` is pending; no root cause or regression PASS is awarded until terminal evidence is recovered.

## ALTERNATIVE

The alternative fixture deliberately changes listener ownership/lifetime rather than another client close-order permutation. It emits phase markers for bind, connect, truncated-frame send, peer EOF consumption, released-port probe, semantic PASS, and expected natural process exit. This allows a future timeout to identify the last completed phase from job stdout.

## EVIDENCE LIMIT

The recovered PASS is bounded loopback/Linux/Dart evidence only. It does not establish WAN behavior, TCP reset/half-close semantics generally, TLS, mobile lifecycle/network transitions, browser networking, application ACK/durable completion, or product protocol correctness. The post-PASS liveness failure remains a real harness/resource-lifecycle defect until a causal mechanism is validated.

## RELATED DOMAIN CHECK

- **Foundations:** F006 transport framing/termination model and F001/F004/F005 Dart execution evidence checked.
- **Architecture:** transport semantic completion and process/resource lifecycle are distinct externally relevant contracts when exposed to callers/automation.
- **Mobile:** `dart:io` evidence is not browser/PWA evidence; Android/iOS lifecycle transfer remains OPEN.
- **Data:** transport termination remains below application durable completion/ACK semantics.
- **Quality:** recovered stdout materially changes failure classification; preserve semantic oracle and harness-liveness verdicts separately.
- **Systems:** independent CI timeout remains valid containment even when target semantic assertions pass; a PASS marker before timeout is not a successful executable run.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this transport/process-liveness diagnosis.
- **Product:** no product repository behavior is claimed or modified.

## HANDOFFS

- **Quality:** classify run `35437455712` as semantic-oracle PASS + executable-process-liveness FAIL, not a single undifferentiated socket failure.
- **Systems:** retain outer timeout; target assertions completing does not imply process/resource cleanup or successful CI completion.
- **Mobile/Data:** consume only the bounded transport semantic result; no platform/product/durability transfer is implied.

## OPEN / VALIDATION

- Recover terminal result and decoded logs for run `35484021836`.
- If the one-shot-listener alternative exits naturally, treat listener-lifecycle structure as a causal candidate and design a minimal A/B reproduction before claiming root cause.
- If it still hangs, use the emitted phase markers to isolate the remaining post-phase resource and do not return to blind close-order permutations.
- No Foundations PASS from this block.
