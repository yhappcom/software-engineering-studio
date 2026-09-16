# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-16  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN |
| Architecture | Stage 1 IN STUDY — A001/A002 substantial; A003 semantic-contract block underway |
| Mobile | Stage 1 READY |
| Data | Stage 1 IN STUDY — D001 substantial first block |
| Quality | Stage 1 IN STUDY — Q001 substantial first block |
| Systems | Stage 1 READY |

No specialist has passed Foundation.

## Meaningful new evidence

### A003 — Interfaces, Contracts, Invariants & API Evolution
Canonical: `research/architecture/A003_interfaces_contracts_api_evolution.md`

A003 now has executable evidence that source/call-shape compatibility does not imply semantic compatibility:
- retained consumer contract expected `total_minutes()` to mean block time; fixture total was 150;
- a same-name/same-signature replacement silently changed meaning to airborne time and returned 125, failing the retained oracle;
- an additive alternative preserved old block-time semantics and exposed airborne total separately;
- a second same-signature replacement strengthened its precondition by rejecting empty input that the old contract accepted as total 0, reproducing a separate compatibility break.

Primary method evidence: current Eiffel Design by Contract documentation was checked for precondition/postcondition/invariant responsibility semantics. Studio synthesis treats an operational contract as accepted input + returned meaning + state transition + invariant + failure semantics + observable side effects where relevant.

Evidence limit: Python synchronous fixture only. No ABI, Dart/Flutter, persisted schema, protocol, mobile, or production compatibility claim.

## Cross-track handoffs
- **Data:** D003 must separate schema/representation compatibility from semantic invariants and retained reader/writer contracts.
- **Quality:** compatibility tests should use prior consumer expectations/invariants as independent oracles; compilation success is insufficient.
- **Mobile:** plugin/platform API evolution requires behavioral/failure-contract evidence in addition to Dart signatures.
- **Systems:** release/versioning work must name the compatibility dimension claimed: source, binary, data/schema, protocol, or behavioral.

## Current Balance Loop
F001 direct Dart JIT/AOT and Flutter runtime validation remains OPEN because no trustworthy execution environment has become available; no simulated evidence was substituted.

A003 remains the highest-value coherent continuation because its professional boundary is incomplete and directly constrains future LogMate ledger/import/sync contracts and MintTap calculation/data boundaries. Next evidence should build a provider/consumer compatibility matrix and test invariant evolution plus an additive change that is nevertheless breaking. M001 remains high product leverage but runtime-toolchain constrained; S001 remains the strongest independent alternative if Architecture becomes blocked.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
