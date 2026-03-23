class HybridRetriever:

    def __init__(self, vector_db, bm25_retriever, tfidf_retriever):

        self.vector_db = vector_db
        self.bm25 = bm25_retriever
        self.tfidf = tfidf_retriever

        print("Hybrid Retriever initialized.")


    def vector_search(self, query_vector, k=10):
        """
        Semantic search using FAISS vector DB
        """

        docs = self.vector_db.similarity_search_by_vector(
            query_vector,
            k=k
        )

        return docs


    def search(self, query, k=10):
        """
        Hybrid retrieval combining BM25 + TF-IDF + Vector
        """

        bm25_docs = self.bm25.search(query, k)
        tfidf_docs = self.tfidf.search(query, k)
        vector_docs = self.vector_db.similarity_search(query, k)

        # combine results
        combined = bm25_docs + tfidf_docs + vector_docs

        # remove duplicates
        unique_docs = list({doc.page_content: doc for doc in combined}.values())

        return unique_docs[:k]