# S007 × W013 — PR51 iOS same-PID launch boundary and Native fresh-only adoption proposal

**Date:** 2026-11-08 Asia/Seoul. **Lead:** Systems S007; support: Mobile, Data, Architecture, Quality. **Classification:** SOURCE / PRODUCT-REPORTED EXECUTION / SYNTHESIS / ENGINEERING JUDGMENT / OPEN / DEPENDENCY / CHANGE WATCH. This Studio cycle **read evidence only**; no Studio-run iOS/Android tests, product writes, PR changes, CI dispatch, device access or deployment.

## Source identities and current change

- **Product:** `yhappcom/logmate → docs/w013-ios-boundary-adoption-20261108@62d7295da6b447ba45dd3f0196c81ec449f2cdf9 → pubspec 1.0.0+1 → 2026-11-08`. Draft PR51, base `verify/w013-android-runtime-20261108@c08feb25517c32a6104f4cc1ef49e7a4a9f33ddd` (PR50); 66 branches and 17 open PRs at this audit. `main@f4bcd2f7b7e77039e29653baa1cc93797673885b` is older and not assumed deployed.
- **Driver:** `68bbb302f11f29f1b1259ae4957000f333704785`; source-audit reports exact executed-driver SHA256 `a3631473c90a4afc7a3bd7444a6f96f279e76af563aae6e7fc8a643e426c2de8` matching committed file. The final run was immediately before the commit. **Installed executable:** older `ce81418fe5c962b06e5cd42264ec3d2165794d3d`, matched against 172 artifact files. Submission HEAD is documentation/evidence, **not a new product executable**.
- **Product-authored evidence:** [PR51 evidence](https://github.com/yhappcom/logmate/blob/62d7295da6b447ba45dd3f0196c81ec449f2cdf9/docs/evidence/w013-ios-boundary-adoption-2026-11-08.md), [result](https://github.com/yhappcom/logmate/blob/62d7295da6b447ba45dd3f0196c81ec449f2cdf9/docs/evidence/w013-ios-boundary-adoption-2026-11-08/ios-launch-boundary-final/results.json), [proposed adoption scope](https://github.com/yhappcom/logmate/blob/62d7295da6b447ba45dd3f0196c81ec449f2cdf9/docs/specs/backup-file-flow-spec.md#w013-production-adoption-review-20261108). These links may require access to the private product repository.

## New bounded observation and exact negative boundary

An existing Firebase-free iPhone17/iOS26.1 ARM64 Simulator acceptance bundle was launched twice without terminating the first process. Both `simctl launch` results reported **PID 76822**; the test app remained `LOCKED_BEFORE_FACTORY`, with **0 DB factory calls** and no second Repository process. A prior initial run also reported one PID reused across two launches (PID 76063), but final driver source and checks were changed after that first run. The existing artifact has no app extension or independent Repository actor; its Android-only actor is not an iOS execution proof.

**Observed product claim:** the ordinary second launch reused the first process, so this particular test **cannot** exercise a competing second iOS Sembast Repository. This is a bounded launch-path observation, **not** an iOS lock failure, proof of universal single-process operation, a second-process ownership PASS, or proof that a separate signed test target is impossible.

The iOS **independent Repository/Seal/Epoch/History gate is still NOT RUN**. The 172-file bundle equality is an artifact identity check, not a replacement for the missing test. The installed Simulator entitlement dump had no data; it does not prove production/physical-device signing or App Group support. The result explicitly did not open a DB or test durable ledger state. The product's earlier iOS C-helper and isolate checks remain distinct, narrower evidence.

## Proposal and engineering decision boundary

PR51 adds a **not-yet-approved** Native integration package, without product runtime changes. It proposes an app-private Application Support path `logmate/supported-writer-v1/primary/ledger.db`, default release enrollment **OFF**, and a narrow **fresh-only** integration: neither legacy nor supported DB may already exist, existing Auth/Owner gates must hold, and the selected platform's required runtime gates must be satisfied before any rollout.

Existing legacy-only installations would continue using the old DB without being silently enrolled, moved or deleted. Both legacy and supported paths present, unknown/corrupt supported path, or an old-client downgrade fork would HOLD; neither timestamp, path existence nor a B1 import is an owner/Generation proof. Legacy Pending/History/IDs and provenance must be preserved. No persisted Guard, Selector, Lease, new capability, B1 format, Restore Event or activation authority is introduced in this narrow proposal. The proposal explicitly acknowledges that cross-path existence checks are **not atomic against an uncooperating old binary**. Consequently this integration cannot establish restart-persistent Seal, cross-version fencing, account deletion completeness or Restore Activation.

**Advisory disposition:** a fresh-only integration with release disabled is a bounded way to test the selected Native resource, but it cannot be described as supported production writer protection. The unresolved iOS independent-Repository gate, physical devices, old-client fork safety and any future persistent protocol remain separate explicit approval/validation units. No application-integration approval can be inferred from this Studio note.

## Causal discrimination and next falsifiable test

- **Hypothesis rejected for this artifact:** two ordinary launches of one iOS app bundle yield two independently opened Repositories. Actual observed PID equality and factory0 reject this specific route.
- **Alternative 1:** separately authorized Simulator-only two-VM test host with two independent actual OS processes and one shared canonical directory; require A holds pre-open, B attempts pre-open, B's factory0, A closes/crashes, B retry, epoch/history/third independent read. The host must not impersonate a product extension or production entitlement.
- **Alternative 2:** separately authorized dedicated extension/shared-fixture target with reviewed signing/App Group and artifact provenance; higher integration cost, and no implied production adoption. Apple's [App Extensions](https://developer.apple.com/documentation/technologyoverviews/app-extensions) and [Configuring App Groups](https://developer.apple.com/documentation/xcode/configuring-app-groups) explain separate-process/shared-container capability, not proof that LogMate has it.
- **Release/legacy negative:** initialize fresh supported path, simulate a legacy-only writer creating its old path after the existence check, then verify supported re-entry detects the fork and HOLDS **before** any further ledger factory/write. This is not an atomic prevention proof and must not be promoted to old-client fencing. Add partial-bootstrap, same-path alias, unsupported ABI, wrong UID and downgrade/re-entry negatives. Use synthetic data only, exact target artifact and no existing user DB.

The acceptance oracle must include **two independently identified Repository OS PIDs/VMs, the same canonical directory/file identity, explicit pre-factory refusal, actual persistence/epoch/history read-back and a documented no-bypass limitation**. One PID launched twice, an Isolate, a C helper or a green build is insufficient. A physical target needs its own signing/runtime/storage test.

## RELATED DOMAIN CHECK / HANDOFFS

- **Systems (owner):** keep S007 deletion and W013 activation separate; do not convert PR51's proposal into approval.
- **Mobile:** current iOS Simulator harness cannot provide the two-Repository PID case; test-target/entitlement route requires explicit separate authorization. Android API36 A/B/C product-reported PASS remains bounded to its prior acceptance build.
- **Architecture:** namespace selector and Owner/Generation authority must remain fail-closed; no fallback or in-place silent migration.
- **Data:** no B1/capability/codec or Pending/History change was made; future transfer needs independent snapshot/Owner/Generation provenance and explicit policy.
- **Quality:** source SHA vs installed artifact vs submission HEAD and actual run outcome must be distinct; a negative non-execution boundary is valuable evidence but not acceptance PASS.
- **Foundations:** process vs isolate vs runtime library identity; PID equality cannot exercise interprocess exclusion.
- **Design/Web/Marketing:** no immediate visual, served PWA or marketing contract change from this isolated Native proposal.
- **LogMate owner/Codex:** review/revise the **single proposed fresh-only Native integration package** before code changes; if approving, explicitly preserve disabled release enrollment and outstanding iOS PID/physical/legacy gates. No new Work ID or policy is approved by this handoff.

**OPEN:** iOS independent Repository PID, signed/physical-device acceptance, restart/power-loss, old-client fork atomicity, legacy migration, S007 37-store deletion/A→B, W013 supported writer production enrollment and Restore Activation. **No Stage-1 PASS** and no product modification in this Studio cycle.
