import streamlit as st
from langchain_groq import ChatGroq


def get_llm():

    if "GROQ_API_KEY" not in st.secrets:
        raise ValueError("GROQ_API_KEY not found in Streamlit secrets")

    return ChatGroq(
        model="llama3-8b-8192",
        groq_api_key=st.secrets["GROQ_API_KEY"],
        temperature=0
    )
