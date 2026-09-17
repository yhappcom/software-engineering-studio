# M003 — App Sandbox, Files, Permissions, Secure Storage & Platform APIs

Status: **IN STUDY — first integrated Foundation block with bounded executable classification evidence**  
Evidence date: 2026-09-18

## Problem / scope

Mobile storage correctness is often weakened by collapsing several independent properties into one label such as “private”, “secure”, or “persistent”. This block separates isolation, authorization, purgeability, uninstall behavior, user-visible persistence, cryptographic/data-protection policy, credential storage and platform API semantics.

This is a Foundation study, not a claim about any current product implementation.

## SOURCE

### Android

Current Android Developers storage guidance distinguishes app-specific internal persistent files from cache and external/shared storage. Internal app-specific directories require no storage permission for the app itself; other apps cannot access them through the ordinary app model. App-specific files are removed on uninstall. Internal cache can be removed earlier when storage is constrained. Android documentation therefore does not support treating “inside the sandbox” as either “durable forever” or “survives uninstall”.

Sources checked 2026-09-18:
- Android Developers — Access app-specific files: https://developer.android.com/training/data-storage/app-specific
- Android Developers — Data and file storage overview: https://developer.android.com/training/data-storage
- Android Developers — Minimize permission requests: https://developer.android.com/privacy-and-security/minimize-permission-requests
- Android Developers — Security checklist / best practices: https://developer.android.com/privacy-and-security/security-tips and https://developer.android.com/privacy-and-security/security-best-practices

Android also recommends minimizing permission requests and using system-mediated selectors/APIs where they avoid broad storage authority. Storage permission is therefore an authority decision, not a generic prerequisite for file access.

### Apple platforms

Current Apple file documentation exposes file data-protection classes and explicitly recommends choosing protection according to the sensitivity/access requirements of stored data. `completeFileProtection` makes data accessible only while the device is unlocked; other protection modes trade availability against protection. Apple Keychain accessibility classes likewise encode materially different access/migration semantics. For example, `kSecAttrAccessibleWhenUnlocked` is accessible only while unlocked and can migrate through encrypted backups, whereas `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly` remains available after first unlock until restart but does not migrate to a new device.

Sources checked 2026-09-18:
- Apple Developer — Files and directories: https://developer.apple.com/documentation/technologyoverviews/files-and-directories
- Apple Developer — NSData.WritingOptions / file-protection options: https://developer.apple.com/documentation/foundation/nsdata/writingoptions/nofileprotection
- Apple Developer — kSecAttrAccessibleWhenUnlocked: https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlocked
- Apple Developer — kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly
- Apple Developer — kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: https://developer.apple.com/documentation/security/ksecattraccessiblewhenpasscodesetthisdeviceonly

## SYNTHESIS — storage property vector

Treat a mobile storage choice as a vector, not a single adjective:

`location/namespace × access principals × operation authority × purgeability × uninstall behavior × backup/migration behavior × lock-state availability × confidentiality/integrity protection × sharing/export semantics × recovery role`.

Consequences:

1. **Sandboxed ≠ durable.** A private cache may be sandboxed and still be purgeable.
2. **Persistent file ≠ survives uninstall.** Android app-specific persistent files are removed on uninstall.
3. **No runtime storage permission ≠ globally public.** Android internal app-specific files are accessible to the app without a storage permission precisely because the platform gives the app its own namespace/authority.
4. **Encrypted/protected ≠ secret-management system.** File data protection and Keychain/Keystore-style credential/key storage have different contracts and threat boundaries.
5. **Secure storage ≠ backup policy.** A protection class can intentionally prevent migration to a new device; this can be desirable for a credential and disastrous if mistakenly used as the only copy of user-owned recoverable data.
6. **User-selected shared/exported document ≠ authoritative internal database by default.** Sharing/export and application source-of-truth roles should be specified independently.

## ENGINEERING JUDGMENT

Before selecting an API, classify the data by role:

- authoritative business state;
- reconstructible cache;
- credential/key/token;
- user-owned export/document;
- temporary/staging data;
- recovery/backup artifact.

Then choose platform storage/permission/protection behavior that satisfies that role. Do not choose an API first and infer its semantics afterward.

## EXECUTABLE VALIDATION — bounded classification model

Fixture: `research/mobile/fixtures/M003_storage_property_vector.py`

Environment: Python 3.13.5/Linux, executed 2026-09-18.

Claim: isolation, purgeability, uninstall persistence and credential protection are independent properties and a storage class can satisfy one while failing another.

Oracle: explicit role predicates independent of the candidate classification objects.

