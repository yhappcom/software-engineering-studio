# F003 — Data Structures, Algorithms & Complexity

Status: **IN STUDY — first integrated Foundation block complete**  
Evidence date: 2026-09-17

## Problem / scope

Software can preserve the same functional result while having materially different growth costs because representation determines which operations are cheap. This block establishes the first professional boundary between abstract data-structure semantics, concrete representation, algorithmic growth, and measured runtime cost.

## SOURCE

Current CPython documentation states that `collections.deque` supports append/pop at either end with approximately O(1) performance, while `list.pop(0)` / front insertion incur O(n) memory movement because remaining elements move. The CPython built-in-type complexity documentation separately records list front-pop as O(n-k), list append/get-item as O(1), iteration/membership as O(n), and sorting as O(n log n).

Primary/current source URLs checked 2026-09-17:
- https://docs.python.org/3/library/collections.html#deque-objects
- https://docs.python.org/3/library/time-complexity.html

These are implementation/runtime-specific claims. They are not Dart collection complexity contracts.

## SYNTHESIS — semantic contract vs cost model

A queue contract can require FIFO behavior without prescribing a representation. A Python list drained by `pop(0)` and a deque drained by `popleft()` can therefore be semantically equivalent for the bounded workload while having different operation-growth behavior.

Complexity notation describes growth as input size changes; it does not provide elapsed-time truth for a particular machine, workload, cache state, allocator, runtime, or constant factor. Conversely, a single benchmark result cannot establish an asymptotic complexity class.

Useful separation:

`abstract operation/invariant → representation → primitive-operation cost → algorithm/workload composition → measured resource behavior`

## VALIDATION — bounded executable comparison

Fixture: `research/foundations/fixtures/F003_queue_structure_complexity.py`

Recorded environment: CPython 3.13.5 / Linux 6.18.44 x86_64.

Claim tested: two queue representations can preserve the same FIFO content result while showing materially different scaling for repeated front removal.

Property/oracle: after draining values `0..n-1`, both implementations must equal the independently derived closed-form checksum `n(n-1)/2`.

Recorded run:

| n | list pop(0) s | deque popleft s | list/deque | semantic oracle |
| ---: | ---: | ---: | ---: | --- |
| 5,000 | 0.000824 | 0.000320 | 2.57x | PASS |
| 10,000 | 0.007818 | 0.000666 | 11.74x | PASS |
| 20,000 | 0.033738 | 0.000731 | 46.14x | PASS |
| 40,000 | 0.124328 | 0.001914 | 64.96x | PASS |

The exact timings and ratios are observations, not portable guarantees. The semantic oracle passed at all four sizes. The source-backed explanation for the divergence is front-removal movement in CPython list versus approximately constant-time deque end removal.

## FAILURE / ROOT CAUSE

Failure class: selecting a representation because it satisfies the abstract API while ignoring the dominant workload operation.

For a FIFO repeatedly removing the front of a CPython list, each removal can move the remaining elements. Repeating that operation over a shrinking list composes many linear-cost operations. The defect is not that list violates FIFO semantics; it is a mismatch between representation and workload cost.

This directly rejects the shortcuts:
- `same output ⇒ same engineering behavior`;
- `container choice is only an implementation detail` when resource constraints matter;
- `O(1) ⇒ instant/fast`;
- `O(n) ⇒ unacceptable` without workload/resource context;
- `one benchmark ⇒ complexity proof`.

## ALTERNATIVE / ENGINEERING JUDGMENT

For CPython FIFO workloads dominated by both-end insertion/removal, deque is the source-supported alternative. For workloads dominated by random indexed access, the same source warns deque access slows toward the middle and recommends lists for fast random access. Data-structure choice therefore follows the operation mix and invariants, not a universal ranking.

At product scale, cost models should include at least time, space, mutation/copy cost, locality/serialization constraints, persistence/index maintenance, and failure/recovery consequences where relevant. This block validates only one in-memory queue dimension.

## TRANSFER VALIDATION / OPEN

- **OPEN:** direct Dart `List`/queue structure complexity and runtime behavior. Do not transfer CPython costs by analogy.
- **OPEN:** Flutter frame-budget/UI-jank transfer.
- **OPEN:** persistent database/index cost transfer, where storage I/O and index maintenance dominate different operations.
- **OPEN:** memory/space measurements and allocator/cache effects.
- **OPEN:** algorithmic search/index comparison and adversarial/hash-collision behavior.
- **VALIDATION:** when Dart SDK becomes available, build a Dart fixture with an explicit semantic oracle and size sweep; use Dart documentation/source or implementation evidence for any complexity claim.

## RELATED DOMAIN CHECK

- **Foundations:** F002 aliasing/representation boundaries checked; F001 Dart execution remains toolchain-blocked.
- **Architecture:** representation can remain hidden behind an interface, but resource behavior can be part of a contract/SLO and therefore cannot always be dismissed as private implementation detail.
- **Mobile:** operation growth can consume frame/startup/background budgets; direct Flutter transfer remains OPEN.
- **Data:** D002 indexing and D004 cache structures depend on workload-sensitive cost models; this F003 block supplies the prerequisite distinction, not a database implementation conclusion.
- **Quality:** performance evidence needs semantic oracles plus controlled size/workload; benchmark timing alone does not prove correctness or complexity.
- **Systems:** S003 should own production profiling/resource-budget evidence; F003 owns the algorithm/data-structure growth model.
- **Design Studio:** not materially relevant to this bounded Foundation mechanism; future UI latency budgets may create a handoff.
- **Web Manager:** not materially relevant to this bounded in-memory mechanism.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no product behavior claim was needed; no product repository audited in this block.

## HANDOFFS

### Foundations → Data
Use `abstract operation → representation → primitive cost → workload composition` when comparing indexes, cache structures, import duplicate detection, and sync queues. Do not transfer CPython constants or container guarantees.

### Foundations → Systems
S003 profiling should distinguish predicted growth class from measured wall-clock/resource evidence. Size sweeps can test whether measurements are consistent with a model, but they do not prove the model alone.

### Foundations → Mobile
When direct Flutter execution is available, transfer-test whether a product-relevant operation mix breaches frame/startup/background budgets; do not infer UI performance from this CPython fixture.

## Gate assessment

F003 has SOURCE + MODEL + executable semantic comparison + a representative cost-mismatch failure + alternative. It remains **IN STUDY**, not PASS: direct Dart transfer, broader structures/algorithms, space complexity, search/index behavior and product/runtime resource validation remain OPEN.
