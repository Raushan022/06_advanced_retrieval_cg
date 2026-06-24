from dotenv import load_dotenv

from data.urls import URLS

from loaders.web_loader import load_web_documents
from loaders.pdf_loader import load_pdf_documets

from cleaning.content_cleaner import clean_documents

from processing.chunking import chunk_documets

from retrieval.bm25_retriever import create_bm25_retriever, retrieve_documents_bm25
from retrieval.dense_retriever import create_dense_retriever, retrieve_documents_dense

from retrieval.hybrid_retriever import reciprocal_rank_fusion

load_dotenv()

def main():
   pdf_documents = load_pdf_documets()
   web_documents = load_web_documents(URLS)

   documents = pdf_documents + web_documents

   print(f"Documents Loaded: {len(documents)}")

   cleaned_documents = clean_documents(documents)

   chunks = chunk_documets(cleaned_documents)

   print(f"Chunks Created: {len(chunks)}")

   print("\nSample Chunk:\n")

   print(chunks[0].page_content[:500])

   bm25 = create_bm25_retriever(chunks)
   dense_retriever = create_dense_retriever(chunks)

   query = "What is a retriever?"

   bm25_results = retrieve_documents_bm25(
      bm25=bm25,
      chunks=chunks,
      query=query,
      k=3,
   )

   dense_results = retrieve_documents_dense(
      vector_store=dense_retriever,
      query=query,
      k=3,
   )

   hybrid_results = reciprocal_rank_fusion(
      [
         bm25_results,
         dense_results
      ]
   )

   print("\n=== BM25 ===")

   for doc in bm25_results:
      print(doc.page_content[:200])

   print("\n=== DENSE ===")

   for doc in dense_results:
      print(doc.page_content[:200])

   print("\n=== HYBRID RESULTS ===")

   for doc in hybrid_results[:3]:
      print(doc.page_content[:200])
      print("\n" + "-" * 50 + "\n")

   
    
if __name__ == "__main__":
   main()
