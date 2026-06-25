from langchain_openai import ChatOpenAI

from config.settings import LLM_MODEL

def generate_answer(query, context):
   llm = ChatOpenAI(
      model=LLM_MODEL,
      temperature=0
   )

   prompt = f"""
   You are a helpful AI assistant.

   Answer the user's question using only the provided context.

   Context:
   {context}

   Question:
   {query}
   """

   response = llm.invoke(prompt)

   return response.content