class MultiQueryExpander:

    def __init__(self, llm):

        self.llm = llm

    def expand(self, query):

        prompt = f"""

You are helping a medical search system retrieve information about asthma.

Given a user question, generate 6 different search queries that could help
find relevant medical documents.

Include variations such as:
• synonyms
• medical terminology
• alternative phrasing
• related terms

User question:
{query}

Search queries:
"""


        response = self.llm.invoke(prompt)

        queries = response.content.split("\n")

        return [q.strip() for q in queries if q.strip()]