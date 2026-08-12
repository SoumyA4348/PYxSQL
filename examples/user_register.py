import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    with db:
        db.execute_query("""
            CREATE TABLE IF NOT EXISTS login (
                id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)

        print("=== User Registration ===")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        query = "INSERT INTO login (username, password) VALUES (%s, %s)"
        count = db.execute_query(query, (username, password))
        if count > 0:
            print("[OK] User registered successfully.")

if __name__ == "__main__":
    main()
