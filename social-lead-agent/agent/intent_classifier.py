from agent.llm import get_llm

llm = get_llm()


def classify_intent(user_message):

    prompt = f"""
Classify the user intent into ONE of these labels:

greeting
product_inquiry
high_intent

User message: {user_message}

Return ONLY the label.
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()
