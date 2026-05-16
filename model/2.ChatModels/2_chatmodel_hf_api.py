from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    temperature=0.1,
    max_new_tokens=512
)


# Initialize the Hugging Face Chat Model
model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of France?")

print(response.content)