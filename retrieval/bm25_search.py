from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, documents):

        self.documents = documents

        self.corpus = [
            doc.page_content.split() for doc in documents
        ]

        self.bm25 = BM25Okapi(self.corpus)

        print("BM25 index created.")

    def search(self, query, k=5):

        tokenized_query = query.split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:k]

        results = [self.documents[i] for i in ranked_indices]

        return results