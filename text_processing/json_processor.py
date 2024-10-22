import json
import jsonschema
import re

def extract_json(llm_response: str, json_start: str, json_end: str) -> dict | None:
    """
    Extract and parse JSON from an LLM response using regex.
    
    Args:
        llm_response (str): The response from an LLM containing JSON.
        json_start (str): The start string of the JSON object.
        json_end (str): The end string of the JSON object.

    Returns:
        dict | None: Parsed JSON object if found and valid, None otherwise.
    """
    try:
        # Remove all new line characters from the llm_response
        cleaned_response = llm_response.replace("\\n", "")
        
        # Build regex patterns for json_start and json_end
        def make_pattern(s):
            # Escape special characters and add optional whitespace between each character
            escaped = [re.escape(char) for char in s]
            # \s* matches spaces, \t* matches tabs, \n* matches newlines
            return r'[\s\t\n]*'.join(escaped)

        pattern_start = make_pattern(json_start)
        pattern_end = make_pattern(json_end)

        # Create a pattern to match the JSON content
        pattern = f"{pattern_start}(.*?){pattern_end}"

        # Find the JSON content
        match = re.search(pattern, cleaned_response, re.DOTALL)
        
        if match:
            json_str = match.group(1)
            full_json_str = f"{json_start}{json_str}{json_end}"
            return json.loads(full_json_str)
        else:
            return None

    except json.JSONDecodeError:
        return None

def compare_json(data: dict, schema: dict) -> bool:
    """
    Compare a JSON object with a JSON schema.

    Args:
        data (dict): The JSON object to validate.
        schema (dict): The JSON schema to validate against.

    Returns:
        bool: True if the data matches the schema, False otherwise.
    """
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False
