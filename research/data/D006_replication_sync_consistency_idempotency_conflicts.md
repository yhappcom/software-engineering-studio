# D006 — Replication, Synchronization, Consistency, Idempotency & Conflicts

Status: **IN STUDY — SOURCE/MODEL + TWO EXECUTABLE FAILURE/ALTERNATIVE BLOCKS**  
Date: 2026-09-17  
Lead: Data, Persistence & Distributed Systems

## Problem
Once data has more than one writer or a request can be retried after an ambiguous failure, local correctness is insufficient. Delivery, application, acknowledgement, replication, conflict resolution and visible state are distinct events.

Working model:

`operation identity → delivery attempt(s) → apply/deduplicate → acknowledgement → replicated observations → conflict detection/resolution → converged/accepted state`

Deletion adds another semantic state: absence at one replica is not enough to communicate that a prior value must stay absent under delayed/reordered delivery.

## SOURCE
Primary sources checked 2026-09-17:
- IETF RFC 9110 §9.2.2 defines an idempotent method by the intended server effect of multiple identical requests being the same as one request. It explains why an idempotent request can be retried after a communication failure where the client cannot know whether the first request took effect, and warns against automatically retrying non-idempotent requests without stronger knowledge.
- Current Firebase Firestore offline documentation states that local changes synchronize after reconnect and documents last-write-wins for multiple changes to the same document.
- Current Firestore transaction documentation states that transactions may rerun when concurrently read documents change, never partially apply writes, and transaction functions may execute more than once; transaction callbacks therefore must not be treated as once-only side-effect boundaries.
- Current Firestore API documentation distinguishes pending writes from backend acknowledgement; terminating a client does not cancel pending writes and persisted pending writes resume on restart.

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

### Delete is a state transition, not merely missing data
If synchronization physically removes a record and retains no ordering information for the deletion, a delayed stale update can recreate it. A tombstone is one possible representation of deletion history; it is useful only with an ordering/causality rule and a retention/garbage-collection policy that prevents forgotten deletes from being defeated by still-deliverable stale operations.

## EXECUTABLE VALIDATION 1 — ambiguous retry and concurrent update conflict
Fixture: `research/data/fixtures/D006_retry_conflict_semantics.py`

Environment executed: Python 3.13.5 / Linux container, 2026-09-17.

### CLAIM A — ambiguous retry can duplicate a non-idempotent effect
A modeled server applies `+10`; the response is lost; the client retries the same logical intent. Without operation identity the total becomes 20. With stable `operation_id=op-1` and server-side deduplication, the second delivery returns the prior result and total remains 10.

Observed: `unsafe_retry_total=20 keyed_retry_total=10`.

**ROOT CAUSE:** the unsafe server identifies attempts, not logical operations. The client cannot distinguish `not applied` from `applied but acknowledgement lost` after the modeled failure.

**ALTERNATIVE:** stable operation identity plus deduplication for this bounded mutation contract.

### CLAIM B — whole-record LWW can converge while losing concurrent intent
Base record: `{night:10, ifr:20}`. Writer A changes night to 15. Writer B concurrently changes IFR to 25 from the same base. Whole-record LWW chooses B and yields `{night:10, ifr:25}`, discarding A's independent change. A bounded fieldwise comparison yields `{night:15, ifr:25}`.

**ROOT CAUSE:** record-level replacement treats the entire stale snapshot as the conflict unit, so B's unchanged `night=10` overwrites A's newer semantic update.

**EVIDENCE LIMIT:** the fieldwise alternative is only valid for this deliberately independent two-field model. It is not a universal merge algorithm.

## EXECUTABLE VALIDATION 2 — reordered stale update vs delete/tombstone
Fixture: `research/data/fixtures/D006_reorder_tombstone_semantics.py`

Environment executed: Python 3.13.5 / Linux 6.18.44 x86_64, 2026-09-17. Deterministic enumeration of both permutations of `delete_v3` and `stale_update_v2`; no random seed.

**CLAIM:** physical absence alone is insufficient to preserve a delete when an older update can still arrive after it.

**SPEC/PROPERTY / ORACLE:** version 3 deletion is newer than version 2 update, therefore accepted terminal state must remain deleted for both delivery orders.

Observed:
```text
order=('delete_v3', 'stale_update_v2') naive={'exists': True, 'value': 'v2-from-stale-base'} guarded={'exists': False, 'value': None, 'version': 3, 'tombstone': True}
order=('stale_update_v2', 'delete_v3') naive={'exists': False, 'value': None} guarded={'exists': False, 'value': None, 'version': 3, 'tombstone': True}
naive_failures=1/2
tombstone_failures=0/2
VERDICT=PASS
```

**FAILURE / ROOT CAUSE:** naive state replacement has no durable representation that a newer deletion occurred. When the stale update is delivered after physical deletion, it is indistinguishable from a legitimate create/update and resurrects the record.

**ALTERNATIVE:** the bounded comparison retains a versioned tombstone and accepts only strictly newer versions. It preserves deletion in both enumerated orders.

**CONTRADICTION:** the universal assumption `delete + eventual delivery implies eventual absence` is false for a protocol that physically deletes state while delayed stale updates remain admissible.

