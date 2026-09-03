import os
from dotenv import load_dotenv
import google.genai as genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Simple single question with Chat helper (correct API for google-genai)
chat = client.chats.create(model="gemini-2.0-flash")
response = chat.send_message("What is the meaning of life?")

print("Response:", response.text)
