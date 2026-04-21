import streamlit as st
from agent.agent_graph import run_agent
from agent.memory import state

st.set_page_config(page_title="AutoStream AI", page_icon="🎬")

st.title("🎬 AutoStream AI Assistant")
st.write("Ask about pricing, features, or sign up for AutoStream.")

st.sidebar.title("About AutoStream")

st.sidebar.write("""
AutoStream is an AI-powered video editing platform for creators.

Plans:
Basic - $29/month  
Pro - $79/month
""")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Type your message...")


if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    if "name:" in user_input.lower():
        state.name = user_input.split(":")[1].strip()

    elif "email:" in user_input.lower():
        state.email = user_input.split(":")[1].strip()

    elif "platform:" in user_input.lower():
        state.platform = user_input.split(":")[1].strip()

    response = run_agent(user_input)

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
