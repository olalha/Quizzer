import os
import streamlit as st

from utils.database.db_setup import session
from utils.database.models import UploadedFile, LearningMaterial
from config.settings import UPLOAD_FOLDER
from text_extraction.pdf_extractor import extract_text_from_pdf
from text_processing.batch_splitting import split_pages_into_batches, test_batch_word_counts

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload a Lecture File", type=['pdf', 'pptx', 'docx'])

if uploaded_file:
    
    # Save the uploaded file to the local 'uploads' folder
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    # Add file details to the database
    new_file = UploadedFile(filename=uploaded_file.name, filepath=file_path, title="Lecture material")
    session.add(new_file)
    session.commit()
    
    st.write(f"File '{uploaded_file.name}' uploaded and saved to database.")
    
    # If the uploaded file is a PDF, extract and display the first page content
    if uploaded_file.name.lower().endswith('.pdf'):
        
        # TESTING AREA AFTER A PDF IS UPLOADED
        
        # print(split_pages_into_batches(extract_text_from_pdf(file_path), 500))
        # print(test_batch_word_counts(extract_text_from_pdf(file_path), split_pages_into_batches(extract_text_from_pdf(file_path), 500)))
        
        """
        extracted_text = extract_text_from_pdf(file_path)
        first_page_text = extracted_text.get(1)
        
        if first_page_text:
            st.subheader("First Page Content:")
            st.text(first_page_text)
        else:
            st.warning("No text found on the first page of the PDF.")
        """
