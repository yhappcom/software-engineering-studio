# D005 — iPad Simulator File Provider custody, retry and synthetic snapshot oracle

**Evidence date:** 2026-11-07 Asia/Seoul. **Status:** SOURCE / PRODUCT-EXECUTED SIMULATOR VALIDATION (transferred evidence) / SYNTHESIS / ENGINEERING JUDGMENT / OPEN. **Studio execution:** no new Dart/Flutter/Simulator tests. No product approval or policy change.

## Exact identity and changed evidence

- Studio baseline: `yhappcom/software-engineering-studio → main@86f2d54f7595494b851ce38d6f808ba6595b92ab → 2026-11-07`.
- Product: `yhappcom/logmate → verify/w013-target-file-resume-20261107@aa4faeb4feba23655be79e2d11dc7c6393fec0f7 → pubspec 1.0.0+1 → 2026-11-07`; Draft PR #46, base PR #45 `55a1ff894fcaa9e66765fcfe690c576dda61df98`; `main@f4bcd2f7b7e77039e29653baa1cc93797673885b` separately. 61 branches and 12 open Draft PRs enumerated. Production/deployed ref unknown.
- Product documentation/test-parent `9da013466705e18cb23d27f5011fb2cc15bc3393`; **frozen executable artifact source** `bd31058569e54f838a667c57865554aed1b3547e`; served `main.dart.js` SHA256 `90ec7b525a07c7a6822984314489381be2a56d15b88a713ebfae7a75b5591d66`. The latest commit is evidence/documentation, **not** a newly tested executable.
- Primary product evidence: `docs/evidence/w013-ipad-simulator-reselection-2026-11-07.md` and its manifest, independent File Provider inventory, UI observations, original-download and post-review comparison JSON. Do not merge this with the distinct physical iPad Safari user report or physical-device byte copy.

## New independent discriminators

1. **OS Provider selection and app acceptance:** iPadOS 26.1 Simulator, Safari normal tab; actual Files `On My iPad` renamed synthetic `.lbk` selected through CUA. App UI reported File read, Decode, Full B1 and isolated Staging reopen successful. Review acknowledgment remained screen-only; Activate unavailable. This resolves the earlier *specific Simulator file-selection/reselection* OPEN, not whole platform acceptance.
2. **Lifecycle and negative control:** Home → user-assisted Safari return caused independently observed Review expiry and cleared checkbox/report; Files X yielded explicit `File selection cancelled.` after an intermediate Checking state; retry of the same file again reached B1 and staging PASS. The intermediary Checking state is not proof of synchronous cancellation. The failed agent Safari-raise action is a CUA limitation, not a product resume failure.
3. **External file identity:** renamed Provider file independently read as **13,276 bytes**, SHA256 `826df401fc2e4827749ccd71463e7c44115d67bb09f97cc7a4124959c95a9366`, matching one earlier original Safari internal download. The user moved/renamed the file; this is a custody bridge for this synthetic input, not evidence that every Safari download is automatically visible in Files.
4. **Post-review source oracle:** after selection/review/expiry/cancel/retry, a *new* Safari internal download of **13,276 bytes** matched the same SHA; six existing synthetic downloads and renamed input were unchanged. The evidence supports identical **serialized synthetic memory-source B1 snapshots** before and after the flow. It does **not** prove persistent local database isolation, crash durability, external publication of the *new* download, authenticated owner/Generation, or activation atomicity.
5. **Cause isolation:** original and renamed filenames both end in `.lbk`; file location and filename changed together. Therefore a file-extension/OS-registration explanation for prior failures is **NOT CONFIRMED**. A controlled same-location rename/type experiment would be required before assigning root cause.

## Acceptance ladder and independent oracles

| Gate | Verdict for exact source | Why / limit |
| --- | --- | --- |
| Simulator Provider `.lbk` choose → B1 → isolated reopen | **PASS (transferred product evidence)** | Actual CUA selection and reported UI state; synthetic Harness, not real persistent product |
| Simulator Review expiry / cancel / retry | **PASS (bounded)** | User-assisted return, explicit eventual cancellation, repeated selection; no instant-callback timing claim |
| Original Safari cache ↔ renamed Files Provider byte identity | **PASS (bounded)** | Independent 13,276-byte SHA match; does not prove general download publication |
| Before/after synthetic B1 snapshot equivalence | **PASS (bounded)** | Matching new export hash; not proof all database stores remained untouched |
| New post-flow export published to user-accessible Files | **OPEN** | Only Safari internal Downloads inspected |
| Physical iPad, installed/offline/managed EFB PWA, Android and production owner | **OPEN / separately evidenced** | Simulator cannot transfer those verdicts |
| Restore Activation, writer fence, cross-owner and S007 37-store terminal wipe | **OPEN** | No production ledger replacement or account-deletion canary |

**Failure oracle for next execution:** change only one factor (same file bytes/location but filename, or same filename/type but Provider location) and record both OS picker and app callback, including explicit Cancel and re-entry; independently inspect the newly downloaded output in a user-accessible Files destination. Use a separate persisted test database to compare pre/post **all 37 stores**; the current memory-source export hash cannot establish that claim. Never run destructive A→B or deletion tests on a user DB.

## RELATED DOMAIN CHECK

- **Mobile:** Safari-tab versus installed/offline PWA, Provider location, background/resume and real device separation.
- **Quality:** positive B1 and retry, negative Cancel, source provenance, before/after hash and confounded root-cause hypothesis.
- **Systems:** no inferred owner/Generation authority, S007 terminal deletion and writer-fence remains P0.
- **Architecture:** source memory Harness and isolated IndexedDB candidate are distinct from persistent active-ledger publication.
- **Foundations:** exact bytes and SHA establish equality of two serialized outputs, not equivalence of all underlying mutable states.

## HANDOFFS

- **LogMate/Codex Work (read-only advisory):** preserve current bounded PASS, keep W013 IN PROGRESS / CONDITIONAL, supported Writer §5.4 unapproved and Activation HOLD. If separately authorized, execute controlled Provider-publication and persisted-store oracles on synthetic data.
- **Studio Data / Quality / Mobile:** reuse this evidence rather than repeating Safari CUA checks. Prioritize executable S007 37-store file-backed deletion/old-writer/A→B oracles when a Studio-owned authorized isolated environment exists; otherwise independent prerequisites.
- **Web Manager:** do not convert Simulator Safari-tab evidence to installed managed-EFB PWA retention/recovery PASS.
