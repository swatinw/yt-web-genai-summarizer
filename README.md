# yt-web-genai-summarizer
# 🧠 YouTube & Website Content Summarization GenAI App

This is an AI-powered Streamlit application that summarizes content from **YouTube videos** or **web URLs** using **LangChain**, **Groq LLMs**, and **Prompt Engineering**.

## 🚀 Features
- 🔗 Summarize any public YouTube video (with captions)
- 🌐 Summarize any website article (static or dynamic)
- 🤖 Uses Groq's LLaMA 3 model via LangChain
- 🧱 Handles large inputs with smart chunking
- 💥 Built with Streamlit for an interactive UI

## 🛠 Tech Stack
- Python 3.11+
- Streamlit
- LangChain
- Groq API (LLaMA3-70B / 8B)
- YoutubeLoader / WebBaseLoader
- PromptTemplate + SummarizeChain

## 📦 Installation
```bash
git clone https://github.com/your-username/youtube-website-content-summarization-genai-app.git
cd youtube-website-content-summarization-genai-app
pip install -r requirements.txt
streamlit run app.py
