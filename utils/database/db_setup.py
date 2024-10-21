"""
Database setup and session creation for the application.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

# Set the database URL to the local SQLite database 
DATABASE_URL = 'sqlite:///quiz_generator.db'

# Create a new engine instance and all tables
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
