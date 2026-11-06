import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager
from auth import verify_login

def main():
    db = DatabaseManager()
    with db:
        print("=== User Login Verification ===")
        username = input("Enter username: ").strip()
        password = input("Enter password: ")

        if verify_login(db, username, password):
            print("[SUCCESS] Login successful!")
        else:
            print("[FAILED] Invalid credentials.")

if __name__ == "__main__":
    main()
