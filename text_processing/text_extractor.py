"""
This module provides functionality for extracting text from various file types.
The main function is extract_text_from_file, which takes a file_id 
and returns a dictionary of page numbers and their corresponding text.
"""

import os
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

from utils.file_management import get_file_path

def _extract_text_from_pdf(pdf_path: str) -> dict:
    """
    Extracts all the text from a given PDF file.

    Args:
        pdf_path (str): The path to the PDF file to be processed.

    Returns:
        dict: A dictionary where each key is the page number (starting from 1).
    """
    pdf_text = {}

    # Go through each page of the PDF and extract the text
    for page_number, page_layout in enumerate(extract_pages(pdf_path), start=1):
        page_text = ""
        for element in page_layout:
            # Check if the element is a text container
            if isinstance(element, LTTextContainer):
                page_text += element.get_text()
        pdf_text[page_number] = page_text.strip() or ""
    
    return pdf_text

def extract_text_from_file(file_id: str) -> dict:
    """
    Extracts text from a file given its file_id.
    Chooses the appropriate extraction function based on the file type.
    
    Args:
        file_id (str): The ID of the file to extract text from.

    Returns:
        dict: A dictionary where each key is the page number (starting from 1).
        
    Raises:
        IOError: If there are issues with reading the file.
    """
    file_path = get_file_path(file_id)
    file_type = file_path.split('.')[-1]
    
    # Check if the file path is valid and leads to an existing file
    if not os.path.isfile(file_path):
        raise IOError(f"Error: File does not exist at path: {file_path}")
    
    if file_type == 'pdf':
        return _extract_text_from_pdf(file_path)
    else:
        return None
