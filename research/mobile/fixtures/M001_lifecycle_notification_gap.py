"""M001 bounded model fixture: lifecycle notifications are not durability guarantees.

This is NOT Flutter/Android/iOS runtime evidence. It is an executable model derived
from documented platform/framework behavior: lifecycle notifications can be skipped
under abrupt termination, so correctness that depends on receiving a later lifecycle
callback has an uncovered failure path.
"""

from dataclasses import dataclass
import platform
import sys


NORMAL_BACKGROUND = ["resumed", "inactive", "hidden", "paused", "TERMINATED"]
ABRUPT_TERMINATION = ["resumed", "TERMINATED"]


@dataclass
class SaveOnPausedApp:
    draft: str = ""
    durable: str = ""

    def edit(self, value: str) -> None:
        self.draft = value

    def lifecycle(self, state: str) -> None:
        if state == "paused":
            self.durable = self.draft


@dataclass
class SaveAtMutationBoundaryApp:
    draft: str = ""
    durable: str = ""

    def edit(self, value: str) -> None:
        self.draft = value
        # Model an application-level commit at the semantic mutation boundary.
        # This says nothing about real filesystem/power-loss durability.
        self.durable = value

    def lifecycle(self, state: str) -> None:
        pass


def run(app_type, sequence: list[str]) -> str:
    app = app_type()
    app.edit("flight-123")
    for state in sequence:
        if state == "TERMINATED":
            break
        app.lifecycle(state)
    return app.durable


def main() -> None:
    normal_late = run(SaveOnPausedApp, NORMAL_BACKGROUND)
    abrupt_late = run(SaveOnPausedApp, ABRUPT_TERMINATION)
    normal_boundary = run(SaveAtMutationBoundaryApp, NORMAL_BACKGROUND)
    abrupt_boundary = run(SaveAtMutationBoundaryApp, ABRUPT_TERMINATION)

    assert normal_late == "flight-123"
    assert abrupt_late == ""  # deliberate failure exposure
    assert normal_boundary == "flight-123"
    assert abrupt_boundary == "flight-123"

    print(f"python_version={sys.version.split()[0]}")
    print(f"platform={platform.platform()}")
    print(f"normal_save_on_paused={normal_late!r}")
    print(f"abrupt_save_on_paused={abrupt_late!r}")
    print(f"normal_save_at_mutation={normal_boundary!r}")
    print(f"abrupt_save_at_mutation={abrupt_boundary!r}")
    print("verdict=lifecycle callback arrival cannot be the sole commit guarantee")


if __name__ == "__main__":
    main()
