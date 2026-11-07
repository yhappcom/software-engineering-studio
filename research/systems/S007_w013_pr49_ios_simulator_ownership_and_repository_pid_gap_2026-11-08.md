# S007 × W013 — PR49 iOS Simulator ownership transfer and remaining two-Repository gate

**Evidence date:** 2026-11-08 Asia/Seoul. **Lead:** Systems (S007), supporting Mobile/Data/Quality. **Classification:** SOURCE / PRODUCT-REPORTED EXECUTABLE VALIDATION / SYNTHESIS / CONTRADICTION RESOLVED IN BOUNDED TARGET / TRANSFER VALIDATION OPEN. No Studio-run Dart/Flutter test, no product mutation or CI dispatch.

## Exact identity and stack

- Studio canonical predecessor: `yhappcom/software-engineering-studio → main@b4fb9f44c2c12d90a121d51bcb502c5ae27d40f → 2026-11-08`.
- Product baseline: `yhappcom/logmate → main@f4bcd2f7b7e77039e29653baa1cc93797673885b → declared 1.0.0+1 → 2026-11-08`. This is **not** assumed production.
- New unmerged Draft [PR49](https://github.com/yhappcom/logmate/pull/49): `feat/w013-mobile-ownership-20261108@dd221883edcb01bc879be8fe0f1f1a33d353e477 → 1.0.0+1 → 2026-11-08`, stacked on PR48 `afbdbf037b637bb924ffc9bea173e87385dd398f` → PR47 `e035d70dc8c51941a135c2f174659f280e3766d1`. Earlier product/doc stack and separate verification chain remain unmerged; no automatic merge inference.
- Executable Source **ee5b03629ce804ae31f97a2baa7f89d61fa795a4**; independent Native Host/SDK probe Source **fa2d113a00b1007463672feff928605e496fddbb**; later changes reported documentation/evidence only. The audited native ownership source blob is `ac61619c7aa3d9859fce149760006576902c602e`. Source evidence: [PR49 integrated report](https://github.com/yhappcom/logmate/blob/dd221883edcb01bc879be8fe0f1f1a33d353e477/docs/evidence/w013-mobile-ownership-2026-11-08.md).
- Current branch enumeration returned **64 branch names**; PR search surfaced new #49 on top of #48 (prior 14 open; current full open-PR count not independently confirmed in this run). No branch or PR mutation.

## New independent evidence and precise oracle

**SOURCE:** PR49 adds SDK-separated Darwin64 and Android ARM64 `stat`/flag ABI profiles, compiled header assertions, explicit synthetic-only mobile probe gating and an acceptance-only compiled iOS Simulator check. The actual `openExperimentalOwnedNativeDatabase` source acquires directory ownership **before** calling the Sembast DB factory, retains it through actual close, and deliberately holds ownership on unknown unreturned Open or uncertain Close. Default Legacy opener and ordinary mobile production calls remain unenrolled.

**PRODUCT-REPORTED VALIDATION, not Studio execution:** At final Source: focused Flutter **825 PASS/1 SKIP**, full **1360 PASS/1 SKIP**, actual Chrome **48 PASS**, Web/Android/iOS builds PASS. iOS26.1 ARM64 Simulator executes **nine in-app Session/resource scenarios** and **eight bounded process-recovery groups with 15 distinct app PIDs**; original Operation/Revision/UTC/digests and exact retry/no-duplicate checks are reported. Independent C PID and actual Dart app PID contend on the same directory FD in both directions. With C holding ownership, a fresh Dart app PID rejects before Sembast DB factory (**0 calls**); after actual Close the peer can acquire. The initial iOS `Platform.environment`-based attempt failed; acceptance-only compiled Simulator identity replaced it. Android NDK28.2/API24 ARM64 compile/ABI assertions PASS, including correction of an initially wrong Open constant. The macOS Host regression remains 9 groups/41 PIDs at its separate identical executable chain. These suites overlap; counts must not be summed.

**ORACLE LIMIT:** C does not execute the second Repository's Seal/Epoch/History commands. The important **two independent mobile Repository PID** contention→seal→old-writer rejection→fresh third-Repository persisted-state oracle is **NOT RUN**. iOS Simulator SIGKILL is neither physical-device/power-loss nor iOS OS-restart durability. Android ARM64 runtime/device/PID/crash is **NOT RUN**, even though an APK was built; physical iOS and default production enrollment are not validated. Kernel advisory ownership cannot compel an old/raw/Legacy binary to cooperate.

## S007 and product-policy transfer

PR49 leaves existing Owner/Deletion/read authorization, 31 repository fences, B1 registry, schema and default Legacy path unchanged. The S007 original **29 explicit terminal drops versus 37 persisted definitions**, direct phase admission and deletion-intent/LocalOwnerAccess.lock concerns therefore remain **OPEN**, pending fresh exact deletion-function diff and executable file-backed A-delete→B reopen. This is not a demonstrated A→B leak.

The owner-approved **Automatic + Manual Delta Sync**, conditional native automatic Backup and fourth onboarding Restore option are policy only, not activation or production implementation. The exact approved Sync contract explicitly requires authenticated Receipt/Cursor/Owner/Generation and idempotent convergence; F1 local persistence is not live Sync. A Simulator lock PASS cannot authorize restore, sync, account deletion or a production namespace.

**ENGINEERING JUDGMENT / ALTERNATIVES:** Keep isolated opt-in probing while deciding a durable production namespace and old-client/downgrade/fork migration separately. In-place adoption of advisory locking leaves old raw writers; new namespace may isolate cooperating writers but introduces continuity/fork/migration risk. No new policy is approved here.

## RELATED DOMAIN CHECK / HANDOFFS

- **Foundations:** file-description lock lifetime, independent process caches, FFI ABI and process death; F001 Dart/Flutter bounded execution already exists.
- **Architecture:** shared Session/Resource core; admission must precede DB open, not merely transaction checks; Legacy bypass persists.
- **Mobile:** iOS Simulator runtime is a meaningful transfer beyond Host; physical iOS, Android runtime and managed PWA are not covered.
- **Data:** 37-store B1 inventory does not establish S007 terminal erasure; D006 Receipt/Cursor and Generation are separate.
- **Quality:** use third-process persisted-state oracle, independently started Repository PIDs, negative cases, and source-specific CI/artifact provenance. Simulator and build PASS have separate oracles.
- **Systems:** S007 remains OPEN; PR49 only advances opt-in mobile ownership feasibility. No claim of release or security barrier against raw writers.
- **Design Studio / Web Manager / Marketing Manager:** no new visual, website or marketing authority; do not advertise supported restore/sync or EFB offline guarantees from this experiment.
- **LogMate handoff (approval required):** owner/Codex Work must explicitly authorize any product-run S007 deletion canary; seed all 37 stores, exercise intent/phase negatives, supported and raw old writers, interruption/concurrent driver, terminal wipe, fresh raw C inspection and B reopen. W013 team needs two Repository PIDs on mobile, authorized synthetic Android runtime, physical device/OS interruption, old-client/downgrade and stable namespace decisions before enrollment.

**GATES:** iOS Simulator synthetic opt-in ownership **bounded PASS (product-reported)**; independent two-Repository mobile Gate **OPEN**; Android runtime **NOT RUN**; Supported Writer **OPEN/BLOCKED**; Restore Activation **HOLD**; S007 account deletion/37-store A→B **OPEN**. No Studio-run tests, CI or production/release acceptance.

**CHANGE WATCH:** [Apple flock](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/flock.2.html), [Android bionic sys/file.h](https://android.googlesource.com/platform/bionic/+/refs/heads/main/libc/include/sys/file.h), [Android NDK ABI](https://developer.android.com/ndk/guides/abis). Platform ABI conclusions are scoped to pinned SDK assertions and reported simulator, not generalized from documentation.
