from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}/{settings.DATABASE_NAME}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    # Drop tables
    models.Base.metadata.drop_all(bind=engine)
    # Database init
    models.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)