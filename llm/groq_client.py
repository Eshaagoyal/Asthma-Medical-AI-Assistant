from langchain_groq import ChatGroq
import os


def load_llm():

    llm = ChatGroq(
        model_name="llama3-70b-8192",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )

    return llm