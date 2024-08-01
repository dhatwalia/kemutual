# Database configuration
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "sqlite:///./test.db"  # Update this URL based on your database

# Create a new engine instance
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # SQLite-specific argument
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models
Base = declarative_base()
