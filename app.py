import os

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from safety.guardrails import Guardrails

# Query processing
from query_processing.tokenization import Tokenizer
from query_processing.bigram_model import BigramModel
from query_processing.query_expansion import MultiQueryExpander
from query_processing.hyde import HydeGenerator
from query_processing.query_pipeline import QueryPipeline

# Retrieval modules
from retrieval.vector_search import load_vector_store
from retrieval.bm25_search import BM25Retriever
from retrieval.tfidf_search import TFIDFRetriever
from retrieval.hybrid_search import HybridRetriever
from retrieval.retrieval_pipeline import RetrievalPipeline

# RAG pipeline
from rag.rag_chain import RAGPipeline


def initialize_system():

    print("Initializing Asthma RAG System...\n")

    # Embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Groq LLM
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )

    # Load vector database
    vector_db = load_vector_store(embeddings)

    # Load stored documents for keyword retrieval
    documents = vector_db.similarity_search("", k=1000)

    # Keyword retrievers
    bm25_retriever = BM25Retriever(documents)
    tfidf_retriever = TFIDFRetriever(documents)

    # Hybrid retriever
    hybrid_retriever = HybridRetriever(
        vector_db,
        bm25_retriever,
        tfidf_retriever
    )

    # Query intelligence
    tokenizer = Tokenizer()
    bigram_model = BigramModel()
    multiquery = MultiQueryExpander(llm)
    hyde = HydeGenerator(llm, embeddings)

    query_pipeline = QueryPipeline(
        tokenizer,
        bigram_model,
        multiquery,
        hyde
    )

    # Retrieval pipeline
    retrieval_pipeline = RetrievalPipeline(
        query_pipeline,
        hybrid_retriever
    )

    # RAG pipeline
    rag = RAGPipeline(
        retrieval_pipeline,
        llm
    )

    print("System Ready!\n")

    return rag


def main():

    rag = initialize_system()

    # Initialize guardrails
    guard = Guardrails()

    print("Asthma Medical AI Assistant")
    print("Type 'exit' to quit.\n")

    short_query_map = {
        "symptom": "What are the symptoms of asthma?",
        "symptoms": "What are the symptoms of asthma?",
        "treatment": "How is asthma treated?",
        "treat": "How is asthma treated?",
        "inhaler": "What inhalers are used for asthma?",
        "inhalers": "What inhalers are used for asthma?",
        "causes": "What causes asthma?",
        "cause": "What causes asthma?",
        "triggers": "What triggers asthma attacks?",
        "trigger": "What triggers asthma attacks?",
        "attack": "What happens during an asthma attack?",
        "prevention": "How can asthma attacks be prevented?"
    }

    previous_query = ""

    while True:

        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        # Guardrail safety check
        safe, response = guard.filter_query(query)

        if not safe:
            print("\nAnswer:\n")
            print(response)
            print("\n---------------------------\n")
            continue

        normalized_query = query.lower().strip()

        # Handle follow-up questions using previous query
        if previous_query and any(word in normalized_query for word in ["it","its","this","that","they","them","these","those"]):
            query = previous_query + " " + query

        # Ensure asthma context
        if "asthma" not in normalized_query:
            query = "In asthma, " + query

        # Improve short queries
        for key in short_query_map:
            if key in normalized_query:
                query = short_query_map[key]
                break

        answer = rag.run(query)

        print("\nAnswer:\n")
        print(answer)

        print("\n---------------------------\n")

        previous_query = query


if __name__ == "__main__":
    main()