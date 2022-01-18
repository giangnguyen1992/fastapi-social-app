from app import schema


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    def validate(post):
        return schema.PostResponse(**post)

    posts_map = map(validate, res.json())
    posts_list = posts_map

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
