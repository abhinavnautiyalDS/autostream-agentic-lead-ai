import json
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

with open("data/knowledge_base.json") as f:
    knowledge = json.load(f)

def answer_query(question):

    context = json.dumps(knowledge)

    prompt = f"""
You are AutoStream AI assistant.

Answer the user question using this knowledge base.

Knowledge:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
