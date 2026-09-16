# D006 — Replication, Synchronization, Consistency, Idempotency & Conflicts

Status: **IN STUDY — SOURCE/MODEL + FIRST EXECUTABLE FAILURE/ALTERNATIVE**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem
Once data has more than one writer or a request can be retried after an ambiguous failure, local correctness is insufficient. Delivery, application, acknowledgement, replication, conflict resolution and visible state are distinct events.

Working model:

`operation identity → delivery attempt(s) → apply/deduplicate → acknowledgement → replicated observations → conflict detection/resolution → converged/accepted state`

## SOURCE
Primary sources checked 2026-09-17:
- IETF RFC 9110 §9.2.2 defines an idempotent method by the intended server effect of multiple identical requests being the same as one request. It explains why an idempotent request can be retried after a communication failure where the client cannot know whether the first request took effect, and warns against automatically retrying non-idempotent requests without stronger knowledge.
- Current Firebase Firestore offline documentation states that local changes synchronize after reconnect and documents last-write-wins for multiple changes to the same document.
- Current Firestore transaction documentation states that transactions may rerun when concurrently read documents change, never partially apply writes, and transaction functions may execute more than once; transaction callbacks therefore must not be treated as once-only side-effect boundaries.
- Current Firestore contention/isolation documentation states transaction isolation/serialization semantics separately from nontransactional offline conflict behavior.

## SYNTHESIS
### Retry is not idempotency
A retry policy answers **whether/when another attempt is sent**. Idempotency answers **whether repeated attempts of one logical operation preserve its intended effect**. Transport delivery count and logical mutation count are therefore different quantities.

An ambiguous failure is especially important: the server may have applied a mutation while the acknowledgement/response is lost. Retrying an increment-like operation without stable operation identity can apply the user's intent twice.

### Delivery is not acknowledgement
`sent`, `received`, `applied`, `durably committed`, `acknowledged`, and `observed by another replica` are separate states. A timeout cannot by itself prove non-application.

### Replication is not a conflict policy
Replicating values says how copies move; it does not determine what to do with concurrent semantic changes. A whole-record last-write-wins policy can converge while losing a valid concurrent field update. Convergence and preservation of user intent are separate properties.

### Conflict resolution requires domain semantics
A fieldwise merge is not universally correct either. It is safe only when the fields/operations are independently composable under the domain invariant. Counters, sets, ordered logs, mutually dependent fields and destructive edits require different policies.

## EXECUTABLE VALIDATION 1
Fixture: `research/data/fixtures/D006_retry_conflict_semantics.py`

Environment executed: Python 3.13.5 / Linux container, 2026-09-17.

### CLAIM A — ambiguous retry can duplicate a non-idempotent effect
A modeled server applies `+10`; the response is lost; the client retries the same logical intent. Without operation identity the total becomes 20. With stable `operation_id=op-1` and server-side deduplication, the second delivery returns the prior result and total remains 10.

Observed:
```text
unsafe_retry_total=20 keyed_retry_total=10
```

**ROOT CAUSE:** the unsafe server identifies attempts, not logical operations. The client cannot distinguish `not applied` from `applied but acknowledgement lost` after the modeled failure.

**ALTERNATIVE:** stable operation identity plus deduplication for this bounded mutation contract.

### CLAIM B — whole-record LWW can converge while losing concurrent intent
Base record: `{night:10, ifr:20}`. Writer A changes night to 15. Writer B concurrently changes IFR to 25 from the same base. Whole-record LWW chooses B and yields `{night:10, ifr:25}`, discarding A's independent change. A bounded fieldwise comparison yields `{night:15, ifr:25}`.

Observed:
```text
lww={'night': 10, 'ifr': 25, 'ts': 3} independent_field_merge={'night': 15, 'ifr': 25}
VERDICT=PASS
```

**ROOT CAUSE:** record-level replacement treats the entire stale snapshot as the conflict unit, so B's unchanged `night=10` overwrites A's newer semantic update.

