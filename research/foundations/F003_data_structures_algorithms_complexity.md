# F003 — Data Structures, Algorithms & Complexity

Status: **IN STUDY — CPython evidence + direct Dart transfer harness executing**  
Evidence date: 2026-09-20

## Problem / scope
Software can preserve the same functional result while having materially different growth costs because representation determines which operations are cheap. The professional boundary is between abstract data-structure semantics, concrete representation, algorithmic growth, and measured runtime cost.

## SOURCE
Prior CPython evidence remains valid for its bounded runtime only; it is not transferred to Dart by analogy.

Current authoritative Dart API evidence checked 2026-09-20:
- `dart:collection ListQueue` documents a cyclic-buffer representation with constant-time peek/remove operations and amortized constant-time add operations: https://api.dart.dev/dart-collection/ListQueue-class.html
- `ListBase.removeAt` specifies that removal moves all later objects down one position; its implementation closes the resulting gap: https://api.dart.dev/dart-collection/ListBase/removeAt.html
- `ListQueue.removeFirst` advances the queue head in its cyclic table: https://api.dart.dev/dart-collection/ListQueue/removeFirst.html
- `List` documents the default growable list as an internal buffer and guarantees amortized constant time for a sequence of adds, while warning other implementations may differ: https://api.dart.dev/dart-core/List-class.html

**SOURCE boundary:** the Dart complexity statement used here is specifically the documented `ListQueue` contract. The fixture does not infer a universal complexity contract for every `List` implementation from elapsed time.

## SYNTHESIS — semantic contract vs cost model
A FIFO contract does not prescribe representation. Both a growable `List` repeatedly using `removeAt(0)` and a `ListQueue` using `removeFirst()` can return the same sequence while exercising materially different representation mechanics.

Useful separation:

`abstract operation/invariant → representation → primitive-operation cost → workload composition → measured resource behavior`

Complexity describes growth, not a portable elapsed-time promise. A benchmark can be consistent with a cost model but cannot by itself prove an asymptotic class.

## VALIDATION — retained CPython comparison
Fixture: `research/foundations/fixtures/F003_queue_structure_complexity.py`.

Recorded environment: CPython 3.13.5 / Linux 6.18.44 x86_64. Both list-front removal and deque-front removal satisfied the independent checksum `n(n-1)/2` at n=5,000/10,000/20,000/40,000, while measured timings diverged materially. Exact timing ratios remain observations, not portable guarantees.

## TRANSFER VALIDATION — direct Dart harness
Fixture: `research/foundations/fixtures/F003_dart_queue_structure.dart`  
Workflow: `.github/workflows/f003-dart-structures-complexity-validation.yml`  
Requested runtime: Dart 3.13.3 / GitHub-hosted Ubuntu, with a 3-minute job bound and 1-minute fixture-step bound.  
Exact fixture head: `68d5b64c12f8a201a64e8c8332fae73c498242db`  
Workflow run: `35458320697`; job `105937470606`.

### Claim / property / oracle
- **CLAIM:** the semantic FIFO result can be preserved across two Dart representations while the source-defined primitive mechanics differ.
- **INPUT:** n = 5,000, 10,000, 20,000, 40,000 with values `0..n-1`.
- **ORACLE:** both implementations must equal independently derived checksum `n(n-1)/2`; a small explicit front-removal case must produce identical remaining FIFO sequence `1,2,3`.
- **OBSERVATION:** run is currently executing; no PASS/FAIL is recorded until the fixture step reaches a terminal verdict.
- **TIMING:** Stopwatch measurements are emitted as diagnostics only. There is deliberately no timing-ratio PASS threshold because shared CI timing is not an independent complexity oracle.

This design avoids the invalid shortcut `one benchmark ⇒ complexity proof`. If the fixture succeeds, it transfer-validates Dart semantic equivalence and executable use of the two structures while complexity remains grounded in the authoritative operation contracts. If it fails, preserve the failure before changing the oracle.

## FAILURE / ROOT CAUSE MODEL
Failure class: selecting a representation because it satisfies the abstract API while ignoring the dominant workload operation. Repeated front removal from an indexed growable list can require later elements to change positions; `ListQueue` is explicitly designed as a cyclic queue with constant-time remove operations. The engineering defect is representation/workload mismatch, not a FIFO semantic violation.

Rejected shortcuts:
- `same output ⇒ same engineering behavior`;
- `container choice is only an implementation detail` when resource constraints matter;
- `O(1) ⇒ instant/fast`;
- `O(n) ⇒ unacceptable` without workload/resource context;
- `one benchmark ⇒ complexity proof`.

## ALTERNATIVE / ENGINEERING JUDGMENT
For Dart FIFO workloads dominated by end operations, `ListQueue` is the source-supported queue representation. This is not a universal ranking: representation choice follows invariants and operation mix. At product scale the cost model should include time, space, mutation/copy cost, locality/serialization constraints, persistence/index maintenance, and recovery effects where relevant.

## OPEN / VALIDATION / CHANGE WATCH
- **VALIDATION:** recover terminal result for run `35458320697`; do not claim direct Dart PASS while it is nonterminal.
- **OPEN:** memory/space measurement and allocator/cache effects.
- **OPEN:** broader search/index/hash behavior and adversarial equality/hash distributions.
- **OPEN:** Flutter frame-budget/UI-jank transfer and product-runtime resource budgets.
- **OPEN:** persistent database/index cost transfer.
- **CHANGE WATCH:** Dart collection implementation/docs are version-sensitive; preserve SDK/API evidence date and exact execution identity.

## RELATED DOMAIN CHECK
- **Foundations:** F001 direct Dart execution is now available; F002 direct alias/resource evidence checked. This block uses the same hosted-Dart evidence discipline without transferring CPython costs.
- **Architecture:** representation may be hidden, but resource behavior can become contractual under an SLO/budget.
- **Mobile:** operation growth can consume frame/startup/background budgets; direct Flutter/product performance transfer remains OPEN.
- **Data:** D002 indexing and D004 cache structures depend on workload-sensitive cost models; this note supplies the prerequisite model, not a database conclusion.
- **Quality:** semantic oracle is independent of timing; timing is diagnostic only. CI bounds prevent an accidental workload from becoming an unbounded validation run.
- **Systems:** S003 owns profiling/resource-budget evidence; F003 owns structure/algorithm growth reasoning.
- **Design Studio / Web Manager / Marketing Manager:** considered; no current canonical decision changes this bounded in-memory mechanism.
- **Product source/ref:** no product behavior claim is made in this block, so no product repository audit is required.

## HANDOFFS
### Foundations → Data
Use `abstract operation → representation → primitive cost → workload composition` for indexes, caches, import duplicate detection and sync queues. Do not transfer container constants across runtimes.

### Foundations → Systems / Quality
Keep semantic correctness oracles separate from timing observations. Production profiling must bind workload/environment; CI benchmark ratios are not complexity proof.

### Foundations → Mobile
Use this model when selecting product-relevant queues, but require Flutter/device/browser execution before asserting frame or lifecycle budget impact.

## Gate assessment
F003 remains **IN STUDY / NOT PASS**. It has SOURCE + MODEL + retained executable failure/comparison evidence and now a direct Dart transfer harness with an explicit non-timing oracle. Direct Dart execution must reach a terminal verdict before that rung is credited; space complexity, broader algorithms and product/platform resource transfer remain OPEN.
