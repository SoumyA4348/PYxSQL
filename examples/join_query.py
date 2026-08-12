import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    search = input("Enter email search pattern (e.g. example.com): ")
    query = """
        SELECT info.id, info.name, info.age, contact.email, contact.phone_number
        FROM info
        JOIN contact ON contact.id = info.id
        WHERE contact.email LIKE %s
    """
    with db:
        results = db.fetch_all(query, ('%' + search + '%',))
        if results:
            for row in results:
                print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Email: {row[3]} | Phone: {row[4]}")
        else:
            print("No matching records found.")

if __name__ == "__main__":
    main()
