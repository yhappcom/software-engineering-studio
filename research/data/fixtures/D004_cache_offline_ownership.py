from dataclasses import dataclass

@dataclass
class Record:
    value: int
    version: int

def unsafe_cache_refresh():
    remote = Record(60, 1)
    cache = Record(remote.value, remote.version)
    # Offline edit is accepted into local visible state.
    cache = Record(90, 2)
    # Reconnect fetch returns the older server state before local acknowledgement.
    fetched = remote
    cache = Record(fetched.value, fetched.version)  # destructive refresh
    return cache.value

def safe_pending_overlay():
    remote = Record(60, 1)
    base_cache = Record(remote.value, remote.version)
    pending = Record(90, 2)
    # Server refresh updates the confirmed base, not the pending mutation.
    fetched = remote
    base_cache = Record(fetched.value, fetched.version)
    visible = pending if pending is not None else base_cache
    return visible.value, base_cache.value, pending.value

def cached_absence():
    remote = {"F1": 60}
    cache = {}  # F1 has never been fetched into this cache.
    cache_query_says_absent = "F1" not in cache
    authoritative_absent = "F1" not in remote
    return cache_query_says_absent, authoritative_absent

if __name__ == "__main__":
    unsafe = unsafe_cache_refresh()
    visible, base, pending = safe_pending_overlay()
    cache_absent, remote_absent = cached_absence()
    print(f"unsafe_after_refresh={unsafe}")
    print(f"safe_visible={visible} base={base} pending={pending}")
    print(f"cache_says_absent={cache_absent} authoritative_absent={remote_absent}")
    assert unsafe == 60, "failure case should lose local visible edit"
    assert visible == 90 and base == 60 and pending == 90
    assert cache_absent is True and remote_absent is False
    print("VERDICT=PASS")
