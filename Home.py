import streamlit as st

st.set_page_config(
    page_title="Asthma Medical AI Assistant",
    page_icon="🫁",
    layout="centered"
)

st.title("🫁 Asthma Medical AI Assistant")

st.markdown(
"""
Welcome to the **Asthma Medical AI Assistant**, an AI-powered platform designed to help users understand asthma using trusted medical documents and intelligent retrieval systems.

This tool combines **Retrieval-Augmented Generation (RAG)** with curated medical knowledge to explain asthma symptoms, triggers, treatments, and breathing-related situations in a clear and accessible way.

The goal is to make complex respiratory health information **easier to understand for patients, caregivers, and students.**
"""
)

st.markdown("---")

st.subheader("🔎 What This AI Can Help With")

st.markdown(
"""
**💬 Chat Assistant**  
Ask questions about asthma symptoms, causes, treatments, inhalers, and prevention.

**🩺 Scenario Advisor**  
Describe a breathing-related situation and the AI will analyze possible explanations using medical knowledge.


)

st.markdown("---")

st.subheader("⚙️ How This AI Works")

st.markdown(
"""
This system uses modern AI techniques to retrieve and explain medical information from a knowledge base of asthma-related documents.

Key technologies used in this system include:

• Retrieval-Augmented Generation (RAG)  
• Hybrid document retrieval (vector + keyword search)  
• Medical document embeddings and chunking  
• Scenario-based reasoning for breathing situations  
• Guardrails for safer AI responses  

Before generating an answer, the AI retrieves relevant information from the medical knowledge base to improve accuracy and relevance.
"""
)

st.markdown("---")

st.subheader("🧠 Knowledge Base")

st.markdown(
"""
The assistant retrieves information from asthma-related medical resources including:

• Clinical asthma guidelines  
• Educational respiratory health materials  
• Asthma management and treatment resources  

These documents help the system generate responses grounded in **real medical knowledge**.
"""
)

st.markdown("---")

st.subheader("⚠️ Responsible Use")

st.info(
"""
This AI assistant provides **information based on medical knowledge sources** and is intended to support understanding of asthma and respiratory health.

However, medical conditions can vary between individuals.  
For diagnosis or treatment decisions, it is recommended to consult a **qualified healthcare professional**.
"""
)

st.markdown("---")

st.success("Use the **sidebar** to explore the tools and start interacting with the AI assistant.")

# streamlit run home.py