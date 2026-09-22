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
- `M003` — runtime dangerous-permission shell grant/revoke, user-dialog, repeated-denial/`USER_FIXED`, and ordinary one-time expiry have bounded transfer evidence. Android Keystore semantics have bounded REPLICATION at API-35 emulator scope; intermittent first-launch ROOT CAUSE remains OPEN. The one-time CAMERA foreground-service causal path is now closed at bounded transfer scope by exact head `07b389dfbbe3abf9440a00e7f80668a367b556f3`, run `35695122004`, artifact `10680900102`, digest `sha256:fe3ab7cbe28ec5a210c210cb27444d41da349787fe6e46d812451f603447ad0c`: authority/PID/service state survived the 90-second HOME hold while the camera FGS was active; app-owned stop was independently confirmed by UI acknowledgement via `content-desc` and Android `service_active=False`; after HOME without the FGS, authority expired at the observed 60.9s point and a new app-originated request exposed the permission dialog again. Verdict `FGS_HELD_THEN_APP_STOPPED_EXPIRED_AND_REQUESTABLE`. 60.9s is an observation, not a timeout contract; physical/OEM/other-API independent replication remains OPEN. Canonical includes `research/mobile/M003_fgs_discriminator_run4_post_stop_closure.md` plus prior run/failure-isolation notes.
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