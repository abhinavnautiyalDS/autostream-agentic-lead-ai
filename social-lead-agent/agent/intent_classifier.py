import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=st.secrets["GEMINI_API_KEY"],
    temperature=0
)

def classify_intent(user_message):

    prompt = f"""
Classify the user intent into one of the following:

1 greeting
2 product_inquiry
3 high_intent

User message: {user_message}

Return only the label.
"""

    response = llm.invoke(prompt)

    return response.content.strip()
