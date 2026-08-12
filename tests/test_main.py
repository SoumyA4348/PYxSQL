import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import run_demo

def test_run_demo_mocked():
    """Verifies that run_demo calls the expected DatabaseManager methods."""
    with patch('main.DatabaseManager') as MockDB:
        mock_db_instance = MockDB.return_value
        # Mocking context manager behavior:
        mock_db_instance.__enter__.return_value = mock_db_instance
        
        # Setup mock returns
        mock_db_instance.fetch_all.return_value = [(1, "Alice", 22, "alice@example.com")]
        mock_db_instance.fetch_one.return_value = [22.0]
        mock_db_instance.execute_many.return_value = 3
        
        run_demo()
        
        # Verify key calls
        mock_db_instance.setup_database.assert_called_once()
        assert mock_db_instance.execute_query.call_count >= 2 # Create tables, Update, Delete
        mock_db_instance.execute_many.assert_called_once()
        assert mock_db_instance.fetch_all.call_count >= 1
        mock_db_instance.fetch_one.assert_called()
