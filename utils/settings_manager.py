"""

This module is responsible for loading and managing the application settings
from a YAML configuration file. It ensures that the settings variables are
available and accessed safely.
"""

import yaml

settings = {}

# Load settings
with open('_config/settings.yaml', 'r') as file:
    settings = yaml.safe_load(file)
if not settings:
    raise ValueError("Error: Settings file is empty.")

def get_setting(*keys):
    current = settings
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            raise ValueError(f"Error: '{'.'.join(keys)}' is missing from the settings file.")
    return current
