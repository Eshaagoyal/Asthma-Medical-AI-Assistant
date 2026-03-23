from langchain_community.embeddings import HuggingFaceEmbeddings


def load_embeddings():
    """
    Load embedding model used for semantic search
    """

    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    print("Embedding model loaded:", model_name)

    return embeddings