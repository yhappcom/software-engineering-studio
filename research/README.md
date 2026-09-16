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
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**. Source/model + OS process/I/O evidence; direct Dart JIT/AOT and Flutter runtime validation remain OPEN. Environment rechecked 2026-09-17: no trustworthy `dart`/`flutter` executable available.

### Architecture
- `A001` — `research/architecture/A001_information_hiding_change_pressure.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `A002` — `research/architecture/A002_dependency_direction_state_ownership.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `A003` — `research/architecture/A003_interfaces_contracts_api_evolution.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.

### Mobile
- `M001` — `research/mobile/M001_flutter_runtime_widget_lifecycle_platform_boundary.md` — **IN STUDY / first integrated Foundation block complete**. Source model + lifecycle-gap executable model; real Flutter/device/process-death validation OPEN.

### Data
- `D001` — `research/data/D001_state_persistence_durability_source_of_truth.md` — **IN STUDY**. State/persistence/durability/SSOT/invariant model + SQLite process-kill evidence.
- `D002` — `research/data/D002_representation_files_database_indexes_transactions.md` — **IN STUDY / two integrated Foundation blocks complete**. Serialization/publication/transaction/index and DELETE-vs-WAL application-process-exit evidence.
- `D003` — `research/data/D003_schema_evolution_migration_rollback_compatibility.md` — **IN STUDY / two integrated Foundation blocks complete**. Old/new compatibility and publication failure plus constraint-transform failure, fail-closed rollback alternative, and FK enforcement-vs-validation evidence. Actual rollback-release, backup/restore and mobile migration remain OPEN.

### Quality
- `Q001` — `research/quality/Q001_correctness_specification_oracle_reproducibility.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `Q002` — `research/quality/Q002_test_levels_evidence_boundaries.md` — **IN STUDY / first integrated Foundation block complete**.

### Systems
- `S001` — `research/systems/S001_trust_artifact_provenance_foundations.md` — **IN STUDY / two integrated executable blocks complete**.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS.

Do not create files merely to count activity. Prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record:
`repository → exact ref/tag/branch/commit → declared version if available → evidence date`.

A product observation is not automatically reusable Studio truth. State why the mechanism transfers before promoting it.
