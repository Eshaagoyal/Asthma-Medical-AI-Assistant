from rag.context_builder import ContextBuilder
from rag.prompt_template import build_prompt, SYSTEM_PROMPT


class RAGPipeline:

    def __init__(self, retrieval_pipeline, llm):

        self.retrieval_pipeline = retrieval_pipeline
        self.llm = llm
        self.context_builder = ContextBuilder()


    def run(self, query):

        # 1️⃣ Retrieve relevant documents
        documents = self.retrieval_pipeline.retrieve(query)
        context = self.context_builder.build_context(documents)
        # if len(context.strip()) < 50:
            # from tools.api_fallback import fallback_answer
            # return fallback_answer(query)
       

        # 2️⃣ Build context
        context = self.context_builder.build_context(documents)

        # 3️⃣ Build user prompt
        user_prompt = build_prompt(context, query)

        # 4️⃣ Send system + user messages to LLM
        response = self.llm.invoke([
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ])

        return response.content