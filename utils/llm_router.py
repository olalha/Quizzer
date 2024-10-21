
import os

from langchain_community.chat_models import ChatOpenAI

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

class ChatOpenRouter(ChatOpenAI):
    openai_api_base: str
    openai_api_key: str
    model_name: str

    def __init__(self, model_name: str,
                openai_api_key: str = OPENROUTER_API_KEY,
                openai_api_base: str = OPENROUTER_API_BASE,
                **kwargs):
        
        super().__init__(openai_api_base=openai_api_base,
                         openai_api_key=openai_api_key,
                         model_name=model_name, **kwargs)
    