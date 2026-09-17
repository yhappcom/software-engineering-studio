# F006 — OS, File, Socket & Network Foundations

Status: **IN STUDY — two integrated Foundation blocks complete**  
Evidence date: 2026-09-17

## Problem / scope
D006 already models retry, acknowledgement loss, reordering and conflicts, but those logical models need a transport foundation. F006 now establishes (1) application framing over byte-stream I/O and (2) the distinction among frame completion, graceful EOF, abort/reset and application acknowledgement.

## SOURCE
- IETF RFC 9293 (TCP, STD 7, August 2022): TCP is a reliable ordered byte-stream transport; application record/message semantics are not supplied by TCP. Normal close is directional/simplex, half-close is possible, and reset aborts a connection. A remote FIN and RST are distinct terminal conditions that the local application must be informed about.
- Python socket documentation: `send` may send fewer bytes than requested; `sendall()` continues until all bytes are sent or an error occurs, but on error does not report how much was successfully sent. `recv()` returning zero bytes indicates peer closure.
- POSIX short-count semantics remain relevant at the OS I/O boundary.

## SYNTHESIS — boundary model
`application operation/message → framing/serialization → socket API → transport byte stream → peer socket → peer buffering/framing → application processing → durable commit → application acknowledgement`

Distinct claims:
- bytes accepted by local send ≠ peer application processed the operation;
- one send ≠ one peer recv;
- one recv ≠ one complete application message;
- complete application frame observed ≠ application operation applied/durably committed;
- graceful EOF ≠ reset/abort;
- connection terminal state ≠ business-operation terminal state;
- transport ordering ≠ application-level exactly-once processing.

## VALIDATION 1 — bounded executable framing failure
Fixture: `research/foundations/fixtures/F006_stream_framing_boundary.py`

- **CLAIM:** stream reads must not be treated as application-message completion.
- **SPEC/PROPERTY:** frame = two-byte big-endian length + exactly that many payload bytes.
- **TARGET:** local Unix `SOCK_STREAM` socket pair through Python.
- **INPUT:** `00 05 HELLO`; receiver deliberately requests one byte first.
- **ORACLE:** naive parser cannot have a complete header; buffered parser must reconstruct length 5/body `HELLO`.
- **ENVIRONMENT:** Python 3.13.5; Linux 6.18.44 x86_64.
- **OBSERVATION:** first receive `00`; buffered alternative decoded `HELLO`.
- **VERDICT:** bounded alternative PASS; one-read-as-frame assumption falsified.
- **LIMIT:** local socket pair; not Dart/Flutter, packet-loss, TLS, mobile or production evidence.

## VALIDATION 2 — termination / partial-delivery ambiguity
Fixture: `research/foundations/fixtures/F006_connection_termination_ambiguity.py`

### Test Evidence Contract
- **CLAIM:** connection termination and application-frame completion are distinct observations; terminal transport errors alone cannot identify application processing state.
- **SPEC/PROPERTY:** same length-prefixed frame contract as Validation 1. A complete frame requires header length 5 plus exactly five payload bytes.
- **TARGET:** Python socket API on Linux; AF_UNIX stream for graceful truncation and loopback TCP for abortive close.
- **INPUT/STATE A:** sender transmits only `00 05 HE`, then `shutdown(SHUT_WR)`; receiver reads until EOF.
- **INPUT/STATE B:** TCP server sends complete `00 05 HELLO`, configures abortive `SO_LINGER(1,0)`, closes; client reads until reset/EOF.
- **ORACLE:** A must end with EOF while frame remains incomplete; B must demonstrate that complete application bytes can be observed before the terminal reset in this bounded environment.
- **ENVIRONMENT:** Python 3.13.5; Linux 6.18.44 x86_64; local execution 2026-09-17.
- **OBSERVATION A:** bytes `00054845`, declared length 5, body `HE`, then EOF.
- **OBSERVATION B:** bytes `000548454c4c4f`, body `HELLO`, then `ConnectionResetError`.
- **VERDICT:** PASS for the bounded distinction. EOF did not make a truncated frame valid; reset did not imply zero application bytes were received.
- **FAILURE MODEL:** application code that equates EOF with successful message completion, or equates reset with proof that the peer received/applied nothing.
- **REPRODUCTION:** run fixture with Python 3 on Linux. Abortive-close details are OS/socket-stack dependent and must not be promoted as universal sequencing.
- **EVIDENCE LIMIT:** no proof that the peer application applied/durably committed the complete frame in case B; no real network partition, packet capture, cross-OS, Dart Socket, Flutter, mobile radio, TLS, multi-device or production evidence.

