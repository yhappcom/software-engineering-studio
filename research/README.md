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
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**. Source/model + OS process/I/O evidence; direct Dart JIT/AOT and Flutter runtime validation remain OPEN.
- `F002` — `research/foundations/F002_values_references_memory_lifetime.md` — **IN STUDY / first integrated block complete**.
- `F003` — `research/foundations/F003_data_structures_algorithms_complexity.md` — **IN STUDY / first integrated block complete**.
- `F004` — `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md` — **IN STUDY / two integrated blocks complete**.
- `F005` — `research/foundations/F005_async_event_loop_futures_cancellation.md` — **IN STUDY / two integrated blocks complete**.
- `F006` — `research/foundations/F006_os_file_socket_network_foundations.md` — **IN STUDY / two integrated blocks complete**.

### Architecture
- `A001` — `research/architecture/A001_information_hiding_change_pressure.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `A002` — `research/architecture/A002_dependency_direction_state_ownership.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `A003` — `research/architecture/A003_interfaces_contracts_api_evolution.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `A005` — `research/architecture/A005_refactoring_technical_debt_evolutionary_boundaries.md` — **IN STUDY / first integrated Foundation block complete**.

### Mobile
- `M001` — `research/mobile/M001_flutter_runtime_widget_lifecycle_platform_boundary.md` — **IN STUDY / first integrated Foundation block complete**.
- `M002` — `research/mobile/M002_process_lifecycle_termination_background_execution.md` — **IN STUDY / first source/failure-model block complete**.

### Data
- `D001` — `research/data/D001_state_persistence_durability_source_of_truth.md` — **IN STUDY**.
- `D002` — `research/data/D002_representation_files_database_indexes_transactions.md` — **IN STUDY / two integrated blocks complete**.
- `D003` — `research/data/D003_schema_evolution_migration_rollback_compatibility.md` — **IN STUDY / two integrated migration blocks complete**.
- `D004` — `research/data/D004_cache_offline_first_data_ownership.md` — **IN STUDY / first integrated block complete**.
- `D005` — `research/data/D005_backup_restore_recovery_acceptance.md` — **IN STUDY / two integrated backup-restore blocks complete**.
- `D006` — `research/data/D006_replication_sync_consistency_idempotency_conflicts.md` — **IN STUDY / two integrated blocks complete**.

### Quality
- `Q001` — `research/quality/Q001_correctness_specification_oracle_reproducibility.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `Q002` — `research/quality/Q002_test_levels_evidence_boundaries.md` — **IN STUDY / first integrated block complete**.
- `Q003` — `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md` — **IN STUDY / two integrated blocks complete**.
- `Q004` — `research/quality/Q004_property_model_based_testing_invariants.md` — **IN STUDY / first executable counterexample + shrinking evidence**.
- `Q005` — `research/quality/Q005_debugging_fault_isolation_observability.md` — **IN STUDY / first integrated block complete**.
- `Q006` — `research/quality/Q006_fault_injection_recovery_regression_governance.md` — **IN STUDY / first integrated block complete**.

### Systems
- `S001` — `research/systems/S001_trust_artifact_provenance_foundations.md` — **IN STUDY / two integrated executable blocks complete**.
- `S002` — `research/systems/S002_threat_model_least_privilege_secrets_secure_storage.md` — **IN STUDY / first integrated executable Foundation block complete**.
- `S003` — `research/systems/S003_resource_cost_models_profiling_foundations.md` — **IN STUDY / first integrated executable Foundation block complete**.
- `S004` — `research/systems/S004_dependency_supply_chain_build_system_foundations.md` — **IN STUDY / first integrated executable Foundation block complete**. Separates manifest constraints, resolved graph, content integrity, build inputs/platform, artifact and provenance; bounded Python resolution-drift/integrity failure evidence complete; direct Dart/pub/build transfer OPEN.
- `S005` — `research/systems/S005_ci_signing_versioning_release_evidence.md` — **IN STUDY / first integrated executable Foundation block complete**. Separates CI verdict, version, source, artifact digest, signature/attestation, verification policy and deployment identity; bounded stale-source/changed-bytes release-gate evidence complete; real CI/signing/reproducibility/mobile deployment OPEN.
- `S006` — `research/systems/S006_rollback_incident_change_safety_governance.md` — **IN STUDY / first integrated executable Foundation block complete**. Models rollback as a multi-state transition rather than deployment inverse; bounded Python evidence shows old-artifact failure after incompatible durable-state evolution and recovery after compatible-state restoration; real deployment/database/mobile/production transfer OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS.

Do not create files merely to count activity. Prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record:
`repository → exact ref/tag/branch/commit → declared version if available → evidence date`.

A product observation is not automatically reusable Studio truth. State why the mechanism transfers before promoting it.
