from app import schema
from .database import client, session


def test_root(client):
    res = client.get("/")
    assert res.json().get("Welcome") == "to root!!!!"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "gggggggiang@web.de", "password": "123"}
    )
    new_user = schema.UserResponse(**res.json())
    assert new_user.email == "gggggggiang@web.de"
    assert res.status_code == 201
