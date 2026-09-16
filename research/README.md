# Research Index

Canonical reusable research is organized by specialist ownership.

- `research/foundations/` — `F###`
- `research/architecture/` — `A###`
- `research/mobile/` — `M###`
- `research/data/` — `D###`
- `research/quality/` — `Q###`
- `research/systems/` — `S###`

## Current studies

### Foundations
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**. Source/model + OS process/I/O evidence; direct Dart JIT/AOT and Flutter runtime validation remain OPEN. Environment rechecked 2026-09-16: no trustworthy `dart`/`flutter` executable available.

### Architecture
- `A001` — `research/architecture/A001_information_hiding_change_pressure.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**. Positive change-locality, over-abstraction counterexample, exact-ref LogMate transfer.
- `A002` — `research/architecture/A002_dependency_direction_state_ownership.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**. Authority/projection second-writer failure and materially different dependency-direction alternative comparison complete.
- `A003` — `research/architecture/A003_interfaces_contracts_api_evolution.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**. Semantic compatibility, pre/postcondition matrix, invariant violation and additive-breaking protocol counterexample executable-tested.

### Mobile
- `M001` — `research/mobile/M001_flutter_runtime_widget_lifecycle_platform_boundary.md` — **IN STUDY / first integrated Foundation block complete**. Current Flutter/Dart/Android/iOS source model separates runtime/UI/lifecycle/platform boundaries; executable language-neutral lifecycle-gap model demonstrates why skipped lifecycle notifications cannot be the sole durable-commit guarantee. Real Flutter/device/process-death validation remains OPEN.

### Data
- `D001` — `research/data/D001_state_persistence_durability_source_of_truth.md` — **IN STUDY**. State/persistence/durability/SSOT/invariant model + SQLite process-kill evidence; mobile/power-loss/migration/backup/distributed evidence remain OPEN.

### Quality
- `Q001` — `research/quality/Q001_correctness_specification_oracle_reproducibility.md` — **IN STUDY / substantial first block complete**. Weak oracle passed a deliberate defect; stronger exact/invariant oracles detected it; seeded cases reproduced identically; Test Evidence Contract promoted Studio-wide.

### Systems
- `S001` — `research/systems/S001_trust_artifact_provenance_foundations.md` — **IN STUDY / two integrated executable blocks complete**. Artifact-identity counterexample plus artifact+unsigned-checksum substitution and authentic-but-unauthorized identity cases now separate integrity, authenticity, authorization and provenance. Public-key/key lifecycle, least privilege, CI trust boundary, mobile delivery and resource evidence remain OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS.

Do not create files merely to count activity. Prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record:
`repository → exact ref/tag/branch/commit → declared version if available → evidence date`.

A product observation is not automatically reusable Studio truth. State why the mechanism transfers before promoting it.
