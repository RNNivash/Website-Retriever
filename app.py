import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import time

# Load environment variables (e.g., GOOGLE_API_KEY)
load_dotenv()

# Page Title
st.title("🔍 Webpage Question Answering with Gemini")
st.caption("© Nivash R N | 2025")
# User input: URL
url = st.text_input("Enter a URL to fetch content from", placeholder="https://example.com")

if url:
    try:
        with st.spinner("🔎 Loading and processing the URL..."):
            # Load webpage content
            loader = WebBaseLoader(url)
            docs = loader.load()

            # Split text into chunks
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            split_docs = splitter.split_documents(docs)

            # Embedding model (Gemini)
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))

            # Create vector index
            vectorstore = FAISS.from_documents(split_docs, embeddings)

            # LLM (Gemini Flash 1.5)
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-flash", temperature=0.3, google_api_key=os.getenv("GOOGLE_API_KEY")
            )

            # Prompt template
            prompt = ChatPromptTemplate.from_template("""
            Answer the question using only the following context:
            <context>
            {context}
            </context>
            Question: {input}
            """)

            # Create chains
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = vectorstore.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            # Input prompt
            user_question = st.text_input("Ask a question about the webpage:")

            if user_question:
                start = time.process_time()
                response = retrieval_chain.invoke({"input": user_question})
                st.success("✅ Answer:")
                st.write(response["answer"])
                st.caption(f"⏱️ Response time: {round(time.process_time() - start, 2)}s")

                with st.expander("🧾 Similar Document Chunks"):
                    for i, doc in enumerate(response["context"]):
                        st.markdown(doc.page_content)
                        st.markdown("---")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
