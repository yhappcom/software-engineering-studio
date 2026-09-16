"""A003 bounded contract-evolution fixture.

Shows two compatibility failures that preserve the Python method name/signature:
1) changing the semantic meaning of a result;
2) strengthening a precondition by rejecting an input previously accepted.
Also shows an additive alternative that preserves the old contract.
"""

import platform
import sys


FLIGHTS = [
    {"block": 90, "airborne": 75},
    {"block": 60, "airborne": 50},
]


class V1BlockTimeApi:
    def total_minutes(self, flights):
        return sum(flight["block"] for flight in flights)


class SilentSemanticBreakApi:
    # Same method name/signature, different meaning.
    def total_minutes(self, flights):
        return sum(flight["airborne"] for flight in flights)


class V2CompatibleApi:
    # Old semantic contract preserved; new meaning gets a new operation.
    def total_minutes(self, flights):
        return sum(flight["block"] for flight in flights)

    def total_airborne_minutes(self, flights):
        return sum(flight["airborne"] for flight in flights)


class EmptyAllowedApi:
    def total_minutes(self, flights):
        return sum(flight["block"] for flight in flights)


class EmptyRejectedApi:
    # Same signature, but a stronger precondition than the old contract.
    def total_minutes(self, flights):
        if not flights:
            raise ValueError("non-empty flights required")
        return sum(flight["block"] for flight in flights)


def main():
    expected_block_total = 150
    expected_airborne_total = 125

    assert V1BlockTimeApi().total_minutes(FLIGHTS) == expected_block_total

    semantic_break_observed = (
        SilentSemanticBreakApi().total_minutes(FLIGHTS) != expected_block_total
    )
    assert semantic_break_observed

    compatible = V2CompatibleApi()
    assert compatible.total_minutes(FLIGHTS) == expected_block_total
    assert compatible.total_airborne_minutes(FLIGHTS) == expected_airborne_total

    assert EmptyAllowedApi().total_minutes([]) == 0
    strengthened_precondition_break_observed = False
    try:
        EmptyRejectedApi().total_minutes([])
    except ValueError:
        strengthened_precondition_break_observed = True
    assert strengthened_precondition_break_observed

    print(f"python_version={sys.version.split()[0]}")
    print(f"platform={platform.platform()}")
    print("same_method_name_and_signature=True")
    print(f"v1_block_total={expected_block_total}")
    print(f"silent_semantic_break_total={SilentSemanticBreakApi().total_minutes(FLIGHTS)}")
    print(f"semantic_break_detected={semantic_break_observed}")
    print("additive_old_contract_preserved=True")
    print(f"strengthened_precondition_break_detected={strengthened_precondition_break_observed}")


if __name__ == "__main__":
    main()
