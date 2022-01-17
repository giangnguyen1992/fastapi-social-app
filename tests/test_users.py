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
