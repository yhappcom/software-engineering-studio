import hashlib

registry = {
    "lib": {
        "1.0.0": b"lib-v1.0.0",
        "1.1.0": b"lib-v1.1.0",
    }
}


def resolve_caret_1(reg):
    return sorted(reg["lib"])[-1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


# Build A resolves when only 1.0.0 is available.
registry_a = {"lib": {"1.0.0": registry["lib"]["1.0.0"]}}
resolved_a = resolve_caret_1(registry_a)
lock = {
    "lib": {
        "version": resolved_a,
        "sha256": digest(registry_a["lib"][resolved_a]),
    }
}

# Same manifest later, registry has compatible 1.1.0.
resolved_unlocked_b = resolve_caret_1(registry)
resolved_locked_b = lock["lib"]["version"]
assert resolved_a == "1.0.0"
assert resolved_unlocked_b == "1.1.0"
assert resolved_locked_b == "1.0.0"

# Tamper the locked package contents while retaining version identity.
tampered = b"lib-v1.0.0-TAMPERED"
observed_hash = digest(tampered)
integrity_ok = observed_hash == lock["lib"]["sha256"]
assert not integrity_ok

print("manifest_only_A=", resolved_a)
print("manifest_only_B=", resolved_unlocked_b)
print("locked_B=", resolved_locked_b)
print("tampered_integrity_ok=", integrity_ok)
print("PASS: lock stabilizes this resolution; content hash detects same-version content change")
