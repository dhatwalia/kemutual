from . import crud, database, models, schemas
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session
from typing import List

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

@app.post("/tasks/", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskWithId)
def create_task(task: schemas.Task, db: Session = Depends(get_db)):
    """
    Create a new task.
    - task: Task object that needs to be added to the database.
    - return: Returns the newly created task with ID.
    """
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.TaskWithId])
def get_all_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all tasks from the database with pagination.
    - skip: Number of records to skip (for pagination).
    - limit: Maximum number of records to return.
    - return: List of tasks.
    """
    tasks = crud.get_all_tasks(db, skip=skip, limit=limit)
    return tasks
