from utils.settings_manager import get_setting
from utils.api_request import prompt_llm
from .json_processor import extract_json, compare_json
from .batch_splitter import split_pages_into_batches
from .prompt_builder import render_prompt
from .text_extractor import extract_text_from_file
from .schema.topics import topics_json_schema, topics_json_example, topics_json_start, topics_json_end

def generate_summary(file_id: int):
    
    # Extract text from file and validate
    text = extract_text_from_file(file_id)
    if not text:
        raise ValueError(f"Error: No text found in the file id: {file_id}")
    
    # Validate target_word_count_per_batch setting
    target_word_count_per_batch = get_setting('target_word_count_per_batch')
    if target_word_count_per_batch <= 0:
        raise ValueError(f"Error: Setting target_word_count_per_batch is invalid: {target_word_count_per_batch}")
    
    batches = split_pages_into_batches(text, target_word_count_per_batch)
    batch_user_prompts = []
    
    # Generate prompts for each batch
    for inx, batch_start in enumerate(batches):
        
        # Select the pages for the current batch
        selected_pages = {}
        page_num = batch_start
        batch_end = batches[inx+1] if inx+1 < len(batches) else len(text)+1
        while page_num < batch_end:
            if page_num in text.keys():
                selected_pages[page_num] = text[page_num]
            page_num += 1

        # Render the user prompt for the current batch
        rendered_user_prompt = render_prompt('usr_summarize.html', context={"pages": selected_pages})
        batch_user_prompts.append(rendered_user_prompt)
    
    # Render the system prompt for summarizing topics
    sys_prompt_context = {
        "min": get_setting('min_topics_per_batch'), 
        "max": get_setting('max_topics_per_batch'),
        "json_example": topics_json_example
    }
    sys_prompt = render_prompt('sys_sum_tpcs.html', context=sys_prompt_context)
    
    # Create messages for the LLM
    messages = [
        [
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
        for user_prompt in batch_user_prompts
    ]
    
    # Send messages to the LLM
    llm_responses = prompt_llm(get_setting('models', 'Summarize-Primary'), messages)
    
    # Extract the topics in JSON format from the LLM responses
    topics = []
    for response in llm_responses:
        if response and 'choices' in response:
            choices = response.get('choices', [])
            if choices and 'message' in choices[0] and 'content' in choices[0]['message']:
                message_content = choices[0]['message']['content']
                json_data = extract_json(message_content, topics_json_start, topics_json_end)
                if json_data:
                    if compare_json(json_data, topics_json_schema):
                        topics.append(json_data)
                    else:
                        raise ValueError(f"Error: Invalid JSON in the LLM response: {message_content}")
                else:
                    raise ValueError(f"Error: No JSON found in the LLM response: {message_content}")
            else:
                raise ValueError(f"Error: Missing 'message' or 'content' in the LLM response choices: {choices}")
        else:
            raise ValueError(f"Error: No 'choices' found in the LLM response: {response}")
    
    return topics
