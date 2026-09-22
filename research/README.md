# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/`, `research/architecture/`, `research/mobile/`, `research/data/`, `research/quality/`, and `research/systems/`.

## Current studies

### Foundations
- `F001` — direct Dart JIT/AOT, Flutter host→Chrome bounded transfer validated; native/Safari/PWA/product/release transfer OPEN.
- `F002`–`F005` — bounded direct evidence retained.
- `F006` — Dart/Linux loopback professional boundary closed with root-cause/fix/regression; cross-platform/native/product transfer OPEN.

### Architecture
- `A001`–`A003` — substantial Foundation blocks complete.
- `A005` — repeated-change evidence + natural exact-ref LogMate evolution transfer.
- `A006` — executable governance + natural LogMate decision-state transfer; natural ADR lifecycle OPEN.

### Mobile
- `M001` — bounded Android Emulator application transfer validated; physical Android/iOS/product/release OPEN.
- `M002` — controlled Android force-stop + app-specific persistent-file recovery and ordinary HOME background/resume validated; system kill/physical durability/iOS/product remain OPEN.
- `M003` — runtime dangerous-permission shell grant/revoke transfer validated. Android Keystore process/tamper semantics have bounded REPLICATION at API-35 emulator scope: initial complete PASS at exact head `0ea436129fa150b578c777abf1ac6a6500b84a4e`, run `35538756528`, job `106152447185`, followed by intervening first-launch-adjacent failures, then second complete semantic execution at exact head `8163960e333751df91f4dc639c59590f23eea1e8`, run `35557564657`, job `106204067727`; intermittent first-launch ROOT CAUSE remains OPEN. User-driven permission-dialog transfer has bounded TRANSFER VALIDATION at exact head `6fda0223249e723f2b9ee636a7329a97ec64b697`, run `35589277729`, job `106299744861`, Flutter 3.47.5 + API-35 x86_64 Pixel 6 emulator. Repeated-denial/`USER_FIXED` lifecycle has bounded TRANSFER VALIDATION at exact head `5c088398f9f527b96b0da926b26e5aa77d9de000`, run `35619492437`, job `106398675688`. One-time ordinary-background expiry has bounded TRANSFER VALIDATION at exact head `ae5597cc15fca07fcc63688a91f1cf8da9ac15f4`, run `35662745671`, artifact `10667827225`: grant remained through 55.4s after HOME and was revoked at 60.4s, followed by re-requestability; 60.4s is an observation, not a portable timeout contract. `M003_one_time_permission_foreground_service_discriminator.md` now specifies the materially different foreground-service causal branch; executable validation is pending. Independent physical/OEM/other-API replication, auto-reset/hibernation, iOS/product/production remain OPEN. Canonical includes `research/mobile/M003_android_keystore_secure_storage_transfer.md`, `research/mobile/M003_first_launch_observation_isolation.md`, `research/mobile/M003_keystore_semantic_first_launch_instrumentation.md`, `research/mobile/M003_android_user_permission_dialog_transfer.md`, `research/mobile/M003_android_repeated_denial_user_fixed_lifecycle.md`, `research/mobile/M003_one_time_permission_expiry_background_boundary.md`, and `research/mobile/M003_one_time_permission_foreground_service_discriminator.md`.
- `M004`–`M005` — professional/model evidence retained; broader physical/native platform execution OPEN.
- `M006` — Chromium offline/restart/update/cold-start evidence; Safari/iPadOS/EFB, physical network, Flutter/LogMate artifact and production OPEN.

### Data
- `D001`–`D004` — Foundation executable/professional evidence.
- `D005` — recovery/storage/WAL/backup interruption evidence; physical power/mobile durability OPEN.
- `D006` — sync/TCP/link interruption/LogMate protocol transfer; actual product persistence/Sync OPEN.

### Quality
- `Q001`–`Q005` — professional Foundation boundaries; Q004 mutation/search evidence.
- `Q006` — process crash/restart + persistent-state oracle discrimination; mobile/backend/production OPEN.

### Systems
- `S001`–`S003` — Foundation executable/professional evidence.
- `S004` — exact product baseline/lock/build-path transfer; canonical source build/artifact identity remains dependent on source acquisition.
- `S005` — release identity + hosted attestation evidence; verifier contradiction retained.
- `S006` — rollback/change-safety + directory-sync publication failure evidence; hard-power-loss transfer OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. Default branch is never assumed production without evidence.