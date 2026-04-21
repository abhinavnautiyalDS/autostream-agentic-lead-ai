import json
import os
from agent.llm import get_llm

llm = get_llm()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "knowledge_base.json")

with open(DATA_PATH) as f:
    knowledge = json.load(f)


def answer_query(question):

    context = json.dumps(knowledge, indent=2)

    prompt = f"""
You are an AI assistant for AutoStream.

Answer the user's question using ONLY the knowledge base.

Knowledge Base:
{context}

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
