import os

# from langchain_openai import ChatOpenAI
from langchain.chat_models import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def openai_gpt():
    gpt_3_5_turbo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=OPENAI_API_KEY,
        max_tokens=1024,
    )
    return gpt_3_5_turbo
