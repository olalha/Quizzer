import math

def split_pages_into_batches(pdf_text: dict, target_word_count: int) -> list:
    """
    Splits pages from a PDF text dictionary into batches of similar word count.
    Inputed pages do not need to be sequential.
    Ensures that each batch has at least one page.

    Args:
        pdf_text (dict): Dictionary of page numbers to page text.
        target_word_count (int): Approximate target word count for each batch.

    Returns:
        list: An array of page numbers indicating the starting page of each batch.
    """
    
    # Perform input validation
    if target_word_count <= 0:
        raise ValueError("Error: target_word_count must be a positive integer.")
    if not pdf_text:
        return []

    # Pre-calculate word counts for each page
    word_counts = {page: len(text.split()) for page, text in pdf_text.items()}
    
    # Calculate total words and pages
    total_words = sum(word_counts.values())
    total_pages = len(pdf_text)

    # Calculate the number of batches and ideal batch size
    num_batches = min(math.ceil(total_words / target_word_count), total_pages)
    ideal_batch_size = total_words / num_batches

    sorted_pages = sorted(pdf_text.keys())
    batch_starts = [sorted_pages[0]]  # First batch starts at the lowest page number
    current_word_count = 0

    for i, page_num in enumerate(sorted_pages):
        current_word_count += word_counts[page_num]

        # Check if we've reached or exceeded the ideal size for the current batch
        if current_word_count >= ideal_batch_size * len(batch_starts) and len(batch_starts) < num_batches:
            if i + 1 < len(sorted_pages):
                batch_starts.append(sorted_pages[i + 1])

    return batch_starts

def test_batch_word_counts(pdf_text: dict, batch_starts: list) -> list:
    """
    Calculates the word count for each batch created by split_pages_into_batches.

    Args:
        pdf_text (dict): Dictionary of page numbers to page text.
        batch_starts (list): List of page numbers indicating the starting page of each batch.

    Returns:
        list: An array displaying the word count for each batch.
    """
    
    # Pre-calculate word counts for each page
    word_counts = {page: len(text.split()) for page, text in pdf_text.items()}
    
    batch_word_counts = []
    sorted_pages = sorted(pdf_text.keys())
    
    # Iterate through batch start pages
    for i, start_page in enumerate(batch_starts):
        
        # Determine the end page for the current batch
        end_page = batch_starts[i + 1] if i + 1 < len(batch_starts) else None
        
        # Calculate the word count for the current batch
        batch_word_count = 0
        for page_num in sorted_pages:
            if page_num >= start_page and (end_page is None or page_num < end_page):
                batch_word_count += word_counts[page_num]
        
        batch_word_counts.append(batch_word_count)
    
    return batch_word_counts
