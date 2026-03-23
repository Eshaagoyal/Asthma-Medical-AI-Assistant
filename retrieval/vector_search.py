from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embeddings):
    """
    Create FAISS vector database from chunks
    """

    print("Creating FAISS vector database...")

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_db.save_local("vector_db")

    print("Vector database saved in /vector_db")

    return vector_db


def load_vector_store(embeddings):
    """
    Load existing FAISS vector database
    """

    print("Loading FAISS vector database...")

    vector_db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db