from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_create_shortener():
    response = client.post(
        "/api/v1/url-shortener",
        headers={"Content-Type": "application/json"},
        json={"original_url": "https://www.example.com/some/long/path"}
        )
    assert response.status_code == 201
    assert response.json() == {"ok": True, "message": "URL Shortener created succesfully"}