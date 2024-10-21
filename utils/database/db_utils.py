"""
Utility functions for managing uploaded files in the database and filesystem.
Includes functions for saving, deleting, and cleaning up file records and their
corresponding physical files.
"""

import os
from sqlalchemy.orm import Session

from .models import UploadedFile

SUPPORTED_FILE_TYPES = ['pdf', 'pptx', 'docx']
UPLOAD_FOLDER = '_data/uploads'

def save_uploaded_file(session: Session, uploaded_file):
    """
    Save an uploaded file to the filesystem and create a database record.

    Args:
        session (Session): SQLAlchemy database session
        uploaded_file: File object to be saved
    """
    # Create upload directory if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # Construct file path
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    
    # Check if the file type is supported
    file_type = file_path.split('.')[-1]
    if file_type not in SUPPORTED_FILE_TYPES:
        raise IOError(f"Error: Unsupported file type: {file_type}")
    
    # Write file to disk
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    # Create database record
    new_file = UploadedFile(filename=uploaded_file.name, filepath=file_path)
    session.add(new_file)
    session.commit()

def delete_uploaded_file(session: Session, file_id: int):
    """
    Delete a single uploaded file record and its corresponding file.

    Args:
        session (Session): SQLAlchemy database session
        file_id (int): ID of the uploaded file to delete
    """
    file_record = session.query(UploadedFile).filter(UploadedFile.id == file_id).first()
    if file_record:
        # Delete the file from the filesystem
        file_path = os.path.join(UPLOAD_FOLDER, file_record.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Delete the record from the database
        session.delete(file_record)
        session.commit()

def cleanup_all_uploaded_files(session: Session):
    """
    Delete all uploaded file records and their corresponding files.

    Args:
        session (Session): SQLAlchemy database session
    """
    # Query all uploaded file records
    uploaded_files = session.query(UploadedFile).all()

    # Delete each file and its record
    for file_record in uploaded_files:
        delete_uploaded_file(session, file_record.id)

    # Remove any remaining files in the uploads folder
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
