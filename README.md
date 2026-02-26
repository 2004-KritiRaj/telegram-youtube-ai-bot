# Telegram YouTube Summarizer & Q&A Bot

A Telegram-based AI assistant that helps users quickly understand YouTube videos by generating structured summaries and enabling future contextual Q&A.  
Built as part of the **Eywa SDE Internship assignment**.

---

## 🚀 Features

- 📎 Accepts YouTube video links via Telegram  
- 🎥 Detects valid YouTube URLs and extracts video IDs  
- 📝 Fetches video transcripts using public APIs  
- 📌 Generates **structured summaries**:
  - Key Points  
  - Important Timestamps  
  - Core Takeaway  
- ⚠️ Gracefully handles transcript-unavailable scenarios  
- 🧩 Modular architecture designed for future:
  - Multilingual support  
  - Contextual Q&A (RAG)  
  - Embedding-based search  

---

## 🧠 Business Objective

The goal is to build a **smart AI research assistant for YouTube** that enables users to:

- Understand long videos quickly  
- Extract key insights without watching the full video  
- Ask contextual questions *(planned)*  
- Consume content in their preferred language *(planned)*  

---

## 🏗️ Architecture Overview

The project follows a **clean, service-oriented architecture**:

```text
telegram-youtube-ai-bot/
│
├── youtube_bot/
│   ├── main.py                 # Entry point
│   ├── bot/
│   │   └── telegram_bot.py     # Telegram message handling
│   │
│   ├── services/
│   │   ├── transcript_service.py   # YouTube transcript retrieval
│   │   ├── summary_service.py      # Text preprocessing & summarization
│   │   ├── language_service.py     # (Planned) multilingual support
│   │   └── qa_service.py           # (Planned) Q&A over transcript
│   │
│   ├── utils/
│   │   ├── youtube_utils.py        # URL validation & video ID extraction
│   │   └── text_utils.py           # Cleaning & chunking utilities
│   │
│   ├── embeddings/
│   │   ├── embedder.py             # (Placeholder) embedding generation
│   │   └── vector_store.py         # (Placeholder) vector storage
│   │
│   ├── config/
│   │   └── settings.py             # Centralized configuration
│   │
│   └── data/cache/                 # (Planned) transcript caching
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 Tech Stack

- **Language:** Python 3  
- **Bot Framework:** `python-telegram-bot`  
- **Transcript API:** `youtube-transcript-api`  
- **Environment:** Virtualenv  
- **Planned LLM Integration:** OpenClaw / LLM-based summarization  

---

## ▶️ Setup & Run Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/telegram-youtube-ai-bot.git
cd telegram-youtube-ai-bot
```
### 2️⃣ Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Set environment variables

Create a `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```
### 5️⃣ Run the bot
```bash
python -m youtube_bot.main
```
## 📱 Usage Flow

- Open Telegram and start the bot  
- Send `/start`  
- Send a YouTube video link  

**Bot responds with:**
- Structured summary *(if transcript available)*  
- Or a clear error message *(if transcript is restricted)*  

---

## ⚠️ Transcript Handling & Limitations

This project uses **public YouTube transcript APIs**.

Some videos:
- Show captions in the YouTube UI  
- But **restrict programmatic transcript access**

In such cases, the bot:
- Does **not crash**  
- Clearly informs the user  
- Continues running reliably  

This behavior is **intentional and expected**, ensuring transparency and robustness.

---

## 🌍 Multilingual & Q&A Support (Planned)

- `language_service.py`: placeholder for future translation or multilingual LLMs  
- `qa_service.py`: placeholder for transcript-based question answering  
- `embeddings/`: reserved for future RAG (Retrieval-Augmented Generation)  

These modules are included to demonstrate **scalability and forward-thinking design**, without over-engineering the MVP.

---

## 🎥 Demo

A short demo video (3–5 minutes) demonstrates:
- Bot startup  
- Telegram interaction  
- YouTube link handling  
- Graceful transcript failure handling  

📸 Screenshots included in submission.

---

## 🏁 Conclusion

This project demonstrates:
- Clean backend architecture  
- Real-world API limitations handling  
- Business-focused AI assistant design  
- Readiness for future extensions  

It meets all **core functional and architectural requirements** of the Eywa SDE Internship assignment.

---

## 🙌 Author

**Kriti Raj**  
Undergraduate Student | Aspiring Software Engineer