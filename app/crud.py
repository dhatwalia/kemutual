# This file performs CRUD operations on our database.
from . import models, schemas
from datetime import datetime
from sqlalchemy.orm import Session

def create_task(db: Session, task: schemas.TaskWithId):
    time = datetime.now()
    db_task = models.Task(
        title=task.title, 
        description=task.description, 
        status=models.TaskStatus(task.status),
        created_at=time,
        updated_at=time,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()
