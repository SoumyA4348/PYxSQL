"""
PYxSQL — Python + MySQL demo runner.
Refactored using OOP DatabaseManager.
"""

from database import DatabaseManager

def run_demo():
    db = DatabaseManager()
    
    print("=== PYxSQL Demo ===\n")
    
    # 1. Setup
    db.setup_database()
    
    with db:
        # 2. Create Tables
        db.execute_query("""
            CREATE TABLE IF NOT EXISTS info (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        """)
        db.execute_query("""
            CREATE TABLE IF NOT EXISTS contact (
                contact_id INT PRIMARY KEY AUTO_INCREMENT,
                id INT,
                phone_number VARCHAR(20),
                FOREIGN KEY (id) REFERENCES info(id) ON DELETE CASCADE
            )
        """)
        print("[OK] Tables created.")

        # 3. Insert Sample Data
        users = [
            ("Alice Johnson", 22, "alice@example.com"),
            ("Bob Smith",     25, "bob@example.com"),
            ("Carol White",   19, "carol@example.com"),
        ]
        count = db.execute_many(
            "INSERT IGNORE INTO info (name, age, email) VALUES (%s, %s, %s)", users
        )
        print(f"[OK] Inserted {count} row(s).")

        # 4. Fetch All
        rows = db.fetch_all("SELECT * FROM info")
        print("\n--- All Users ---")
        for row in rows:
            print(row)

        # 5. Update
        db.execute_query("UPDATE info SET email = %s WHERE id = %s", ("alice_updated@example.com", 1))
        print("[OK] Updated user 1.")

        # 6. Average Age
        result = db.fetch_one("SELECT AVG(age) FROM info")
        avg = result[0] if result and result[0] is not None else 0
        print(f"\nAverage age: {avg:.2f}")

        # 7. Login Verification
        email, name = 'bob@example.com', 'Bob Smith'
        found = db.fetch_one("SELECT id FROM info WHERE email = %s AND name = %s", (email, name))
        print(f"\nLogin check (valid):   {found is not None}")

        # 8. Delete
        db.execute_query("DELETE FROM info WHERE name = %s", ("Carol White",))
        print("[OK] Deleted Carol White.")

        # Final Fetch
        rows = db.fetch_all("SELECT * FROM info")
        print("\n--- Final Users ---")
        for row in rows:
            print(row)

    print("\n[DONE]")

if __name__ == "__main__":
    run_demo()
