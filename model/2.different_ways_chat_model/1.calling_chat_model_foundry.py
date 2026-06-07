import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load the environment variables from the .env file
load_dotenv()

# Retrieve variables securely
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")

# Initialize the OpenAI client with the custom base URL and API key
client = AzureOpenAI(
    base_url=endpoint,
    api_key=api_key,
    api_version="2024-05-01-preview"
)

# Call the model using your deployment name
completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    temperature=0.7,
    max_tokens=250
)

# Extract only the text content from the response
print(completion.choices[0].message.content)
