import os
import tempfile
import pytest
from pathlib import Path
import DAL
from app import app as flask_app

@pytest.fixture
def app():
    """Create application for testing"""
    return flask_app

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def test_db():
    """Create a temporary test database"""
    db_fd, db_path = tempfile.mkstemp()
    old_db_path = DAL.DB_PATH
    DAL.DB_PATH = Path(db_path)
    DAL.create_table()
    
    yield db_path
    
    os.close(db_fd)
    os.unlink(db_path)
    DAL.DB_PATH = old_db_path

@pytest.fixture
def sample_project():
    """Sample project data for tests"""
    return {
        "title": "Test Project",
        "description": "A test project description",
        "imageFileName": "images/test.jpg"
    }