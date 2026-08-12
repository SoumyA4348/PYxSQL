import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    n = int(input("Enter the number of records to insert: "))
    records = []
    for i in range(n):
        print(f"\n--- Record {i+1} ---")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")
        records.append((name, age, email))

    query = "INSERT INTO info (name, age, email) VALUES (%s, %s, %s)"
    with db:
        count = db.execute_many(query, records)
        print(f"\n[OK] {count} row(s) inserted successfully.")

if __name__ == "__main__":
    main()
