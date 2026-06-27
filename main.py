from dotenv import load_dotenv

from data.urls import URLS

from loaders.web_loader import load_web_documents
from loaders.pdf_loader import load_pdf_documets

from processing.metadata import normalize_metadata
from processing.chunking import chunk_documets

from cleaning.content_cleaner import clean_documents

from vectorstore.faiss_manager import load_or_create_vector_store

from retrieval.bm25_retriever import create_bm25_retriever
from retrieval.reranker import create_reranker
from retrieval.retrieval_service import retrieve_documents

from rag.context_builder import build_context

from rag.generator import generate_answer

load_dotenv()

def main():
   
   print("Loading documents...")

   pdf_documents = load_pdf_documets()
   web_documents = load_web_documents(URLS)

   documents = pdf_documents + web_documents

   print(f"Documents Loaded: {len(documents)}")

   documents = normalize_metadata(documents)
   documents = clean_documents(documents)
   chunks = chunk_documets(documents)

   print(f"Chunks Created: {len(chunks)}")

   vector_store = load_or_create_vector_store(chunks)

   bm25 = create_bm25_retriever(chunks)
   reranker = create_reranker()

   print("\nAdvanced Retrieval System Ready!")

   while True:
      query = input("\nAsk: ").strip()

      if query.lower() in ["exit", "quit", "q"]:
         print("Goodbye!!")
         break

      retrieved_docs = retrieve_documents(
         query=query,
         bm25=bm25,
         chunks=chunks,
         vector_store=vector_store,
         reranker=reranker
      )

      context = build_context(retrieved_docs)
      answer = generate_answer(query=query, context=context)

      print("\nAnswer:\n")
      print(answer)

      print("\nSources:")

      sources = {
         doc.metadata.get("source_name", "Unknown") for doc in retrieved_docs
      }

      for source in sources:
         print(f"- {source}")
    
if __name__ == "__main__":
   main()
