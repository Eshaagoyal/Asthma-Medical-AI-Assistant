from ingestion.document_loader import load_documents
from ingestion.chunking import split_documents
from ingestion.embedding import load_embeddings
from retrieval.vector_search import create_vector_store


def build_vector_database():

    print("\nSTEP 1: Loading documents...")
    docs = load_documents()

    if not docs:
        print("No documents loaded.")
        return

    print("\nSTEP 2: Chunking documents...")
    parent_chunks, child_chunks = split_documents(docs)

    print("\nSTEP 3: Loading embedding model...")
    embeddings = load_embeddings()

    print("\nSTEP 4: Creating vector database...")
    vector_db = create_vector_store(child_chunks, embeddings)

    print("\nVector database creation complete!")


if __name__ == "__main__":
    build_vector_database()