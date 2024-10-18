import os
from sqlalchemy.orm import Session
from .models import UploadedFile
from _config.settings import UPLOAD_FOLDER

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
