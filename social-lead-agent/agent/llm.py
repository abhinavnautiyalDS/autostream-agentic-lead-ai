import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():

    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=st.secrets["GEMINI_API_KEY"],
        temperature=0
    )
