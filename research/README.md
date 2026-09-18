# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/` (`F###`), `research/architecture/` (`A###`), `research/mobile/` (`M###`), `research/data/` (`D###`), `research/quality/` (`Q###`), and `research/systems/` (`S###`).

## Current studies

### Foundations
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**; direct Dart JIT/AOT and Flutter runtime validation OPEN.
- `F002` — `research/foundations/F002_values_references_memory_lifetime.md` — first integrated block complete.
- `F003` — `research/foundations/F003_data_structures_algorithms_complexity.md` — first integrated block complete.
- `F004` — `research/foundations/F004_processes_threads_scheduling_synchronization_hazards.md` — two integrated blocks complete.
- `F005` — `research/foundations/F005_async_event_loop_futures_cancellation.md` — two integrated blocks complete.
- `F006` — `research/foundations/F006_os_file_socket_network_foundations.md` — two integrated blocks complete.

### Architecture
- `A001` — `research/architecture/A001_information_hiding_change_pressure.md` — substantial Foundation block complete.
- `A002` — `research/architecture/A002_dependency_direction_state_ownership.md` — substantial Foundation block complete.
- `A003` — `research/architecture/A003_interfaces_contracts_api_evolution.md` — substantial Foundation block complete.
- `A005` — `research/architecture/A005_refactoring_technical_debt_evolutionary_boundaries.md` — first integrated block complete.
- `A006` — `research/architecture/A006_evidence_preserving_architecture_decisions.md` — first integrated decision-evidence block complete.

### Mobile
- `M001` — `research/mobile/M001_flutter_runtime_widget_lifecycle_platform_boundary.md` — first integrated block complete.
- `M002` — `research/mobile/M002_process_lifecycle_termination_background_execution.md` — first source/failure-model block complete.
- `M003` — `research/mobile/M003_sandbox_files_permissions_secure_storage_platform_apis.md` — first integrated block + bounded executable evidence.
- `M004` — `research/mobile/M004_plugin_platform_channel_native_integration_boundaries.md` — first integrated block + bounded executable evidence.
- `M005` — `research/mobile/M005_cross_platform_portability_divergence.md` — first integrated block + bounded executable capability evidence.
- `M006` — `research/mobile/M006_native_pwa_web_deployment_constraints.md` — first integrated block + bounded executable acceptance evidence; real platform acceptance OPEN.

### Data
- `D001` — `research/data/D001_state_persistence_durability_source_of_truth.md` — substantial first block complete.
- `D002` — `research/data/D002_representation_files_database_indexes_transactions.md` — two integrated blocks complete.
- `D003` — `research/data/D003_schema_evolution_migration_rollback_compatibility.md` — two integrated migration blocks complete.
- `D004` — `research/data/D004_cache_offline_first_data_ownership.md` — first integrated block complete.
- `D005` — `research/data/D005_backup_restore_recovery_acceptance.md` — two integrated blocks complete.
- `D006` — `research/data/D006_replication_sync_consistency_idempotency_conflicts.md` — two integrated blocks complete.

### Quality
- `Q001` — `research/quality/Q001_correctness_specification_oracle_reproducibility.md` — substantial Foundation block complete.
- `Q002` — `research/quality/Q002_test_levels_evidence_boundaries.md` — first integrated block complete.
- `Q003` — `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md` — two integrated blocks complete.
- `Q004` — `research/quality/Q004_property_model_based_testing_invariants.md` + `research/quality/Q004_mutation_sensitivity_search_strength.md` — **two executable blocks complete**: generated counterexample/shrinking plus deliberate mutation sensitivity and bounded exhaustive-vs-generated comparison.
- `Q005` — `research/quality/Q005_debugging_fault_isolation_observability.md` — first integrated block complete.
- `Q006` — `research/quality/Q006_fault_injection_recovery_regression_governance.md` — first integrated block complete.

### Systems
- `S001` — `research/systems/S001_trust_artifact_provenance_foundations.md` — two integrated executable blocks complete.
- `S002` — `research/systems/S002_threat_model_least_privilege_secrets_secure_storage.md` — first integrated executable block complete.
- `S003` — `research/systems/S003_resource_cost_models_profiling_foundations.md` — first integrated executable block complete.
- `S004` — `research/systems/S004_dependency_supply_chain_build_system_foundations.md` — first integrated executable block complete.
- `S005` — `research/systems/S005_ci_signing_versioning_release_evidence.md` — first integrated executable block complete.
- `S006` — `research/systems/S006_rollback_incident_change_safety_governance.md` — first integrated executable block complete.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS. Do not create files merely to count activity; prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. A product observation is not automatically reusable Studio truth; state mechanism and transfer limits.
