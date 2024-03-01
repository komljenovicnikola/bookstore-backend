from fastapi.testclient import TestClient

from app.main import app
from unittest.mock import patch

client = TestClient(app)


@patch('app.api.endpoints.book.Book.create_and_borrow')
def test_borrow_book_success(mock_borrow):
    mock_book_data = {
        "id": 1,
        "title": "test book",
        "author": "test author",
        "year": 2021
    }
    mock_borrow.return_value = mock_book_data

    request_payload = {
        "title": "test book",
        "author": "test author",
        "year": 2021,
        "user_id": 1
    }
    response = client.post("/books/borrow", json=request_payload)

    assert response.status_code == 201

    assert response.json() == mock_book_data


def test_borrow_book_invalid_payload():
    invalid_payload = {}
    response = client.post("/books/borrow", json=invalid_payload)
    assert response.status_code == 422
