"""
This module provides functions for making API requests to OpenRouter's LLM service.
It includes utilities for sending requests and handling responses.
"""

import asyncio
import aiohttp
import os
from typing import List, Dict, Union

async def _send_openrouter_request(model: str, messages: List[Dict]) -> Dict:
    """
    Send an asynchronous request to OpenRouter API and return the JSON response.
    """
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={"model": model, "messages": messages}
        ) as response:
            return await response.json()

async def prompt_llm_async(model: str, messages: List[List[Dict]]) -> List[Dict]:
    """
    Send prompts to the specified LLM model via OpenRouter API in parallel.
    
    Args:
        model (str): The name of the LLM model to use.
        messages (List[List[Dict]]): A list of message lists, each representing a separate request.
    
    Returns:
        List[Dict]: A list of processed API responses.
    
    Raises:
        ValueError: If there are issues with the API response.
    """
    async def process_request(msg):
        try:
            response = await _send_openrouter_request(model, msg)
            
            if 'error' in response:
                error_message = response.get('error', {}).get('message', 'Unknown error occurred')
                raise ValueError(f"Error: OpenRouter API request failed: \n{msg} \n\n{error_message}")
            if 'choices' not in response or not response['choices']:
                raise ValueError(f"Error: 'choices' not found or empty in api response: \n{msg}")
            
            return response
        
        except Exception as e:
            print(f"{str(e)}")
            return None

    tasks = [process_request(msg) for msg in messages]
    return await asyncio.gather(*tasks)

def prompt_llm(model: str, messages: Union[List[Dict], List[List[Dict]]]) -> List[Dict]:
    """
    Send prompts to the specified LLM model via OpenRouter API.
    Handles requests in parallel if multiple messages are provided.
    
    Args:
        model (str): The name of the LLM model to use.
        messages (Union[List[Dict], List[List[Dict]]]): Either a single list of message dictionaries
                   for one prompt, or a list of message lists for multiple prompts.
    
    Returns:
        List[Dict]: A list of processed API responses.
    
    Raises:
        ValueError: If the messages parameter is not in the correct format.
    """

    # If messages is a single request, wrap it in another list
    if messages and isinstance(messages, list) and isinstance(messages[0], dict):
        messages = [messages]
    
    # Validate input
    if not isinstance(messages, list) or not all(isinstance(m, list) for m in messages):
        raise ValueError("Error: Each item in messages for prompt_llm must be a list.")
    if not all(all(isinstance(d, dict) for d in m) for m in messages):
        raise ValueError("Error: Each message may only contain dictionaries for prompt_llm.")

    # Run the async function and return the result
    return asyncio.run(prompt_llm_async(model, messages))
