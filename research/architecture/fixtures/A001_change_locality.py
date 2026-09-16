"""A001: bounded demonstration of representation knowledge and change locality."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Flight:
    callsign: str
    minutes: int


# Version 1 representation: "CALLSIGN|minutes"
def hidden_decode_v1(raw: str) -> Flight:
    callsign, minutes = raw.split("|")
    return Flight(callsign, int(minutes))


# Version 2 representation: a keyed record. Only the owner changes.
def hidden_decode_v2(raw: dict[str, object]) -> Flight:
    return Flight(str(raw["flight"]), int(raw["block_minutes"]))


def semantic_summary(flight: Flight) -> str:
    return f"{flight.callsign}:{flight.minutes}m"


def semantic_is_long(flight: Flight) -> bool:
    return flight.minutes >= 120


# Leaky clients duplicate V1 representation knowledge.
def leaky_summary(raw: str) -> str:
    callsign, minutes = raw.split("|")
    return f"{callsign}:{int(minutes)}m"


def leaky_is_long(raw: str) -> bool:
    _callsign, minutes = raw.split("|")
    return int(minutes) >= 120


def main() -> None:
    v1 = "7C101|135"
    v2 = {"flight": "7C101", "block_minutes": 135}

    # Hidden design: semantic clients are unchanged.
    f1 = hidden_decode_v1(v1)
    f2 = hidden_decode_v2(v2)
    assert semantic_summary(f1) == semantic_summary(f2) == "7C101:135m"
    assert semantic_is_long(f1) is semantic_is_long(f2) is True

    # Leaky design: both clients know V1 syntax and fail after representation change.
    failures = 0
    for client in (leaky_summary, leaky_is_long):
        try:
            client(v2)  # type: ignore[arg-type]
        except (AttributeError, TypeError, ValueError):
            failures += 1

    assert failures == 2
    print("hidden_clients_unchanged=2")
    print("leaky_clients_broken_by_representation_change=2")
    print("bounded_claim=PASS")


if __name__ == "__main__":
    main()
