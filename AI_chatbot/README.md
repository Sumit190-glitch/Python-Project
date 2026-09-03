# 🤖 Google Gemini AI Chatbot

This project includes three implementations of an AI chatbot powered by Google's Gemini API.

## 📋 Project Structure

- **main2.py** - Simple chatbot script that sends a single question and receives a response
- **main1.py** - Interactive chatbot with conversation history
- **main.py** - Advanced chatbot with persistent conversation context (named Jarvis)
- **.env** - Environment configuration file storing the API key securely

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
pip install google-genai python-dotenv
```

### 2. API Key Configuration
The API key is already stored in the `.env` file:
```
GEMINI_API_KEY=AIzaSyBhp8FCbma7fBfWRl5rOqt5xHMuUlI9JHs
```

### 3. Running the Scripts

#### Simple One-Shot Query (main2.py)
```bash
python main2.py
```
**Output:** Gets a single response to "What is the meaning of life?"

#### Interactive Chat (main1.py)
```bash
python main1.py
```
**Features:**
- Type your questions and get responses
- Maintains conversation context
- Type 'exit' to quit

#### Advanced Jarvis Chatbot (main.py)
```bash
python main.py
```
**Features:**
- Full conversation history
- Better context awareness
- Formatted output with Jarvis personality
- Type 'exit' to quit

## 🔑 API Key Security Best Practices

⚠️ **Important:** The API key in `.env` should **NOT** be committed to version control!

**Recommended Setup:**
1. Create a `.gitignore` file with:
   ```
   .env
   __pycache__/
   *.pyc
   .venv/
   ```

2. Share `.env.example` with your team:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. Each developer creates their own `.env` file locally

## 🐛 Troubleshooting

### Error: "You exceeded your current quota"
- **Cause:** Free tier API quota has been reached
- **Solution:** 
  1. Check your Google Cloud Console billing settings
  2. Set up a paid account or wait for the quota to reset
  3. https://ai.google.dev/gemini-api/docs/rate-limits

### Error: "Model not found"
- **Cause:** Using outdated model names (e.g., `gemini-pro`)
- **Solution:** Use `gemini-2.0-flash` or check available models at:
  https://ai.google.dev/models

### Error: "Import not found"
- **Solution:** Ensure all dependencies are installed:
  ```bash
  pip install google-genai python-dotenv
  ```

## 📊 Available Models

- `gemini-2.0-flash` - Fast, efficient model (recommended)
- `gemini-2.0-flash-exp` - Experimental version
- Other models available in your Google Cloud Console

## 💡 Tips & Features

- All scripts maintain conversation history
- Automatic error handling with informative messages
- Environment variable management for secure API key storage
- Compatible with Windows, macOS, and Linux

## 📝 API Documentation

For more information:
- https://ai.google.dev/
- https://ai.google.dev/gemini-api/docs
- https://ai.google.dev/gemini-api/docs/models/gemini-2-5-flash

## 🔄 Conversation Flow

```
User → Chatbot → Gemini API → Response
         ↓
    Store in History
         ↓
    Use for Context
```

## 📦 Dependencies

- `google-genai` - Google Gemini API client
- `python-dotenv` - Environment variable management

---

**Version:** 1.0  
**Created:** 2026-03-25  
**Python:** 3.13.5
