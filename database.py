import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from typing import List, Tuple, Any, Optional, Dict

load_dotenv()

class DatabaseManager:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        if config:
            self.config = config
        else:
            self.config = {
                "host": os.getenv("DB_HOST", "localhost"),
                "port": int(os.getenv("DB_PORT", 3306)),
                "user": os.getenv("DB_USER", "root"),
                "password": os.getenv("DB_PASSWORD", ""),
                "database": os.getenv("DB_NAME", "pyxsql_demo"),
            }
        self.connection = None

    def connect(self, include_db: bool = True):
        """Establishes a connection to the MySQL server."""
        try:
            cfg = self.config.copy()
            if not include_db:
                cfg.pop("database", None)
            
            self.connection = mysql.connector.connect(**cfg)
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def close(self):
        """Closes the current connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> int:
        """Executes a non-returning query (INSERT, UPDATE, DELETE)."""
        cursor = None
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Query error: {e}")
            if self.connection:
                self.connection.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def execute_many(self, query: str, data: List[Tuple]) -> int:
        """Executes a query against multiple data records."""
        cursor = None
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()
            cursor = self.connection.cursor()
            cursor.executemany(query, data)
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Executemany error: {e}")
            if self.connection:
                self.connection.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def fetch_all(self, query: str, params: Optional[Tuple] = None) -> List[Tuple]:
        """Executes a query and returns all result rows."""
        cursor = None
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Error as e:
            print(f"Fetch error: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def fetch_one(self, query: str, params: Optional[Tuple] = None) -> Optional[Tuple]:
        """Executes a query and returns a single result row."""
        cursor = None
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchone()
        except Error as e:
            print(f"Fetch one error: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def setup_database(self):
        """Creates the database if it doesn't exist."""
        db_name = self.config.get("database")
        cfg_no_db = self.config.copy()
        cfg_no_db.pop("database", None)
        
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**cfg_no_db)
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            conn.commit()
            print(f"[OK] Database '{db_name}' ready.")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
