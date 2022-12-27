from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_userpage():
    response = client.get("/user/100000")
    assert response.status_code == 404

    response = client.get("/user/33")
    assert response.status_code == 200


def test_user_video():
    response = client.get("/user/33/video")
    assert response.status_code == 200


def test_like_video():
    response = client.get("/user/33/video/like")
    assert response.status_code == 200


def test_dislike_video():
    response = client.get("/user/33/video/dislike")
    assert response.status_code == 200