**EVIDENCE LIMIT:** this does not prove that scalar versions are sufficient for multi-writer causality, that wall-clock timestamps are safe ordering tokens, or that tombstones should be retained forever. It does not model tombstone GC, clock skew, concurrent delete/recreate, identity reuse, partitions, actual Firestore internals, network transport, process death, or multi-device runtime.

## ENGINEERING JUDGMENT
For offline-first/multi-device applications, define at minimum:
- stable logical operation identity where ambiguous retry can duplicate effects;
- acknowledgement semantics distinct from local visibility;
- conflict unit and detection rule;
- resolution policy tied to domain invariants;
- explicit treatment of duplicate, reordered, stale and concurrent operations;
- delete semantics, delete ordering metadata, and tombstone/retention behavior when stale delivery is possible;
- recovery behavior when conflict resolution cannot be automatic.

Do not promise exactly-once behavior merely because a client retries with a key. End-to-end exactly-once requires all relevant state/effect boundaries to participate in the protocol; these fixtures prove only bounded model properties.

## FIRESTORE TRANSFER BOUNDARY
**SOURCE:** Firestore documents offline synchronization and last-write-wins for multiple changes to the same document; current API docs separately expose pending-write acknowledgement and state that termination does not cancel persisted pending writes.

**SYNTHESIS:** offline synchronization does not remove application-level questions about domain conflict units, delete/recreate semantics, or whether a user-visible local state is backend-acknowledged.

**CHANGE WATCH:** exact Firebase/FlutterFire behavior and available primitives are version/platform sensitive; recheck exact product SDK versions before implementation advice. This study does not claim Firestore itself implements the bounded tombstone fixture.

## PRODUCT TRANSFER
Exact-ref rechecked 2026-09-17: `yhappcom/logmate → main → b551ce434ad72b1895033e0f3617c73b026d40ea → declared version 1.0.0+1 → Dart SDK ^3.10.7`. This remains a **TRANSFER CANDIDATE**, not a production ref assertion, defect finding, or technology decision.

For future LogMate multi-device sync, FlightRecord identity, duplicate import/sync identity, concurrent edit semantics, deletion/tombstone behavior, and local-vs-remote acknowledgement must be specified before choosing LWW or another merge policy. MintTap repository identity remains unresolved; no implementation claim is made.

## RELATED DOMAIN CHECK
- **Foundations:** F004/F005 ordering/async evidence reused; F001 direct Dart/Flutter execution rechecked 2026-09-17 and remains OPEN because neither executable is available. F006 network foundations remain a future mechanism prerequisite.
- **Architecture:** A002 state ownership and A003 contracts apply to operation identity, conflict units, delete semantics and compatibility.
- **Mobile:** background/process death/connectivity can interrupt delivery and acknowledgement; real platform validation remains required.
- **Data:** D004 pending-vs-confirmed ownership is reused; D006 extends it to multiple attempts/writers and deletion history.
- **Quality:** Q003 explicit schedule enumeration transferred directly into the two-event reorder matrix here.
- **Systems:** authentication/authorization of operation identity and replay protection are distinct from idempotency correctness; tombstone retention also has privacy/storage implications.
- **Design Studio:** repository search found no directly applicable current `sync conflict pending offline` canonical evidence; future conflict/deletion UX must map engineering states without redefining them.
- **Web Manager:** repository search found no directly applicable evidence; browser/service-worker transfer is separate.
- **Marketing Manager:** repository search found no materially relevant evidence.
- **Product:** LogMate exact main ref and declared version rechecked; default branch is not assumed to equal production.

## HANDOFFS
- **Data → Quality:** retain event-alphabet/order-matrix method; next reliability work should include delete/recreate, tombstone GC and delayed operation cases with independent terminal-state oracles.
- **Data → Architecture:** deletion is a semantic state transition; operation identity, conflict unit, recreate policy and tombstone lifecycle are contracts, not transport details.
- **Data → Mobile:** reproduce pending/delete/reconnect/process-death behavior on the eventual exact LogMate sync stack.
- **Data → Design Studio:** conflict/pending/deleted/synced labels need acknowledgement and delete-state contracts before UX finalization.
- **Data → Systems:** evaluate retention/privacy/security and replay implications before treating correctness tombstones or operation IDs as security controls.

## OPEN / VALIDATION
1. Compare operation-based vs state-based synchronization under explicit invariants.
2. Add concurrent delete/recreate and tombstone garbage-collection safety cases.
3. Validate real network/backend retry and delete behavior when an exact product stack exists.
4. Add multi-process/device or emulator evidence; current fixtures are deterministic single-process model evidence only.
5. Study consistency/partition vocabulary without implying CAP slogans beyond their formal scope.
6. Direct Dart/Flutter execution remains OPEN until a trustworthy SDK environment exists.

## Current judgment
D006 now has two coherent Foundation blocks: retry/idempotency/concurrent-update semantics and reordered stale-update/delete semantics. It has authoritative source grounding, executable failures, root-cause separation, bounded alternatives and Q003 method transfer. It is **not PASS** and does not establish a production synchronization design.
