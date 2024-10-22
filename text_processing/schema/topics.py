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