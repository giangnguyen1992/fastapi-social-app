from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.json().get("Welcome") == "to root!!!!"
    assert res.status_code == 200
