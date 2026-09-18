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
- `A005` — base study + repeated-change evidence — two executable blocks complete.
- `A006` — evidence-preserving decisions + governance fixture — two integrated blocks; natural-corpus/product transfer OPEN.

### Mobile
- `M001`–`M006` — all planned Foundation boundaries have first professional/model evidence; direct Flutter/native/browser/EFB transfer remains OPEN. See `progress/MOBILE_STATUS.md` for canonical per-topic state.

### Data
- `D001` — `research/data/D001_state_persistence_durability_source_of_truth.md` — substantial first block complete.
- `D002` — `research/data/D002_representation_files_database_indexes_transactions.md` — two integrated blocks complete.
- `D003` — `research/data/D003_schema_evolution_migration_rollback_compatibility.md` — two integrated migration blocks complete.
- `D004` — `research/data/D004_cache_offline_first_data_ownership.md` — first integrated block complete.
- `D005` — base recovery study + process-crash + bounded SQLite `SQLITE_FULL` studies — real application-process crash/restart and bounded capacity evidence; real OS/filesystem ENOSPC, power/device/mobile durability OPEN.
- `D006` — base sync study + real TCP ambiguous-retry + isolated kernel link interruption + `research/data/D006_logmate_inbound_cursor_atomicity_transfer.md` — exact-ref LogMate product-spec transfer now adds process-death evidence for inbound semantic-apply/cursor publication atomicity; actual LogMate persistence/Sync remains OPEN.

### Quality
- `Q001`–`Q006` — all professional Foundation boundaries initiated; Q004 includes generated shrinking plus mutation/exhaustive-search evidence. See `progress/QUALITY_STATUS.md`.

### Systems
- `S001`–`S006` — all planned Foundation boundaries initiated with executable/professional evidence. See `progress/SYSTEMS_STATUS.md`.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS. Do not create files merely to count activity; prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. A product observation is not automatically reusable Studio truth; state mechanism and transfer limits.
