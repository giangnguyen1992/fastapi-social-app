from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users


# Database init
models.Base.metadata.create_all(bind=engine)

# FastAPI init
app = FastAPI()


app.include_router(posts.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
