# Research Index

Canonical reusable research is organized by specialist ownership: `research/foundations/`, `research/architecture/`, `research/mobile/`, `research/data/`, `research/quality/`, and `research/systems/`.

## Current studies

### Foundations
- `F001` — direct Dart JIT/AOT, Flutter host→Chrome, and bounded macOS Safari runtime transfer validated; native/iOS/iPadOS/product/release transfer OPEN.
- `F002`–`F005` — bounded direct evidence retained.
- `F006` — Dart/Linux loopback professional boundary closed with root-cause/fix/regression; cross-platform/native/product transfer OPEN.

### Architecture
- `A001`–`A003` — substantial Foundation blocks complete.
- `A005` — repeated-change evidence + natural exact-ref LogMate evolution transfer.
- `A006` — executable governance + natural LogMate decision-state transfer; natural ADR lifecycle OPEN.

### Mobile
- `M001` — bounded Android Emulator application transfer validated; physical Android/iOS/product/release OPEN.
- `M002` — controlled Android force-stop + app-specific persistent-file recovery and ordinary HOME background/resume validated; system kill/physical durability/iOS/product remain OPEN.
- `M003` — runtime dangerous-permission shell grant/revoke, user-dialog, repeated-denial/`USER_FIXED`, ordinary one-time expiry and FGS held→app-stop→expiry→requestability have bounded transfer evidence. Android Keystore semantics have bounded REPLICATION at API-35 emulator scope; intermittent first-launch ROOT CAUSE remains OPEN. Physical/OEM/other-API independent replication remains OPEN.
- `M004`–`M005` — professional/model evidence retained; broader physical/native platform execution OPEN.
- `M006` — Chromium offline/restart/update/cold-start evidence plus bounded macOS Safari runtime and Safari service-worker lifecycle **TRANSFER VALIDATION**. Safari origin-down discriminator exact head `91c5374bc7f09c6103c7f216bd7bf1146b78f40d`, run `35780706023`, artifact `10718495328`, digest `sha256:ec95755ab0c98a8b9e8f6ead62bc3d190c3edeedd6e4b0a0f78b6e7d2113c563`: online control/cache and origin-down proof passed; same-session offline navigation reached `M006_APP_READY` with controller=true; fresh SafariDriver session repeatedly returned `Failed to open page`. Same-session origin-down offline fetch/cache is bounded VALIDATION; fresh-WebDriver cold-start is CONTRADICTION, with lower-level implementation ROOT CAUSE OPEN. Ordinary Safari relaunch/profile, iOS/iPadOS/EFB, physical network, LogMate product artifact and production remain OPEN. Canonical includes `research/mobile/M006_safari_offline_cold_start_failure_isolation.md`.

### Data
- `D001`–`D004` — Foundation executable/professional evidence.
- `D005` — recovery/storage/WAL/backup interruption evidence; physical power/mobile durability OPEN.
- `D006` — sync/TCP/link interruption/LogMate protocol transfer; actual product persistence/Sync OPEN.

### Quality
- `Q001`–`Q005` — professional Foundation boundaries; Q004 mutation/search evidence.
- `Q006` — process crash/restart + persistent-state oracle discrimination; CI exit-propagation regression now has natural false-green motivation, failed first discriminator/isolation repair, and hosted Ubuntu/Bash success at exact head `bd763b301752b3adebd36b963c06d064aec94ca8`, run `35792678785`, artifact `10722128536`, digest `sha256:6b8e03ea4f4bd01d10334ddee40065b7fbc6c1acaf4b85cb2719baabfc61f903`. Repository-wide semantic CI audit, non-Bash shell transfer and production release-gate transfer remain OPEN. Canonical: `research/quality/Q006_ci_pipeline_exit_status_oracle_integrity.md`.

### Systems
- `S001`–`S003` — Foundation executable/professional evidence.
- `S004` — exact product baseline/lock/build-path transfer; canonical source build/artifact identity remains dependent on source acquisition.
- `S005` — release identity + hosted attestation evidence; verifier contradiction retained.
- `S006` — rollback/change-safety + directory-sync publication failure evidence; hard-power-loss transfer OPEN.

## Research note minimum contract
A substantial note should contain, as applicable: problem/scope, authoritative sources, mechanism/model, implementation/worked example, executable validation/environment, failure/root cause, alternatives, RELATED DOMAIN CHECK, transfer limits, OPEN/VALIDATION/CHANGE WATCH, and HANDOFFS.

## Product evidence
When a study inspects a real product, record `repository → exact ref/tag/branch/commit → declared version if available → evidence date`. Default branch is never assumed production without evidence.
