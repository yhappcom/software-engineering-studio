# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-23

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome + bounded macOS Safari runtime transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 permission/FGS + bounded Keystore replication; M006 Chromium PWA + macOS Safari runtime + bounded Safari SW registration/update/restart transfer + same-session origin-down offline |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q006 complete selected-pattern workflow inventory + natural false-green repairs/regressions |
| Systems | Stage 1 IN STUDY — S004 product build provenance; S005 generic offline attestation; S007 LogMate account-required Auth/session/onboarding foundations with product-canonical update and runtime validation OPEN |

No specialist has passed Foundation.

## Meaningful new evidence
### Q006 — repository semantic CI audit now found a second natural false-green class
The checkout-local inventory at exact head `d573b47f05a1d5f65daea94d4133dcc221973d2a`, run `35837301494`, directly enumerated 29 workflow files and 131 selected lexical risk hits. This is a complete inventory for the selected patterns at that ref, not a semantic-correctness PASS.

Semantic review found a genuine defect in `.github/workflows/s005-attestation-verification-boundary.yml`: positive attestation query/exact-verification steps used `continue-on-error`, but the aggregate oracle asserted only the two negative controls. A positive failure could therefore be recorded yet omitted from the job verdict.

Commit `6216003dc4d42c1ea2156500bcc1df1d404c045d` repaired the aggregate predicate to require all four positive/negative outcomes. Exact repaired run `35843352058`, job `107123462773`, completed failure specifically at the final aggregate-verdict step after the diagnostic checks ran. **VALIDATION:** the repaired workflow now fails closed when a required positive check fails instead of converting that condition into a green job. The separate historical-attestation availability cause remains OPEN.

Canonical: `research/quality/Q006_complete_workflow_verdict_risk_inventory.md`.

### M006 / Q006 — retained Safari lifecycle transfer
Exact repaired head `54bbd5283920aa3d82057cc2da8a14b0db4bacbf`, run `35810765603`, retains bounded Safari registration/control/update/restart TRANSFER VALIDATION after the historical zero-byte false-green and two navigation-lifetime oracle defects. Fresh-WebDriver origin-down cold start remains a separate CONTRADICTION.

### S005 — retained generic offline attestation boundary
Generic fresh-attestation offline verification remains bounded PASS at exact repaired head `c1ca5a8ae09717fc794b7e064358938e346b56cb`, run `35826855911`. This does not resolve the older historical-subject availability contradiction and does not constitute exact-product release provenance.

## Current Balance Loop
Live LogMate onboarding/Auth work now has the highest immediate product leverage and security/state-model risk. Continue S007 as one coherent block while the owner is finalizing Welcome/onboarding: account-required startup, restored-session routing, provider-neutral Google/Apple/email identity, collision/link/unlink/reauth/deletion boundaries, and executable failure-first startup tests. Q006 remains professionally incomplete and should resume after the live Auth/onboarding handoff reaches a stable implementation contract or if S007 hits an external blocker.

Do not regress to the stale F001 prompt blocker; direct Dart JIT/AOT and bounded Flutter Chrome/Safari runtime evidence already exist.

## CHANGE WATCH / OPEN
- Q006 repository-wide semantic audit remains OPEN; complete selected-pattern inventory does not itself prove semantic correctness.
- Q006 non-Bash shell/platform and production release-gate transfer remain OPEN.
- M006 ordinary Safari relaunch/profile, installed PWA and fresh-SafariDriver origin-down cold-start mechanism remain OPEN.
- M003 physical Android/OEM/other API REPLICATION remains OPEN.
- Physical Android/iOS and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- S005 historical attestation availability cause remains OPEN; exact-product/release provenance remains OPEN.
- Product/default branch is never assumed production without evidence.
- S007 LogMate exact ref `e79f97c...` still contradicts the newly stated account-required startup direction; product-canonical update is OPEN.
- Firebase password-policy configuration and Google/Apple provider operational setup/cross-surface validation are OPEN.

## Evidence rule
No PASS from reading or workflow-green alone. Preserve exact claim/oracle/environment boundaries, subprocess verdict propagation, lifecycle-valid semantic oracles at every navigation boundary, and run-bound semantic evidence; never infer unexecuted evidence.
