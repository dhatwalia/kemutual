# Database models
from .database import Base
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum
from sqlalchemy.types import DateTime

class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(SQLAlchemyEnum(TaskStatus), index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
