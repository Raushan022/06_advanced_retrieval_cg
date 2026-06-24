from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import (
   CHUNK_SIZE,
   CHUNK_OVERLAP
)

def chunk_documets(documents):
   """
    Split documents into chunks.
   """

   text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=CHUNK_SIZE,
      chunk_overlap=CHUNK_OVERLAP,
   )

   return text_splitter.split_documents(documents)