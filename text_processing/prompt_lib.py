"""
Defines templates for user and system prompts and their associated context.
"""

# User prompt templates
user_prompt_templates = {
    "Poem": {
        "file_name": "usr_poem.html",
        "context": [
            "role",
            "topic",
            "additional_text"
        ]
    }
}

# System prompt templates
system_prompt_templates = {}
