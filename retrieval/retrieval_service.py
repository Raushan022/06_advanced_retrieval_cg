# This is where the whole retrieval pipeline lives

from config.settings import (
   BM25_TOP_K,
   DENSE_TOP_K,
   RERANK_TOP_K
)

from retrieval.bm25_retriever import retrieve_documents_bm25
from retrieval.dense_retriever import retrieve_documents_dense
from retrieval.hybrid_retriever import reciprocal_rank_fusion
from retrieval.metadata_filter import filter_documets
from retrieval.reranker import rerank_documents

def retrieve_documents(
      query,
      bm25,
      chunks,
      vector_store,
      reranker,
      metadata_filters=None
):
   bm25_results = retrieve_documents_bm25(bm25=bm25, chunks=chunks, query=query, k=BM25_TOP_K)
   dense_results = retrieve_documents_dense(vector_store=vector_store, query=query, k=DENSE_TOP_K)
   hybrid_result = reciprocal_rank_fusion([bm25_results, dense_results])

   filtered_results = filter_documets(hybrid_result, metadata_filters)

   reranked_results = rerank_documents(reranker=reranker, query=query, documents=filtered_results, top_k=RERANK_TOP_K)

   return reranked_results