## DEBUG / ROOT CAUSE
Validation 1 fails at the framing boundary: receive-call completion was mistaken for frame completion.

Validation 2 demonstrates a different class. In graceful truncation, EOF is a transport terminal observation after only part of the declared application frame arrived. The correct parser must reject/truncate rather than publish a message. In abortive close, the client observed the complete frame before reset. Therefore reset is not a valid oracle for `peer received zero bytes`; still less is it an oracle for `peer applied zero operations`.

The business-level ambiguity remains above TCP: after connection failure, a caller may know neither whether the peer parsed the frame nor whether an operation was applied/durably committed. D006 operation identity/idempotency and application ACK semantics are therefore not replaced by transport reliability.

## ALTERNATIVES / ENGINEERING JUDGMENT
- Frame explicitly and reject EOF before frame completion.
- Treat graceful EOF, reset, timeout and application rejection as distinct failure classes.
- Keep logical operation identity stable across connection retries where duplicate application matters.
- Define an application acknowledgement at the semantic boundary required by the product; do not infer it from local send success or connection close alone.
- Do not blindly retry non-idempotent operations after an ambiguous connection failure.

## TRANSFER VALIDATION
`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`.

F006 remains a **TRANSFER CANDIDATE** for future LogMate device/server synchronization. No socket protocol or defect is inferred from that ref and default branch is not assumed to be production.

## RELATED DOMAIN CHECK
- **Foundations:** F001 process/I/O, F004 concurrency and F005 timeout/cancellation checked. Direct Dart/Flutter execution remains OPEN.
- **Architecture:** framing, terminal-state and acknowledgement semantics become interface contracts when consumer-visible.
- **Mobile:** process/background/connectivity interruption may produce transport ambiguity; exact Android/iOS/Flutter execution remains OPEN.
- **Data:** D006 operation identity, delivery/apply/durable-commit/ACK distinctions directly depend on this boundary.
- **Quality:** Q005/Q006 should preserve terminal condition, bytes/frame state, logical operation ID and acknowledgement state separately during fault injection/debugging.
- **Systems:** TLS/authentication, socket/resource exhaustion and network performance remain separate Systems concerns.
- **Design Studio / Web Manager / Marketing Manager:** no current canonical evidence materially changes this low-level transport conclusion.
- **Product:** LogMate exact ref retained above; MintTap repository identity remains unresolved.

## OPEN / VALIDATION
- direct Dart `Socket` / Flutter runtime execution;
- timeout where local caller stops waiting while connection/peer work may continue;
- real TCP partition/reconnect and packet-level observation;
- cross-OS reset/half-close behavior;
- DNS/IP/routing/ports and UDP/message-oriented contrast;
- application ACK + retry integration with D006;
- mobile platform connectivity/background transfer;
- TLS/security and resource/performance boundaries.

## CHANGE WATCH
Runtime socket APIs and mobile networking/background restrictions are version/platform-sensitive. Recheck exact Dart/Flutter/Android/iOS contracts before product implementation advice.

## HANDOFFS
- **Data / D006:** ambiguous transport termination does not establish whether an operation was applied. Keep logical operation identity and explicit application ACK/durable state above connection retries.
- **Quality / Q005-Q006:** inject EOF-before-frame, reset-after-complete-frame, timeout and late ACK as separate failures; preserve first-failure trace and semantic state.
- **Mobile:** future LogMate sync validation needs exact platform/build/network prestate and process/background behavior before transfer is accepted.
