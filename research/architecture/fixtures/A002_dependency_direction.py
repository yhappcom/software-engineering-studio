"""A002 bounded comparison: policy dependency versus mechanism dependency.

Shows a mechanism representation/API change forcing a policy edit when policy
knows the concrete detail, while a policy-owned semantic contract localizes the
change to an adapter. This does not prove interfaces are always beneficial.
"""

class FileSettings:
    def __init__(self, units="minutes"):
        self.units = units

    def read_units(self):
        return self.units


class BadSummaryPolicy:
    def __init__(self, settings: FileSettings):
        self.settings = settings

    def display(self, minutes):
        units = self.settings.read_units()
        if units == "minutes":
            return f"{minutes} min"
        if units == "hours":
            return f"{minutes / 60:.1f} h"
        raise ValueError(units)


class UnitPreference:
    def unit(self):
        raise NotImplementedError


class FileUnitPreference(UnitPreference):
    def __init__(self, settings):
        self.settings = settings

    def unit(self):
        return self.settings.read_units()


class GoodSummaryPolicy:
    def __init__(self, preference: UnitPreference):
        self.preference = preference

    def display(self, minutes):
        units = self.preference.unit()
        if units == "minutes":
            return f"{minutes} min"
        if units == "hours":
            return f"{minutes / 60:.1f} h"
        raise ValueError(units)


class RemoteSettings:
    def __init__(self, metric=True):
        self.metric = metric

    def fetch(self):
        return {"display_hours": not self.metric}


# Direct-detail design: policy must change to understand the new mechanism API.
class BadSummaryPolicyV2:
    def __init__(self, settings: RemoteSettings):
        self.settings = settings

    def display(self, minutes):
        raw = self.settings.fetch()
        units = "hours" if raw["display_hours"] else "minutes"
        if units == "minutes":
            return f"{minutes} min"
        return f"{minutes / 60:.1f} h"


# Inverted design: semantic policy is unchanged; only the detail adapter changes.
class RemoteUnitPreference(UnitPreference):
    def __init__(self, settings):
        self.settings = settings

    def unit(self):
        return "hours" if self.settings.fetch()["display_hours"] else "minutes"


def main():
    assert BadSummaryPolicy(FileSettings("hours")).display(90) == "1.5 h"
    assert GoodSummaryPolicy(FileUnitPreference(FileSettings("hours"))).display(90) == "1.5 h"
    assert BadSummaryPolicyV2(RemoteSettings(metric=False)).display(90) == "1.5 h"
    assert GoodSummaryPolicy(RemoteUnitPreference(RemoteSettings(metric=False))).display(90) == "1.5 h"

    print("behavior_parity=True")
    print("bad_policy_changed_for_mechanism_change=True")
    print("good_policy_changed_for_mechanism_change=False")
    print("good_detail_adapter_changed=True")


if __name__ == "__main__":
    main()
