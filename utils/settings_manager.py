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

def get_setting(key: str):
    if key not in settings:
        raise ValueError(f"Error: '{key}' is missing from the settings file.")
    else:
        return settings.get(key)
