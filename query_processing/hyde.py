class HydeGenerator:

    def __init__(self, llm, embeddings):

        self.llm = llm
        self.embeddings = embeddings

    def generate_vector(self, query):

        prompt = f"""

You are a medical expert.

Write a short factual paragraph answering the
following asthma-related question.

Question:
{query}

Use medical terminology when possible.
"""

        response = self.llm.invoke(prompt)

        hypothetical_doc = response.content

        vector = self.embeddings.embed_query(hypothetical_doc)

        return vector