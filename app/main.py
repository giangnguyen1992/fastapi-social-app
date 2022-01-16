from fastapi import FastAPI
from .routers import posts, users, auth, votes
from fastapi.middleware.cors import CORSMiddleware

# from . import models
# from .database import engine


# Database init
# models.Base.metadata.create_all(bind=engine)

# FastAPI init
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Welcome": "to root"}


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)
