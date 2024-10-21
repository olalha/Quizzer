"""
Database setup and session creation for the application.
"""

import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .models import Base

load_dotenv()

try:
    # Set the database URL to the local SQLite database 
    DATABASE_URL = os.getenv('DATABASE_URL')

    if not DATABASE_URL:
        raise ValueError("Error: DATABASE_URL environment variable is not set.")

    if not DATABASE_URL.startswith('sqlite:///'):
        raise ValueError("Error: Invalid DATABASE_URL. Expected a SQLite database URL (sqlite:///...).")

    # Create a new engine instance and all tables
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

except (ValueError, SQLAlchemyError) as e:
    print(f"{str(e)}")
    
    # Exit the application as the database setup failed
    sys.exit(1)
