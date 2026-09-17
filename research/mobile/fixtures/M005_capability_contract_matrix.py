"""M005 bounded model: portability is a semantic capability contract, not API-name equality.
Environment used for canonical run: Python 3.13.5 / Linux, 2026-09-18.
This is NOT Flutter/Android/iOS/browser runtime evidence.
"""

from dataclasses import dataclass


class UnsupportedCapability(RuntimeError):
    pass


@dataclass(frozen=True)
class PlatformCaps:
    name: str
    arbitrary_filesystem: bool
    background_retry: bool
    native_secure_key: bool


NATIVE = PlatformCaps("native-mobile", True, True, True)
WEB = PlatformCaps("browser-web", False, False, False)


def unsafe_shared_implementation(caps: PlatformCaps) -> str:
    """Wrong portability model: assumes one implementation contract everywhere."""
    if not caps.arbitrary_filesystem:
        raise UnsupportedCapability("arbitrary filesystem unavailable")
    return "saved"


def export_record(caps: PlatformCaps) -> str:
    """Portable semantic contract with platform-specific mechanism/fallback."""
    if caps.arbitrary_filesystem:
        return "saved-to-app-file"
    # Browser implementation can satisfy the user-level export contract by download.
    return "download-offered"


def require_background_retry(caps: PlatformCaps) -> str:
    """No silent semantic downgrade when the required guarantee is absent."""
    if not caps.background_retry:
        raise UnsupportedCapability("background retry guarantee unavailable")
    return "background-retry-scheduled"


def main() -> None:
    assert unsafe_shared_implementation(NATIVE) == "saved"
    try:
        unsafe_shared_implementation(WEB)
    except UnsupportedCapability:
        pass
    else:
        raise AssertionError("unsafe portability assumption should fail on web model")

    assert export_record(NATIVE) == "saved-to-app-file"
    assert export_record(WEB) == "download-offered"

    try:
        require_background_retry(WEB)
    except UnsupportedCapability:
        pass
    else:
        raise AssertionError("required capability must not silently degrade")

    print("PASS: capability divergence detected; semantic fallback/explicit unsupported preserved")


if __name__ == "__main__":
    main()
