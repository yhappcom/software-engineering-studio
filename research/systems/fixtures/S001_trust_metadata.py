"""S001 bounded trust-boundary fixture: integrity metadata is not self-authenticating.

HMAC is used only as a compact executable stand-in for a verifier-held authentication
secret. This fixture does NOT claim HMAC is equivalent to public-key code signing,
non-repudiation, SLSA provenance, or a production release system.
"""
import hashlib
import hmac
import json
import platform
import sys

VERIFIER_KEY = b"trusted-verifier-key"
TRUSTED_BUILDERS = {"trusted-builder"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def metadata(data: bytes, builder: str = "trusted-builder") -> dict[str, str]:
    return {"sha256": sha256(data), "builder": builder}


def authenticate(meta: dict[str, str]) -> str:
    payload = json.dumps(meta, sort_keys=True, separators=(",", ":")).encode()
    return hmac.new(VERIFIER_KEY, payload, hashlib.sha256).hexdigest()


def verify_authenticated(meta: dict[str, str], tag: str) -> bool:
    return hmac.compare_digest(authenticate(meta), tag)


def main() -> None:
    canonical = b"app-binary-v1"
    tampered = b"app-binary-v1+evil"

    canonical_meta = metadata(canonical)
    canonical_tag = authenticate(canonical_meta)

    # Attacker can rewrite both artifact and adjacent unsigned checksum metadata.
    attacker_meta = metadata(tampered)
    weak_accepts_tampered = sha256(tampered) == attacker_meta["sha256"]

    strong_accepts_canonical = (
        verify_authenticated(canonical_meta, canonical_tag)
        and sha256(canonical) == canonical_meta["sha256"]
        and canonical_meta["builder"] in TRUSTED_BUILDERS
    )

    # Reusing the trusted tag after rewriting metadata must fail authentication.
    rewritten_meta_authenticates = verify_authenticated(attacker_meta, canonical_tag)
    strong_accepts_rewritten = (
        rewritten_meta_authenticates
        and sha256(tampered) == attacker_meta["sha256"]
        and attacker_meta["builder"] in TRUSTED_BUILDERS
    )

    # Authenticity and authorization are deliberately separate checks.
    unauthorized_meta = metadata(canonical, builder="unapproved-builder")
    unauthorized_tag = authenticate(unauthorized_meta)
    authentic_but_unauthorized = (
        verify_authenticated(unauthorized_meta, unauthorized_tag)
        and unauthorized_meta["builder"] not in TRUSTED_BUILDERS
    )

    assert weak_accepts_tampered is True
    assert strong_accepts_canonical is True
    assert rewritten_meta_authenticates is False
    assert strong_accepts_rewritten is False
    assert authentic_but_unauthorized is True

    print(f"python_version={sys.version.split()[0]}")
    print(f"platform={platform.platform()}")
    print(f"canonical_sha256={sha256(canonical)}")
    print(f"tampered_sha256={sha256(tampered)}")
    print(f"weak_unsigned_checksum_accepts_tampered={weak_accepts_tampered}")
    print(f"authenticated_metadata_accepts_canonical={strong_accepts_canonical}")
    print(f"rewritten_metadata_authenticates_with_old_tag={rewritten_meta_authenticates}")
    print(f"authenticated_policy_accepts_rewritten={strong_accepts_rewritten}")
    print(f"authentic_but_unauthorized_builder_detected={authentic_but_unauthorized}")


if __name__ == "__main__":
    main()
