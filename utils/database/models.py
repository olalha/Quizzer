"""
Database models for file uploads and learning materials.
"""

import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Table for uploaded files
class UploadedFile(Base):
    __tablename__ = 'uploaded_files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    description = Column(Text)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)

# Table for quizzes
class LearningMaterial(Base):
    __tablename__ = 'learning_materials'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    file_id = Column(Integer, nullable=False)
    summary_json = Column(String, nullable=False)
    notes_json = Column(String)
    quiz_json = Column(String)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
