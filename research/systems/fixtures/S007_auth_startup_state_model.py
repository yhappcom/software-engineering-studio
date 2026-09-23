#!/usr/bin/env python3
"""Executable S007 startup/auth state model.

This is a reusable semantic fixture, not LogMate product code and not Firebase runtime evidence.
It exercises fail-closed routing and idempotent owner initialization under duplicate/replayed
Auth observations.
"""
from dataclasses import dataclass, replace
from enum import Enum, auto
import unittest

class Auth(Enum):
    UNRESOLVED = auto()
    SIGNED_OUT = auto()
    AUTHENTICATED = auto()
    INIT_FAILURE = auto()

class Setup(Enum):
    INCOMPLETE = auto()
    COMPLETE = auto()

class Route(Enum):
    STARTUP = auto()
    WELCOME = auto()
    ONBOARDING = auto()
    HOME = auto()
    RECOVERY = auto()

@dataclass(frozen=True)
class State:
    auth: Auth = Auth.UNRESOLVED
    auth_uid: str | None = None
    owner_uid: str | None = None
    setup: Setup = Setup.INCOMPLETE
    owner_init_count: int = 0
    explicit_sign_out: bool = False


def route(s: State) -> Route:
    if s.auth in (Auth.UNRESOLVED, Auth.INIT_FAILURE):
        return Route.STARTUP
    if s.auth is Auth.SIGNED_OUT:
        return Route.WELCOME
    assert s.auth is Auth.AUTHENTICATED and s.auth_uid
    if s.owner_uid is not None and s.owner_uid != s.auth_uid:
        return Route.RECOVERY
    if s.owner_uid is None or s.setup is Setup.INCOMPLETE:
        return Route.ONBOARDING
    return Route.HOME


def observe_authenticated(s: State, uid: str) -> State:
    """Observe Firebase-authenticated UID; initialize owner exactly once or fail closed."""
    s = replace(s, auth=Auth.AUTHENTICATED, auth_uid=uid, explicit_sign_out=False)
    if s.owner_uid is None:
        return replace(s, owner_uid=uid, owner_init_count=s.owner_init_count + 1)
    return s


def observe_init_failure(s: State) -> State:
    """Transport/init failure is not explicit sign-out and does not mutate owner."""
    return replace(s, auth=Auth.INIT_FAILURE, auth_uid=None)


def explicit_sign_out(s: State) -> State:
    """Explicit user intent locks routing but retains owner binding."""
    return replace(s, auth=Auth.SIGNED_OUT, auth_uid=None, explicit_sign_out=True)


class S007StartupModelTests(unittest.TestCase):
    def test_unresolved_never_routes_welcome_or_home(self):
        self.assertEqual(route(State()), Route.STARTUP)

    def test_init_failure_is_not_signout_and_preserves_owner(self):
        before = State(owner_uid="u1", setup=Setup.COMPLETE)
        after = observe_init_failure(before)
        self.assertEqual(route(after), Route.STARTUP)
        self.assertEqual(after.owner_uid, "u1")
        self.assertFalse(after.explicit_sign_out)

    def test_duplicate_auth_callback_initializes_owner_once(self):
        s = observe_authenticated(State(), "u1")
        s = observe_authenticated(s, "u1")
        s = observe_authenticated(s, "u1")
        self.assertEqual(s.owner_uid, "u1")
        self.assertEqual(s.owner_init_count, 1)
        self.assertEqual(route(s), Route.ONBOARDING)

    def test_wrong_uid_fails_closed_without_rebind(self):
        s = State(owner_uid="u1", setup=Setup.COMPLETE)
        after = observe_authenticated(s, "u2")
        self.assertEqual(route(after), Route.RECOVERY)
        self.assertEqual(after.owner_uid, "u1")
        self.assertEqual(after.owner_init_count, 0)

    def test_matching_complete_owner_routes_home(self):
        s = observe_authenticated(State(owner_uid="u1", setup=Setup.COMPLETE), "u1")
        self.assertEqual(route(s), Route.HOME)

    def test_matching_incomplete_owner_resumes_onboarding(self):
        s = observe_authenticated(State(owner_uid="u1", setup=Setup.INCOMPLETE), "u1")
        self.assertEqual(route(s), Route.ONBOARDING)

    def test_explicit_signout_retains_owner_and_routes_welcome(self):
        s = observe_authenticated(State(owner_uid="u1", setup=Setup.COMPLETE), "u1")
        after = explicit_sign_out(s)
        self.assertEqual(route(after), Route.WELCOME)
        self.assertEqual(after.owner_uid, "u1")
        self.assertTrue(after.explicit_sign_out)

    def test_reauthentication_after_explicit_signout_restores_home(self):
        s = explicit_sign_out(State(owner_uid="u1", setup=Setup.COMPLETE))
        after = observe_authenticated(s, "u1")
        self.assertEqual(route(after), Route.HOME)
        self.assertFalse(after.explicit_sign_out)
        self.assertEqual(after.owner_init_count, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
