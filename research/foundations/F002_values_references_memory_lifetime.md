# F002 — Values, References, Memory Models and Lifetime

Status: **IN STUDY — first integrated Foundation block complete**  
Evidence date: 2026-09-17

## Problem / scope

Programs routinely fail when engineers conflate a variable/name with an object, rebinding with mutation, shallow structural copying with ownership isolation, object reachability with deterministic resource lifetime, or implementation memory layout with language semantics. This block establishes those boundaries before Architecture state ownership, Mobile lifecycle/resource work, Data snapshots/caches, or Systems memory/resource analysis build on them.

## SOURCE

Current Dart core documentation states that Dart is garbage collected: an object that is no longer referenced may be disposed by the garbage collector. `WeakReference` does not keep its target alive. Dart `Finalizer` callbacks are not guaranteed to run. `NativeFinalizer` has stronger native-resource guarantees, and `Finalizable` can keep a local value alive through the declaring block. Dart core also exposes `identical(a, b)` specifically to ask whether two references designate the same object.

Sources:
- https://dart.dev/libraries/dart-core — current Dart core documentation, checked 2026-09-17.
- https://api.dart.dev/dart-core/ — current dart:core API, checked 2026-09-17.
- https://api.dart.dev/dart-isolate/Isolate-class.html — isolate access boundary, checked 2026-09-17.

## SYNTHESIS — semantic model

Use these as separate concepts:

1. **name/variable/binding** — a program location through which a value is accessed or changed according to language rules;
2. **value/object** — the semantic datum or object being designated;
3. **identity** — whether two designations refer to the same object, where the language exposes such a distinction;
4. **mutation** — changing state reachable through an object;
5. **rebinding/assignment** — changing which value a mutable binding designates; this need not mutate the old object;
6. **aliasing** — two reachable paths designate the same mutable object/state;
7. **reachability/liveness** — whether runtime rules still treat an object as reachable/alive;
8. **resource lifetime** — when an external resource such as a file/socket/native handle is released; this must not be assumed to equal garbage-collection timing;
9. **implementation layout** — stack, heap, register, escape-analysis or representation choices. These can explain a particular runtime but are not automatically language-level contracts.

Therefore `variable = object`, `assignment = copy`, `final = immutable object`, `unreachable = immediately destroyed`, and `GC = deterministic resource cleanup` are invalid universal shortcuts.

## EXECUTABLE TEST / FAILURE CASE / ALTERNATIVE

Fixture: `research/foundations/fixtures/F002_aliasing_lifetime_boundary.py`

Environment: Python 3.13.5 / Linux 6.18.44 x86_64, executed 2026-09-17.

Claim under test: a mutable object graph can remain shared through multiple names or a shallow copy; rebinding one name is distinct from mutating the previously shared object; an explicit graph-copy alternative can isolate this bounded graph.

Property/oracle:
- mutating through a direct alias must be observable through the original name;
- shallow-copying only the outer mapping must not be mistaken for nested ownership isolation;
- `deepcopy` must isolate the deliberately simple nested graph used by this fixture;
- rebinding `y` after `y = x` must not mutate `x`.

Observed:
`{'alias_mutation': 101, 'shallow_nested_alias': 101, 'deepcopy_original': 100, 'rebind_original': 1}`

Verdict: PASS for the bounded Python object-graph claims. The shallow-copy case is the representative failure: code that treats a copied outer container as an independent snapshot still mutates the original nested state.

Root cause: ownership/isolation was inferred from outer-container copying while a nested mutable object remained aliased.

Alternative: recursive copying isolates this deliberately simple graph. **ENGINEERING JUDGMENT:** deep copying is not a universal architecture recommendation; immutable value objects, explicit ownership, serialization boundaries, persistent data structures, or domain-specific copy semantics may be preferable depending on identity, cycles, resources, cost and invariants.

## Dart transfer boundary

**SOURCE:** Dart exposes object identity via `identical`, garbage collection, weak references and finalization semantics. **OPEN / VALIDATION:** no trustworthy `dart` or `flutter` executable exists in the current execution environment, so the Python alias/copy fixture is not Dart runtime evidence. Direct Dart validation should test identity, mutable collection aliasing, `final` binding versus object mutation, weak-reference/finalizer behavior where deterministic enough to test, and JIT/AOT differences only when the SDK is available.

**SYNTHESIS:** stack-versus-heap vocabulary is useful only when tied to a specific runtime/ABI/optimization claim. Correctness contracts should normally be stated in semantic terms—identity, reachability, mutation, ownership, lifetime—not inferred from a presumed physical stack/heap placement.

## RELATED DOMAIN CHECK

- Foundations: F001 execution/runtime distinctions constrain which memory claims can be language-level versus runtime-specific; F004/F005 add concurrency/async lifetime pressure.
- Architecture: A002 state ownership should treat aliasing as an ownership/coupling mechanism; shared mutable reachability can bypass intended dependency boundaries.
- Mobile: M001/M002 lifecycle callbacks do not define object/resource lifetime or durable state. Flutter/Dart transfer remains OPEN.
- Data: D001/D004 snapshot/cache/source-of-truth reasoning must distinguish copied representation from independent mutable ownership.
- Quality: Q001/Q005 require oracles that can observe aliasing side effects at the intended ownership boundary.
- Systems: deterministic release of files/sockets/native handles is a resource-management contract, not a generic GC timing guarantee.
- Design Studio: not materially relevant to this semantic block.
- Web Manager: not materially relevant.
- Marketing Manager: not materially relevant.
- Product repository: no product implementation claim was needed; no product ref audited in this block.

## HANDOFFS

### Architecture
Use F002 aliasing vocabulary when revisiting A002: `shared mutable reachability` is a concrete coupling/ownership mechanism. Do not equate `final` bindings or container copies with immutable/isolated domain state.

### Data
For caches, snapshots, import previews and backup staging, verify whether a representation is structurally independent at every mutable level required by the invariant. A shallow copy can preserve hidden write-through aliases.

### Mobile / Systems
Treat GC reachability, lifecycle callbacks and external-resource cleanup as separate contracts. Native/file/socket cleanup that must happen predictably needs explicit API/lifetime reasoning rather than ordinary Dart `Finalizer` assumptions.

## OPEN / VALIDATION / CHANGE WATCH

- OPEN: direct Dart JIT/AOT and Flutter runtime execution remains unavailable.
- VALIDATION: Dart identity/alias/final-binding fixture when SDK becomes available.
- VALIDATION: explicit external-resource lifetime comparison (deterministic close/dispose versus GC/finalizer) in a suitable runtime.
- OPEN: runtime-specific stack/heap/escape behavior should only be studied against exact Dart VM/compiler/backend versions when a decision actually depends on it.
- CHANGE WATCH: Dart runtime/compiler GC and optimization implementation details are version/backend sensitive; semantic language/API guarantees must be separated from implementation observations.

## Gate

F002 is **IN STUDY**, not PASS. First-principles semantic distinctions plus one executable failure/alternative comparison exist, but direct Dart/Flutter transfer and deterministic resource-lifetime evidence remain open.
