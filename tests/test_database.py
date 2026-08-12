import sys
import os
import pytest
from unittest.mock import MagicMock, patch

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

@pytest.fixture
def mock_db_config():
    return {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "",
        "database": "test_db",
    }

@pytest.fixture
def db_manager(mock_db_config):
    return DatabaseManager(config=mock_db_config)

def test_connect(db_manager):
    with patch('mysql.connector.connect') as mock_connect:
        db_manager.connect()
        mock_connect.assert_called_once_with(**db_manager.config)

def test_execute_query(db_manager):
    with patch('mysql.connector.connect') as mock_connect:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.rowcount = 1
        
        count = db_manager.execute_query("UPDATE table SET col = %s", ("val",))
        
        assert count == 1
        mock_cursor.execute.assert_called_once_with("UPDATE table SET col = %s", ("val",))
        mock_conn.commit.assert_called_once()

def test_fetch_all(db_manager):
    with patch('mysql.connector.connect') as mock_connect:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(1, "Alice"), (2, "Bob")]
        
        results = db_manager.fetch_all("SELECT * FROM users")
        
        assert len(results) == 2
        assert results[0][1] == "Alice"
        mock_cursor.execute.assert_called_once_with("SELECT * FROM users", ())

def test_context_manager(db_manager):
    with patch('mysql.connector.connect') as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.is_connected.return_value = True
        
        with db_manager as db:
            assert db.connection == mock_conn
            
        mock_conn.close.assert_called_once()
