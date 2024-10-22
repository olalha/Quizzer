topics_json_schema = {
    "type": "object",
    "properties": {
        "topics": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "pages": {
                        "type": "array",
                        "items": {"type": "integer"}
                    }
                },
                "required": ["title", "pages"]
            }
        }
    },
    "required": ["topics"]
}

topics_json_example = """
{
    "topics": [
        {"title": "", "pages": []},
        {"title": "", "pages": []},
        {"title": "", "pages": []}
    ]
}
"""

topics_json_start = "{\"topics\":[{\"title\":"
topics_json_end = "}]}"
