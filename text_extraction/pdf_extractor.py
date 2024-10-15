from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    
    """
    Extracts all the text from a given PDF file

    Args:
        pdf_path (str): The path to the PDF file to be processed

    Returns:
        dict: A dictionary where each key is the page number (starting from 1)
    """
    
    reader = PdfReader(pdf_path)
    pdf_text = {}

    for page_number, page in enumerate(reader.pages, start=1):
        pdf_text[page_number] = page.extract_text() or ""
    
    return pdf_text