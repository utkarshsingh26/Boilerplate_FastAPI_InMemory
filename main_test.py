import pytest
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI instance

client = TestClient(app)

def test_create_book_api():
    """Test the POST /books/{title} endpoint."""
    payload = {
        "title": "Mistborn",
        "genre": "FANTASY", # Matches your Enum
        "price": 25.0,
        "stock_count": 10
    }
    response = client.post("/books/Mistborn", json=payload)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Book added to catalog"}

def test_get_catalog_api():
    """Test the GET /catalog endpoint and pricing logic."""
    # First, add a rare book (low stock)
    client.post("/books/TheWayOfKings", json={
        "title": "The Way of Kings",
        "genre": "FANTASY",
        "price": 10.0,
        "stock_count": 2
    })
    
    response = client.get("/catalog")
    assert response.status_code == 200
    
    # Check if the dynamic pricing was applied correctly
    # (10.0 * 1.2 rare) * 0.9 fantasy = 10.8
    catalog = response.json()
    book = next(b for b in catalog if b["title"] == "The Way of Kings")
    assert book["price"] == pytest.approx(10.8)

def test_purchase_not_found():
    """Test 404 behavior for a non-existent book."""
    response = client.post("/purchase/NonExistentBook")
    assert response.status_code == 400 # Or 404 depending on your implementation
