import re
from rank_bm25 import BM25Okapi

def tokenize_text(text: str):
   """
   Normalize and tokenize text.
   """

   text = text.lower()
   text = re.sub(r"[^\w\s]", "", text)

   return text.split()

def create_bm25_retriever(chunks):
   """
    Build BM25 index from chunks.
   """

   tokenized_chunks = [
      tokenize_text(chunk.page_content)
      for chunk in chunks
   ]

   bm25 = BM25Okapi(tokenized_chunks)

   return bm25

def retrieve_documents_bm25(
   bm25,
   chunks,
   query,
   k=5,
):
   """
   Retrieve top-k chunks using BM25.
   """

   tokenized_query = tokenize_text(query)

   scores = bm25.get_scores(tokenized_query) 

   ranked_indices = sorted(
      range(len(scores)),
      key=lambda i: scores[i],
      reverse=True
   )

   top_indices = ranked_indices[:k]

   return [chunks[i] for i in top_indices]