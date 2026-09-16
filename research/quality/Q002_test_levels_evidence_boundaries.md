# Q002 — Test Levels, Evidence Boundaries & Trade-offs

Status: **IN STUDY — first integrated Foundation block**
Date: 2026-09-16
Lead: Quality

## Problem
Teams often treat unit, integration, system, end-to-end, and acceptance tests as a hierarchy of confidence or as tool labels. The engineering question is narrower: **what test object, interaction, environment, and claim does each test actually exercise, and what failure classes remain invisible?**

## SOURCE
- IEEE Computer Society SWEBOK v4 Software Testing KA distinguishes unit testing, integration testing, system testing, and acceptance testing by target and objective. Integration testing verifies interactions among SUT elements; system testing targets the behavior of the system as a whole; acceptance testing targets deployment readiness and satisfaction of requirements/end-user expectations.
- ISTQB CTFL v4.0.1 (2024-09-15) distinguishes component, component-integration, system, system-integration, and acceptance testing by test object, objectives, test basis, typical defects/failures, approach, responsibilities, and environment.

These sources support classification vocabulary; they do not prove that a particular project has sufficient tests.

## SYNTHESIS — evidence-boundary model
A useful test-level classification should start from the **claim boundary**, not the framework command or filename.

For each test record:
1. target/test object;
2. real versus substituted collaborators;
3. process/runtime/platform boundary crossed;
4. environment fidelity relevant to the claim;
5. oracle/specification;
6. failure classes the arrangement can and cannot expose.

A fast isolated test is strong evidence for local semantic logic when its oracle is valid. It is weak evidence for real wiring, serialization, database behavior, plugin/native boundaries, network behavior, OS lifecycle, packaging, or deployment unless those mechanisms are actually exercised.

Conversely, a broad end-to-end test is not automatically stronger for every claim. It can make fault localization harder, introduce nondeterminism, and still use an invalid oracle. Test breadth and evidence quality are separate dimensions.

## VALIDATION — isolated pass versus integration failure
Fixture: `research/quality/fixtures/Q002_test_level_boundary.py`

Environment executed before persistence:
- Python 3.13.5
- Linux container environment

### Test Evidence Contract
- **CLAIM:** a passing isolated component/unit test using a fake collaborator does not establish correctness of real collaborator integration/wiring.
- **SPEC/PROPERTY:** `Service.add(7)` must cause the repository-visible state to contain `7`.
- **TARGET:** same Service semantic path under a fake repository versus a concrete collaborator boundary.
- **INPUT/STATE:** empty repository, positive value `7`.
- **ORACLE:** repository-visible rows must equal `[7]` after the operation.
- **OBSERVATION:** isolated fake test PASS; concrete control PASS; deliberate real-collaborator variant that silently drops writes FAIL as expected.
- **ROOT CAUSE:** the isolated test substitutes away the collaborator behavior in which the deliberate defect exists. The local Service contract can be correct while the integrated path is defective.
- **VERDICT:** the bounded claim is validated.
- **EVIDENCE LIMIT:** this is not database, Flutter, network, device, process-death, or production evidence. It does not imply integration tests are generally superior to unit tests.

## CONTRADICTION — invalid shortcuts
The fixture directly contradicts:
- `unit tests pass → integration is correct`;
- `a fake that satisfies the expected interface → production collaborator satisfies it`.

The source model also rejects the opposite shortcut:
- `end-to-end test → strongest evidence for every claim`.

A test level changes **which mechanisms are present and which defects are observable**. It does not replace Q001's oracle discipline.

## ENGINEERING JUDGMENT — portfolio selection
Select the narrowest test that contains the mechanism relevant to the claim, then add broader tests for risks that arise only from collaboration, runtime/platform, packaging, deployment, or user workflow.

Examples:
- pure calculation invariant → component/unit candidate;
- serializer ↔ schema or service ↔ repository contract → integration candidate;
- complete local persistence/restart behavior → system/runtime candidate;
- app ↔ external Firebase/service → system-integration candidate;
- business/user deployment readiness → acceptance candidate.

These are candidate placements, not rigid naming rules. A project's architecture can move a boundary.

## DEPENDENCY / HANDOFFS
- **Mobile:** M001 lifecycle/process-death claims require tests that actually cross the platform/process boundary; widget/component tests cannot establish OS callback or termination behavior.
- **Data:** D002 database/index/transaction claims require real persistence integration where storage semantics are the target; fake repositories are insufficient for those claims.
- **Systems:** release/signing/artifact/deployment claims require exact artifact/environment evidence rather than source-level unit tests.
- **Architecture:** contract tests can validate A003 semantic boundaries, but substituted implementations must not be mistaken for proof about every provider.

## RELATED DOMAIN CHECK
- Foundations: F001 runtime/process distinction reused; direct Dart/Flutter execution remains OPEN.
- Architecture: A001-A003 boundary/contract evidence reused.
- Mobile: M001 establishes lifecycle/platform claims that need broader runtime evidence.
- Data: D001 demonstrates a real SQLite process-boundary persistence claim and is an example of mechanism-matched evidence.
- Systems: S001 artifact identity shows why test environment/build identity matters.
- Design Studio: not materially needed for this generic first block; design semantics may later supply acceptance specifications.
- Web Manager: browser/PWA acceptance requires environment/artifact provenance, but no new Web Manager audit was required here.
- Marketing Manager: not materially relevant to this generic test-level mechanism.
- Product repositories: no new product behavior claim; no product audit required.

## OPEN / VALIDATION
- Add a broader system-style failure showing a defect invisible to both isolated and collaborator integration tests.
- Compare test-double types by semantic risk rather than vocabulary alone.
- Study nondeterminism/flakiness in Q003 before treating broad asynchronous tests as reliable evidence.
- Transfer-test against exact Flutter/product tests once a trustworthy Dart/Flutter execution environment is available.

## Current conclusion
Test levels are **evidence boundaries**, not prestige levels. A test proves only claims whose relevant mechanisms are present, whose oracle is valid, and whose environment is identified. Use isolated tests for fast/local evidence and broader tests when the risk lives in interactions, runtime/platform, deployment, or user workflow.