"""Q002 bounded evidence: a passing isolated component test does not prove integration wiring."""

class Repository:
    def __init__(self):
        self.rows = []

    def save(self, value):
        self.rows.append(value)


class FakeRepository:
    def __init__(self):
        self.rows = []

    def save(self, value):
        self.rows.append(value)


class Service:
    def __init__(self, repository):
        self.repository = repository

    def add(self, value):
        if value <= 0:
            raise ValueError("value must be positive")
        self.repository.save(value)


def isolated_component_test():
    repository = FakeRepository()
    Service(repository).add(7)
    assert repository.rows == [7]


def integration_control_test():
    repository = Repository()
    Service(repository).add(7)
    assert repository.rows == [7]


def integration_broken_wiring_test():
    class BrokenRepository(Repository):
        def save(self, value):
            pass  # deliberate integration defect: write is silently dropped

    repository = BrokenRepository()
    Service(repository).add(7)
    assert repository.rows == [7]


def main():
    isolated_component_test()
    integration_control_test()
    try:
        integration_broken_wiring_test()
    except AssertionError:
        print("isolated_component_test=PASS")
        print("integration_control_test=PASS")
        print("integration_broken_wiring_test=FAIL_EXPECTED")
        print("root_cause=real_collaborator_contract/wiring defect outside isolated fake")
        print("bounded_conclusion=unit/component pass does not establish integration correctness")
        return
    raise AssertionError("deliberate integration defect was expected to fail")


if __name__ == "__main__":
    main()
