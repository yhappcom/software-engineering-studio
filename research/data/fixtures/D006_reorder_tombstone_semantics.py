from itertools import permutations

EVENTS = ("delete_v3", "stale_update_v2")


def naive_state_sync(order):
    state = {"exists": True, "value": "v1"}
    for event in order:
        if event == "delete_v3":
            state = {"exists": False, "value": None}
        elif event == "stale_update_v2":
            state = {"exists": True, "value": "v2-from-stale-base"}
    return state


def versioned_tombstone_sync(order):
    state = {"exists": True, "value": "v1", "version": 1, "tombstone": False}
    candidates = {
        "delete_v3": {"exists": False, "value": None, "version": 3, "tombstone": True},
        "stale_update_v2": {"exists": True, "value": "v2-from-stale-base", "version": 2, "tombstone": False},
    }
    for event in order:
        candidate = candidates[event]
        if candidate["version"] > state["version"]:
            state = candidate.copy()
    return state


def deleted_oracle(state):
    return state["exists"] is False


def main():
    naive_failures = []
    tombstone_failures = []
    for order in permutations(EVENTS):
        naive = naive_state_sync(order)
        guarded = versioned_tombstone_sync(order)
        if not deleted_oracle(naive):
            naive_failures.append((order, naive))
        if not deleted_oracle(guarded):
            tombstone_failures.append((order, guarded))
        print(f"order={order} naive={naive} guarded={guarded}")

    print(f"naive_failures={len(naive_failures)}/2")
    print(f"tombstone_failures={len(tombstone_failures)}/2")
    if naive_failures:
        print(f"first_naive_failure={naive_failures[0]}")

    assert len(naive_failures) == 1
    assert len(tombstone_failures) == 0
    print("VERDICT=PASS")


if __name__ == "__main__":
    main()
