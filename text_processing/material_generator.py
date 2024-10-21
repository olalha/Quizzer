from _config.settings import TARGET_WORD_COUNT_PER_BATCH, MIN_TOPICS_PER_BATCH, MAX_TOPICS_PER_BATCH, MODELS

from text_processing.text_extractor import extract_text_from_file
from text_processing.batch_splitter import split_pages_into_batches, get_batch_word_counts
from text_processing import prompt_builder
from utils.api_request import prompt_llm

def generate_summary_json(file_id):

    # TODO: Try catch for extract_text_from_file
    text = extract_text_from_file(file_id)
    
    # TODO: Check that batches make sense (i.e. not empty) and that target word count is positive
    batches = split_pages_into_batches(text, TARGET_WORD_COUNT_PER_BATCH)
    
    batch_prompts = []
    
    for inx, batch_start in enumerate(batches):
        selected_pages = {}
        page_num = batch_start
        batch_end = batches[inx+1] if inx+1 < len(batches) else len(text)+1
        
        while page_num < batch_end:
            if page_num in text.keys():
                selected_pages[page_num] = text[page_num]
            page_num += 1

        try:
            rendered_user_prompt = prompt_builder.render_prompt('usr_summarize.html', context={"pages": selected_pages})
            batch_prompts.append(rendered_user_prompt)
            
        except Exception as e:
            print(f"{e}")
            return None
        
    """
    TESTING CODE (WIP)
    
    SENDS REQUEST TO LLM FOR FIRST BATCH
    """
    
    # TODO: Check that MIN_TOPICS_PER_BATCH and MAX_TOPICS_PER_BATCH are set
    system_prompt = prompt_builder.render_prompt('sys_summarize.html', context={"min": MIN_TOPICS_PER_BATCH, "max": MAX_TOPICS_PER_BATCH})  
    
    # Prepare messages for LLM
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": batch_prompts[0]
        }
    ]
    
    try:
        # TODO: Check that model is set and is valid
        response = prompt_llm(model=MODELS['Summarize-Primary'], messages=messages)
        return response
        
    except Exception as e:
        print(f"{e}")
        return None
    