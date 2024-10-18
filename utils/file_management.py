import os
from utils.database.db_setup import session
from utils.database.models import UploadedFile
from utils.database.db_utils import delete_uploaded_file, cleanup_all_uploaded_files
from _config.settings import UPLOAD_FOLDER

def load_files():
    return session.query(UploadedFile).all()

def save_uploaded_file(uploaded_file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    new_file = UploadedFile(filename=uploaded_file.name, filepath=file_path, title="Lecture material")
    session.add(new_file)
    session.commit()

def handle_file_deletion(file_id):
    delete_uploaded_file(session, file_id)
    return load_files()

def handle_delete_all():
    cleanup_all_uploaded_files(session)
    return load_files()
