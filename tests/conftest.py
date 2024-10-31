import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def fastapi_client():
    # Initializes and provides the FastAPI test client
    return TestClient(app)