**EVIDENCE LIMIT:** the fieldwise alternative is only valid for this deliberately independent two-field model. It is not a universal merge algorithm.

## ENGINEERING JUDGMENT
For offline-first/multi-device applications, define at minimum:
- stable logical operation identity where ambiguous retry can duplicate effects;
- acknowledgement semantics distinct from local visibility;
- conflict unit and detection rule;
- resolution policy tied to domain invariants;
- explicit treatment of duplicate, reordered, stale and concurrent operations;
- recovery behavior when conflict resolution cannot be automatic.

Do not promise exactly-once behavior merely because a client retries with a key. End-to-end exactly-once requires all relevant state/effect boundaries to participate in the protocol; this fixture proves only deduplication of one modeled server effect.

## FIRESTORE TRANSFER BOUNDARY
**SOURCE:** Firestore documents offline synchronization and last-write-wins for multiple changes to the same document; transaction functions can be retried under contention and should not directly mutate application state.

**SYNTHESIS:** SDK retry or offline synchronization semantics do not remove the need for application-level domain conflict semantics when concurrent edits can carry independent user intent.

**CHANGE WATCH:** exact Firebase/FlutterFire behavior and available primitives are version/platform sensitive; recheck exact product SDK versions before implementation advice.

## PRODUCT TRANSFER
Retained exact-ref evidence: `yhappcom/logmate → main b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → evidence date 2026-09-17`. Prior audit found Sync not implemented at that ref, so this remains a **TRANSFER CANDIDATE**, not a defect finding or technology decision.

For future LogMate multi-device sync, FlightRecord identity, duplicate import/sync identity, concurrent edit semantics, deletion/tombstone behavior, and local-vs-remote acknowledgement must be specified before choosing LWW or another merge policy. MintTap repository identity remains unresolved; no implementation claim is made.

## RELATED DOMAIN CHECK
- **Foundations:** F004/F005/F006 concurrency/async/network foundations will deepen ordering and failure mechanics; F001 Dart/Flutter execution remains OPEN.
- **Architecture:** A002 state ownership and A003 contracts apply to operation identity, conflict units and compatibility semantics.
- **Mobile:** background/process death/connectivity can interrupt delivery and acknowledgement; real platform validation remains required.
- **Data:** D004 pending-vs-confirmed ownership is reused; D006 extends it to multiple attempts/writers.
- **Quality:** Q003 should test schedule/order sensitivity; fault injection must include lost acknowledgement, duplicate delivery, reorder and concurrent edits.
- **Systems:** authentication/authorization of operation identity and replay protection are distinct from idempotency correctness.
- **Design Studio:** future conflict/sync UI must not label locally visible or merely delivered data as globally synchronized without the corresponding engineering state.
- **Web Manager:** not materially relevant to this bounded native/offline-first mechanism block.
- **Marketing Manager:** not materially relevant.

## HANDOFFS
- **Data → Quality:** use lost-ACK/duplicate/reorder/concurrent-writer cases as Q003/Q006 reliability inputs.
- **Data → Architecture:** operation identity and conflict unit are semantic contracts, not transport implementation details.
- **Data → Mobile:** reproduce retry/pending/process-death behavior on the eventual exact LogMate sync stack.
- **Data → Design Studio:** conflict/pending/synced labels need acknowledgement/conflict-state contracts before UX finalization.

## OPEN / VALIDATION
1. Add reordered delivery and stale-delete/tombstone failure cases.
2. Compare operation-based vs state-based synchronization under explicit invariants.
3. Validate real network/backend retry behavior when an exact product stack exists.
4. Add multi-process/device or emulator evidence; current fixture is deterministic single-process model evidence only.
5. Study consistency/partition vocabulary without implying CAP slogans beyond their formal scope.

## Current judgment
D006 now has a coherent first Foundation block with authoritative source grounding, two executable failure mechanisms, root-cause separation and bounded alternatives. It is **not PASS** and does not establish a production synchronization design.
