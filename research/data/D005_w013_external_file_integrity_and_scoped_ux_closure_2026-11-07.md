# D005 — W013 external-file integrity and scoped File UX closure: provenance and acceptance boundaries

**Evidence date:** 2026-11-07 Asia/Seoul. **Status:** SOURCE / PRODUCT-EXECUTED VALIDATION (reported, not rerun in Studio) / USER-REPORTED PHYSICAL TRANSFER / SYNTHESIS / OPEN. **Studio execution:** no new Dart/Flutter/device tests. **Authority:** independent engineering advisory; no product approval or policy change.

## Source identity and current branch audit

- Product: `yhappcom/logmate → verify/w013-target-file-resume-20261107@9da013466705e18cb23d27f5011fb2cc15bc3393 → pubspec 1.0.0+1 → 2026-11-07`. PR46 Draft/Open/unmerged, base PR45 `55a1ff894fcaa9e66765fcfe690c576dda61df98`; main separately `f4bcd2f7b7e77039e29653baa1cc93797673885b`. 61 remote branches and 12 open PRs enumerated. Production/deployed ref unknown.
- Executable Web/File UX source: **`bd31058569e54f838a667c57865554aed1b3547e`** (served `main.dart.js` SHA-256 `90ec7b525a07c7a6822984314489381be2a56d15b88a713ebfae7a75b5591d66`). Native installed synthetic artifact: **`f484e0824c809fb7e8267bfb90bf8391bc534cb7`**. The PR46 latest documentation HEAD is neither executed build; no production release is identified.
- Canonical product evidence: [independent copied-file readback and B1 IO run](https://github.com/yhappcom/logmate/blob/9da013466705e18cb23d27f5011fb2cc15bc3393/docs/evidence/w013-ipad-saved-file-2026-11-07.md); [File UX round and actual PR diff audit](https://github.com/yhappcom/logmate/blob/9da013466705e18cb23d27f5011fb2cc15bc3393/docs/evidence/w013-file-ux-wrap-2026-11-07.md); [scoped machine-readable observations](https://github.com/yhappcom/logmate/tree/9da013466705e18cb23d27f5011fb2cc15bc3393/docs/evidence/w013-file-ux-wrap-2026-11-07).

## Materially new evidence versus prior D005 transfer

Earlier D005 physical-Safari transfer at `0073619...` explicitly marked external saved-file independent bytes/hash **NOT VERIFIED** and Files Provider explicit Cancel **NOT RUN**. New product evidence changes those two precise classifications, **without** changing the installed/offline PWA or Production Activation gate:

1. **External artifact identity — PRODUCT-EXECUTED, host side.** A user-transferred synthetic `.lbk` (13,276 bytes) was independently read and SHA-256 hashed as `5aa9cb8a06142612258eb45ed0f2fb0b26d1f7c83a320d4d332d797cf68648a5`; the user-reported Safari Expected SHA equals all 64 hex digits. Strict UTF-8 roundtrip, v2 preliminary decode, existing full B1/37-store validation, temporary Sembast candidate reopen, locked synthetic Owner and new Destination Replica checks all passed in a **single product-side Dart CLI run (exit 0)**. Before/after file length, hash, mtime and mode matched, candidate temp root was empty. The **device-origin and displayed Expected SHA remain user reports**; independently measured host bytes are stronger evidence but not a captured OS browser-save trace or power-loss durability proof.
2. **Physical iPad Files Cancel/Retry and Review expiry — USER-REPORTED.** On iPad9/iPadOS18.6.2 Safari ordinary tab, user reported both specifically requested scenarios passed: explicit Files Provider Cancel/X followed by reselect→B1/Staging; Review acknowledgement followed by Home→same tab showing expired review and disabled Activation. Unlike prior source-menu dismissal, this report addresses actual Provider cancellation. No independent screen recording or callback trace was captured.
3. **Native iPhone Simulator — bounded observed UI.** Existing installed synthetic app opened real Files panel, produced visible `File selection cancelled.`, re-enabled Choose, and reopened Files on retry; disabled Activate remained visible. Files internal AX and coordinate input were inaccessible, so this run did **not** select a file or rerun B1/review. Historical native B1 success belongs to the older run, not this one.
4. **iPad Simulator Safari — bounded observed UI.** Correct-source page→Check Backup→photo/camera/Choose File→actual Files panel was reached with normal keyboard input. Files contents/Cancel/B1/review were **not verified** in Simulator. A concurrent UI change was not attributed to the product.
5. **PR46 audit and provenance.** Product-side 96-file remote/local diff and reporter-hash audit found executable changes limited to file-picker Reader, Web option helper/native stub, browser regression test and locked dependency declarations; no new full Flutter/Chrome/CI run. Historic 41 Chrome and 1255 Flutter PASS/1 SKIP apply to their frozen source only. Source audit found no *new verified* Critical/High/Medium defect in its scope, not an independent security/release approval.

## Acceptance matrix: do not collapse distinct gates

| Claim | Current evidence | Verdict |
| --- | --- | --- |
| Synthetic physical Safari File UX, specified Cancel/Retry/B1/Staging/Review expiry | User reported two requested scenarios pass at frozen source | **PASS — user-reported, scoped** |
| Synthetic external file bytes and B1 host validation | Product-side independently measured 13,276 bytes, SHA, exit 0, isolated candidate | **PASS — product-executed host IO, scoped** |
| Native Simulator cancel/retry-open | Visible real app UI outcome, no file-selection automation | **PASS — bounded cancel/retry only** |
| iPad Simulator actual file select/B1/review | No usable supported Files input channel | **NOT VERIFIED** |
| Safari normal-tab export → persistent user Files custody across restarts | One user-transferred artifact measured, no controlled browser-save/restart/provider persistence trace | **PARTIAL; durability and generality OPEN** |
| Installed/offline/managed EFB PWA | Normal Safari tab, memory source, no owned worker | **NOT RUN** |
| Actual owner-authenticated persistent logbook Restore Activation and writer fence | Synthetic Owner and candidate; Activation disabled | **HOLD / NOT IMPLEMENTED** |
| S007 37-store terminal deletion and UID A→B reopen | No new file-backed deletion run | **OPEN** |

**Discriminator:** product-side copied-file IO/B1 is a genuinely stronger evidence class than the earlier user-reported B1 UI alone. However, the full chain is **not** one instrumented device-to-server-to-active-ledger E2E; it combines distinct user/device and host observations. “Executed File UX round PASS” is defensible only for the enumerated synthetic cases, not W013 completion, managed EFB PWA, or release acceptance.

## Next bounded validation / engineering judgment

- Preserve this scoped File UX closure. Do **not** repeat the same synthetic B1/Cancel tests simply to produce another document.
- P0 remains independent S007 terminal wipe/phase/old-writer/UID A→B file-backed canary at exact authorized product source; Studio-only fixture if feasible, otherwise explicit LogMate/Codex Work handoff. Do not infer a new deletion PASS from B1's 37-store backup validation.
- For D005's next *different* boundary, require installed/offline managed-EFB PWA file custody after browser/profile restart, or separately authorized Supported Writer transaction fence and interrupted Activation; no silent change to owner-approved policy.
- D006 remote onboarding projection restore-value and receipt/cursor/idempotency contract remain distinct OPEN questions. Successful synthetic File UX does not establish onboarding completion or operational telemetry truth.

## RELATED DOMAIN CHECK

- **Foundations:** bounded Dart/Flutter runtime exists; avoid outdated unavailable-runtime assertion.
- **Architecture:** ephemeral Review acknowledgement and candidate reopen do not imply committed owner ledger transition.
- **Mobile/Web:** physical Safari normal tab is not installed/offline managed PWA; simulator AX restrictions are tool limitations, not a diagnosed platform defect.
- **Data:** byte SHA, B1 digest, candidate reopen, browser file custody and active ledger replace are separate oracles.
- **Quality:** product-run exit 0, user-report and transcribed CUA observations have different independence and reproducibility.
- **Systems:** deletion authority and stale-writer barriers are not exercised by synthetic Restore.
- **Design/Marketing:** disabled Activate and review flow are functional observations, not final Figma or public production claim.

## HANDOFFS

- **LogMate (READ ONLY):** keep W013 IN PROGRESS/CONDITIONAL, PR46 Draft; no Activation or Supported Writer authorization inferred. Preserve exact test SHA and existing test reports; next implementation requires separately authorized owner Session/Facade + transaction fence + command outcome/retry recovery.
- **Web Manager:** accept scoped physical Safari File UX progress and host-verified copied file; retain installed/offline/managed-EFB release HOLD.
- **Marketing Manager:** do not advertise production backup restore, managed PWA, or authenticated Sync based on synthetic tests.
- **Studio Systems/Quality:** retain S007 deletion negative-oracle priority; no Stage-1 PASS.
