import json
import jsonschema

def extract_json(llm_response: str) -> dict | None:
    """
    Extract and parse JSON from an LLM response.

    Args:
        llm_response (str): The response from an LLM containing JSON.

    Returns:
        dict | None: Parsed JSON object if found and valid, None otherwise.
    """
    try:
        start = llm_response.index('{')
        end = llm_response.rindex('}') + 1
        json_str = llm_response[start:end]
        return json.loads(json_str)
    except (ValueError, json.JSONDecodeError):
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
