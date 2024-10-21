"""
This module provides functions for making API requests to OpenRouter's LLM service.
It includes utilities for sending requests and handling responses.
"""

import requests
import json

from _config.settings import OPENROUTER_API_KEY

def _send_openrouter_request(model: str, messages: list) -> dict:
    """
    Send a request to OpenRouter API and return the JSON response.
    """
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}",},
        data=json.dumps({
            "model": model,
            "messages": messages
            })
    )
    
    return response.json()

def prompt_llm(model: str, messages: list) -> dict:
    """
    Send a prompt to the specified LLM model via OpenRouter API.
    
    Args:
        model (str): The name of the LLM model to use.
        messages (list): A list of message dictionaries for the conversation.
    
    Returns:
        dict: The processed API response.
    
    Raises:
        ValueError: If there are issues with the input parameters or API response.
    """
    
    # Check if the API key is set
    if not OPENROUTER_API_KEY:
        raise ValueError("Error: OPENROUTER_API_KEY is not set in settings.py")
    
    # Validate input parameters
    if not messages or not isinstance(messages, list):
        raise ValueError("Error: messages must be a list")
    if not model or not isinstance(model, str):
        raise ValueError("Error: model must be a string")
    
    # Send the request to OpenRouter API
    response = _send_openrouter_request(model, messages)
    
    # Check if the response contains an error
    if 'error' in response:
        error_message = response.get('error', {}).get('message', 'Unknown error occurred')
        raise ValueError(f"Error: Request failed with message: {error_message}")
    
    # Check if the response contains the expected 'choices' key
    if 'choices' not in response or not response['choices']:
        raise ValueError("Error: 'choices' not found or empty in api response")
    
    return response
