import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv(dotenv_path="./configs/.env")

def get_llm():
    return ChatOpenAI(
        temperature=0,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base=os.getenv("OPENROUTER_BASE_URL"),
        model_name=os.getenv("MODEL_NAME")
    )
