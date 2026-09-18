#!/usr/bin/env python3
"""S005 bounded real public-key signing/verification fixture.

Evidence target: OpenSSL CLI public-key signature verification over exact artifact bytes.
This is not CI, mobile code signing, certificate-chain validation, key custody, or provenance.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import tempfile
from pathlib import Path


def run(*args: str, expect: int = 0) -> subprocess.CompletedProcess[str]:
    cp = subprocess.run(args, text=True, capture_output=True)
    if cp.returncode != expect:
        raise AssertionError(
            f"expected rc={expect}, got {cp.returncode}: {' '.join(args)}\n"
            f"stdout={cp.stdout}\nstderr={cp.stderr}"
        )
    return cp


def verify(openssl: str, pub: Path, sig: Path, artifact: Path) -> bool:
    cp = subprocess.run(
        [openssl, "dgst", "-sha256", "-verify", str(pub), "-signature", str(sig), str(artifact)],
        text=True,
        capture_output=True,
    )
    return cp.returncode == 0 and "Verified OK" in cp.stdout


def main() -> None:
    openssl = shutil.which("openssl")
    if not openssl:
        raise SystemExit("OPEN: openssl executable unavailable")

    version = run(openssl, "version").stdout.strip()
    with tempfile.TemporaryDirectory(prefix="s005-signature-") as td:
        root = Path(td)
        artifact = root / "artifact.bin"
        tampered = root / "tampered.bin"
        key = root / "key.pem"
        pub = root / "pub.pem"
        other_key = root / "other-key.pem"
        other_pub = root / "other-pub.pem"
        sig = root / "artifact.sig"

        artifact.write_bytes(b"artifact-v1\nsource=abc123\nbuild=42\n")
        tampered.write_bytes(artifact.read_bytes() + b"TAMPER\n")

        run(openssl, "genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048", "-out", str(key))
        run(openssl, "pkey", "-in", str(key), "-pubout", "-out", str(pub))
        run(openssl, "dgst", "-sha256", "-sign", str(key), "-out", str(sig), str(artifact))

        good = verify(openssl, pub, sig, artifact)
        tamper_rejected = not verify(openssl, pub, sig, tampered)

        run(openssl, "genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048", "-out", str(other_key))
        run(openssl, "pkey", "-in", str(other_key), "-pubout", "-out", str(other_pub))
        wrong_key_rejected = not verify(openssl, other_pub, sig, artifact)

        artifact_digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
        tampered_digest = hashlib.sha256(tampered.read_bytes()).hexdigest()

        assert good, "canonical artifact must verify under signer public key"
        assert tamper_rejected, "changed bytes must not verify under original signature"
        assert wrong_key_rejected, "signature must not verify under unrelated public key"
        assert artifact_digest != tampered_digest

        print(f"environment={version}")
        print(f"artifact_sha256={artifact_digest}")
        print(f"tampered_sha256={tampered_digest}")
        print(f"good={good}")
        print(f"tamper_rejected={tamper_rejected}")
        print(f"wrong_key_rejected={wrong_key_rejected}")
        print("PASS: signature verification binds exact bytes to possession of the corresponding private key in this bounded fixture")


if __name__ == "__main__":
    main()
