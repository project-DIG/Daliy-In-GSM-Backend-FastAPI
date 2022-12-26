from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_signin():
    data = {"email": "test@test.com", "password": "testtest"}
    response = client.post("/signin", json=data)
    assert response.status_code == 400


def test_refresh():
    data = {"refresh_token": "test"}
    response = client.post("/signin/refresh", json=data)
    assert response.status_code == 401
