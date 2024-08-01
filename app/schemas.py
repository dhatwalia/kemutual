# Schemas for our API endpoints that we use in Postman
from datetime import datetime
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    status: str

class TaskWithId(Task):
    id: int
    created_at: datetime
    updated_at: datetime
