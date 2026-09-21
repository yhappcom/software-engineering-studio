# Software Engineering Studio Global Status

Operating state: **ACTIVE — FOUNDATION STUDY UNDERWAY**  
Governance sync: 2026-09-22

## Specialist map
| Specialist | Current state |
| --- | --- |
| Foundations | Stage 1 IN STUDY — F001 direct Dart JIT/AOT + Flutter host→Chrome transfer; F006 bounded root-cause/fix/regression chain CLOSED |
| Architecture | Stage 1 IN STUDY — A001-A003 substantial; A005 natural LogMate evolution transfer; A006 governance + product decision-state transfer |
| Mobile | Stage 1 IN STUDY — M001 Android Emulator; M002 process/file + HOME lifecycle; M003 user-dialog + repeated-denial/USER_FIXED bounded TRANSFER VALIDATION + bounded Keystore semantic REPLICATION; M006 Chromium lifecycle |
| Data | Stage 1 IN STUDY — D001-D006 initiated; D005 real rollback/storage/WAL/backup interruption evidence |
| Quality | Stage 1 IN STUDY — Q001-Q006 professional boundaries; Q004 mutation/search; Q006 crash recovery-oracle transfer |
| Systems | Stage 1 IN STUDY — S004 exact product baseline/lock/build-path transfer; hosted source acquisition remains credential-context dependency |

No specialist has passed Foundation.

## Meaningful new evidence
### M003 — repeated-denial / USER_FIXED lifecycle bounded transfer validated
Exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, attempt 1, job `106398675688` completed **success** on Flutter 3.47.5 / Dart 3.13.4 + Android API-35 x86_64 Pixel 6 emulator.

The executable lifecycle observed first user denial with `USER_SET`, a second app-originated request exposing the state-specific Permission Controller `permission_deny_and_dont_ask_again_button`, second denial producing `USER_FIXED`, and a third app-originated request with no Permission Controller denial controls while Flutter callback/UI remained denied. The sequence was produced by actual app/system-dialog interaction rather than shell-manufacturing the permission flags.

The preceding failure chain established a bounded harness root cause: the oracle incorrectly reused the first-denial control identity after the platform had transitioned to a different state-specific second-denial control. Updating only that observation/interaction identity allowed the unchanged application permission sequence to complete.

**TRANSFER VALIDATION:** awarded only for the exact Studio fixture/environment above. This is not independent REPLICATION, physical-device/OEM, other-API, product, release or production evidence.

### M003 — user-driven one-time/fresh-denial transfer retained
Exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861` remains the bounded user-dialog transfer for one-time grant plus independent fresh-install denial. Permission Controller resource identity is a test observation, not a portable product API contract.

## Retained evidence
M001, both bounded M002 transfers, shell-controlled M003 runtime permission transfer, bounded M003 Keystore semantic REPLICATION, M006 Chromium transfer, F006 regression closure, and S004 authorization dependency remain unchanged.

## Current Balance Loop
The repeated-denial professional boundary is complete at bounded API-35 emulator transfer-validation scope; do not repeat the green fixture merely to accumulate runs. Re-rank across tracks. Highest-value next candidates are materially different evidence classes: one-time expiry/background grace or auto-reset/hibernation when trustworthy automation can observe them; physical/native lifecycle/storage/connectivity; Safari/iPadOS/EFB; authorized exact-product runtime/build; physical publication durability; or natural release/ADR evidence.

F001 direct Dart/Flutter is not the historical blocker stated in older prompts: direct Dart JIT/AOT, Flutter framework/test binding, and host→Chrome evidence already exist. Native Android/iOS, Safari/iPadOS/EFB, canonical product and release transfer remain OPEN.

## CHANGE WATCH / OPEN
- M003 repeated-denial independent REPLICATION remains OPEN across physical Android/OEM/other API versions.
- Permission Controller resource IDs and permission-flag diagnostics are implementation/version-sensitive test observations.
- One-time permission expiry/background grace and auto-reset/hibernation OPEN.
- M003 intermittent Keystore first-launch ROOT CAUSE OPEN; semantic REPLICATION closed only at bounded API-35 emulator scope.
- Hardware-backed/StrongBox, user-auth-bound key invalidation, backup/restore, reinstall/key rotation/device migration OPEN.
- Physical Android/iOS, Safari/iPadOS/EFB and canonical product runtime remain OPEN.
- System-initiated process pressure and physical power-loss/storage durability remain OPEN.
- S004 canonical LogMate source build/artifact identity remains dependent on execution-context source authorization.
- Product/default branch is never assumed production without evidence.

## Evidence rule
No PASS from reading alone. Preserve exact claim/oracle/environment boundaries and never infer unexecuted evidence.
