from . import database, models
from fastapi import FastAPI

# Create all database tables
models.Base.metadata.create_all(bind=database.engine)

# Configure FastAPI to use this encoder
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
