import math

# TODO: See if both functions can be made faster
# TODO: Comment the code for the word count calculation function

def split_pages_into_batches(pdf_text, target_word_count):
    """
    Splits pages from a PDF text dictionary into batches of similar word count.
    The function ensures that each batch has at least one page and all batches
    are of approximately equal length.

    Args:
        pdf_text (dict): Dictionary of page numbers to page text.
        target_word_count (int): Target word count for each batch.

    Returns:
        list: An array of page numbers indicating the starting page of each batch.
    """
    
    # Perform input validation
    if target_word_count <= 0:
        raise ValueError("target_word_count must be a positive integer.")
    if not pdf_text:
        return []

    # Calculate total words and pages
    total_words = sum(len(text.split()) for text in pdf_text.values())
    total_pages = len(pdf_text)

    # Calculate the number of batches and ideal batch size
    num_batches = min(math.ceil(total_words / target_word_count), total_pages)
    ideal_batch_size = total_words / num_batches

    batch_starts = [1]  # First batch always starts at page 1
    current_word_count = 0
    current_batch = 1

    # Iterate over sorted page numbers (handling non-sequential keys)
    sorted_pages = sorted(pdf_text.keys())
    for idx, page_num in enumerate(sorted_pages):
        # Count words on the current page
        page_word_count = len(pdf_text[page_num].split())
        current_word_count += page_word_count

        # Check if we've reached or exceeded the ideal batch size
        if current_word_count >= ideal_batch_size * current_batch and len(batch_starts) < num_batches:
            next_index = idx + 1
            if next_index < len(sorted_pages):
                next_page = sorted_pages[next_index]
                batch_starts.append(next_page)
                current_batch += 1

    return batch_starts

def test_batch_word_counts(pdf_text, batch_starts):
    """
    Tests the word count for each batch created by split_pages_into_batches.

    Args:
        pdf_text (dict): Dictionary of page numbers to page text.
        batch_starts (list): List of page numbers indicating the starting page of each batch.

    Returns:
        list: An array displaying the word count for each batch.
    """
    
    batch_word_counts = []
    sorted_pages = sorted(pdf_text.keys())
    
    for i in range(len(batch_starts)):
        start_page = batch_starts[i]
        end_page = batch_starts[i + 1] if i + 1 < len(batch_starts) else sorted_pages[-1] + 1
        
        batch_word_count = 0
        for page_num in range(start_page, end_page):
            if page_num in pdf_text:
                batch_word_count += len(pdf_text[page_num].split())
        
        batch_word_counts.append(batch_word_count)
    
    return batch_word_counts
