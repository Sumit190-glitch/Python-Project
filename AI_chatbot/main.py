import os
from dotenv import load_dotenv
import google.genai as genai

# Load API key securely from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Create chat session once at the start (maintains conversation history automatically)
chat = client.chats.create(model="gemini-2.0-flash")

def completion(user_message):
    """Send message to Gemini and maintain conversation context"""
    # Send message and get response
    response = chat.send_message(user_message)
    
    # Display the response
    print(f"Jarvis: {response.text}\n")

if __name__ == "__main__":
    print("=" * 60)
    print("🤖 Jarvis: Hi, I am Jarvis, powered by Google Gemini!")
    print("Type 'exit' to quit")
    print("=" * 60 + "\n")
    
    while True:
        try:
            user_question = input("You: ").strip()
            
            if user_question.lower() == 'exit':
                print("Jarvis: Goodbye! Have a great day! 👋")
                break
            
            if not user_question:
                continue
            
            print(f"You: {user_question}")
            completion(user_question)
            
        except KeyboardInterrupt:
            print("\n\nJarvis: Goodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {str(e)}\n")
            