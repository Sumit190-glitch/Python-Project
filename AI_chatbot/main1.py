import os
from dotenv import load_dotenv
import google.genai as genai

# Load API key from environment
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Start interactive chatbot
print("=" * 50)
print("🤖 AI Chatbot powered by Google Gemini")
print("=" * 50)
print("Type 'exit' to quit\n")

# Create chat session once at the start (maintains history automatically)
chat = client.chats.create(model="gemini-2.0-flash")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'exit':
        print("Goodbye! 👋")
        break
    
    if not user_input:
        continue
    
    try:
        # Send message and get response
        response = chat.send_message(user_input)
        
        # Extract and display the response
        print(f"\nAssistant: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")