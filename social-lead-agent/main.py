from agent.agent_graph import run_agent
from agent.memory import state

print("AutoStream AI Agent Started")

while True:

    user = input("User: ")

    if "name:" in user.lower():
        state.name = user.split(":")[1].strip()

    elif "email:" in user.lower():
        state.email = user.split(":")[1].strip()

    elif "platform:" in user.lower():
        state.platform = user.split(":")[1].strip()

    response = run_agent(user)

    print("Agent:", response)
