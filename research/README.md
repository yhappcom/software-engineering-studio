# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/` (`F###`), `research/architecture/` (`A###`), `research/mobile/` (`M###`), `research/data/` (`D###`), `research/quality/` (`Q###`), and `research/systems/` (`S###`).

## Current studies

### Foundations
- `F001` — `research/foundations/F001_program_execution_foundations.md` — **IN STUDY**; direct Dart JIT/AOT and Flutter runtime validation OPEN.
- `F002`–`F006` — initial integrated executable/model Foundation blocks complete; see `progress/FOUNDATIONS_STATUS.md`.

### Architecture
- `A001`–`A003` — substantial Foundation blocks complete.
- `A005` — base study + repeated-change executable evidence + natural exact-ref LogMate evolution transfer; direct Flutter runtime and long-horizon product evolution OPEN.
- `A006` — evidence-preserving decisions + governance fixture; natural ADR-corpus validation OPEN.

### Mobile
- `M001`–`M006` — all planned Foundation boundaries have first professional/model evidence; direct Flutter/native/browser/EFB transfer remains OPEN.

### Data
- `D001`–`D004` — Foundation studies initiated with executable/professional evidence.
- `D005` — recovery/process crash/storage faults/short-write/torn-image model + real WAL crash/checkpoint/main-file-copy boundary + `research/data/D005_wal_checkpoint_reader_starvation.md`. New Python 3.13.5/SQLite 3.46.1 evidence pins an active reader at an earlier WAL end mark: PASSIVE could not advance in the fixture, TRUNCATE returned busy and could not reset the 16512-byte WAL, then succeeded and truncated to zero after the reader ended. Checkpoint invocation is therefore not unconditional consolidation; reader lifetime and checkpoint mode are progress inputs. Physical power loss, checkpoint interruption, sustained starvation thresholds, Online Backup API and mobile durability remain OPEN.
- `D006` — base sync + real TCP ambiguous retry + isolated kernel link interruption + LogMate inbound cursor atomicity transfer; actual LogMate persistence/Sync remains OPEN.

### Quality
- `Q001`–`Q005` — professional Foundation boundaries initiated; Q004 includes generated shrinking plus mutation/exhaustive-search evidence.
- `Q006` — model fault campaign plus real child-process crash/restart + SQLite persistent-state oracle discrimination; Dart/Flutter/mobile/backend/production transfer OPEN.

### Systems
- `S001`–`S004`, `S006` — planned Foundation boundaries initiated with executable/professional evidence.
- `S005` — release-identity model + real OpenSSL asymmetric signature verification + bounded GCC/ld reproducibility + exact-ref LogMate build-identity transfer. CI/OIDC/attestation, authorization/key lifecycle, mobile signing/build execution, hermeticity, independent-host reproducibility and production delivery remain OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS. Do not create files merely to count activity; prefer coherent integrated studies.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. A product observation is not automatically reusable Studio truth; state mechanism and transfer limits.
