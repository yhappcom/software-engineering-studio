# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-16  
Canonical curriculum: `LEARNING_ROADMAP.md`

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart/Flutter execution OPEN |
| Architecture | Stage 1 IN STUDY — A001/A002/A003 substantial Foundation blocks complete |
| Mobile | Stage 1 READY |
| Data | Stage 1 IN STUDY — D001 substantial first block |
| Quality | Stage 1 IN STUDY — Q001 substantial first block |
| Systems | Stage 1 READY |

No specialist has passed Foundation.

## Meaningful new evidence

### A003 — Interfaces, Contracts, Invariants & API Evolution
Canonical: `research/architecture/A003_interfaces_contracts_api_evolution.md`

A003 professional boundary was advanced from first semantic-break evidence to a bounded provider/consumer compatibility matrix:
- weaker precondition preserved old legal callers; stronger precondition rejected old-legal `x=0`;
- stronger postcondition preserved the retained guarantee; weaker postcondition violated it;
- replacement account expanded reachable state to `balance=-1`, violating the retained non-negative invariant;
- an additive JSON `source` field broke an existing strict V1 consumer that accepted exactly `minutes`, demonstrating that additive change shape is not itself compatibility proof.

Primary source added: Liskov/Wing 1994 behavioral-subtyping paper, checked via CMU-hosted author copy. The result reinforces the Studio rule that compatibility is `provider evolution × retained consumer properties × compatibility dimension`.

Evidence environment: Python 3.13.5, Linux 6.18.44 x86_64/glibc 2.41. Evidence is bounded to the fixture; no Dart/Flutter, ABI, persisted-schema, protocol-standard, or production claim.

## Cross-track handoffs
- **Data:** D003 should build explicit old/new reader-writer matrices and separate schema shape from semantic invariants.
- **Quality:** retained consumer contracts/invariants are compatibility oracles; include failure semantics, not just values.
- **Mobile:** plugin/platform upgrades require behavioral evidence beyond Dart signatures.
- **Systems:** release/versioning must name the compatibility dimension and rollback claim.

## Current Balance Loop
F001 direct Dart JIT/AOT and Flutter runtime validation was rechecked in the available execution environment: neither `dart` nor `flutter` executable is available. The gap remains OPEN; no simulated evidence was substituted.

A003 is now a substantial Foundation block and should not be extended merely for Architecture rotation. Architecture as a track remains NOT PASS because architecture-vs-design-vs-implementation and refactoring/technical-debt fundamentals remain incomplete.

Next-run candidate comparison should give particular weight to:
1. **M001** — highest live MintTap/LogMate platform leverage, but executable Flutter evidence remains toolchain-constrained; source/model work can proceed only with explicit validation limits;
2. **S001** — independent, high cross-track leverage for trust/resource/build boundaries and not blocked by Flutter execution;
3. **Architecture Foundation closure** — useful but lower urgency than opening Mobile/Systems unless a live architecture decision requires it;
4. **D002/Q002** — strong correctness leverage but currently less urgent than the untouched Mobile/Systems foundations.

Balance Loop must choose from actual evidence opportunity, not this ordering mechanically.

## Evidence rule
No PASS from reading alone. Expected progression where applicable:
`SOURCE → MODEL → EXECUTABLE EXAMPLE → FAILURE → DEBUG/ROOT CAUSE → ALTERNATIVE → TRANSFER → PRODUCTION EVIDENCE`.
