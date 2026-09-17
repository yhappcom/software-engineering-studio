from copy import copy, deepcopy


def run():
    # FAILURE CASE: two names designate the same mutable object.
    original = {"profile": {"hours": 100}}
    alias = original
    alias["profile"]["hours"] += 1
    assert original["profile"]["hours"] == 101

    # FAILURE CASE: a shallow copy isolates the outer container but retains
    # the nested mutable object's aliasing relationship.
    original = {"profile": {"hours": 100}}
    shallow = copy(original)
    shallow["profile"]["hours"] += 1
    assert original["profile"]["hours"] == 101

    # ALTERNATIVE: recursive copy for this bounded object graph isolates the
    # nested mutable state. This is not a universal ownership strategy.
    original = {"profile": {"hours": 100}}
    isolated = deepcopy(original)
    isolated["profile"]["hours"] += 1
    assert original["profile"]["hours"] == 100
    assert isolated["profile"]["hours"] == 101

    # Rebinding a name is distinct from mutating the previously designated object.
    x = {"n": 1}
    y = x
    y = {"n": 2}
    assert x["n"] == 1

    print(
        {
            "alias_mutation": 101,
            "shallow_nested_alias": 101,
            "deepcopy_original": 100,
            "rebind_original": 1,
        }
    )


if __name__ == "__main__":
    run()
