from fastapi.testclient import TestClient

from app.main import app
from unittest.mock import patch

client = TestClient(app)


@patch('app.api.endpoints.user.User.register')
def test_register_user_success(mock_register):
    mock_user_data = {
        "id": 1,
        "email": "test@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "role": "customer"
    }
    mock_register.return_value = mock_user_data

    request_payload = {
        "email": "test@example.com",
        "password": "password123",
        "first_name": "John",
        "last_name": "Doe",
        "role": "customer"
    }
    response = client.post("/users/register", json=request_payload)

    assert response.status_code == 201

    assert response.json() == mock_user_data


def test_register_user_invalid_payload():
    invalid_payload = {}
    response = client.post("/users/register", json=invalid_payload)
    assert response.status_code == 422
