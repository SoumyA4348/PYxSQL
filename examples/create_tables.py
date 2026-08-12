import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

def main():
    db = DatabaseManager()
    query = """
    CREATE TABLE IF NOT EXISTS contact (
        contact_id INT PRIMARY KEY AUTO_INCREMENT,
        id INT,
        email VARCHAR(50),
        phone_number VARCHAR(20),
        FOREIGN KEY (id) REFERENCES info(id) ON DELETE CASCADE
    )
    """
    with db:
        db.execute_query(query)
        print("[OK] Table 'contact' created or already exists.")

if __name__ == "__main__":
    main()
