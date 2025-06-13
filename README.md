
# 🌐 Gemini WebQA: Webpage Question Answering using Gemini 1.5

👉 [Web Scrapper](https://nivash-website-retriever-6gxvtixqbtxuyyfqhkghqn.streamlit.app/)

---
<img width="1110" alt="Image" src="https://github.com/user-attachments/assets/5acb6cf7-2239-48b6-add4-6db5a8c75e1e" />
---
This project is a Streamlit web app that allows users to:
- Enter any webpage URL
- Scrape the content from that URL
- Embed the content using Google's Gemini Embeddings (`embedding-001`)
- Ask questions about that content using Gemini 1.5 Flash LLM
- Retrieve context-aware answers and view relevant source chunks

---

## 🚀 Features

- 🔎 Dynamic URL input
- ⚡ Powered by Gemini 1.5 Flash (via `langchain-google-genai`)
- 🧠 Semantic embeddings using Gemini Embedding Model
- 📄 Chunk-based context retrieval using FAISS
- 🧵 Question-answering pipeline using LangChain

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/gemini-webqa.git
cd gemini-webqa

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

Also install FAISS:
```bash
pip install faiss-cpu  # or faiss-gpu if you have a CUDA GPU
```

---

## 🔑 Environment Variables

Create a `.env` file with your Google API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```

---

## 🧪 Run the App

```bash
streamlit run app.py
```

---

## 📚 Tech Stack

- Python 🐍
- Streamlit
- LangChain
- Gemini 1.5 Flash (via Google Generative AI)
- FAISS
- WebBaseLoader for scraping

---

## 🙋‍♂️ Author

Made with ❤️ by **Nivash R N**  
🔗 [LinkedIn](https://www.linkedin.com/in/nivash-r-n/)  
📧 hello.nivashinsights@gmail.com
