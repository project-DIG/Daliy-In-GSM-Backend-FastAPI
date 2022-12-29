from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_userpage():
    response = client.get("/user/ㅋㅋㅋ")
    assert response.status_code == 404

    response = client.get("/user/이주원")
    assert response.status_code == 200


def test_user_video():
    response = client.get("/user/이주원/video")
    assert response.status_code == 200


def test_like_video():
    response = client.get("/user/이주원/video/like")
    assert response.status_code == 200


def test_dislike_video():
    response = client.get("/user/이주원/video/dislike")
    assert response.status_code == 200
