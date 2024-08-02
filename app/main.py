from . import crud, database, models, schemas
from fastapi import Depends, FastAPI, HTTPException, status
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

# Check to see if the task status string is within the TaskStatus enum
def check_task_status(status: str):
    try:
        models.TaskStatus(status)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid task status: {status}")

@app.post("/tasks/", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskWithId)
def create_task(task: schemas.Task, db: Session = Depends(get_db)):
    """
    Create a new task.
    - task: Task object that needs to be added to the database.
    - return: Returns the newly created task with ID.
    """
    check_task_status(task.status)
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

@app.get("/tasks/{task_id}", response_model=schemas.TaskWithId)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a task by its ID.
    - task_id: Unique ID of the task.
    - return: Single task detail if found. If not found, returns a 404 error.
    """
    db_task = crud.get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schemas.TaskWithId)
def update_task_by_id(task_id: int, task: schemas.Task, db: Session = Depends(get_db)):
    """
    Update a task by its ID.
    - task_id: Unique ID of the task to be updated.
    - task: Updated task object.
    - return: Updated task object if successful. If the task status is invalid or task not found, raises an error.
    """
    check_task_status(task.status)
    db_task = crud.update_task_by_id(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_by_id(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by its ID.
    - task_id: Unique ID of the task to be deleted.
    - return: None. Returns a 204 status code if successful, or a 404 if the task cannot be found.
    """
    success = crud.delete_task_by_id(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
