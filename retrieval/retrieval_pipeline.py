from collections import defaultdict


class RetrievalPipeline:

    def __init__(self, query_pipeline, hybrid_retriever):

        self.query_pipeline = query_pipeline
        self.hybrid_retriever = hybrid_retriever


    def reciprocal_rank_fusion(self, results, k=60):

        scores = defaultdict(float)
        doc_map = {}

        for docs in results:

            for rank, doc in enumerate(docs):

                key = doc.page_content

                scores[key] += 1 / (k + rank)

                doc_map[key] = doc

        ranked_docs = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [doc_map[key] for key, _ in ranked_docs]


    def retrieve(self, query, top_k=20):

        query_data = self.query_pipeline.process(query)

        queries = query_data["all_queries"]
        hyde_vector = query_data["hyde_vector"]

        results = []


        # Hybrid retrieval for expanded queries
        for q in queries[:6]:

            docs = self.hybrid_retriever.search(q)

            results.append(docs)


        # HyDE vector retrieval
        hyde_docs = self.hybrid_retriever.vector_search(hyde_vector)

        results.append(hyde_docs)


        # Rank fusion
        fused_docs = self.reciprocal_rank_fusion(results)

        return fused_docs[:top_k]