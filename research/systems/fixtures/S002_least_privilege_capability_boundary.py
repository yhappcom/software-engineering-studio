from dataclasses import dataclass

FILES = {
    "profile": "pilot-profile",
    "tax": "tax-adjustment",
}

class AmbientStore:
    def read(self, key):
        return FILES[key]

@dataclass(frozen=True)
class ReadCapability:
    allowed: frozenset[str]
    def read(self, key):
        if key not in self.allowed:
            raise PermissionError(key)
        return FILES[key]

def plugin_ambient(store):
    # Compromised/buggy plugin asks for unrelated sensitive data.
    return store.read("tax")

def plugin_scoped(cap):
    return cap.read("tax")

def main():
    ambient = AmbientStore()
    leaked = plugin_ambient(ambient)
    assert leaked == "tax-adjustment"

    scoped = ReadCapability(frozenset({"profile"}))
    try:
        plugin_scoped(scoped)
    except PermissionError as e:
        blocked = str(e)
    else:
        raise AssertionError("least-privilege boundary failed open")
    assert blocked == "tax"

    assert scoped.read("profile") == "pilot-profile"
    print("ambient_authority=LEAKED:tax-adjustment")
    print("scoped_authority=BLOCKED:tax")
    print("required_operation=PASS:pilot-profile")

if __name__ == "__main__":
    main()
