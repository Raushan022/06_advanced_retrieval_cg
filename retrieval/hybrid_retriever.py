from collections import defaultdict

def reciprocal_rank(rank, k=60):
   return 1 / (k + rank)

def reciprocal_rank_fusion(result_lists):
   """
   Combine rankings from multiple retrieval systems.
   """
   scores = defaultdict(float)

   document_map = {}

   for results in result_lists:
      for rank, doc in enumerate(results, start=1):
         doc_key = id(doc)
         document_map[doc_key] = doc
         scores[doc_key] += reciprocal_rank(rank)

         # doc_id = doc.page_content
         # scores[doc_id] += reciprocal_rank(rank)

   ranked_docs = sorted(
      scores.items(),
      key=lambda item: item[1],
      reverse=True,
   )

   return [
      document_map[doc_key]
      for doc_key, _ in ranked_docs
   ]
