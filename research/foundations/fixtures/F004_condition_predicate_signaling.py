#!/usr/bin/env python3
import platform
import sys
import threading


def notification_as_state_failure():
    """Show that a past notify is not durable application state for a later waiter."""
    cv = threading.Condition()
    state = {"ready": False}
    observed = {}

    # Producer completes before the waiter exists.
    with cv:
        state["ready"] = True
        cv.notify()  # no waiter exists; notification is not queued for the future

    def waiter():
        with cv:
            observed["notified"] = cv.wait(timeout=0.05)
            observed["ready_after_timeout"] = state["ready"]

    t = threading.Thread(target=waiter)
    t.start()
    t.join(timeout=1)
    assert not t.is_alive(), "bounded waiter failed to terminate"
    return observed


def predicate_state_alternative():
    """Wait for the durable predicate rather than treating notification as the state."""
    cv = threading.Condition()
    state = {"ready": False}
    observed = {}

    with cv:
        state["ready"] = True
        cv.notify()

    def waiter():
        with cv:
            observed["predicate_satisfied"] = cv.wait_for(
                lambda: state["ready"], timeout=0.05
            )
            observed["ready"] = state["ready"]

    t = threading.Thread(target=waiter)
    t.start()
    t.join(timeout=1)
    assert not t.is_alive(), "bounded predicate waiter failed to terminate"
    return observed


def main():
    failure = notification_as_state_failure()
    alternative = predicate_state_alternative()
    print("python", sys.version.split()[0], "platform", platform.platform())
    print("notification_as_state", failure)
    print("predicate_state", alternative)

    assert failure == {"notified": False, "ready_after_timeout": True}, failure
    assert alternative == {"predicate_satisfied": True, "ready": True}, alternative
    print("PASS")


if __name__ == "__main__":
    main()
