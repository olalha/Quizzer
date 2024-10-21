"""
SETTINGS FILE

This file needs to be configured by the user before running the application.

"""

# Data storage location
UPLOAD_FOLDER = '_data/uploads'
GENERATED_DATA_FOLDER = '_data/generated'

# OpenRouter settings
MODELS = {
    'Summarize-Primary': 'mistralai/ministral-8b'
}

# Text processing settings
TARGET_WORD_COUNT_PER_BATCH = 500
MIN_TOPICS_PER_BATCH = 3
MAX_TOPICS_PER_BATCH = 5
