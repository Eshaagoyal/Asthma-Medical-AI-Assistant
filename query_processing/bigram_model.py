from collections import defaultdict


class BigramModel:

    def __init__(self):

        self.bigram_counts = defaultdict(lambda: defaultdict(int))

    def train_from_documents(self, documents):

        for doc in documents:

            words = doc.page_content.lower().split()

            for i in range(len(words)-1):

                w1 = words[i]
                w2 = words[i+1]

                self.bigram_counts[w1][w2] += 1

    def suggest(self, word, top_k=3):

        candidates = self.bigram_counts[word]

        ranked = sorted(
            candidates.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [w for w,_ in ranked[:top_k]]