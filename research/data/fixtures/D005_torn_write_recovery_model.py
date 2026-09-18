import hashlib

SECTOR = 512
PAGE = 4096
old = bytes((i * 17 + 3) % 256 for i in range(PAGE))
new = bytes((i * 29 + 11) % 256 for i in range(PAGE))
assert old != new


def h(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()[:16]


def torn_write(base: bytes, replacement: bytes, completed_sectors: int) -> bytes:
    out = bytearray(base)
    for sector in range(completed_sectors):
        start = sector * SECTOR
        end = start + SECTOR
        out[start:end] = replacement[start:end]
    return bytes(out)


# Model a power loss after 3 of 8 sectors of a 4096-byte page reached durable media.
torn = torn_write(old, new, 3)
assert torn != old and torn != new
assert torn[: 3 * SECTOR] == new[: 3 * SECTOR]
assert torn[3 * SECTOR :] == old[3 * SECTOR :]

# Without a durable pre-image, the observed page is neither allowed atomic outcome.
no_journal_ok = torn in (old, new)
assert not no_journal_ok

# Alternative: a complete durable pre-image can restore the old atomic outcome.
recovered = old
assert recovered == old

# Deliberate mutant: an incomplete pre-image cannot reconstruct the original page.
partial_journal = old[: 2 * SECTOR] + b"?" * (PAGE - 2 * SECTOR)
mutant_recovered = partial_journal
assert mutant_recovered != old

print("old", h(old), "new", h(new), "torn", h(torn))
print("torn_atomic_oracle", no_journal_ok)
print("complete_preimage_recovery", recovered == old)
print("partial_preimage_recovery", mutant_recovered == old)
print("PASS")
