import requests
import json
from _config.settings import OPENROUTER_API_KEY

def _send_openrouter_request(model, messages):
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}",},
        data=json.dumps({
            "model": model,
            "messages": messages
            })
    )
    
    return response.json()

def prompt_llm(model, messages):
    
    if not OPENROUTER_API_KEY:
        raise ValueError("Error: OPENROUTER_API_KEY is not set in settings.py")
    
    if not messages or not isinstance(messages, list):
        raise ValueError("Error: messages must be a list")
    
    if not model or not isinstance(model, str):
        raise ValueError("Error: model must be a string")
    
    response = _send_openrouter_request(model, messages)
    
    # Check if the response contains an error
    if 'error' in response:
        error_message = response.get('error', {}).get('message', 'Unknown error occurred')
        raise ValueError(f"Error: Request failed with message: {error_message}")
    
    # Check if the response contains the expected 'choices' key
    if 'choices' not in response or not response['choices']:
        raise ValueError("Error: 'choices' not found or empty in api response")
    
    # If we've made it this far, the response is likely valid
    return response
