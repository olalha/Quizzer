from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

# Table for uploaded files
class UploadedFile(Base):
    __tablename__ = 'uploaded_files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(Text)
    description = Column(Text)

# Table for quizzes
class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(Integer, nullable=False)
    quiz_content = Column(JSON, nullable=False)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(Text)
    description = Column(Text)
