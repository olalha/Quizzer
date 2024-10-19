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
    
    return response