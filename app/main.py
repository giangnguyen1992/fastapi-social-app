from fastapi import FastAPI
from dotenv import load_dotenv
from . import models
from .database import engine
from .routers import posts, users, auth


# Env
load_dotenv()

# Database init
models.Base.metadata.create_all(bind=engine)

# FastAPI init
app = FastAPI()


# REGULAR SQL
# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi-social-app",
#             user="postgres",
#             password=os.environ.get("DATABASE_PASSWORD"),
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print(f"Connecting to database failed. Error was {error}")
#         time.sleep(2)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
