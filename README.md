# AutoStream Agentic Lead AI

**An Agentic Conversational AI system that converts user conversations into qualified SaaS leads using LLM reasoning, Retrieval-Augmented Generation (RAG), and automated lead capture.**

---

# Live Demo

**Streamlit App**

You can interact with the deployed chatbot here:

🔗 **Live Application:**
https://autostream-agentic-lead-ai-ditskrqbjvt8hfvy8cjb3f.streamlit.app/
The application allows users to:

* ask questions about the AutoStream product
* explore pricing and features
* simulate signing up for a plan
* automatically capture lead information through the AI agent workflow

---

# Demo Preview

Below is a preview of the chatbot interaction.

![AutoStream Demo](demo.gif)

*(Replace `demo.gif` with your recorded demo GIF once uploaded to the repository.)*

---

# Project Overview

Modern SaaS businesses receive thousands of messages daily through:

* website chat
* social media
* customer support
* creator platforms

Most of these conversations contain **potential customers**, but identifying **high-intent users** manually is inefficient and time-consuming.

This project demonstrates how an **AI Agent** can automatically:

1. Understand user queries
2. Answer product questions using verified knowledge
3. Detect buying intent
4. Capture lead information
5. Convert conversations into potential sales opportunities

The system simulates a **real-world SaaS assistant** for a fictional product called **AutoStream**, an AI-powered video editing platform for content creators.

---

# Key Features

**Conversational AI Agent**

The chatbot understands natural language queries and responds intelligently using an LLM.

**Intent Detection**

User messages are classified into:

* greeting
* product inquiry
* purchase intent

**Retrieval-Augmented Generation (RAG)**

Answers are generated using a structured knowledge base to ensure accurate and consistent responses.

**Automated Lead Capture**

When the system detects high purchase intent, it automatically collects user details such as:

* name
* email
* creator platform

**Conversation Memory**

The chatbot remembers information across messages to complete the lead generation workflow.

**Interactive Web Interface**

A Streamlit chat interface provides a real-time conversational experience.

---

# Problem Statement

Businesses often lose potential customers because user conversations are not converted into actionable leads.

Users may ask questions such as:

* “What are your pricing plans?”
* “Does this work for YouTube creators?”
* “How can I start using this?”

Without automation, these users leave without signing up.

This project solves the problem by creating an **AI-powered conversational agent** that can:

* answer product questions
* detect purchase intent
* collect user contact information
* simulate storing leads for future outreach

This enables businesses to **scale customer acquisition through conversational AI**.

---

# System Architecture

The system follows an **agent-based architecture** where each component performs a specific role.

User messages pass through multiple modules before a response is generated.

```
User
 ↓
Streamlit Chat Interface
 ↓
Agent Controller
 ↓
Intent Detection
 ↓
Decision Router
 ├── Greeting Response
 ├── RAG Knowledge Retrieval
 └── Lead Capture Tool
 ↓
LLM Response
 ↓
User
```

---

# Technology Stack

**Programming Language**

Python

**AI Framework**

LangChain

**Large Language Model**

Groq API

**Model Used**

Llama 3.3 70B Versatile

**Frontend Interface**

Streamlit

**Deployment**

Streamlit Cloud

---

# Core Components

## LLM Layer

The reasoning engine of the system is powered by a large language model.

The model performs:

* natural language understanding
* conversational response generation
* intent classification
* contextual reasoning

The system currently uses Groq’s hosted Llama model for **fast inference and low latency**.

The architecture is **model-agnostic**, meaning it can easily switch between providers such as:

* Groq
* OpenAI
* Gemini
* Anthropic

---

## Intent Detection

Intent detection is the **decision-making layer** of the system.

Each user message is classified into one of three categories:

* greeting
* product_inquiry
* high_intent

Example:

User message:

```
Hi
```

Intent:

```
greeting
```

User message:

```
What are your pricing plans?
```

Intent:

```
product_inquiry
```

User message:

```
I want to sign up for the Pro plan
```

Intent:

```
high_intent
```

The detected intent determines the next step in the agent workflow.

---

## Retrieval-Augmented Generation (RAG)

