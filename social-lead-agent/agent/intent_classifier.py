from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def classify_intent(user_message):

    prompt = f"""
Classify the user intent into one of these:

1. greeting
2. product_inquiry
3. high_intent

User message: {user_message}

Return only the label.
"""

    response = llm.invoke(prompt)

    return response.content.strip()
