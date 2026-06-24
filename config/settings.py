# chunking
CHUNK_SIZE=1000
CHUNK_OVERLAP = 200

# Embeddings
EMBEDDING_MODEL = "text-embedding-3-small"

# LLM
LLM_MODEL = "gpt-4o-mini"

# Vector Store
VECTOR_STORE_PATH = "vector_store/faiss_index"

# Retrieval
TOP_K = 20

# Hybrid Search
DENSE_TOP_K = 20
BM25_TOP_K = 20

# Reranking
RERANK_TOP_K = 5

# Data
PDF_FOLDER = "data/pdfs"