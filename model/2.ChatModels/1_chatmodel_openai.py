from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI Chat Model
model  = ChatOpenAI(model="gpt-4o", temperature=0)
response = model.invoke("What is the capital of France?")
print(response)
