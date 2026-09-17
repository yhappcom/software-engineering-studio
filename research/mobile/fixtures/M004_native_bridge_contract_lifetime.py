class MissingPlugin(Exception):
    pass


class PlatformError(Exception):
    pass


class NativePlugin:
    def __init__(self, methods, attached=True):
        self.methods = methods
        self.attached = attached

    def call(self, method, arg):
        if not self.attached or method not in self.methods:
            raise MissingPlugin(method)
        return self.methods[method](arg)


def unsafe_bridge(plugin, method, arg):
    # Deliberate anti-pattern: collapses unavailable implementation into a value.
    try:
        return plugin.call(method, arg)
    except MissingPlugin:
        return None


def strict_bridge(plugin, method, arg):
    value = plugin.call(method, arg)
    if not isinstance(value, dict) or value.get("schema") != 1 or "value" not in value:
        raise PlatformError("contract mismatch")
    return value["value"]


ok = NativePlugin({"read": lambda _: {"schema": 1, "value": 7}})
missing = NativePlugin({})
bad_contract = NativePlugin({"read": lambda _: {"schema": 2, "payload": 7}})

assert strict_bridge(ok, "read", None) == 7
assert unsafe_bridge(missing, "read", None) is None

try:
    strict_bridge(missing, "read", None)
    raise AssertionError("missing implementation was accepted")
except MissingPlugin:
    pass

try:
    strict_bridge(bad_contract, "read", None)
    raise AssertionError("contract mismatch was accepted")
except PlatformError:
    pass

# Model distinct plugin instances owned by distinct engine lifetimes.
engine_1 = NativePlugin({"read": lambda _: {"schema": 1, "value": 1}})
engine_2 = NativePlugin({"read": lambda _: {"schema": 1, "value": 2}})
engine_1.attached = False

try:
    strict_bridge(engine_1, "read", None)
    raise AssertionError("detached engine instance was accepted")
except MissingPlugin:
    pass

assert strict_bridge(engine_2, "read", None) == 2

print(
    "PASS: success, missing-registration, contract-mismatch, "
    "and per-engine lifetime boundaries"
)
