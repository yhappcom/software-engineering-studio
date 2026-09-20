# F006 — Process Liveness / Listener Lifecycle Phase Isolation

Status: **IN STUDY — SEMANTIC SOCKET ORACLES PASS; NATURAL PROCESS EXIT FAILS AFTER ALL PHASES; FOUR-WAY A/B ISOLATION PENDING**  
Evidence date: 2026-09-20

## Problem

The original F006 run reached its semantic socket PASS marker and then remained alive until the outer CI deadline. A one-shot `server.first` alternative was introduced to test whether the prior open-ended `ServerSocket.listen` ownership structure caused the retained liveness. This block recovers that alternative before forming another hypothesis.

## VALIDATION — original failure retained

Exact historical target:

- repository: `yhappcom/software-engineering-studio`
- exact head: `835104ea9dac410b4f0a4d17f748882710f5921c`
- workflow run: `35437455712`
- job: `105882433731`
- Dart: `3.13.3 stable`, `linux_x64`
- OS: Ubuntu 24.04.5 LTS; runner image `ubuntu-24.04` version `20260907.300.1`

The decoded log emitted `F006_DART_SOCKET_PASS truncated_eof_rejected=true connect_failure_observed=true` before the command later timed out. Runner cleanup terminated the orphan Dart process. The bounded truncated-frame EOF and released-port failure oracles therefore passed while natural process/resource-lifecycle completion failed.

## CONTRADICTION — one-shot listener hypothesis falsified

Exact alternative:

- exact head: `3904ca9806d8e48bb90b5f6019acbdffc60feffb`
- workflow run: `35484021836`
- job: `106006913686`
- Dart: `3.13.3 stable`, `linux_x64`
- OS: Ubuntu 24.04.5 LTS; runner image `ubuntu-24.04` version `20260907.300.1`

The decoded log completed every instrumented phase:

`bind_server → connect_client → send_truncated_frame → consume_peer_eof → connect_failure_probe → F006_DART_SOCKET_PASS → natural_process_exit_expected`

The final phase marker appeared at `02:27:29.6768082Z`; the command nevertheless timed out roughly one minute later and runner cleanup again terminated the orphan Dart process.

**VALIDATION:** replacing `ServerSocket.listen` with one-shot `server.first`, awaiting `server.close`, bounding peer/client operations, and preserving the semantic oracles did **not** restore natural process exit.

**CONTRADICTION:** the prior listener-ownership hypothesis is falsified at this bounded target. The retained liveness occurs after every application phase in the alternative, so another blind close-order/listener permutation is not justified.

## DEBUG — next causal isolation

A new fixture `research/foundations/fixtures/F006_liveness_ab.dart` decomposes the combined target into four independently executed cases:

1. `server-close` — bind then close a server without accepting a connection;
2. `accepted-close` — accept one loopback connection and close/destroy both endpoints;
3. `truncated-eof` — execute only the truncated-frame EOF path;
4. `refused-connect` — execute only the released-port connection-failure probe.

Workflow `.github/workflows/f006-liveness-ab.yml` runs these as separate matrix jobs under the same Dart 3.13.3 / Ubuntu 24.04 class, with an independent one-minute deadline per process. Exact workflow head `75ba5067f8b173cc2ce8e7fdf7a7effb2e9dcefe`, run `35486660067` is queued/pending at this record. No root cause is awarded before terminal per-case evidence.

The diagnostic is intentionally phase-decomposed rather than another combined fixture edit. If one isolated case hangs, it narrows the retained-resource family. If all four exit independently while the combined fixture hangs, the evidence instead points toward interaction/composition or a lifecycle detail absent from the isolated cases.

## SYNTHESIS

F006 now has three distinct verdict dimensions:

1. **transport semantic oracle:** PASS at the bounded Dart/Linux loopback target;
2. **combined executable natural liveness:** FAIL in both the original and structurally different one-shot-listener fixtures;
3. **specific retained-resource root cause:** OPEN.

A target PASS marker and successful process completion remain non-equivalent evidence. A plausible resource-lifecycle explanation is not promoted to root cause without a causal discriminator.

## EVIDENCE LIMIT

This is bounded loopback/Linux/Dart evidence only. It does not establish WAN behavior, TCP reset/half-close semantics generally, TLS, mobile lifecycle/network transitions, browser networking, application ACK/durable completion, or product protocol correctness. The A/B matrix is diagnostic evidence; even a clean isolated case does not prove absence of resource leaks in other compositions.

## RELATED DOMAIN CHECK

- **Foundations:** F006 transport framing/termination plus F001/F004/F005 Dart execution evidence checked.
- **Architecture:** transport semantic completion and process/resource lifecycle remain separate observable contracts for callers/automation.
- **Mobile:** `dart:io` loopback evidence is not browser/PWA or Android/iOS lifecycle evidence.
- **Data:** transport termination remains below application durable completion/ACK semantics.
- **Quality:** the failed alternative is valuable falsification evidence; preserve per-case process exit as an independent oracle.
- **Systems:** the independent CI deadline remains valid containment; semantic PASS before timeout does not make the executable green.
- **Design Studio / Web Manager / Marketing Manager:** considered; not materially relevant to this process-liveness diagnosis.
- **Product:** no MintTap/LogMate implementation behavior is claimed or modified.

## HANDOFFS

- **Quality:** classify both combined runs as semantic-oracle PASS + executable-process-liveness FAIL; the one-shot listener hypothesis is now falsified, not merely unverified.
- **Systems:** retain outer deadlines and per-case process completion as release/harness evidence separate from internal assertions.
- **Mobile/Data:** consume only the bounded transport semantic result; no platform/product/durability transfer is implied.

## OPEN / VALIDATION

- Recover terminal per-job results/logs for run `35486660067`.
- Use the first hanging isolated case, if any, to form the next causal hypothesis; do not name root cause from code inspection alone.
- If all isolated cases exit, construct the smallest composition that reproduces the combined hang before changing cleanup semantics.
- No Foundations PASS from this block.
