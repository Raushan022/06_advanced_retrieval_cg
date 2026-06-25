from sentence_transformers import CrossEncoder

def create_reranker():
   return CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank_documents(
      reranker,
      query,
      documents,
      top_k=5
):
   pairs = [
      (
         query,
         doc.page_content,
      )
      for doc in documents
   ]

   scores = reranker.predict(pairs)

   ranked_docs = sorted(
      zip(documents, scores),
      key=lambda item: item[1],
      reverse=True
   ) 

   return [
      doc for doc, score in ranked_docs[:top_k]
   ]
