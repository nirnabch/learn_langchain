import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

model_id = "Qwen/Qwen2.5-0.5B-Instruct"

# Step 1: Explicitly load the model and the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

# Step 2: Inject the tokenizer cleanly into the processing pipeline
hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,             # Required to parse structural chat tokens
    max_new_tokens=512,
    temperature=0.1,
    do_sample=True,
    return_full_text=False          # Keeps the original prompt from duplicating in the output
)

# Step 3: Instantiate LangChain components
llm = HuggingFacePipeline(pipeline=hf_pipeline)
chat_model = ChatHuggingFace(llm=llm)

# Step 4: Run the cleaned execution sequence
response = chat_model.invoke("Write a 5 line poem on cricket?")
print(response.content)
