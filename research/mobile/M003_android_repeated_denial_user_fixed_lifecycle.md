# M003 — Android repeated-denial / USER_FIXED lifecycle

Status: **VALIDATION IN PROGRESS — EXECUTABLE API-35 EMULATOR ORACLE COMMITTED**  
Evidence date: 2026-09-21

## Problem / professional boundary
The prior user-dialog transfer validates one-time CAMERA grant and one fresh-install denial, but it does not validate Android's repeated-denial lifecycle. Android 11+ documents a materially different state transition: after the user denies the same permission more than once during an installation lifetime, subsequent requests do not show the system permission dialog. The platform exposes `USER_SET` after denial and `USER_FIXED` after permanent repeated denial for testing/diagnostics.

This block tests that lifecycle as mutable OS authority rather than treating `DENIED` as one undifferentiated state.

## SOURCE
Android Developers, rechecked 2026-09-21:
- `https://developer.android.com/about/versions/11/privacy/permissions` — repeated denial suppresses subsequent permission dialogs; denied-once is flagged `USER_SET`, denied-permanently after two denials is flagged `USER_FIXED`; the documented adb reset command clears those flags for testing.
- `https://developer.android.com/training/permissions/requesting` — apps must check permission state at each protected operation and gracefully degrade after denial/revocation; one-time permission is a separate temporary-authority lifecycle.
- `https://developer.android.com/guide/topics/permissions/overview` — runtime permission authority is system-managed and must not be assumed previously granted.

## SYNTHESIS
A boolean granted/denied UI projection is insufficient to describe the request lifecycle. `DENIED + requestable` and `DENIED + USER_FIXED/dialog-suppressed` can present the same access result while requiring different interaction behavior. Therefore permission validation needs both an access-state oracle and a requestability/dialog-state oracle.

## ENGINEERING JUDGMENT
Repeated denial is a higher-value next block than merely repeating the already-green one-time grant fixture. It adds a distinct failure/UX state with cross-track leverage for Mobile, Quality, Architecture and Design handoff, while remaining executable in the currently trustworthy Android emulator environment.

## VALIDATION contract
Workflow: `.github/workflows/m003-android-user-permission-dialog.yml`  
Exact committed validation head: `bab16cc993d72d1ca98f3c9f2aa2bf4a4bbf8aa4`  
Target environment: pinned Flutter 3.47.5; Android API 35 x86_64 Pixel 6 emulator; GitHub-hosted Ubuntu runner; Studio fixture only.

The existing one-time grant path is retained as a control. After fresh reinstall, the extended oracle requires:
1. first user denial through the real Permission Controller control;
2. Flutter callback/UI remains `CAMERA:DENIED` and package state remains denied;
3. package diagnostics contain `USER_SET`;
4. a second app-originated request still exposes a denial control;
5. second user denial completes and package diagnostics contain `USER_FIXED`;
6. a third app-originated request does **not** expose the Permission Controller denial control;
7. the app callback/UI remains denied;
8. phase-specific CI classifiers expose the first failed lifecycle operation;
9. natural workflow completion is required for PASS.

The oracle deliberately does not use `pm clear-permission-flags` to manufacture the target transition. The system/user interactions create the denial history; package diagnostics independently observe flags.

## OPEN / VALIDATION
- No PASS is awarded until the committed workflow executes successfully and the exact run/job/environment are recorded.
- If the run fails, the first named phase is failure evidence only; root cause requires reproduction/isolation before attribution.
- Auto-reset/hibernation and one-time expiry/background grace are separate lifecycle classes and remain OPEN.
- Physical Android/OEM/API-version replication remains OPEN.
- Product runtime, iOS and production remain OPEN.

## RELATED DOMAIN CHECK
- Foundations: OS-managed mutable authority and process callbacks; existing execution evidence sufficient for this bounded block.
- Architecture: permission state needs access authority and requestability/interaction state rather than one boolean contract.
- Mobile: owning track; extends M003 lifecycle coverage.
- Data: not materially relevant; no durability claim.
- Quality: independent UI/package-state oracles and phase classifiers are material.
- Systems: least privilege/revocation implications noted; this is not complete authorization-policy evidence.
- Design Studio: materially relevant downstream; a permanently denied/request-suppressed state may require settings/rationale recovery UX distinct from an ordinary first denial. No Design Studio canonical file edited.
- Web Manager / Marketing Manager: not materially relevant.
- Product source/ref: no product repository audited; Studio fixture only.

## HANDOFFS
- Design Studio: if product permission UX is designed, distinguish ordinary denial from a state where the system dialog will no longer reappear; Engineering validation is still bounded to API-35 emulator until the run completes.
- Quality: preserve package permission flags as an independent diagnostic oracle; do not infer requestability from `granted=false` alone.
- Architecture: model authority and requestability as separate externally meaningful state dimensions when permission-gated features need recovery flows.
