class ContextBuilder:

    def __init__(self, max_chunks=12, max_characters=6000):

        # number of retrieved chunks to include
        self.max_chunks = max_chunks

        # total characters allowed in prompt context
        self.max_characters = max_characters


    def build_context(self, documents):

        context_parts = []
        total_chars = 0

        for doc in documents[:self.max_chunks]:

            text = doc.page_content.strip()

            # limit individual chunk size
            text = text[:1200]

            if total_chars + len(text) > self.max_characters:
                break

            context_parts.append(text)
            total_chars += len(text)

        context = "\n\n".join(context_parts)

        return context