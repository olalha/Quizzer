from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

def extract_text_from_pdf(pdf_path):
    
    """
    Extracts all the text from a given PDF file

    Args:
        pdf_path (str): The path to the PDF file to be processed

    Returns:
        dict: A dictionary where each key is the page number (starting from 1)
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