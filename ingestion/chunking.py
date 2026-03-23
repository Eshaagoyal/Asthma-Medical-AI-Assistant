from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Perform hierarchical chunking:
    Parent chunks (large context)
    Child chunks (retrieval units)
    """

    # Parent chunks
    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    parent_docs = parent_splitter.split_documents(documents)

    # Child chunks
    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    child_docs = child_splitter.split_documents(parent_docs)

    print(f"Parent chunks created: {len(parent_docs)}")
    print(f"Child chunks created: {len(child_docs)}")

    return parent_docs, child_docs