Observed: PASS. The model rejects purgeable cache as the only non-reconstructible authoritative record, rejects app-private internal files when “must survive uninstall” is required, and rejects ordinary private files when a credential-protection property is required. It accepts cache only when reconstructible, a modeled shared document for uninstall-surviving user ownership, and a credential-store class for secrets.

### Evidence limit

This fixture is **not Android/iOS execution evidence**. It validates the reasoning model only. It does not prove filesystem permissions, encryption, backup, Keychain, Keystore, process-death, plugin behavior or Flutter API mappings.

## FAILURE MODEL / ROOT-CAUSE BOUNDARY

Representative design failures:

- authoritative record stored only in purgeable cache → disappearance is expected platform behavior, not necessarily corruption;
- only copy of user-owned recovery artifact kept in app-specific storage → uninstall can destroy it;
- broad permission requested merely because file access is needed → authority wider than necessary when app-private or system-mediated access would suffice;
- secret placed in an ordinary private file and described as “secure storage” → sandbox isolation is being substituted for credential/key-management semantics;
- device-only credential accessibility selected for data expected to migrate → security policy conflicts with recovery requirement.

Root cause must still be established on the exact platform/API/configuration. These are failure classes, not product diagnoses.

## ALTERNATIVES / TRADE-OFFS

- app-private persistent file/database: low sharing authority, suitable for app-owned state, but uninstall behavior and backup policy must be explicit;
- cache: appropriate only for reconstructible/dispensable state;
- system document/file picker and shared/user-visible location: useful when the user owns or intentionally exchanges the artifact; broad storage permission should not be assumed;
- Keychain/Keystore-backed credential handling: appropriate for secrets/keys according to required availability/migration policy, but does not replace database durability/backup design;
- additional application-layer encryption: may be warranted for sensitive files but adds key lifecycle/recovery complexity and does not by itself solve authorization, backup or integrity semantics.

## RELATED DOMAIN CHECK

- **Foundations:** F001/F002/F006 checked. File/process boundaries and resource lifetime do not establish platform durability/security.
- **Architecture:** A002 state ownership and A003 contracts apply; storage location is subordinate to explicit ownership/recovery semantics.
- **Mobile:** M001/M002 checked. Lifecycle callback arrival cannot be the persistence guarantee; M003 adds storage/authority axes.
- **Data:** D001/D005 checked. Source-of-truth and backup/restore acceptance are separate from sandbox/security properties.
- **Quality:** Q006 checked. Real transfer needs permission revocation, cache loss, uninstall/reinstall/restore and lock-state failure campaigns with semantic oracles.
- **Systems:** S002 checked. Least privilege and secure-storage threat boundaries are consumed here rather than redefined.
- **Design Studio:** considered; recovery/export UX semantics could constrain storage choice, but no canonical design decision is changed by this Foundation block.
- **Web Manager:** not materially relevant to this native-storage block; PWA/browser storage belongs to M006/web overlap.
- **Marketing Manager:** not materially relevant.
- **Product source/ref:** no product behavior audited in this block; therefore no implementation claim is made.

## OPEN / VALIDATION / CHANGE WATCH

- **OPEN / TRANSFER VALIDATION:** Android emulator/device: internal files vs cache loss, permission denial/revocation, uninstall/reinstall and backup/restore behavior.
- **OPEN / TRANSFER VALIDATION:** iOS simulator/device: container/file protection, Keychain accessibility across lock/reboot and migration/restore scenarios.
- **OPEN:** Flutter/plugin mapping to exact Android/iOS storage APIs and protection classes.
- **OPEN:** hardware-backed key behavior and compromise boundaries belong jointly with S002.
- **CHANGE WATCH:** Android storage/permission/backup policy, Apple Data Protection/Keychain behavior, Flutter/plugin APIs and store/platform policies are version-sensitive.
- Direct Dart/Flutter execution remains blocked in the current environment; do not infer runtime PASS from this Python model.

## HANDOFFS

### Data
Use the storage-property vector when specifying D001/D005 persistence and recovery. “App-private” must not substitute for durability, backup, restore acceptance or uninstall-survival requirements.

### Quality
Future mobile campaigns should inject cache eviction, permission denial/revocation, process death, lock/reboot, uninstall/reinstall and restore boundaries where applicable, then judge independent semantic/recovery oracles.

### Systems
S002 remains canonical for threat model/least privilege/secrets. M003 consumes those principles at mobile platform APIs; platform isolation or encryption must not be promoted into a complete security claim.

### Product teams
Before implementing local storage, classify each data category by authority, purgeability, uninstall, backup/migration, lock-state availability, sharing/export and recovery role. Exact product decisions remain in product repositories.
