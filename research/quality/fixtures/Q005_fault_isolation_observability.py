from dataclasses import dataclass


@dataclass
class Result:
    output: int
    events: list


def pipeline(raw: int, *, normalize_bug=False, aggregate_bug=False, instrument=False):
    events = []
    correlation_id = "case-1"
    decoded = raw
    if instrument:
        events.append((correlation_id, "decoded", decoded))

    normalized = decoded * 2 + (1 if normalize_bug else 0)
    if instrument:
        events.append((correlation_id, "normalized", normalized))

    output = normalized + (1 if aggregate_bug else 0)
    if instrument:
        events.append((correlation_id, "output", output))
    return Result(output, events)


def main():
    expected = 10
    normalize_failure = pipeline(5, normalize_bug=True)
    aggregate_failure = pipeline(5, aggregate_bug=True)

    # Same externally observed symptom: both independent defects produce output 11.
    assert normalize_failure.output == 11
    assert aggregate_failure.output == 11
    assert normalize_failure.output != expected

    normalize_trace = pipeline(5, normalize_bug=True, instrument=True)
    aggregate_trace = pipeline(5, aggregate_bug=True, instrument=True)

    normalize_state = {stage: value for _, stage, value in normalize_trace.events}
    aggregate_state = {stage: value for _, stage, value in aggregate_trace.events}

    # Independent boundary property: normalize(x) must equal decoded * 2.
    assert normalize_state["normalized"] != normalize_state["decoded"] * 2
    assert aggregate_state["normalized"] == aggregate_state["decoded"] * 2

    # Causal intervention/falsification: removing both injected defects restores the oracle.
    fixed = pipeline(5, instrument=True)
    assert fixed.output == expected

    print("final_only=", {"normalize_bug": normalize_failure.output, "aggregate_bug": aggregate_failure.output})
    print("normalize_trace=", normalize_trace.events)
    print("aggregate_trace=", aggregate_trace.events)
    print("fixed_trace=", fixed.events)


if __name__ == "__main__":
    main()