To ensure responses are accurate and consistent, the system uses **RAG**.

Instead of relying solely on the LLM, the system retrieves information from a knowledge base.

Example knowledge:

```
Basic Plan
$29/month
10 videos
720p resolution

Pro Plan
$79/month
Unlimited videos
4K resolution
AI captions
```

When a user asks:

```
What is your pricing?
```

The system retrieves relevant information and generates a response using that context.

Benefits of RAG:

* reduces hallucinations
* ensures factual answers
* keeps product information consistent

---

## Lead Capture Tool

When high purchase intent is detected, the system initiates a **lead capture workflow**.

The chatbot collects:

* user name
* email
* creator platform

Example interaction:

User:

```
I want the Pro plan for my YouTube channel
```

Assistant:

```
Great! What is your name?
```

After collecting details, the system triggers the lead capture tool.

Example output:

```
Lead captured successfully: Abhinav, abhinav@email.com, YouTube
```

This simulates storing a lead in a CRM system.

---

## Conversation Memory

The system maintains state using a memory module.

Stored attributes include:

* name
* email
* platform

This allows the agent to remember previous inputs and complete the lead generation process.

---

## Agent Controller

The agent controller orchestrates the system logic.

Example workflow logic:

```
If greeting
 → send welcome message

If product inquiry
 → use RAG to answer question

If high intent
 → collect lead information
 → trigger lead capture tool
```

This transforms the chatbot into an **agentic system capable of decision making**.

---

## Streamlit Chat Interface

The user interface is built using Streamlit.

Features include:

* real-time chat interaction
* conversation history
* sidebar product information
* interactive conversational UI

This makes the system behave like a **real SaaS product assistant**.

---

# Example Conversation

User:

```
Hi
```

Assistant:

```
Hello! How can I help you with AutoStream today?
```

User:

```
What are your pricing plans?
```

Assistant:

```
We offer two plans:
Basic – $29/month for 10 videos
Pro – $79/month with unlimited videos and AI captions
```

User:

```
I want the Pro plan for my YouTube channel
```

Assistant:

```
Great! What is your name?
```

The agent then collects details and captures the lead.

---

# Business Impact

This system demonstrates how conversational AI can improve **customer acquisition and engagement**.

Benefits for businesses:

* automated lead generation
* instant responses to user queries
* reduced manual support workload
* higher conversion rates
* scalable customer engagement

Instead of losing potential customers, businesses can convert conversations into **actionable leads**.

---

# Real-World Applications

This architecture can be used in:

SaaS platforms capturing trial users
E-commerce product assistants
Marketing campaign chatbots
Customer support automation
Social media conversational agents

---

# Project Structure

```
autostream-agentic-lead-ai
│
├── agent
│   ├── agent_graph.py
│   ├── intent_classifier.py
│   ├── rag_pipeline.py
│   ├── tools.py
│   ├── memory.py
│   └── llm.py
│
├── data
│   └── knowledge_base.json
│
├── streamlit.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository.

```
git clone https://github.com/your-username/autostream-agentic-lead-ai
```

Install dependencies.

```
pip install -r requirements.txt
```

Add your API key to Streamlit secrets.

```
GROQ_API_KEY = "your_api_key"
```

Run the application.

```
streamlit run streamlit.py
```

---

# Skills Demonstrated

This project demonstrates skills in:

* Generative AI systems
* Retrieval-Augmented Generation
* conversational agent design
* LLM integration
* tool-based agent workflows
* full-stack AI application deployment

---

# Future Improvements

Possible future enhancements include:

* vector database integration (FAISS or Pinecone)
* WhatsApp or Slack chatbot integration
* CRM integration for real lead storage
* analytics dashboard for lead tracking
* multilingual conversational support

---

# Conclusion

AutoStream Agentic Lead AI demonstrates how modern AI systems can transform simple conversations into meaningful business outcomes.

By combining **LLM reasoning, RAG knowledge retrieval, intent detection, and automated lead capture**, the system creates an intelligent conversational agent capable of assisting users while simultaneously generating potential sales leads.

This project reflects how **real-world conversational AI systems are built and deployed in modern SaaS platforms.**
