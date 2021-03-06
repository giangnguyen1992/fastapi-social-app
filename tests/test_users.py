from fastapi import status
import pytest
from app import schema
from jose import jwt
from app.config import settings


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


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@gmail.com", "password123", 403),
        ("sanjeev@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "password123", 422),
        ("sanjeev@gmail.com", None, 422),
    ],
)
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login/", data={"username": email, "password": password})

    assert res.status_code == status_code
