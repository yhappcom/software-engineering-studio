# S006 — Rollback, Incident Evidence, Production Change Safety & Release Governance

Status: **IN STUDY — first integrated executable Foundation block complete**  
Evidence date: 2026-09-18

## Problem / scope
Rollback is often described as “put the old version back.” That collapses several independently changing states: application artifact, configuration, schema/data, infrastructure, traffic routing, external dependencies and operator/control-plane state. A previous artifact can be known-good in its old environment yet fail after newer state has crossed a compatibility boundary.

## SOURCE

### Google SRE — canarying and release safety
Google SRE's Canarying Releases chapter defines a canary as a partial, time-limited production deployment evaluated against a control before broader rollout. It emphasizes reproducible/automated release mechanics, small deployments, evaluation, and rollback/pause when the candidate is bad. Production exposure exists because pre-production tests cannot reproduce all production behavior.

Primary source: https://sre.google/workbook/canarying-releases/

Google SRE configuration guidance also states that rollback capability reduces incident duration and warns that rollback becomes difficult when configuration is not hermetic because referenced external resources may have changed.

Primary source: https://sre.google/workbook/configuration-design/

### AWS CodeDeploy — rollback is a new deployment
Current AWS CodeDeploy documentation states that rollback redeploys a previously deployed application revision as a **new deployment with a new deployment ID**; it is not restoration of the old deployment event. It also documents that deployment scripts can leave state/content that later deployment mechanics do not automatically reconcile.

Primary source: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html

### AWS Well-Architected — validate outcomes and automate rollback
AWS Well-Architected guidance recommends post-deployment validation and automatic rollback to a previous known-good state when desired outcomes are not achieved. This is operational guidance, not proof that every stateful system is safely reversible by binary rollback alone.

Primary source: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_mit_deploy_risks_auto_testing_and_rollback.html

## SYNTHESIS — change/rollback state vector
Treat deployed state as a vector rather than a single version:

`artifact + configuration + durable data/schema + infrastructure + routing + external dependency state + secrets/credentials + control-plane/operator state`

A rollback changes one or more coordinates. It is not generally an inverse function of the original deployment.

Separate these claims:
- **known-good artifact:** artifact previously satisfied its acceptance evidence in a recorded context;
- **rollback target:** exact artifact/configuration/state combination selected for mitigation;
- **rollback compatibility:** target can operate safely against the state that exists at rollback time;
- **rollback execution:** mitigation action completed;
- **recovery acceptance:** independent health/correctness/data-integrity oracle passes after mitigation;
- **incident root cause:** causal explanation for the original failure; recovery success does not establish it.

Invalid shortcuts:
- `previously known-good artifact => safe against current state`;
- `old source rebuilt => previous artifact restored`;
- `rollback command succeeded => service recovered`;
- `metrics recovered => data integrity recovered`;
- `rollback fixed symptom => release was proven root cause`;
- `deploy succeeded => change is safe`.

## VALIDATION — state compatibility failure
Canonical fixture: `research/systems/fixtures/S006_rollback_state_compatibility.py`

### Test Evidence Contract
- **CLAIM:** code/artifact-only rollback can fail when a newer release has already advanced durable state beyond the old artifact's read contract; restoring a separately validated compatible state allows the bounded old artifact to run.
- **SPEC/PROPERTY:** a rollback target is acceptable only when the artifact's supported schema range includes the durable state presented to it.
- **TARGET:** deterministic Python model, not a real database, deployment platform or product.
- **INPUT/STATE:** `v1-known-good` supports schema 1; `v2-bad-release` supports schema 2; durable state has already advanced to schema 2 when v2's runtime defect is detected.
- **ORACLE:** `run()` must reject a state schema greater than the artifact's declared supported maximum; healthy recovery requires successful execution with compatible state.
- **ENVIRONMENT:** Python 3.13.5, Linux 6.18.44 x86_64, 2026-09-18.
- **OBSERVATION:** direct v1 rollback against schema 2 raised `v1-known-good cannot read schema 2`; after substituting a modeled separately validated schema-1 snapshot, v1 returned `healthy`; assertions passed.
- **VERDICT:** PASS for the bounded compatibility property and failure case.
- **FAILURE MODEL:** backward-incompatible durable-state evolution followed by binary-only rollback.
- **REPRODUCTION:** run the canonical fixture with Python 3.13.5.
- **EVIDENCE LIMIT:** does not establish safe real database rollback, snapshot consistency, data-loss acceptability, migration reversibility, distributed recovery, mobile/store rollback, CI/CD behavior or production incident handling.

Observed output:
```text
naive rollback: v1-known-good cannot read schema 2
coordinated rollback: healthy
PASS
```

## DEBUG / ROOT CAUSE
The old artifact did not become defective. The environment/state contract changed. The naive rollback changes only the artifact coordinate while leaving durable state at schema 2, so the old artifact's precondition is false. The alternative restores compatibility before traffic/acceptance. This isolates the failure mechanism to rollback-state incompatibility in the model.

