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
| Quality | Stage 1 IN STUDY — Q001 substantial + Q002 first + Q003 two integrated blocks |
| Systems | Stage 1 IN STUDY — S001 two executable trust-boundary blocks complete |

No specialist has passed Foundation.

## Meaningful new evidence

### D006 — reordered stale update vs delete/tombstone
Canonical: `research/data/D006_replication_sync_consistency_idempotency_conflicts.md`  
Fixture: `research/data/fixtures/D006_reorder_tombstone_semantics.py`

Q003's explicit schedule-enumeration method was transferred into a bounded Data-owned delete/reorder model.
- event alphabet: newer `delete_v3` and delayed `stale_update_v2`;
- independent property: terminal state must remain deleted because version 3 is newer than version 2;
- naive physical-delete/state-replacement model failed 1/2 delivery orders: `delete → stale update` resurrected the record;
- bounded versioned-tombstone comparison failed 0/2 orders;
- root cause: physical absence retained no ordering history capable of rejecting the delayed stale update;
- the result does not establish scalar-version sufficiency, wall-clock timestamp safety, tombstone GC safety, Firestore internals, real network/multi-device behavior, or a production sync design.

Current Firebase documentation was rechecked: offline local changes synchronize on reconnect and multiple changes to the same document use last-write-wins; current Firestore API documentation separately exposes pending-write acknowledgement and states termination does not cancel persisted pending writes. These sources support keeping local visibility, pending work, acknowledgement and conflict policy distinct, but do not prove the bounded tombstone implementation.

## Retained evidence
- **F001:** source/runtime/process model + OS process/I/O fixture; direct Dart JIT/AOT and Flutter runtime execution remain OPEN. Environment rechecked 2026-09-17: neither executable is available.
- **F004:** lock-order/circular-wait plus condition predicate/signaling.
- **F005:** timeout-vs-underlying-work/cancellation plus ordering/error/cleanup.
- **Q003:** shared-memory schedule failure plus explicit 24-order async event matrix.
- **D001-D006, Q001-Q003, A001-A003, M001, S001:** prior evidence retained.

## Product transfer
LogMate exact ref rechecked: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → Dart SDK ^3.10.7 → evidence date 2026-09-17`. Default branch is not assumed to equal production. D006 remains a **TRANSFER CANDIDATE**; no LogMate defect or sync-technology decision is inferred. MintTap repository identity remains unresolved; no MintTap implementation claim is made.

## Cross-track handoffs
- **Foundations:** direct Dart runtime remains OPEN; F006 networking would deepen D006 transport/partition mechanisms.
- **Architecture:** delete/recreate policy, conflict unit, operation identity and tombstone lifecycle are semantic contracts.
- **Mobile:** exact lifecycle/connectivity/process-death transfer remains required on the eventual sync stack.
- **Data:** D006 now has two integrated blocks; next depth should target operation-vs-state sync or concurrent delete/recreate/tombstone-GC only when it outranks broader Foundation gaps.
- **Quality:** Q003 event-order method successfully transferred into Data; future Q006 should include deletion/GC failure schedules.
- **Systems:** correctness tombstones/operation IDs are not automatically security/replay controls; retention also has privacy/storage implications.
- **Design Studio:** repository search found no directly applicable current sync/conflict/offline evidence; future UI handoff remains semantic-state mapping.
- **Web Manager:** no directly applicable evidence found; browser/service-worker transfer remains separate.
- **Marketing Manager:** not materially relevant.

## Current Balance Loop
F001 direct Dart/Flutter execution remains toolchain-blocked and was not simulated; environment rechecked 2026-09-17.

D006 has now completed the high-value Q003→Data transfer requested by the previous global queue. Strong next candidates:
1. `Q005` debugging/fault-isolation/observability foundations — Quality Stage 1 still lacks a dedicated symptom→reproduction→isolation→causal-test block and this method has broad cross-track leverage;
2. `F006` OS/file/socket/network foundations — prerequisite for moving D006 from logical scheduling models toward transport/partition behavior;
3. D006 operation-based vs state-based sync or concurrent delete/recreate/tombstone-GC if risk evidence makes deeper Data work dominant;
4. return immediately to direct F001/F005 Dart/Flutter execution when a trustworthy SDK environment exists.

Selection remains prerequisite/risk/evidence driven rather than rotational.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
