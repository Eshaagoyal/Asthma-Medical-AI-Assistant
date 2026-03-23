from transformers import AutoTokenizer


class Tokenizer:

    def __init__(self):

        self.tokenizer = AutoTokenizer.from_pretrained(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def tokenize(self, text):

        return self.tokenizer.tokenize(text.lower())
        