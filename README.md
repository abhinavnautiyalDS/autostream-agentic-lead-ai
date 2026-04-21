This project implements an Agentic Conversational AI system using LangGraph to simulate a real-world social-to-lead workflow.

LangGraph was chosen because it allows explicit control over agent state, decision flow, and tool execution. The architecture separates the system into three core components: intent detection, knowledge retrieval, and tool execution.

The intent classifier determines whether the user message is a greeting, product inquiry, or high-intent lead. For product inquiries, a RAG pipeline retrieves information from a local knowledge base stored in JSON format. The LLM uses this retrieved context to generate accurate responses about pricing, features, and policies.

When high intent is detected, the agent transitions into a lead qualification state where it sequentially collects the user’s name, email, and creator platform. This state is stored using a simple memory object to maintain conversation context across multiple turns.

Once all required fields are collected, the agent calls a tool function `mock_lead_capture()` to simulate backend CRM integration.

This modular architecture makes the system easy to extend for real deployments such as WhatsApp or website chatbots.
