from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
import os

from dotenv import load_dotenv
import chainlit as cl

# Load environment variables from .env file
load_dotenv()

@cl.on_chat_start
async def start():
    await cl.Avatar(
        name="Singularitii",
        url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d1553023f8ea0921fba0debbe92a8c5f840dd9&v=4",
    ).send()

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN, 
                     repo_id=repo_id, 
                     model_kwargs={"temperature":0.7, "max_new_tokens":500})


template = """
You are a helpful AI assistant and provide the answer for the question asked politely.

{question}
"""

@cl.langchain_factory
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    return llm_chain



