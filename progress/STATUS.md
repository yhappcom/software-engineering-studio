# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-17  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN; F004 two synchronization blocks + F005 two async blocks complete |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 IN STUDY — M001 first integrated Foundation block complete |
| Data | Stage 1 IN STUDY — D001 substantial + D002 two + D003 two + D004 first + D005 two + D006 two blocks |
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 two + Q005 first integrated block |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### Q005 — debugging, fault isolation and observability foundations
Canonical: `research/quality/Q005_debugging_fault_isolation_observability.md`  
Fixture: `research/quality/fixtures/Q005_fault_isolation_observability.py`

The previously untouched Quality Foundation gap around symptom→isolation→causal testing now has a bounded executable block.
- two independent injected stage defects produced the identical external result `11` for the same input;
- final-output-only evidence therefore could not discriminate which stage was causal;
- correlated boundary observations plus an independent normalize invariant isolated the first violated contract;
- normalize-defect trace: `decoded=5 → normalized=11 → output=11`;
- aggregate-defect trace: `decoded=5 → normalized=10 → output=11`;
- disabling injected defects restored expected output `10` in the bounded intervention;
- OpenTelemetry source evidence supports trace/log/resource correlation, but correlation is explicitly not promoted to root-cause proof.

The debugging model is now:
`symptom → reproduction → isolation → causal hypothesis → discriminating observation/intervention → falsification/confirmation → root cause → fix → regression evidence`.

Evidence limit: Python 3.13.5 deterministic single-process model; no distributed clocks, telemetry sampling/drop, production observability, crash dump, Flutter DevTools/native symbolication or automated causal-inference claim.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **F004:** lock-order/circular-wait plus condition predicate/signaling.
- **F005:** timeout-vs-underlying-work/cancellation plus ordering/error/cleanup.
- **Q003:** shared-memory schedule failure plus explicit 24-order async event matrix.
- **D006:** retry/idempotency/conflict plus reordered stale-update/delete/tombstone model.
- **D001-D005, Q001-Q002, A001-A003, M001, S001:** prior evidence retained.

## Cross-track handoffs
- **Foundations:** F006 networking is now the strongest untouched prerequisite for taking D006 from logical schedules toward transport/partition behavior.
- **Architecture:** A003 contracts/invariants are useful fault-isolation boundaries; observability must not redefine semantic contracts.
- **Mobile:** M002 lifecycle/process-death diagnosis should capture exact prestate and distinguish missing callback, failed durable write and failed recovery.
- **Data:** D006 should record logical operation identity plus delivery/apply/ack/conflict state and first violated invariant for future sync debugging.
- **Quality:** Q005 has first bounded block; crash/exception/distributed observability and regression governance remain OPEN.
- **Systems:** telemetry must bind to artifact/version/environment identity; diagnostic fields require privacy/security review.
- **Design Studio / Web Manager:** cross-repository search found no directly applicable current debugging/telemetry evidence.
- **Marketing Manager:** not materially relevant.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

Q005 removed a broad Quality prerequisite gap and adds a reusable debugging method for later persistence, sync, lifecycle and release failures. Strong next candidates:
1. `F006` OS/file/socket/network foundations — highest prerequisite leverage for D006 transport, timeout, partial delivery and partition reasoning;
2. `Q006` fault injection, recovery verification and regression governance — strongest Quality continuation if recovery risk outranks transport foundations;
3. `M002` Android/iOS process lifecycle/background execution when trustworthy platform evidence can materially exceed M001's current source/model level;
4. return immediately to direct F001/F005 Dart/Flutter execution when a trustworthy SDK environment exists.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
