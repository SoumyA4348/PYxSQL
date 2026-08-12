import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    with db:
        print("=== User Login Verification ===")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        query = "SELECT * FROM login WHERE username = %s AND password = %s"
        result = db.fetch_all(query, (username, password))

        if result:
            print("[SUCCESS] Login successful!")
        else:
            print("[FAILED] Invalid credentials.")

if __name__ == "__main__":
    main()
