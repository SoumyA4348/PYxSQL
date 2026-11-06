import sys
import os
from unittest.mock import MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auth import hash_password, verify_password, register_user, verify_login


def test_hash_is_salted_and_not_plaintext():
    a, b = hash_password("hunter2"), hash_password("hunter2")
    assert a != b
    assert "hunter2" not in a
    assert a.startswith("scrypt$")


def test_verify_password_accepts_correct_and_rejects_wrong():
    stored = hash_password("correct horse")
    assert verify_password("correct horse", stored)
    assert not verify_password("wrong horse", stored)


def test_verify_password_is_case_and_whitespace_sensitive():
    stored = hash_password("Secret pass")
    assert not verify_password("secret pass", stored)
    assert not verify_password("Secret pass ", stored)


def test_verify_password_rejects_malformed_stored_values():
    for bad in ["", "plaintext", "scrypt$1$2", "bcrypt$16384$8$1$aa$bb", "scrypt$x$8$1$zz$00"]:
        assert not verify_password("anything", bad)


def test_register_user_stores_hash_not_password():
    db = MagicMock()
    db.execute_query.return_value = 1
    assert register_user(db, "alice", "pw123")
    query, params = db.execute_query.call_args[0]
    assert "password_hash" in query and "%s" in query
    assert params[0] == "alice"
    assert params[1] != "pw123" and params[1].startswith("scrypt$")


def test_verify_login_unknown_user_is_false():
    db = MagicMock()
    db.fetch_one.return_value = None
    assert not verify_login(db, "ghost", "pw")


def test_verify_login_checks_hash():
    db = MagicMock()
    db.fetch_one.return_value = (hash_password("pw123"),)
    assert verify_login(db, "alice", "pw123")
    assert not verify_login(db, "alice", "nope")
