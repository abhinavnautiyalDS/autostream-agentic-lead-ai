import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():

    if "GEMINI_API_KEY" not in st.secrets:
        raise ValueError("GEMINI_API_KEY not found in Streamlit secrets")

    os.environ["GOOGLE_API_KEY"] = st.secrets["GEMINI_API_KEY"]

    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        temperature=0
    )
