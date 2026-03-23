from langchain_groq import ChatGroq

def fallback_answer(query):

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0.2
    )

    prompt = f"""
The asthma knowledge base did not contain a detailed answer.

Provide a short, simple medical explanation.

Question: {query}
"""

    response = llm.invoke(prompt)

    return response.content