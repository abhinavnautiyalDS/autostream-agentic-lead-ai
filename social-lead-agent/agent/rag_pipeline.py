import json
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=st.secrets["GEMINI_API_KEY"]
)

with open("data/knowledge_base.json") as f:
    knowledge = json.load(f)

def answer_query(question):

    context = json.dumps(knowledge)

    prompt = f"""
You are an AI assistant for AutoStream.

Use the knowledge base below to answer the user's question.

Knowledge Base:
{context}

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
