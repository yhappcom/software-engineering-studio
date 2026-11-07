# D005 — Physical iPad Safari B1 selection and review: evidence-strength transfer

**Status:** SOURCE / PRODUCT-REPORTED TRANSFER VALIDATION / SYNTHESIS / OPEN. **Evidence date:** 2026-11-07 (Asia/Seoul). **No Studio-run tests or product writes.**

## Exact identity and scope

- Product: `yhappcom/logmate → verify/w013-target-file-resume-20261107@0073619667944f760366e37cc3b38774cb44611d → pubspec 1.0.0+1 → 2026-11-07`; Draft PR #46 open/unmerged, stacked on PR #45 `55a1ff894fcaa9e66765fcfe690c576dda61df98`. Product main separately `f4bcd2f7b7e77039e29653baa1cc93797673885b`. Production/deployed ref unknown.
- Executed **product test source** is older and frozen: `bd31058569e54f838a667c57865554aed1b3547e`, Web `main.dart.js` SHA256 `90ec7b525a07c7a6822984314489381be2a56d15b88a713ebfae7a75b5591d66`. The PR #46 HEAD is **documentation provenance**, not the tested executable SHA.
- Device: user-reported physical iPad 9th generation, iPadOS 18.6.2, **Safari normal tab**, temporary same-Wi-Fi served synthetic memory-source harness. **Not installed PWA, offline, authenticated Firebase owner, persistent ledger, production Restore or Activation**.
- Primary evidence: [first user-reported B1/staging](https://github.com/yhappcom/logmate/blob/0073619667944f760366e37cc3b38774cb44611d/docs/evidence/w013-safari-device-retest-2026-11-07.md), [later menu/reselection/review](https://github.com/yhappcom/logmate/blob/0073619667944f760366e37cc3b38774cb44611d/docs/evidence/w013-safari-review-retry-2026-11-07.md). Both explicitly lack independent agent device screenshot/telemetry in this trial. Product evidence documents, not fresh Studio execution.

## Distinct observed gates and oracles

| Gate | Reported observation | Evidence verdict and limit |
| --- | --- | --- |
| Safari file-source menu and dismissal | Source menu opens; tap outside dismisses; choose button re-enables | **USER-REPORTED PASS** for source-menu dismissal only; not explicit Files Provider Cancel callback |
| Re-selection and internal B1 validation | Selecting the synthetic backup again shows Full B1 validation Passed | **USER-REPORTED PASS** for this exact physical Safari tab/test source |
| Temporary staging reopen | Previous trial explicitly showed Passed | **USER-REPORTED PASS in preceding trial**, not separately reported on later re-selection; do not combine as a single instrumented E2E |
| Review acknowledgement | Checkbox produces screen-only acknowledged text | **USER-REPORTED PASS** for UI state, not durable consent |
| Activation fail-closed | Activate backup remains unavailable before/after acknowledgement | **USER-REPORTED PASS** for disabled UI, **not** Restore Activation success |
| Saved-file independent bytes/hash and source invariance | No physical-iPad independent external readback or before/after source comparison | **NOT VERIFIED** |
| Files Provider explicit Cancel→Retry, background/resume, installed/offline PWA, real Owner/Generation, active ledger replace | Not exercised | **NOT RUN** |

## Cross-evidence correction and why it matters

Earlier Studio D005 evidence ladder classified Safari as download-complete/internal SHA without verified user-accessible Files custody or re-pick. That historical conclusion was valid for its earlier **different** trial, but cannot be carried forward as a blanket claim that *physical Safari file selection/B1 never succeeded*. The later user-reported physical Safari trial reached B1 and temporary staging, and a subsequent report reached review/disabled activation. This **narrows** the file-selection uncertainty, without proving the earlier browser download destination, durable external file custody, provider-wide cancellation, installed PWA, or release Restore. Do not equate selecting an already saved synthetic file with proving the app's own browser download was stored externally.

A second independent provenance boundary: `0073619...` is a documentation-only commit; no new Flutter/Chrome/CI was executed at that HEAD. Previously reported 41 Chrome PASS and 1255 Flutter PASS/1 SKIP apply to the frozen older source and are not rerun counts. User-reported device PASS is not a Studio-executed test and is not independent product-source attestation.

## Next discriminating tests (without touching product in this Studio run)

1. **Provider cancellation:** same device/build, enter Files Provider and explicitly tap **Cancel**, observe callback and button state, then retry. Distinguish this from dismissing Safari's initial source menu.
2. **Custody:** independently capture size/SHA of a *newly browser-downloaded* synthetic file in a user-visible provider destination; terminate/reopen tab and select that same file. Verify byte identity before B1.
3. **Preservation:** compare independent synthetic source before/after a failed/cancelled review and re-selection, not only internal B1 status. Record source and artifact SHA and negative control (tampered file rejection).
4. **Transfer:** installed/offline managed iPad PWA and physical native/Android separately. Production owner, Generation, stale-writer and full Activation require explicit product approval and independent evidence; no surrogate PASS.

**Gate:** D005 bounded Safari file-UX evidence **advanced**, W013 **IN PROGRESS / CONDITIONAL**, production Activation **HOLD**, S007 37-store deletion and owner-A→B file-backed validation **OPEN**. No new product policy or release approval.

## RELATED DOMAIN CHECK

- **Mobile:** Safari normal-tab lifecycle/Provider and installed PWA are different targets; device-specific claims cannot be promoted.
- **Quality:** separate user report, internal B1 oracle, external byte custody, and production source; negative/provider tests remain necessary.
- **Systems:** owner binding, generation and stale writer remain unproven; no S007 change.
- **Architecture:** screen-only acknowledgement is not a durable state transition.
- **Foundations:** bounded Dart/Flutter execution already exists; no stale runtime blocker.

## HANDOFFS

- **LogMate (read-only advisory):** preserve exact tested source SHA and physical-device report; target explicit Provider Cancel and independently verified browser-export→Files→re-pick sequence, then separate installed/offline PWA and Activation approval.
- **Web Manager:** update any historical 'Safari cannot reselect' blanket assertion; retain external custody/managed-EFB release HOLD.
- **Design Studio:** acknowledgement/disabled-action UX evidence is screen-only, not final design approval.
- **Marketing Manager:** do not claim physical iPad production Restore or installed PWA support from synthetic harness.
