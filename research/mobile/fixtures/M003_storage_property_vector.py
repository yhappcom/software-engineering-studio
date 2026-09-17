from dataclasses import dataclass


@dataclass(frozen=True)
class StorageClass:
    name: str
    app_private: bool
    purgeable: bool
    survives_uninstall: bool
    credential_protected: bool


internal_files = StorageClass("internal_files", True, False, False, False)
internal_cache = StorageClass("internal_cache", True, True, False, False)
shared_document = StorageClass("shared_document", False, False, True, False)
credential_store = StorageClass("credential_store", True, False, True, True)


def valid_for(
    storage: StorageClass,
    *,
    secret: bool = False,
    must_survive_uninstall: bool = False,
    reconstructible: bool = False,
) -> bool:
    if secret and not storage.credential_protected:
        return False
    if must_survive_uninstall and not storage.survives_uninstall:
        return False
    if storage.purgeable and not reconstructible:
        return False
    return True


# Independent role predicates deliberately expose invalid shortcuts.
assert valid_for(internal_files)
assert not valid_for(internal_cache)
assert valid_for(internal_cache, reconstructible=True)
assert not valid_for(internal_files, must_survive_uninstall=True)
assert valid_for(shared_document, must_survive_uninstall=True)
assert not valid_for(internal_files, secret=True)
assert valid_for(credential_store, secret=True)

print(
    "PASS: isolation, purgeability, uninstall persistence, "
    "and credential protection are independent axes"
)
