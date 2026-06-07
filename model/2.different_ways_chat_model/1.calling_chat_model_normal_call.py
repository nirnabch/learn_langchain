from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
    temperature=0.7,
    max_tokens=100
)

response_dict = response.model_dump()
print(json.dumps(response_dict, indent=2))

#print(response.choices[0].message.content)