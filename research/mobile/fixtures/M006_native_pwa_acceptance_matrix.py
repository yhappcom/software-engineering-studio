"""M006 bounded capability/acceptance model.

This is NOT browser, iOS/iPadOS, Android, Flutter, or EFB execution evidence.
It checks whether a delivery target may be accepted only when every required
semantic guarantee is supported, rather than because it is installable or
shares application code.

Environment expected: Python 3.x.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Target:
    name: str
    offline_launch: bool
    user_install_without_store: bool
    guaranteed_continuous_background_execution: bool


def accepts(target: Target, *, require_offline: bool, require_no_store: bool,
            require_continuous_background: bool) -> bool:
    requirements = (
        (require_offline, target.offline_launch),
        (require_no_store, target.user_install_without_store),
        (require_continuous_background, target.guaranteed_continuous_background_execution),
    )
    return all((not required) or supported for required, supported in requirements)


# Deliberately bounded models, not claims that every native/PWA deployment has
# these properties. The PWA model captures the studied service-worker boundary:
# install/offline capability can exist without a guarantee of continuously
# running background application code.
pwa = Target("pwa-model", True, True, False)
native = Target("native-model", True, False, True)

# EFB-style contract: install path cannot depend on an app store, offline launch
# is required, but continuous background execution is NOT part of the contract.
assert accepts(pwa, require_offline=True, require_no_store=True,
               require_continuous_background=False)
assert not accepts(native, require_offline=True, require_no_store=True,
                   require_continuous_background=False)

# If product semantics are strengthened to require guaranteed continuously
# running background code, installability/offline support do not rescue the PWA.
assert not accepts(pwa, require_offline=True, require_no_store=True,
                   require_continuous_background=True)

# A naive gate that checks only installability would incorrectly accept the
# strengthened contract.
naive_installability_gate = pwa.user_install_without_store
assert naive_installability_gate is True
assert naive_installability_gate != accepts(
    pwa,
    require_offline=True,
    require_no_store=True,
    require_continuous_background=True,
)

print("M006 bounded acceptance matrix: PASS")
