import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    with db:
        # SQL aggregate function method
        result = db.fetch_one("SELECT AVG(age) FROM info")
        if result and result[0] is not None:
            print(f"[SQL Aggregate] Average age: {result[0]:.2f}")
        else:
            print("No data found in database.")

        # Programmatic Python calculation method
        rows = db.fetch_all("SELECT age FROM info")
        if rows:
            ages = [r[0] for r in rows if isinstance(r[0], int)]
            if ages:
                py_avg = sum(ages) / len(ages)
                print(f"[Python In-Memory] Average age across {len(ages)} records: {py_avg:.2f}")

if __name__ == "__main__":
    main()
