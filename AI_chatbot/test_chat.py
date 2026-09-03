"""Quick test to verify main1.py works"""
import os
from dotenv import load_dotenv
import google.genai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("Testing corrected API flow...")
print("=" * 50)

try:
    # Create chat (this is what main1.py and main.py now do)
    chat = client.chats.create(model="gemini-2.0-flash")
    print("✅ Chat created successfully!")
    
    # Try to send a message
    print("\nSending test message...")
    response = chat.send_message("Hello! What is 2+2?")
    
    print(f"✅ Response received!")
    print(f"Answer: {response.text}")
    
except Exception as e:
    error_msg = str(e)
    if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
        print("⏱️  Quota exhausted (expected for free tier)")
        print("Next quota reset: UTC Midnight today")
    else:
        print(f"❌ Error: {error_msg}")
