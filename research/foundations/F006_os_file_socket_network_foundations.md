# F006 — OS, File, Socket & Network Foundations

Status: **IN STUDY — first integrated Foundation block complete**  
Evidence date: 2026-09-17

## Problem / scope
D006 already models retry, acknowledgement loss, reordering and conflicts, but those logical models need a transport foundation. This block establishes the boundary between application messages and byte-stream I/O before advancing to real partition/timeout behavior.

## SOURCE
- IETF RFC 9293 (TCP, STD 7, August 2022): TCP is the Internet transport-layer protocol specified as a reliable ordered byte-stream service; application record/message semantics are not supplied by TCP.
- Python socket documentation / Socket Programming HOWTO: `send` and `recv` operate on network buffers and may handle fewer bytes than requested; applications must continue until their message is complete. `recv()` returning zero bytes indicates peer closure. `sendall()` retries sending until all bytes are sent or an error occurs, but on error does not report how much was successfully sent.
- POSIX `read()` semantics support short-count reasoning at the OS I/O boundary; a requested byte count is not a universal promise that that count will be returned.

## SYNTHESIS — boundary model
`application operation/message → framing/serialization → socket API → transport byte stream → peer socket → peer buffering/framing → application processing → application acknowledgement`

These are distinct claims:
- bytes accepted by local `send`/`sendall` ≠ peer application processed the operation;
- one `send` ≠ one peer `recv`;
- one `recv` ≠ one complete application message;
- transport ordering ≠ application-level exactly-once processing;
- connection state ≠ durable application state.

Application protocols therefore need an explicit framing rule when message boundaries matter: fixed size, delimiter with escaping rules, length prefix, self-describing parse boundary, connection close, or another protocol-defined mechanism.

## VALIDATION — bounded executable framing failure
Fixture: `research/foundations/fixtures/F006_stream_framing_boundary.py`

### Test Evidence Contract
- **CLAIM:** stream reads must not be treated as application-message completion.
- **SPEC/PROPERTY:** a frame consists of a two-byte big-endian length followed by exactly that many payload bytes.
- **TARGET:** local Unix `SOCK_STREAM` socket pair through Python's socket API.
- **INPUT/STATE:** wire bytes `00 05 HELLO` are sent; receiver deliberately requests one byte first.
- **ORACLE:** naive parser cannot have a complete two-byte header after one-byte receive; buffered parser must reconstruct length 5 and body `HELLO`.
- **ENVIRONMENT:** Python 3.13.5; Linux 6.18.44 x86_64; glibc 2.41.
- **OBSERVATION:** first receive `00`; `naive_header_complete=False`; buffered alternative decoded length 5 and body `HELLO`.
- **VERDICT:** PASS for bounded framing alternative; naive one-read assumption falsified.
- **FAILURE MODEL:** incorrect application assumption that a stream read equals a protocol frame/header.
- **REPRODUCTION:** run the fixture with Python 3.
- **EVIDENCE LIMIT:** local socket pair only; no TCP packet loss/retransmission, network partition, MTU behavior, TLS, mobile radio, Dart `Socket`, Flutter, multi-device, or production evidence.

## DEBUG / ROOT CAUSE
The observed failure is not evidence that the transport lost a byte. The application requested only one byte and then attempted to interpret receive-call completion as protocol-frame completion. The violated boundary is application framing/accumulation, not transport reliability.

## ALTERNATIVE
Retain received bytes in a buffer, parse the frame header only when enough bytes exist, then continue receiving until the declared body length is satisfied. EOF before completion is a protocol/connection failure rather than a valid partial message.

## ENGINEERING JUDGMENT
D006 retry logic must be placed above framing and connection semantics. A local send success is too early an event to serve as a business-operation acknowledgement. If a connection fails after some bytes are accepted, the caller may not know whether the peer received, parsed, applied or durably committed the operation; operation identity/idempotency remains an application/data concern.

## TRANSFER VALIDATION
`yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`.

F006 is a **TRANSFER CANDIDATE** for any future LogMate device/server synchronization transport. Repository search did not establish that this ref currently implements such a socket protocol, so no product defect or transport decision is inferred. Default branch is not assumed to be production.

## RELATED DOMAIN CHECK
- **Foundations:** F001 process/I/O boundary, F004 concurrency and F005 timeout/cancellation checked; direct Dart/Flutter execution remains OPEN.
- **Architecture:** framing, timeout and acknowledgement semantics are interface contracts when consumer-visible.
- **Mobile:** mobile connectivity/background/process death can interrupt transport independently of logical operation state; exact platform validation remains OPEN.
- **Data:** D006 operation identity, delivery/apply/ack/conflict distinctions directly depend on this transport boundary.
- **Quality:** Q003 schedule matrices and Q005 fault isolation should distinguish framing/connection failure from application processing failure.
- **Systems:** TLS/authentication, resource exhaustion, socket limits and network performance are outside this first block and remain owned by Systems where appropriate.
- **Design Studio / Web Manager / Marketing Manager:** cross-repository search found no directly applicable current canonical evidence for this bounded socket-framing mechanism.
- **Product:** LogMate exact ref checked as above; MintTap repository identity remains unresolved.

## OPEN / VALIDATION
- direct Dart `Socket` / Flutter runtime execution;
- TCP loopback and then real-network partial I/O/connection-reset experiments;
- timeout vs connection terminal state;
- half-close/reset semantics;
- DNS/IP/routing/ports and UDP/message-oriented contrast;
- partition/reconnect and application acknowledgement ambiguity;
- mobile platform connectivity/background transfer;
- TLS/security and resource/performance boundaries.

## CHANGE WATCH
Runtime socket APIs and mobile networking/background restrictions are version/platform-sensitive. Recheck exact Dart/Flutter/Android/iOS contracts before product implementation advice.

## HANDOFFS
- **Data / D006:** treat transport write, peer receive, parse, apply, durable commit and application ACK as separate states; do not use local send success as operation completion.
- **Quality / Q005-Q006:** future fault injection should isolate truncated frame, EOF, timeout, reset, late ACK and duplicate retry as distinct failure classes.
- **Mobile:** future LogMate sync validation needs exact platform/build/network prestate and process/background behavior before transfer is accepted.
