# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-16  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Mission
Build reusable software-engineering capability that improves real yhappcom product decisions through first-principles understanding, executable verification, failure analysis, and cross-repository collaboration. GitHub is canonical memory; chat is temporary context.

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 open Dart/Flutter validation |
| Architecture | Stage 1 IN STUDY — A001 substantial Foundation block complete; A002 next |
| Mobile | Stage 1 READY |
| Data | Stage 1 IN STUDY — D001 substantial first block complete |
| Quality | Stage 1 IN STUDY — Q001 substantial first block complete |
| Systems | Stage 1 READY |

No specialist has passed Foundation.

## Current integrated evidence

### F001 — Program Execution Foundations
Source/model + Linux/Python process/I/O boundary evidence exist. Direct Dart JIT/AOT and Flutter runtime validation remain OPEN. The current execution environment still does not provide trustworthy Dart/Flutter executables; no simulated evidence is substituted.

### D001 — State, Persistence, Durability & Source of Truth
State/persistence/commit/durability and logical authority were separated. SQLite process-kill evidence showed an uncommitted mutation disappearing after SIGKILL/reopen while a committed row remained reopen-visible, bounded to application-process termination on the recorded Linux environment. LogMate transfer was checked against exact commit `b551ce434ad72b1895033e0f3617c73b026d40ea`.

### Q001 — Correctness, Specification, Oracle & Reproducibility
A deliberate defective implementation passed a weak oracle but failed exact and invariant-based oracles; seeded generated cases reproduced identically. The resulting claim/spec/oracle/environment/reproduction/evidence-limit contract was promoted to `methods/VALIDATION_STANDARD.md`.

### A001 — Information Hiding, Cohesion, Coupling & Change Pressure
Canonical: `research/architecture/A001_information_hiding_change_pressure.md`

A001 now has balanced evidence rather than one-sided abstraction advocacy:
- historical/source model: Parnas-style decomposition around volatile design decisions;
- positive executable fixture: hidden representation knowledge localized a representation change while leaky consumers failed;
- counterexample executable fixture: in a fixed single-source/single-policy scenario, direct and pass-through layered designs had behavior parity while the layered fixture introduced 6 nodes / 9 declared dependency edges and a longer internal failure path without demonstrating locality/substitution benefit;
- exact-ref transfer: `yhappcom/logmate → b551ce434ad72b1895033e0f3617c73b026d40ea → app 1.0.0+1 → 2026-09-16`.

LogMate transfer findings:
- `AirportLookup` owns asset representation decoding plus lookup/autocomplete policy and explicitly remains separate from the still-open canonical FlightRecord airport representation; this is concrete information-hiding evidence;
- `AuthEngine` has both Firebase and preview/test implementations, while auth screens consume the contract rather than Firebase APIs; substitution and vendor/error-policy isolation are evidenced reasons for the boundary;
- local ledger/persistence, FlightRecord/calculation linkage, configuration persistence, Sync, and Backup/Export are not implemented at the inspected ref, so no future Repository/Service layering is inferred from current presentation code.

A001 evidence is mature enough to advance, but Architecture Stage 1 is **not PASS** because state ownership/dependency direction and interface/contract evolution remain underdeveloped.

## Cross-track synthesis
- **F001 → Architecture:** runtime/process boundaries and application module boundaries are different and must not be conflated.
- **D001 → Architecture:** logical mutation/source-of-truth authority must become explicit state ownership in A002.
- **Q001 → Architecture:** boundary contracts must support independent semantic oracles; mockability alone is not enough justification for an abstraction.
- **A001 → Data:** future repositories should own actual schema/durability/cache/sync policy rather than exist by convention.
- **A001 → Mobile/Systems:** platform/vendor/security/runtime facts can justify boundaries but interfaces do not erase platform risks.

## Current product relevance
### LogMate
The timing for A002 is high leverage: the inspected product explicitly has no local ledger/persistence yet. Establishing state ownership and dependency direction before that implementation reduces the risk of retrofitting architecture after storage/sync/UI assumptions have spread.

### MintTap
Future transfer remains financial-calculation ownership, Firebase/vendor representation leakage, persistence/data integrity, instrumentation and release architecture. Exact refs required when audited.

## Current Balance Loop
A001's counterexample and exact-ref transfer obligations are closed. F001 remains blocked on missing Dart/Flutter execution environment.

Highest-value next integrated block: **A002 — Modules, Layers, Boundaries, Dependency Direction & State Ownership**.

Why A002 outranks mechanical rotation now:
1. D001 already established logical mutation authority and durability boundaries;
2. A001 established when architectural boundaries earn their indirection;
3. Q001 supplies contract/oracle discipline for testing ownership;
4. LogMate's local ledger and persistence are explicitly not implemented at the inspected exact ref, so this knowledge can inform future work before implementation hardens;
5. A002 can obtain executable/model/product-structure evidence without fabricating unavailable Flutter runtime execution.

`M001` remains high product leverage and should advance when trustworthy Flutter/mobile source/fixture evidence can support its claims. `S001` remains the strongest cross-track alternative after A002 or if a security/build dependency becomes urgent.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.