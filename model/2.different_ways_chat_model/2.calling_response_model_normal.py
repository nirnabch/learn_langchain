import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Call using the updated Responses API primitive
response = client.responses.create(
    model="gpt-4o",
    instructions="You are a helpful assistant.",  # Correct top-level field
    input="What is the capital of France?",        # Correct top-level field
    temperature=0.7,
    max_output_tokens=1000
)

# Convert the entire response object directly into a clean dict
# response_dict = response.model_dump()
# print(json.dumps(response_dict, indent=2))

print(response.output_text)  # This will print: Paris

# Accessing just the text content is much cleaner now:
# print(response.output_text)  # This will print: Paris
