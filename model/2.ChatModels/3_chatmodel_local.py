from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

# Downloads the model to your PC cache and runs it 100% locally
llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 512, 
        "temperature": 0.1, 
        "do_sample": True
    }
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("Write a 5 line poem on cricket?")

print(response.content)