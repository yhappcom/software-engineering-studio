# S007 — Provider collision and enumeration-safe recovery contract

Date: 2026-09-24
Owner: Systems, Security, Performance & Delivery
Status: SYNTHESIS / PROJECT TRANSFER — exact LogMate runtime validation OPEN

## Scope and product evidence

Product source inspected: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`; production identity unknown.

The product repository remains authoritative for implemented behavior. Its current startup/auth contract still permits account-free first use, while the newer owner direction requires Firebase-backed first use. The current federated-auth operations document also requires `One account per email address`, Email Enumeration Protection, and typed provider-collision handling without automatic email-based UID merge, but still contains the superseded hard-coded 15-character password rule.

This note narrows one implementation-risk block: what LogMate should do when Google/Apple/email credentials collide with an existing Firebase identity while account enumeration protection is enabled.

## Primary-source findings

### SOURCE — linking preserves Firebase UID only when linking succeeds
Firebase Flutter account-linking documentation states that credentials linked to an existing authenticated Firebase user continue to identify the same Firebase UID. `linkWithCredential()` can fail with `credential-already-in-use` when that credential belongs to another Firebase user.

### SOURCE — Firebase examples do not define LogMate merge authority
Firebase Android/Apple/Web account-linking documentation shows an application-specific data-merge step after signing into the credential-owning account when linking collides. That is an example of what an application *may* do; it does not establish that LogMate should merge owners or ledgers. LogMate's owner invariant is stricter: UID is owner authority and email equality is not merge authority.

### SOURCE — enumeration protection invalidates provider-discovery routing
Current Firebase documentation states that Email Enumeration Protection is enabled by default for projects created after 2023-09-15 and disables `fetchSignInMethodsForEmail()` for identifier-first routing. The current JavaScript API reference is stronger: with protection enabled, `fetchSignInMethodsForEmail()` returns an empty list regardless of the actual methods and is deprecated for security reasons.

Therefore the older Firebase error-handling sample that resolves `account-exists-with-different-credential` by calling `fetchSignInMethodsForEmail()` cannot be LogMate's production recovery algorithm if enumeration protection remains a launch requirement.

## SYNTHESIS — collision is an identity recovery state, not an owner merge state

A provider attempt has three materially different outcomes:

1. **sign-in success** → observe resulting Firebase UID; continue through authoritative startup/owner resolution;
2. **link success while already authenticated** → assert resulting UID equals the pre-link UID; ledger owner remains unchanged;
3. **credential collision / account-exists-with-different-credential** → stop. Do not claim, merge, move, rebind, unlock, or rewrite ledger ownership; do not use email lookup to discover another provider.

The pending provider credential is transient recovery material, not proof that two Firebase users are the same LogMate owner. Email equality, verified email, Apple relay email, display name, or provider profile are insufficient to authorize owner migration.

## PROJECT IMPLEMENTATION CONTRACT for Codex

### Provider-neutral result algebra
Auth adapter should map provider SDK/Firebase exceptions into product-neutral results such as:

- `authenticated(uid)`
- `cancelled`
- `interactionUnavailable`
- `networkOutcomeUnknown`
- `credentialCollision(recoveryHandle?)`
- `reauthenticationRequired`
- `providerUnavailable`
- `configurationFailure`

Do not route UI from provider-specific English exception messages.

### Signed-out collision recovery
When a signed-out Google/Apple sign-in returns an account collision:

- do not call `fetchSignInMethodsForEmail()`;
- do not disclose a provider list derived from account existence;
- preserve no durable owner mutation;
- return to a generic recovery surface that lets the user explicitly choose one of LogMate's supported authentication methods to authenticate the existing Firebase account;
- after successful authentication, re-observe `currentUser.uid` and run normal startup/owner resolution;
- if the product retains a pending credential for later linking, keep it ephemeral, bounded to the recovery transaction, and link it only after the user has authenticated the target Firebase account; before and after linking assert the same UID.

A pending credential must be discarded on cancellation, app/account switch, timeout/expiry, explicit sign-out, deletion start, or any UID change.

### Authenticated link collision
When user UID A is authenticated and attempts to link a credential already owned by Firebase UID B:

- do **not** sign into B as an automatic continuation while A's ledger is open;
- do **not** merge A/B data;
- report a typed collision and leave A's owner/ledger unchanged;
- any later account-switch/recovery must pass through explicit authentication and the ordinary SessionGate owner mismatch rules.

This intentionally narrows Firebase's generic merge example for LogMate. The product's no-email-merge invariant wins.

### Unlink safety consequence
Firebase platform docs warn that signing in again with a provider after it was unlinked can create a new separate Firebase user rather than restore the old link. Therefore unlink must remain guarded by an effective-recovery-method policy and should require explicit warning/reauthentication where appropriate. A successful unlink must be followed by provider-data reobservation; local ledger owner UID must not change.

## Failure-first tests required before product PASS

1. Signed-out Google collision does not mutate owner/setup/local ledger and does not invoke email-method discovery.
2. Signed-out Apple collision has the same provider-neutral semantics.
3. Authenticated UID A linking credential owned by UID B leaves A signed in/ledger unchanged or fails closed; no automatic B merge.
4. Recovery authenticates UID A then pending credential link succeeds: UID before/after link is A.
5. Recovery authenticates UID B while local ledger owner is A: SessionGate returns mismatch; no ledger read/rebind.
6. Pending credential is discarded after cancellation/sign-out/UID change/restart unless a separately justified secure resumable protocol is implemented.
7. Enumeration protection enabled: recovery still works without `fetchSignInMethodsForEmail()`.
8. Provider exception message changes do not alter routing; typed code mapping is the oracle.
9. Unlink then provider sign-in creating/returning a different UID cannot access the prior owner's ledger.
10. Android/iOS/PWA execute equivalent identity invariants despite different provider interaction mechanisms.

Independent oracles should inspect Firebase Auth Emulator/Admin user UID/provider state and LogMate durable owner metadata; UI navigation alone is insufficient.

## RELATED DOMAIN CHECK

- Foundations: identity/reference continuity concepts considered; no new canonical finding required.
- Architecture: UID/owner authority and provider adapter boundaries materially relevant; collision recovery must not cross owner-state boundary implicitly.
- Mobile: provider interaction differs across Android/iOS/PWA; semantic transfer remains OPEN.
- Data: no automatic data merge or owner migration on auth collision; durable ledger mutation must remain zero on collision.
- Quality: exact emulator/product tests and independent UID/owner oracles required.
- Systems: canonical owner for auth/security mechanism; this note persists the reusable contract.
- Design Studio: recovery UI must not disclose inferred provider/account existence; no canonical design file edited.
- Web Manager: not materially relevant to this collision mechanism beyond future account-recovery/deletion web surfaces.
- Marketing Manager: not materially relevant.
- Product ref checked: exact ref above.

## CONTRADICTIONS / CHANGE WATCH

- LogMate `e79f97c...` account-free startup remains contradicted by newer account-required product direction.
- LogMate federated-auth operations hard-coded 15-character rule remains superseded by configured-Firebase-policy authority.
- Firebase Flutter error-handling documentation still contains a `fetchSignInMethodsForEmail()` collision sample, while current enumeration-protection documentation says that method is disabled/returns empty under protection. Treat the latter security behavior as controlling for LogMate architecture; keep this on CHANGE WATCH.
- Firebase platform account-linking pages currently carry a known-issue warning for `linkWithCredential(s)` in some projects. Exact FlutterFire/version/project behavior must be validated before release; do not infer correctness from documentation alone.

## HANDOFFS

### LogMate / Codex
Implement collision as typed recovery, not merge. Never use email equality or `fetchSignInMethodsForEmail()` as owner/provider routing authority. Assert UID continuity around successful link and zero owner mutation around collision.

### Quality
Add Auth Emulator/Admin-backed collision fixtures with two distinct UIDs and one credential conflict. Assert both Firebase provider state and local owner state.

### Architecture / Data
Keep identity authentication, credential linking, owner binding, ledger access, and any future account/data migration as separate commands with separate authorization and recovery semantics.

## Evidence boundary
This is primary-source synthesis and exact-ref product transfer. No LogMate runtime, Auth Emulator, native provider, or PWA provider collision was executed in this block; exact-product validation remains OPEN.
