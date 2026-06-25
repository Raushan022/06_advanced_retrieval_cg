from pathlib import Path

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from config.settings import (
   EMBEDDING_MODEL,
   VECTOR_STORE_PATH
)

def create_vector_store(chunks):
   embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

   return FAISS.from_documents(
      chunks,
      embeddings
   )

def save_vector_store(vector_store):
   vector_store.save_local(VECTOR_STORE_PATH)

def load_vector_store():
   embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

   return FAISS.load_local(
      VECTOR_STORE_PATH,
      embeddings,
      allow_dangerous_deserialization=True,
   )

def load_or_create_vector_store(chunks):
   index_path = Path(VECTOR_STORE_PATH)

   if index_path.exists():
      print("Loading FAISS index...")

      return load_vector_store()
   
   print("Creating FAISS index...")

   vector_store = create_vector_store(chunks)

   save_vector_store(vector_store)

   return vector_store

