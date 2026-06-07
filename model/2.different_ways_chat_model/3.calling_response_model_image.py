import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

client = OpenAI()

image_path = r"C:\Users\nirna\OneDrive\Pictures\medallion_architecture.jpg"

base64_image = encode_image_to_base64(image_path)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are an expert image analysis assistant. Describe what you see.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "What is in this image? Please describe it in detail."
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                }
            ]
        }
    ]
)

print(response.output_text)