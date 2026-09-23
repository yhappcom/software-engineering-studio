# S007 — Provider Link/Unlink Identity-Continuity Transfer

Status: **IN STUDY — SOURCE/SYNTHESIS + EXACT-PRODUCT TRANSFER; EXECUTABLE PRODUCT VALIDATION OPEN**
Owner: Systems / Security / Identity
Evidence date: 2026-09-24

## Scope
This block closes the semantic boundary for Google/Apple/email provider linking and unlinking under LogMate's account-required direction. It does not claim provider runtime readiness.

Exact product evidence: `yhappcom/logmate → main → e79f97cb7edd8823860daf14770a589f28a63ffc → declared 1.0.0+1 → evidence date 2026-09-24`. Default branch is not assumed production. The ref's startup/auth spec and federated-auth operations doc remain product implementation truth for the audited ref, but their account-free first-use and hard-coded 15-character password-policy text CONTRADICT newer owner direction and must not be transferred forward.

## SOURCE
Firebase Flutter account-linking documentation states that multiple authentication providers can be linked to one Firebase user and that the user remains identifiable by the same Firebase UID. `linkWithCredential()` is performed on the currently signed-in Firebase user. Documented failures include `provider-already-linked`, `invalid-credential`, and `credential-already-in-use`. Firebase also exposes `unlink(providerId)` and provider membership through `providerData`.

Firebase's platform account-linking guidance warns that after a provider is unlinked, signing in again with that provider can create a separate Firebase account rather than restoring the old link. Therefore unlink is an identity-reachability mutation, not cosmetic account settings.

Apple's Sign in with Apple guidance explicitly warns that an existing product account may not be discoverable by comparing email because the Apple identity may expose a different/private-relay address; Apple recommends making account-link intent explicit for existing accounts. Email therefore cannot be LogMate owner-merge authority.

Apple requires apps supporting account creation to provide in-app account-deletion initiation; apps using Sign in with Apple should revoke Apple tokens as part of deletion. This is deletion authority, not evidence that ordinary provider unlink and whole-account deletion are equivalent operations.

Primary sources rechecked 2026-09-24: Firebase Authentication Flutter account linking; Firebase Android/Apple-platform account linking; Apple Sign in with Apple authentication guidance; Apple in-app account deletion guidance.

## SYNTHESIS — identity continuity invariant
A LogMate ledger owner is bound to a Firebase UID, not to an email address and not to a provider label. Linking is safe only when it adds a credential to the *currently authenticated same UID*. It must never claim/rebind a ledger, merge two UIDs, or infer sameness from matching email.

Provider collision (`credential-already-in-use` / equivalent) means the credential is already controlled by another Firebase account. It is a recovery state, not permission to merge ledgers. The product must preserve both UID identities until an explicit, separately designed account/ledger migration authority exists.

Unlink is safe only if the account retains at least one verified usable sign-in method that is actually supported on the surfaces from which the owner may need to recover access. A raw provider count is insufficient: duplicate providerData entries, unavailable provider configuration, or a method that cannot authenticate on PWA/native may leave the owner stranded.

## ENGINEERING JUDGMENT — capability-based last-provider guard
Before unlink, compute an `effectiveRecoveryMethods` set from linked Firebase providers intersected with LogMate V1 supported methods and operationally enabled methods for the account's supported access surfaces. Refuse unlink when removing the requested provider would make this set empty.

This guard should be evaluated again immediately before the Firebase mutation after any required reauthentication because provider membership can change. After unlink returns success, reload/reobserve Firebase user state and verify both UID continuity and remaining recovery methods before committing product success UI.

A transport interruption after unlink is `outcomeUnknown`: do not retry blindly and do not assume the provider remains linked. Reload/reobserve providerData for the same UID first. If the session itself is lost, recover the same UID through another retained method before allowing any ledger mutation.

## PROJECT DECISION transfer
Current owner direction supersedes audited account-free entry: first use requires Firebase-backed email, Google, or Apple; authenticated completed owners restore Home; established ownership remains offline-first; no legacy local-only compatibility requirement exists pre-launch; password rules follow configured Firebase policy rather than a hard-coded 15-character product rule.

The audited `federated-auth-providers.md` still instructs configuring minimum 15 characters. This is a **CONTRADICTION** against the newer owner decision and must be removed/updated in a future authorized LogMate canonical change. Studio does not edit the product repository.

## Failure-first Codex contract
Required exact-product tests after implementation:

1. email UID A + link Google credential → resulting UID remains A; ledger owner unchanged; provider set gains Google.
2. UID A attempts to link credential already owned by UID B → typed collision; no ledger mutation; no automatic email merge; active owner remains A.
3. Apple private-relay/real-email mismatch → no email-based owner merge path exists.
4. unlink one of two operational recovery methods → same UID remains; removed provider absent after reload; other method can reauthenticate.
5. attempt to unlink the last effective recovery method → rejected before Firebase mutation.
6. unlink call returns network/outcome-unknown → reobserve providerData; no blind second mutation; ledger owner unchanged.
7. reauthentication changes/loses current UID → abort unlink and enter identity recovery; never mutate ledger owner.
8. duplicate unlink callback/replay → idempotent product outcome; no owner/setup mutation.
9. cross-surface matrix: after any allowed unlink, at least one retained method successfully authenticates the same UID on every supported surface required by product policy.
10. account deletion remains a separate command/workflow and cannot be reached by merely unlinking the final provider.

## VALIDATION
No LogMate Dart/Flutter, Firebase Auth Emulator, real Google/Apple, Android/iOS, or PWA link/unlink execution was performed in this block. Reading and synthesis do not award PASS. Exact provider configuration remains unverified.

## CHANGE WATCH
FlutterFire/Firebase link/unlink exception behavior, Google/Apple SDK transport behavior, provider-console configuration, browser redirect lifecycle, and Apple token-revocation requirements remain change-watch items.

## RELATED DOMAIN CHECK
- Foundations: no new prerequisite.
- Architecture: UID ownership must remain separate from provider credentials and UI route state.
- Mobile: native provider acquisition and PWA popup/redirect require separate transfer validation.
- Data: no ledger owner/setup mutation may occur on provider link/unlink collision or ambiguous completion.
- Quality: failure-first matrix above requires executable exact-product tests and independent Firebase state oracle where possible.
- Systems: owns authentication identity continuity and recovery reachability.
- Design Studio: unlink confirmation/recovery copy must reflect access consequences; no canonical files edited.
- Web Manager: PWA provider reachability/authorized-domain readiness affects effective recovery methods; no canonical files edited.
- Marketing Manager: not materially relevant.
- Product: exact LogMate ref checked; no product files edited.

## HANDOFFS
- **LogMate / Codex:** implement provider link/unlink around same-UID continuity, typed collision/outcome-unknown results, capability-based last-effective-provider guard, and post-mutation Firebase reobservation. Never merge by email.
- **Architecture/Data:** treat provider membership as authentication reachability metadata, not ledger ownership; keep UID-owner mutation outside link/unlink.
- **Quality/Mobile:** execute the ten-case matrix, then transfer-test retained sign-in on Android/iOS/PWA before provider release.
- **LogMate canonical owner:** when authorized, remove account-free startup semantics and the hard-coded 15-character provider-operations requirement; configured Firebase password policy is authoritative.
