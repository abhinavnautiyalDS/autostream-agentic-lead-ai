import streamlit as st
from agent.agent_graph import run_agent
from agent.memory import state

st.set_page_config(page_title="AutoStream AI", page_icon="🎬")

st.title("🎬 AutoStream AI Assistant")
st.write("Ask about pricing, features, or sign up for a plan!")

# conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# user input
user_input = st.chat_input("Type your message...")

if user_input:

    # save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # capture lead info
    if "name:" in user_input.lower():
        state.name = user_input.split(":")[1].strip()

    elif "email:" in user_input.lower():
        state.email = user_input.split(":")[1].strip()

    elif "platform:" in user_input.lower():
        state.platform = user_input.split(":")[1].strip()

    # run agent
    response = run_agent(user_input)

    # display response
    with st.chat_message("assistant"):
        st.write(response)

    # store response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
