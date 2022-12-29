from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_email():
    data = {"email": "test@gsm.hs.kr"}
    response = client.post("/signup/email", json=data)
    assert response.status_code == 410


def test_email_check():
    data = {"email": "test@test.com", "code": "123456"}
    response = client.post("/signup/email/check", json=data)
    assert response.status_code == 400


def test_signup():
    data = {"name": "test", "password": "test", "email": "test@test.com"}
    response = client.post("/signup", json=data)
    assert response.status_code == 400
