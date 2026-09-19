# F002 — Direct Dart identity, aliasing and resource-lifetime transfer

Date: 2026-09-20
Lead: Foundations
Status: IN STUDY — executable transfer launched; final verdict pending

## Balance Loop selection
S004 remains the highest product-leverage thread, but its next rung is externally blocked: `yhappcom/logmate` is private and the Studio workflow's repository-scoped `GITHUB_TOKEN` cannot be assumed to read that separate private repository. The exact product ref remains readable through the authorized GitHub connector, but connector access is not an execution-environment source checkout. Repeating unauthenticated clone attempts would not add evidence. F002 is therefore the highest-value independent prerequisite: it is foundational to Architecture ownership, Data snapshot/cache semantics, Mobile resource lifecycle, and Systems resource management, and its prior note explicitly left direct Dart transfer OPEN.

## Existing SOURCE / model retained
Canonical base study: `research/foundations/F002_values_references_memory_lifetime.md`.

Retained semantic distinctions:
- binding/name is not the same concept as object identity;
- mutation is not rebinding;
- `final` constrains reassignment of the binding, not transitive mutability of an object graph;
- a shallow structural copy can have distinct outer identity while retaining nested mutable aliases;
- GC reachability is not a deterministic external-resource cleanup contract;
- stack/heap placement is runtime/backend implementation detail unless a specific contract says otherwise.

## EXECUTABLE TEST launched
Fixture: `research/foundations/fixtures/F002_dart_identity_lifetime.dart`.
Workflow: `.github/workflows/f002-dart-memory-lifetime-validation.yml`.
Exact source head: `d6bc8629f18b2ec8b7f8fb86849e7682f7ff36c2`.
Hosted run: `35455279567`; job `105929339080`.
Requested environment: GitHub-hosted Ubuntu, Dart SDK 3.13.3; workflow records `dart --version`, `uname -a`, and exact Git head.

### Claims / oracles
1. Direct aliasing preserves object identity and mutable writes are observable through the other alias.
2. A `final` binding can designate a mutable `List` that is subsequently mutated.
3. `Map.from` produces a distinct outer map in this bounded case while preserving the nested list reference; mutation through that nested reference remains shared.
4. An explicit nested `List.from` copy isolates the deliberately simple graph used by the fixture.
5. Explicit `RandomAccessFile.closeSync()` creates an observable resource-lifetime boundary: a later write through the closed handle must be rejected, while the bytes written before close remain readable from the path.

The explicit-close oracle is intentionally independent of garbage collection/finalizer timing. No test attempts to force or infer GC timing.

## FAILURE MODEL
The fixture is intended to expose these misunderstandings: `alias = copy`, `final = deep immutability`, `outer copy = ownership isolation`, and `external resource lifetime can be inferred from GC`. It does not test weak-reference collection timing, finalizer scheduling, VM escape analysis, physical stack/heap placement, native handles outside `dart:io`, concurrent aliasing, Android/iOS lifecycle, browser semantics, or production LogMate behavior.

## VALIDATION status
At persistence time, run `35455279567` had started successfully and checkout completed; Dart setup was still in progress. No PASS or FAIL is awarded until the fixture step reaches a terminal verdict. This note deliberately preserves the pending state rather than fabricating execution evidence.

## RELATED DOMAIN CHECK
- Foundations: lead; F001 provides trustworthy hosted Dart execution precedent.
- Architecture: A002 state ownership depends on distinguishing shared mutable reachability from binding immutability.
- Mobile: explicit resource cleanup and OS lifecycle are separate contracts; hosted `dart:io` evidence will not transfer automatically to Android/iOS/browser.
- Data: shallow snapshots/caches can retain hidden write-through aliases.
- Quality: fixture uses independent state/identity/closed-handle oracles and a bounded failure model.
- Systems: deterministic external-resource release is distinct from GC reachability.
- Design Studio: not materially relevant to this semantic/runtime block.
- Web Manager: not materially relevant.
- Marketing Manager: not materially relevant.
- Product: LogMate source-access dependency was rechecked only to choose work; no product implementation claim or product file edit is made here.

## HANDOFFS
- Architecture/Data: if the Dart fixture succeeds, use it as direct language transfer for shared mutable reachability and shallow-copy boundaries, not as a recommendation to deep-copy arbitrary domain graphs.
- Mobile/Systems: if explicit-close succeeds, use only the narrow conclusion that explicit `dart:io` close has an observable hosted-native resource boundary; do not infer platform lifecycle cleanup or GC behavior.
- Systems/S004: keep exact LogMate baseline build OPEN until an execution environment has authorized exact-ref source acquisition; connector read access is not equivalent to runner checkout provenance.

## OPEN / CHANGE WATCH
- Terminal result for run `35455279567` is pending.
- WeakReference/Finalizer behavior remains source/model evidence; nondeterministic GC timing is intentionally not a PASS oracle.
- JIT/AOT equivalence for these F002 semantics is not established by this single `dart run` fixture.
- Dart VM/runtime implementation details remain version/backend sensitive.
