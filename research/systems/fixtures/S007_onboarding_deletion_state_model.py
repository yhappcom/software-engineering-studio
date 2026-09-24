#!/usr/bin/env python3
"""Bounded executable oracle for LogMate S007 onboarding/deletion semantics.

This is a Studio reference model, not LogMate production code.
"""
from dataclasses import dataclass, replace
from enum import Enum, auto
import unittest

class Setup(Enum):
    NONE = auto(); NEW = auto(); PREVIOUS_TOTAL = auto(); IMPORT = auto()

class Delete(Enum):
    NONE = auto(); LOCKED = auto(); REMOTE_ERASED = auto(); IDENTITY_DELETED = auto(); COMPLETE = auto()

@dataclass(frozen=True)
class State:
    uid: str | None
    owner_uid: str | None
    setup: Setup = Setup.NONE
    setup_complete: bool = False
    deletion: Delete = Delete.NONE
    local_data: bool = False
    remote_data: bool = False

class ContractError(Exception): pass

def bind_owner(s: State) -> State:
    if not s.uid: raise ContractError("auth required")
    if s.owner_uid not in (None, s.uid): raise ContractError("owner mismatch")
    return replace(s, owner_uid=s.uid, local_data=True, remote_data=True)

def choose_setup(s: State, setup: Setup) -> State:
    if s.deletion is not Delete.NONE: raise ContractError("deletion locked")
    if s.owner_uid != s.uid or not s.uid: raise ContractError("matching owner required")
    if setup is Setup.NONE: raise ContractError("semantic setup required")
    if s.setup is not Setup.NONE and s.setup != setup: raise ContractError("initial setup already selected")
    return replace(s, setup=setup)

def complete_setup(s: State) -> State:
    if s.setup is Setup.NONE: raise ContractError("no setup selected")
    if s.deletion is not Delete.NONE: raise ContractError("deletion locked")
    return replace(s, setup_complete=True)

def route(s: State) -> str:
    if s.deletion is not Delete.NONE: return "deletion"
    if not s.uid: return "welcome"
    if s.owner_uid != s.uid: return "identity_recovery"
    return "home" if s.setup_complete else "onboarding"

def request_delete(s: State, reauth_uid: str) -> State:
    if not s.uid or s.uid != s.owner_uid or reauth_uid != s.uid:
        raise ContractError("same-uid reauth required")
    return replace(s, deletion=Delete.LOCKED)

def remote_erased(s: State) -> State:
    if s.deletion is not Delete.LOCKED: raise ContractError("delete not locked")
    return replace(s, deletion=Delete.REMOTE_ERASED, remote_data=False)

def identity_deleted(s: State) -> State:
    if s.deletion is not Delete.REMOTE_ERASED: raise ContractError("remote erasure required")
    # Keep owner_uid and deletion marker durable: signed-out is not first-use.
    return replace(s, uid=None, deletion=Delete.IDENTITY_DELETED)

def local_erased_complete(s: State) -> State:
    if s.deletion is not Delete.IDENTITY_DELETED: raise ContractError("identity deletion required")
    return replace(s, owner_uid=None, setup=Setup.NONE, setup_complete=False,
                   deletion=Delete.COMPLETE, local_data=False)

class S007ModelTests(unittest.TestCase):
    def fresh(self): return bind_owner(State(uid="A", owner_uid=None))

    def test_each_initial_setup_requires_explicit_completion(self):
        for method in (Setup.NEW, Setup.PREVIOUS_TOTAL, Setup.IMPORT):
            with self.subTest(method=method):
                s=choose_setup(self.fresh(), method)
                self.assertEqual(route(s), "onboarding")
                self.assertEqual(route(complete_setup(s)), "home")

    def test_route_not_inferred_from_data_presence(self):
        s=replace(self.fresh(), local_data=True, remote_data=True)
        self.assertEqual(route(s), "onboarding")

    def test_owner_mismatch_fails_closed(self):
        s=State(uid="B", owner_uid="A", local_data=True)
        self.assertEqual(route(s), "identity_recovery")
        with self.assertRaises(ContractError): choose_setup(s, Setup.NEW)

    def test_setup_method_cannot_be_rewritten_during_initial_setup(self):
        s=choose_setup(self.fresh(), Setup.IMPORT)
        with self.assertRaises(ContractError): choose_setup(s, Setup.NEW)

    def test_deletion_locks_home_immediately(self):
        s=complete_setup(choose_setup(self.fresh(), Setup.NEW))
        self.assertEqual(route(s), "home")
        locked=request_delete(s, "A")
        self.assertEqual(route(locked), "deletion")
        self.assertTrue(locked.local_data)

    def test_deletion_reauth_must_preserve_uid(self):
        s=complete_setup(choose_setup(self.fresh(), Setup.NEW))
        with self.assertRaises(ContractError): request_delete(s, "B")

    def test_identity_absence_is_not_erasure_or_first_use(self):
        s=request_delete(complete_setup(choose_setup(self.fresh(), Setup.NEW)), "A")
        s=identity_deleted(remote_erased(s))
        self.assertIsNone(s.uid)
        self.assertTrue(s.local_data)
        self.assertEqual(route(s), "deletion")

    def test_completion_requires_local_erasure(self):
        s=request_delete(complete_setup(choose_setup(self.fresh(), Setup.NEW)), "A")
        s=identity_deleted(remote_erased(s))
        done=local_erased_complete(s)
        self.assertFalse(done.local_data)
        self.assertFalse(done.remote_data)
        self.assertIsNone(done.owner_uid)
        self.assertEqual(done.deletion, Delete.COMPLETE)
        self.assertEqual(route(done), "deletion")  # terminal deleted state is not ordinary Welcome

    def test_crash_restart_marker_blocks_stale_ledger_after_identity_delete(self):
        s=request_delete(complete_setup(choose_setup(self.fresh(), Setup.PREVIOUS_TOTAL)), "A")
        persisted=identity_deleted(remote_erased(s))
        # Reconstruction from durable fields must remain deletion-locked.
        restarted=State(**persisted.__dict__)
        self.assertEqual(route(restarted), "deletion")
        self.assertTrue(restarted.local_data)

if __name__ == "__main__": unittest.main(verbosity=2)
