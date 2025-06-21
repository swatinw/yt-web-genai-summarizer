# yt-web-genai-summarizer

# 🧠 YouTube & Website Content Summarization – GenAI App

Summarize any YouTube video or website article using cutting-edge Generative AI models with a sleek Streamlit interface.

---

## 🔗 Live Demo

Try the app here 👉 [yt-web-genai-summarizer Streamlit App](https://yt-web-genai-summarizer-9vemjxm5h4hzpe6ijpsc3n.streamlit.app/)

---

## 🔍 Overview

This project is an **AI-powered Streamlit app** that summarizes long-form content from:

- 🎥 **YouTube Videos** (with transcripts)
- 🌐 **Web Articles** (static or dynamic)

Built with **LangChain**, **Groq LLaMA3**, and smart prompt engineering, it breaks down massive content into digestible, high-quality summaries.

---

## 🚀 Features

- 🔗 Summarize any **public YouTube video** (with captions available)
- 🌍 Summarize **articles from any website** (news, blogs, etc.)
- 🤖 Powered by **Groq’s ultra-fast LLaMA 3 model** via LangChain
- 📦 Handles **large text inputs** using recursive chunking
- ⚡ Interactive and responsive **Streamlit UI**
- 🎯 Customizable summarization prompts via PromptTemplate

---

## 🛠️ Tech Stack

| Layer            | Tools / Libraries                            |
|------------------|-----------------------------------------------|
| Language         | Python 3.11+                                  |
| UI Framework     | Streamlit                                     |
| LLM Interface    | LangChain + Groq API (LLaMA3-70B/8B)          |
| Loaders          | YoutubeLoader, WebBaseLoader (LangChain)      |
| Summarization    | PromptTemplate, SummarizeChain                |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/yt-web-genai-summarizer.git
cd yt-web-genai-summarizer
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 How It Works

1. Enter a YouTube link or webpage URL  
2. App loads transcript or web content  
3. Chunks the content into manageable pieces  
4. Groq LLM processes it using a SummarizeChain  
5. Final summary is displayed beautifully in the UI

---

## 🧪 Future Enhancements

- 🗂 Save summaries to PDF or Notion  
- 🎙️ Add voice narration (TTS)  
- 🌍 Support for multilingual content  
- 🧠 Fine-tuned summarization styles (e.g., TL;DR, detailed, bullet points)

---

## 🙋‍♀️ Author

**Swati Sharma**  

🔗 [LinkedIn](https://www.linkedin.com/in/swati-sharma-17s50s01/)  
📂 [GitHub](https://github.com/swatinw)

---

📬 _Let’s connect and build GenAI tools together!_
