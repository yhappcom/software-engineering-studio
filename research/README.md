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
- `F002` — `research/foundations/F002_values_references_memory_lifetime.md` — **IN STUDY / first integrated Foundation block complete**. Binding/object/identity/mutation/alias/reachability/resource-lifetime distinctions plus bounded alias/shallow-copy failure and isolation comparison; direct Dart/Flutter transfer OPEN.
- `F004` — `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md` — **IN STUDY / two integrated Foundation blocks complete**.
- `F005` — `research/foundations/F005_async_event_loop_futures_cancellation.md` — **IN STUDY / two integrated Foundation blocks complete**.
- `F006` — `research/foundations/F006_os_file_socket_network_foundations.md` — **IN STUDY / two integrated Foundation blocks complete**. Stream framing plus graceful EOF/truncated-frame and abort/reset-after-complete-frame evidence; direct Dart/Flutter, real network/partition, cross-OS/mobile evidence OPEN.

### Architecture
- `A001` — `research/architecture/A001_information_hiding_change_pressure.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `A002` — `research/architecture/A002_dependency_direction_state_ownership.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `A003` — `research/architecture/A003_interfaces_contracts_api_evolution.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.

### Mobile
- `M001` — `research/mobile/M001_flutter_runtime_widget_lifecycle_platform_boundary.md` — **IN STUDY / first integrated Foundation block complete**.
- `M002` — `research/mobile/M002_process_lifecycle_termination_background_execution.md` — **IN STUDY / first source/failure-model block complete**. Android/iOS activity/scene/process/background/durable-state boundaries established from current primary sources; real emulator/device/Dart/Flutter interruption validation OPEN.

### Data
- `D001` — `research/data/D001_state_persistence_durability_source_of_truth.md` — **IN STUDY**.
- `D002` — `research/data/D002_representation_files_database_indexes_transactions.md` — **IN STUDY / two integrated Foundation blocks complete**.
- `D003` — `research/data/D003_schema_evolution_migration_rollback_compatibility.md` — **IN STUDY / two integrated migration blocks complete**.
- `D004` — `research/data/D004_cache_offline_first_data_ownership.md` — **IN STUDY / first integrated Foundation block complete**.
- `D005` — `research/data/D005_backup_restore_recovery_acceptance.md` — **IN STUDY / two integrated backup-restore blocks complete**.
- `D006` — `research/data/D006_replication_sync_consistency_idempotency_conflicts.md` — **IN STUDY / two integrated Foundation blocks complete**. Retry/idempotency + concurrent-update conflict, then Q003-derived reorder/delete matrix; real backend/multi-device/tombstone-GC evidence OPEN.

### Quality
- `Q001` — `research/quality/Q001_correctness_specification_oracle_reproducibility.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `Q002` — `research/quality/Q002_test_levels_evidence_boundaries.md` — **IN STUDY / first integrated Foundation block complete**.
- `Q003` — `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md` — **IN STUDY / two integrated Foundation blocks complete**. Shared-memory schedule failure plus deterministic 24-order timeout/complete/cancel/retry matrix.
- `Q005` — `research/quality/Q005_debugging_fault_isolation_observability.md` — **IN STUDY / first integrated Foundation block complete**. Identical-symptom fault isolation via correlated boundary observations plus independent invariant; production/distributed/crash/runtime transfer OPEN.
- `Q006` — `research/quality/Q006_fault_injection_recovery_regression_governance.md` — **IN STUDY / first integrated Foundation block complete**. Three-point fault campaign with semantic recovery oracle and deliberate idempotency-regression mutant; real crash/restart/durable/network/mobile transfer OPEN.

### Systems
- `S001` — `research/systems/S001_trust_artifact_provenance_foundations.md` — **IN STUDY / two integrated executable blocks complete**.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS.

Do not create files merely to count activity. Prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record:
`repository → exact ref/tag/branch/commit → declared version if available → evidence date`.

A product observation is not automatically reusable Studio truth. State why the mechanism transfers before promoting it.
