"""A001 bounded counterexample: extra abstraction without demonstrated change locality.

This fixture intentionally compares a direct implementation with a pass-through
layered design for one fixed source and one fixed formatting policy. It does NOT
claim that fewer classes are universally better. It demonstrates only that
extra indirection has observable structural/diagnostic carrying cost when no
independent volatility, substitution, ownership, or policy boundary is present.
"""

from __future__ import annotations

import platform
import sys
import traceback


def direct_format(minutes: int) -> str:
    if minutes < 0:
        raise ValueError("minutes must be non-negative")
    hours, remainder = divmod(minutes, 60)
    return f"{hours:02}:{remainder:02}"


class MinutesSource:
    def __init__(self, minutes: int):
        self._minutes = minutes

    def read(self) -> int:
        return self._minutes


class MinutesRepository:
    def __init__(self, source: MinutesSource):
        self._source = source

    def get(self) -> int:
        return self._source.read()


class BlockTimeService:
    def __init__(self, repository: MinutesRepository):
        self._repository = repository

    def total_minutes(self) -> int:
        return self._repository.get()


class BlockTimeFormatter:
    def format(self, minutes: int) -> str:
        if minutes < 0:
            raise ValueError("minutes must be non-negative")
        hours, remainder = divmod(minutes, 60)
        return f"{hours:02}:{remainder:02}"


class BlockTimePresenter:
    def __init__(self, service: BlockTimeService, formatter: BlockTimeFormatter):
        self._service = service
        self._formatter = formatter

    def render(self) -> str:
        return self._formatter.format(self._service.total_minutes())


def layered_format(minutes: int) -> str:
    source = MinutesSource(minutes)
    repository = MinutesRepository(source)
    service = BlockTimeService(repository)
    formatter = BlockTimeFormatter()
    presenter = BlockTimePresenter(service, formatter)
    return presenter.render()


def failure_frames(callable_):
    try:
        callable_(-1)
    except ValueError as error:
        frames = traceback.extract_tb(error.__traceback__)
        return [frame.name for frame in frames if frame.name != "failure_frames"]
    raise AssertionError("expected ValueError")


def edge_count(graph: dict[str, list[str]]) -> int:
    return sum(len(targets) for targets in graph.values())


def main() -> None:
    samples = [0, 59, 60, 135, 6000]
    for minutes in samples:
        assert direct_format(minutes) == layered_format(minutes)

    # These graphs describe declared collaboration/dependency relationships in
    # the bounded fixture; they are not universal maintainability metrics.
    direct_graph = {"direct_format": []}
    layered_graph = {
        "layered_format": [
            "MinutesSource",
            "MinutesRepository",
            "BlockTimeService",
            "BlockTimeFormatter",
            "BlockTimePresenter",
        ],
        "MinutesRepository": ["MinutesSource"],
        "BlockTimeService": ["MinutesRepository"],
        "BlockTimePresenter": ["BlockTimeService", "BlockTimeFormatter"],
        "MinutesSource": [],
        "BlockTimeFormatter": [],
    }

    direct_frames = failure_frames(direct_format)
    layered_frames = failure_frames(layered_format)

    print(f"python_version={sys.version.split()[0]}")
    print(f"platform={platform.platform()}")
    print(f"sample_count={len(samples)}")
    print(
        "behavior_parity="
        f"{all(direct_format(x) == layered_format(x) for x in samples)}"
    )
    print(f"direct_design_nodes={len(direct_graph)}")
    print(f"direct_design_edges={edge_count(direct_graph)}")
    print(f"layered_design_nodes={len(layered_graph)}")
    print(f"layered_design_edges={edge_count(layered_graph)}")
    print(f"direct_failure_frames={direct_frames}")
    print(f"layered_failure_frames={layered_frames}")
    print(
        "bounded_judgment=no demonstrated change-locality benefit in this "
        "fixed single-source/single-policy scenario"
    )


if __name__ == "__main__":
    main()
