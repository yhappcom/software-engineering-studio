from dataclasses import dataclass
import hashlib


@dataclass(frozen=True)
class Artifact:
    source: str
    build: int
    payload: bytes

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.payload).hexdigest()


def release_gate(artifact: Artifact, expected_source: str, expected_build: int, expected_digest: str) -> bool:
    return (
        artifact.source == expected_source
        and artifact.build == expected_build
        and artifact.digest == expected_digest
    )


good = Artifact("abc123", 42, b"signed-release-payload")
expected_digest = good.digest
stale_source = Artifact("old999", 42, b"signed-release-payload")
rebuilt_bytes = Artifact("abc123", 42, b"signed-release-payload-v2")

print("good=", release_gate(good, "abc123", 42, expected_digest))
print("stale_source=", release_gate(stale_source, "abc123", 42, expected_digest))
print("rebuilt_bytes=", release_gate(rebuilt_bytes, "abc123", 42, expected_digest))

assert release_gate(good, "abc123", 42, expected_digest)
assert not release_gate(stale_source, "abc123", 42, expected_digest)
assert not release_gate(rebuilt_bytes, "abc123", 42, expected_digest)
print("PASS: release acceptance binds source, build identity and artifact bytes")
