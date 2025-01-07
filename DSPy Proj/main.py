from dotenv import load_dotenv
import os
import openai

# Load the .env file
load_dotenv()

# Access the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test the OpenAI API
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write a haiku about AI.",
    max_tokens=50
)
print(response.choices[0].text.strip())
