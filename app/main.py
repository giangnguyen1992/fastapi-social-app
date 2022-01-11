from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

load_dotenv()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi-social-app",
        user="postgres",
        password=os.environ.get("DATABASE_PASSWORD"),
        cursor_factory=RealDictCursor,
    )
    cursor = conn.cursor()
    print("Database connection was successfull!")
except Exception as error:
    print(f"Connecting to database failed. Error was {error}")

my_posts = [
    {"title": "Giang", "content": "Hello", "id": 1},
    {"title": "Regina", "content": "Kirchmeier", "id": 2},
]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def root():
    return {"data": my_posts}


@app.get("/posts/{id}")
async def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    return {"post": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} does not exist",
        )

    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} does not exist",
        )
    my_posts.pop(index)
    return {"message": "post was deleted"}
