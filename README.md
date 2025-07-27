# 🤖 Tool-Calling Chatbot Agent (OpenAI Function Calling)

A Python-based AI agent that intelligently extends its capabilities using OpenAI's function-calling feature. This chatbot can handle general queries and decide when to call external tools such as:

- 🧮 Mathematical calculator
- 🕒 Time lookup by city or timezone
- 🌐 Web search via DuckDuckGo

Built to demonstrate foundational agent architecture using GPT-3.5-turbo with tool-use awareness.

---

## 🛠️ Features

- ✅ Automatic tool detection and usage via OpenAI GPT
- ✅ Supports function-calling for real-time decision making
- ✅ Handles 3 tools:
  - `calculator_tool`: Evaluate math expressions safely
  - `get_current_time_by_city`: Get current time for any city or timezone
  - `web_search`: Return top search results using DuckDuckGo API
- ✅ Interactive multi-turn conversation loop
- ✅ Fully extensible — add your own tools!

---

## 📦 Installation Instructions

> 💡 Works with **Python 3.8+** (tested on 3.10+)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tool-calling-bot.git
cd tool-calling-bot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 🔐 How to Get and Use Your API Key

This project requires an OpenAI API key with access to the `gpt-3.5-turbo-0613` model (supports function calling).

### Steps:
1. Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys)
2. Log in and click “Create new secret key”
3. Copy the key
4. In terminal, export it like this:

```bash
export OPENAI_API_KEY="your_api_key_here"  # macOS/Linux
# OR
set OPENAI_API_KEY=your_api_key_here       # Windows
```

> ⚠️ Never commit your key to GitHub!

---

## 🚀 How to Run the Bot

### Run the main script:

```bash
python main.py
```

### Chat Interface:

You can ask anything! GPT will decide when to use tools.

---

## 💬 Example Conversations

### 📌 Basic Chat
```
You: Hello there!
GPT: Hello! How can I help you today?
```

---

### 🧮 Calculator Tool
```
You: What's 15% of 240?
GPT: ✅ Result: 36.0
```

---

### 🕒 Time Lookup Tool
```
You: What time is it in Boston?
GPT: 🕒 Current time in Boston: 2025-07-27 22:14:00 JST+0900
```

---

### 🌐 Web Search Tool (DuckDuckGo)
```
You: Search for Python web scraping tutorials
GPT: 
🔹 Learn Web Scraping with Python
Explore BeautifulSoup and requests for web scraping.
🔗 https://example.com/python-scraping
```

---

### 🔁 Multi-tool Usage
```
You: What’s 12 * 7 and what time is it in New York?
GPT:
✅ Result: 84
🕒 Current time in New York: 2025-07-27 08:15:00 EDT-0400
```

---

## ⚠️ Known Limitations

- ❗ **DuckDuckGo API** does not support advanced queries like weather forecasts
- ❗ GPT may sometimes overuse or skip tool calls
- ❗ Needs internet access for API use and web search
- ❗ Function calling only works on models like `gpt-3.5-turbo-0613` or `gpt-4`
- ❗ No session memory — each run is stateless

---

## 🧱 Project Structure

```
tool_calling_bot/
├── main.py            # Main chat loop and tool-calling logic
├── tools.py           # Python tools: calculator, time, web search
├── config.py          # API key handling
├── requirements.txt   # List of Python dependencies
└── README.md          # This file!
```

---

## ✅ Dependencies (requirements.txt)

```
openai>=1.0.0
requests
pytz
geopy
timezonefinder
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## 👨‍🎓 Credits

Developed by **Paramjeet Singh**  
MS in Information Systems  
Northeastern University, Boston  
July 2025

---

## 💡 Future Ideas

- Replace DuckDuckGo with Google Search API (Serper.dev)
- Add weather support using wttr.in or OpenWeatherMap
- Add unit converters, currency calculators, or Wikipedia summarizers tools 
