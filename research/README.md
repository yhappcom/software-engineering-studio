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
- `D003` — `research/data/D003_schema_evolution_migration_rollback_compatibility.md` — **IN STUDY / two integrated migration blocks complete**. Old/new compatibility and publication failure plus constraint-transform failure, fail-closed rollback alternative, and FK enforcement-vs-validation evidence. Actual rollback-release and mobile migration remain OPEN.
- `D004` — `research/data/D004_cache_offline_first_data_ownership.md` — **IN STUDY / first integrated Foundation block complete**. Cache/freshness/authority separation, destructive stale-refresh failure, pending-overlay alternative and cache-miss-vs-authoritative-absence counterexample. Real Firestore/FlutterFire, durable pending queue, process-death and conflict evidence OPEN.
- `D005` — `research/data/D005_backup_restore_recovery_acceptance.md` — **IN STUDY / two integrated backup-restore blocks complete**. Actual isolated restore + physical/schema/semantic acceptance, corrupt/incompatible artifact failures, destructive publish-before-validation failure, validate-before-publish alternative, and injected pre-publication failure evidence. Crash/power-loss, active-WAL/open-handle and mobile publication semantics remain OPEN.
- `D006` — `research/data/D006_replication_sync_consistency_idempotency_conflicts.md` — **IN STUDY / first integrated Foundation block complete**. Lost-ack retry duplication vs operation-id deduplication, delivery/application/ack separation, and whole-record LWW concurrent-intent loss with bounded alternative. Real network/backend/multi-device/reorder/tombstone evidence OPEN.

### Quality
- `Q001` — `research/quality/Q001_correctness_specification_oracle_reproducibility.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**.
- `Q002` — `research/quality/Q002_test_levels_evidence_boundaries.md` — **IN STUDY / first integrated Foundation block complete**.
- `Q003` — `research/quality/Q003_determinism_nondeterminism_concurrency_flaky_tests.md` — **IN STUDY / first integrated Foundation block complete**. Determinism/reproducibility/flakiness distinctions plus deliberately widened shared-state lost-update failure, synchronized alternative and D006 event-order transfer. Deeper schedule exploration, harness-vs-SUT flake isolation and Dart/network transfer OPEN.

### Systems
- `S001` — `research/systems/S001_trust_artifact_provenance_foundations.md` — **IN STUDY / two integrated executable blocks complete**.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS.

Do not create files merely to count activity. Prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record:
`repository → exact ref/tag/branch/commit → declared version if available → evidence date`.

A product observation is not automatically reusable Studio truth. State why the mechanism transfers before promoting it.
