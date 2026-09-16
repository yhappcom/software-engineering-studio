"""A002 bounded fixture: one mutation authority vs accidental second writer.

A derived projection may be cached/read independently, but it must not become an
independent mutation authority unless reconciliation semantics explicitly say so.
"""
from dataclasses import dataclass

@dataclass
class Flight:
    id: str
    minutes: int

class Ledger:
    def __init__(self, rows):
        self._rows = {r.id: r for r in rows}
        self.revision = 0

    def all(self):
        return list(self._rows.values())

    def replace(self, flight):
        self._rows[flight.id] = flight
        self.revision += 1

class Projection:
    def __init__(self, ledger):
        self.ledger = ledger
        self.revision = -1
        self.total = 0

    def refresh(self):
        self.total = sum(x.minutes for x in self.ledger.all())
        self.revision = self.ledger.revision

    def read(self):
        if self.revision != self.ledger.revision:
            raise RuntimeError("stale projection")
        return self.total

def bad_ui_direct_projection_write(ledger, projection, flight_id, minutes):
    # Accidental second writer: derived state changes while authority does not.
    old = next(x.minutes for x in ledger.all() if x.id == flight_id)
    projection.total += minutes - old
    projection.revision = ledger.revision

def good_edit(ledger, projection, flight_id, minutes):
    ledger.replace(Flight(flight_id, minutes))
    try:
        projection.read()
    except RuntimeError:
        pass
    else:
        raise AssertionError("stale projection should be rejected")
    projection.refresh()

def main():
    ledger = Ledger([Flight("A", 60), Flight("B", 90)])
    projection = Projection(ledger)
    projection.refresh()
    assert projection.read() == 150

    bad_ui_direct_projection_write(ledger, projection, "A", 120)
    assert projection.read() == 210
    authoritative = sum(x.minutes for x in ledger.all())
    print("bad_projection_total", projection.read())
    print("authoritative_total", authoritative)
    assert projection.read() != authoritative

    # Rebuild from authority destroys the unauthorized derived mutation.
    projection.refresh()
    assert projection.read() == 150
    print("bad_write_lost_after_rebuild", True)

    good_edit(ledger, projection, "A", 120)
    assert projection.read() == 210
    assert sum(x.minutes for x in ledger.all()) == 210
    print("good_authority_projection_equal", True)
    print("ledger_revision", ledger.revision)
    print("projection_revision", projection.revision)

if __name__ == "__main__":
    main()
