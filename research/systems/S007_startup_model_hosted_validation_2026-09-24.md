# S007 — Hosted Startup Model Validation

Evidence date: 2026-09-24
Owner: Systems / Security / Identity

## VALIDATION

### Target
- Repository: `yhappcom/software-engineering-studio`
- Exact workflow head: `1bc58ec210408a18cb4fd719be85b5b21e727d2e`
- Workflow: `.github/workflows/s007-auth-startup-state-model.yml`
- Fixture: `research/systems/fixtures/S007_auth_startup_state_model.py`
- GitHub Actions run: `35909442993`
- Job: `107345269055` (`model`)
- Environment observed in job log: GitHub-hosted Ubuntu 24.04.5 LTS, runner `2.337.0`, CPython `3.13.15`.

### Result
Run `35909442993` completed with `conclusion=success`. The `Execute fail-closed startup model` step completed successfully. The job log independently records all eight intended tests as `ok` and `Ran 8 tests ... OK`:

1. duplicate authenticated callback initializes owner once;
2. explicit sign-out retains owner and routes Welcome;
3. initialization failure is not sign-out and preserves owner;
4. matching completed owner routes Home;
5. matching incomplete owner resumes onboarding;
6. reauthentication after explicit sign-out restores Home;
7. unresolved Auth never routes Welcome/Home;
8. wrong UID fails closed without rebinding.

This closes the previously OPEN hosted verdict for the generic deterministic startup model.

## EVIDENCE LIMIT
This is **not** LogMate runtime PASS. The fixture is a Studio model written in Python. It does not execute LogMate Dart/Flutter code, Firebase Auth persistence, Sembast transactions, Firebase Auth Emulator, Google/Apple SDKs, Android/iOS lifecycle, or PWA redirect behavior. It validates the internal consistency and executable feasibility of the startup algebra only.

Do not promote this result to product/provider PASS.

## TRANSFER VALIDATION / NEXT RUNG
The next useful evidence is not another synthetic variant. Transfer the same oracles to exact LogMate code after Codex implements the account-required startup boundary, then add Firebase Auth Emulator integration with an independent UID/account-state oracle. Real Google/Apple Android/iOS/PWA E2E remains a later separate rung.

## RELATED DOMAIN CHECK
- Foundations: no new prerequisite exposed.
- Architecture: validates the proposed separation of unresolved Auth, owner binding, onboarding completion and routing at model level only.
- Mobile: no native/browser runtime evidence gained.
- Data: exactly-once owner initialization is modeled, not persistence-validated.
- Quality: hosted execution supplies reproducible executable evidence and independent CI logs; exact-product tests remain required.
- Systems: owning validation block.
- Design Studio / Web Manager / Marketing Manager: no canonical changes required by this bounded validation.
- Product: no LogMate files edited.

## HANDOFFS
- **LogMate / Codex:** reproduce these eight invariants in Dart/Flutter against the actual startup/auth/repository boundaries; do not cite this Python run as product evidence.
- **Quality:** require exact-product failure injection/restart tests and Firebase Auth Emulator independent account-state checks before any LogMate Auth PASS.
- **Data/Architecture:** retain wrong-UID fail-closed and exactly-once owner initialization as repository/state-machine invariants, not UI sequencing assumptions.
