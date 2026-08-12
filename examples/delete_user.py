import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    n = int(input("Enter the number of records to delete: "))
    names = []
    for _ in range(n):
        name = input("Enter name to delete: ")
        names.append((name,))

    query = "DELETE FROM info WHERE name = %s"
    with db:
        count = db.execute_many(query, names)
        print(f"[OK] Successfully deleted {count} record(s).")

if __name__ == "__main__":
    main()
