from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from config.settings import EMBEDDING_MODEL

def create_dense_retriever(chunks):
   embeddings = OpenAIEmbeddings(
      model=EMBEDDING_MODEL
   )

   vector_store = FAISS.from_documents(
      chunks,
      embeddings
   )

   return vector_store

def retrieve_documents_dense(
      vector_store,
      query,
      k=10,
):
   return vector_store.similarity_search(
      query,
      k=k
   )