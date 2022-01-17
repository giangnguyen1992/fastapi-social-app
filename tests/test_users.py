import pytest
from app import schema
from .database import client, session
from jose import jwt
from app.config import settings


@pytest.fixture
def test_user(client):
    user_data = {"email": "re@web.de", "password": "123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "gggggggiang@web.de", "password": "123"}
    )
    new_user = schema.UserResponse(**res.json())
    assert new_user.email == "gggggggiang@web.de"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        "/login/",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    login_res = schema.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
