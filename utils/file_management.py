"""
This module provides Utility functions for managing 
uploaded files in the database and file system.
"""

from utils.database.db_setup import session
from utils.database.models import UploadedFile
from utils.database.db_utils import delete_uploaded_file, cleanup_all_uploaded_files, save_uploaded_file

# Retrieve all uploaded files from the database
def load_files():
    return session.query(UploadedFile).all()

# Get the file path for a given file ID
def get_file_path(file_id: int):
    file = session.query(UploadedFile).filter(UploadedFile.id == file_id).first()
    if file:
        return file.filepath
    return None

# Get the filename for a given file ID
def get_file_name(file_id: int):
    file = session.query(UploadedFile).filter(UploadedFile.id == file_id).first()
    return file.filename if file else None

# Get the file ID for a given filename
def get_file_id(file_name: str):
    file = session.query(UploadedFile).filter(UploadedFile.filename == file_name).first()
    return file.id if file else None

# Handle file upload, save the file, and return updated file list
def handle_file_upload(uploaded_file):
    save_uploaded_file(session, uploaded_file)
    return load_files()

# Handle file deletion for a given file ID and return updated file list
def handle_file_deletion(file_id: int):
    delete_uploaded_file(session, file_id)
    return load_files()

# Delete all uploaded files and return updated (empty) file list
def handle_delete_all():
    cleanup_all_uploaded_files(session)
    return load_files()