The alternative is deliberately **not** generalized into “always reverse the database.” Real rollback may require backward-compatible expand/contract migrations, forward fixes, feature disablement, traffic switching, restore from an independently accepted backup, or another recovery path. Data loss and consistency constraints can make state reversal unacceptable.

## RELEASE / INCIDENT GOVERNANCE MODEL
A production change record should make these independently answerable:
1. what exact artifact/configuration/infrastructure/data change was intended;
2. what pre-deployment acceptance evidence applied to it;
3. what blast-radius control or staged rollout was used;
4. what signals and thresholds decide continue/pause/rollback;
5. what exact rollback/roll-forward target is available and whether current state is compatible;
6. what recovery oracle proves service/data correctness after mitigation;
7. what evidence is preserved for later root-cause analysis.

`Mitigate first` and `prove root cause` are compatible but distinct incident goals. Rolling back a suspected change can be a bounded causal intervention, but confounding concurrent changes and state transitions can prevent it from proving causality.

## ALTERNATIVES / trade-offs
- **Binary-only rollback:** fast when state/config contracts remain backward compatible; unsafe as a universal assumption.
- **Blue/green or traffic reversal:** can make code/config routing reversal fast while both environments exist; shared mutable data/external state can still block semantic rollback.
- **Feature disablement:** can reduce blast radius without replacing the artifact; only works when the risky behavior is truly isolated and the flag/control path remains available.
- **Roll forward:** often preferable when data/state cannot safely move backward, but requires confidence in diagnosis/fix and consumes incident time.
- **Snapshot restore:** can restore compatible state but introduces recovery-point/data-loss/consistency questions owned by Data D005/D003.
- **Backward-compatible schema evolution:** increases rollback window at design cost; exact compatibility must be validated, not assumed.

## ENGINEERING JUDGMENT
For stateful products, rollback readiness should be evaluated before deployment as a compatibility/recovery property, not written as an emergency command after failure. Preserve exact previously accepted artifact identity from S005 and explicitly evaluate whether configuration, data/schema and external dependencies remain within its operating contract.

## RELATED DOMAIN CHECK
- **Foundations:** F001 process/artifact boundaries and F006 external-system ambiguity support the distinction between command completion and remote/recovered state. Direct Dart/Flutter execution remains unavailable as rechecked 2026-09-18.
- **Architecture:** A003 compatibility contracts define whether old/new components can coexist; A005 observer sets prevent calling externally visible migration/release changes internal refactoring.
- **Mobile:** app-store distribution can constrain downgrade/rollback mechanics; no mobile rollback claim is made without platform evidence.
- **Data:** D003 schema evolution/rollback and D005 recovery acceptance are direct dependencies. Data rollback can be lossy or invalid even when binary rollback is easy.
- **Quality:** Q006 fault injection/recovery requires an independent post-recovery semantic oracle; rollback command success is not the oracle.
- **Systems:** S001/S004/S005 provide artifact/provenance/build/release identity prerequisites.
- **Design Studio:** considered; user-facing recovery semantics may require handoff in a product incident, but no design contract is changed here.
- **Web Manager:** considered; staged web/PWA deployment/cache rollback can require separate transfer validation; no web operational decision is changed here.
- **Marketing Manager:** considered; no marketing canonical decision is changed here.
- **Product source/ref:** no product audit performed; no MintTap/LogMate production behavior is claimed.

## HANDOFFS
### TO Data
Treat rollback target compatibility as a consumer of D003 schema-compatibility and D005 restore-acceptance evidence. Before release, state whether an old artifact can read/write post-change state and whether any restore path has acceptable RPO/data-loss semantics.

### TO Quality
Post-rollback acceptance must exercise semantic health/data-integrity properties, not merely deployment status or process liveness. Preserve the exact injected failure/change and artifact/state identities.

### TO Mobile / Web
Transfer-test actual downgrade/update/cache/service-worker/store behavior on exact delivery platforms before claiming rollback equivalence. Platform distribution may make server-style rollback mechanics unavailable.

## OPEN / VALIDATION / CHANGE WATCH
- **OPEN / VALIDATION:** real staged deployment, automatic rollback trigger, production-like recovery acceptance and incident evidence preservation.
- **OPEN:** expand/contract migration rollback window, feature-flag failure modes, configuration rollback, external dependency drift and partial-fleet rollback.
- **OPEN:** real artifact reuse versus rebuild comparison under a canonical CI pipeline.
- **TRANSFER VALIDATION:** Flutter/mobile store delivery, Firebase/schema changes and PWA/service-worker/cache rollback require exact platform/product evidence.
- **CHANGE WATCH:** deployment-platform rollback semantics and app-store/browser delivery policies are service/version sensitive.

## Gate effect
S006 now has SOURCE → MODEL → EXECUTABLE FAILURE/ALTERNATIVE evidence at a bounded comparison-runtime level. S001-S006 all have at least first professional Foundation evidence, but Systems Stage 1 remains **NOT PASS**: real signing/build/deployment, rollback/recovery, platform transfer and production evidence remain open.
