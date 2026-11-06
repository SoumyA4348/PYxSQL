import hashlib
import hmac
import os
from typing import Optional

from database import DatabaseManager

# scrypt cost parameters (stdlib, no extra dependency)
_N, _R, _P = 2 ** 14, 8, 1

CREATE_LOGIN_TABLE = """
    CREATE TABLE IF NOT EXISTS login (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(100) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL
    )
"""


def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    """Returns 'scrypt$N$r$p$salt_hex$hash_hex' for storage."""
    salt = salt or os.urandom(16)
    digest = hashlib.scrypt(password.encode("utf-8"), salt=salt, n=_N, r=_R, p=_P)
    return f"scrypt${_N}${_R}${_P}${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    """Checks a password against a stored hash in constant time."""
    try:
        scheme, n, r, p, salt_hex, hash_hex = stored.split("$")
        if scheme != "scrypt":
            return False
        digest = hashlib.scrypt(
            password.encode("utf-8"), salt=bytes.fromhex(salt_hex), n=int(n), r=int(r), p=int(p)
        )
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(digest.hex(), hash_hex)


def register_user(db: DatabaseManager, username: str, password: str) -> bool:
    """Creates a login row with a hashed password. Returns True if a row was inserted."""
    count = db.execute_query(
        "INSERT INTO login (username, password_hash) VALUES (%s, %s)",
        (username, hash_password(password)),
    )
    return count > 0


def verify_login(db: DatabaseManager, username: str, password: str) -> bool:
    """Looks the user up by name, then verifies the password against the stored hash."""
    row = db.fetch_one("SELECT password_hash FROM login WHERE username = %s", (username,))
    return bool(row) and verify_password(password, row[0])
