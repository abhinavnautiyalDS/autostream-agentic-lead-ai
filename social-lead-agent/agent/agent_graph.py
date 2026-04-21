from agent.intent_classifier import classify_intent
from agent.rag_pipeline import answer_query
from agent.tools import mock_lead_capture
from agent.memory import state


def run_agent(user_message):

    intent = classify_intent(user_message)

    if intent == "greeting":
        return "Hello! How can I help you with AutoStream today?"

    if intent == "product_inquiry":
        return answer_query(user_message)

    if intent == "high_intent":

        if not state.name:
            return "Great! I'd love to help you get started. What is your name?"

        if not state.email:
            return "Please provide your email address."

        if not state.platform:
            return "Which platform do you create content on? (YouTube, Instagram, etc.)"

        mock_lead_capture(state.name, state.email, state.platform)

        return "Perfect! Your lead has been captured. Our team will contact you shortly."

    return "Could you please clarify your question?"
