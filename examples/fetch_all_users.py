import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    with db:
        rows = db.fetch_all("SELECT * FROM info")
        print("\n--- All Records in 'info' ---")
        for row in rows:
            print(row)

if __name__ == "__main__":
    main()
