from dotenv import load_dotenv
from langchain_openai import ChatOpenAI 
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
client = ChatOpenAI(model="gpt-4o", temperature=0.7, max_tokens=100)

response = client.invoke([
        SystemMessage(content="You are a helpful assistant."), 
        HumanMessage(content="What is the capital of France?")])


print(response.content)
