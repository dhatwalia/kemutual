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

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task_by_id(db: Session, task_id: int, task: schemas.TaskWithId):
    db_task = get_task_by_id(db, task_id)
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.status = models.TaskStatus(task.status)
        db_task.updated_at = datetime.now()
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task_by_id(db: Session, task_id: int):
    db_task = get_task_by_id(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
