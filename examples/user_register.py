import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager
from auth import CREATE_LOGIN_TABLE, register_user

def main():
    db = DatabaseManager()
    with db:
        db.execute_query(CREATE_LOGIN_TABLE)

        print("=== User Registration ===")
        username = input("Enter username: ").strip()
        password = input("Enter password: ")

        if register_user(db, username, password):
            print("[OK] User registered successfully.")

if __name__ == "__main__":
    main()
