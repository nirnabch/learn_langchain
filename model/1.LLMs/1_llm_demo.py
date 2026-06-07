from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# Initialize the OpenAI LLM
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7)

result = llm.invoke("What is the capital of France?")
print(result)