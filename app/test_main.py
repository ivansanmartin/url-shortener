from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_shortener():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"ok": True, "original_url": "https://ivansanmartin.dev/"}

def test_url_shortener_not_found():
    response = client.get("/notfound")
    assert response.status_code == 404
    assert response.json() == {"detail": {"ok": False, "message": "URL Shortener not found."}}