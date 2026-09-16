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
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**. Source/model established; first executable OS process/I/O-boundary evidence recorded; direct Dart JIT/AOT and Flutter runtime validation remain OPEN.

### Architecture
- `A001` — `research/architecture/A001_information_hiding_change_pressure.md` — **SUBSTANTIAL FOUNDATION BLOCK COMPLETE / track not passed**. Parnas-style information-hiding/change-pressure model now has both directions of executable evidence: a representation-hiding fixture demonstrates bounded change locality, while a deliberate over-abstraction fixture shows additional dependency/diagnostic mechanism without demonstrated locality benefit in a fixed single-policy scenario. Exact-ref LogMate transfer (`b551ce434ad72b1895033e0f3617c73b026d40ea`, app `1.0.0+1`, 2026-09-16) validates `AirportLookup` as representation/policy ownership and `AuthEngine` as an actually substituted vendor-isolation boundary. A002/A003 remain required for Architecture Foundation maturity.

### Data
- `D001` — `research/data/D001_state_persistence_durability_source_of_truth.md` — **IN STUDY**. State/persistence/durability/SSOT/invariant model established; executable SQLite process-kill experiment distinguishes uncommitted mutation from committed reopen-visible state; LogMate transfer checked against exact main commit. Power-loss, mobile, WAL, migration, backup and distributed-sync evidence remain OPEN.

### Quality
- `Q001` — `research/quality/Q001_correctness_specification_oracle_reproducibility.md` — **IN STUDY / substantial first block complete**. IEEE SWEBOK v4.0a oracle/replication/testing-limits model integrated with executable deliberate-mutant evidence: weak oracle passed defective behavior, stronger exact/invariant oracles detected it, and seeded generated cases reproduced identically. The resulting Test Evidence Contract V1 was promoted into `methods/VALIDATION_STANDARD.md`.

## Research note minimum contract

A substantial note should contain, as applicable:

1. problem/question and why it matters;
2. scope and non-goals;
3. authoritative sources/specifications and dates/versions where volatile;
4. first-principles mechanism;
5. implementation or worked example;
6. executable validation and environment;
7. failure cases and debugging/root-cause evidence;
8. alternatives and trade-offs;
9. `RELATED DOMAIN CHECK`;
10. project-transfer implications and limits;
11. `OPEN`, `VALIDATION`, `CHANGE WATCH` items;
12. `HANDOFFS` when another track/repository can use the result.

Do not create files merely to count activity. Prefer coherent integrated studies.

## Product evidence

When a study inspects a real product, record:

`repository → exact ref/tag/branch/commit → declared version if available → evidence date`.

A product observation is not automatically reusable Studio truth. State why the mechanism transfers before promoting it.