# AutoStream Agentic Lead AI

**An Agentic Conversational AI system that converts user conversations into qualified SaaS leads using LLM reasoning, Retrieval-Augmented Generation (RAG), and automated lead capture.**

---

# Project Overview

Modern SaaS businesses receive thousands of messages daily through:

* website chat
* social media
* customer support
* creator platforms

Most of these conversations contain **potential customers**, but identifying **high-intent users** manually is difficult and inefficient.

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

The chatbot understands natural language questions and responds intelligently.

**Intent Detection**

User messages are classified into different categories such as greeting, product inquiries, or purchase intent.

**Retrieval-Augmented Generation (RAG)**

The system retrieves answers from a knowledge base to avoid hallucination and provide consistent product information.

**Automated Lead Capture**

When the system detects high purchase intent, it automatically collects user details such as name, email, and platform.

**Conversation Memory**

The system remembers user details across messages to complete the lead generation workflow.

**Interactive Web Interface**

A chatbot interface built using Streamlit allows real-time interaction with the AI system.

---

# Problem Statement

Many companies struggle to convert conversations into sales leads. Users may ask questions like:

* "What are your pricing plans?"
* "Do you support YouTube creators?"
* "How can I sign up?"

Without automation, these potential customers often leave without converting.

This project solves the problem by building an **AI-powered conversational agent** that can:

* answer product questions
* detect purchase intent
* collect lead information automatically

This enables businesses to **scale customer acquisition without manual intervention.**

---

# System Architecture

The system follows an **agent-based architecture**.

User messages pass through multiple modules that decide how the system should respond.

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

Each module performs a specific task in the conversational pipeline.

---

# Technology Stack

**Programming Language**

Python

**AI Framework**

LangChain

**Large Language Model**

Groq LLM API

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

The model is responsible for:

* understanding natural language
* generating responses
* performing intent classification
* answering questions using context

The project uses Groq's hosted Llama model for fast inference and reliable performance.

The architecture is **model-agnostic**, meaning it can easily switch to other providers such as OpenAI, Gemini, or Anthropic.

---

## Intent Detection

Intent detection is the **decision engine** of the system.

Each user message is classified into one of three intents:

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

The intent classification determines the next action in the agent workflow.

---

## Retrieval-Augmented Generation (RAG)

Large language models sometimes hallucinate answers.

To avoid this, the system uses **Retrieval-Augmented Generation**.

The knowledge base contains structured product information such as:

* pricing plans
* features
* company policies

Example knowledge base entry:

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

When a user asks a question like:

```
What is your pricing?
```

The system retrieves the relevant information and provides a grounded response.

Benefits of RAG:

* reduces hallucinations
* ensures factual accuracy
* keeps answers consistent with company policies

---

## Lead Capture Tool

When the system detects **high purchase intent**, it triggers a lead capture workflow.

The agent collects the following information:

* name
* email
* creator platform

Example interaction:

User:

```
I want the Pro plan for my YouTube channel
```

Agent:

```
Great! What is your name?
```

User:

```
Name: Abhinav
```

Agent:

```
Please provide your email address
```

Once all details are collected, the system triggers the lead capture tool.

Example output:

```
Lead captured successfully: Abhinav, abhinav@email.com, YouTube
```

This simulates how companies store leads in a CRM system.

---

## Conversation Memory

The system maintains conversation state using a memory module.

Stored variables:

* user name
* email
* creator platform

This enables the agent to remember previous messages and complete the lead capture process across multiple turns.

---

## Agent Controller

The agent controller orchestrates the entire workflow.

Example logic:

```
If greeting
 → respond with welcome message

If product inquiry
 → use RAG knowledge base

If high intent
 → collect lead information
 → trigger lead capture tool
```

This makes the system **agentic rather than a simple chatbot.**

---

## Streamlit Chat Interface

The user interface is built using Streamlit.

Features include:

* real-time chat interface
* conversation history
* product information sidebar
* interactive user experience

The interface allows users to interact with the AI agent just like a real SaaS chatbot.

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

The agent then collects user details and stores the lead.

---

# Business Impact

This system can significantly improve customer acquisition.

Instead of manually handling conversations, companies can deploy an AI agent that:

* answers customer questions instantly
* identifies high-intent users
* captures leads automatically

Benefits include:

* faster customer response time
* increased conversion rates
* reduced workload for sales teams
* scalable customer engagement

---

# Real-World Applications

This architecture can be applied across multiple industries.

Examples include:

SaaS platforms capturing free trial users

E-commerce stores recommending products

Marketing campaigns converting social media conversations

Customer support automation

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

# Key Skills Demonstrated

This project demonstrates practical skills in:

* Generative AI systems
* LLM integration
* Retrieval-Augmented Generation
* conversational agent design
* AI application deployment
* full-stack AI development

---

# Future Improvements

Possible extensions include:

* vector database integration (FAISS / Pinecone)
* multi-platform integrations (WhatsApp, Slack)
* CRM integration
* real-time analytics dashboard
* multi-language support

---

# Conclusion

AutoStream Agentic Lead AI demonstrates how modern AI systems can transform simple conversations into meaningful business outcomes.

By combining **LLM reasoning, RAG knowledge retrieval, and automated lead capture**, the system creates an intelligent conversational agent capable of assisting users while simultaneously generating potential sales leads.

This architecture reflects how real-world AI assistants are built and deployed in modern SaaS products.
