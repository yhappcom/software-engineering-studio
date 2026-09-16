"""S001 bounded validation: source identity is not artifact identity.

Demonstrates that two artifacts can share the same declared source ref while
having different bytes after a post-build transform. A verifier that checks
only source_ref accepts both; an independent digest check distinguishes them.
"""
from __future__ import annotations

import hashlib
import platform
import sys

SOURCE_REF = "abc123"
SOURCE = b"print('hello')\n"
CANONICAL = b"BUNDLE\n" + SOURCE
POST_BUILD = CANONICAL + b"POST_BUILD_PATCH=offline\n"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    expected_digest = sha256(CANONICAL)
    cases = {
        "canonical": CANONICAL,
        "post_build": POST_BUILD,
    }

    assert CANONICAL != POST_BUILD
    assert sha256(CANONICAL) != sha256(POST_BUILD)

    for name, artifact in cases.items():
        source_ref_match = SOURCE_REF == "abc123"
        digest_match = sha256(artifact) == expected_digest
        print(
            f"{name} source_ref_match={source_ref_match} "
            f"digest_match={digest_match} sha256={sha256(artifact)}"
        )

    # Deliberate weak verifier: source identity alone accepts both artifacts.
    assert all(SOURCE_REF == "abc123" for _ in cases.values())
    # Stronger bounded verifier: only the expected canonical bytes match.
    assert sha256(CANONICAL) == expected_digest
    assert sha256(POST_BUILD) != expected_digest

    print(f"python={sys.version.split()[0]}")
    print(f"platform={platform.platform()}")


if __name__ == "__main__":
    main()
