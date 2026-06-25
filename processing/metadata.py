from pathlib import Path

def normalize_metadata(documents):
   """
   Normalize metadata across sources.
   """

   normalized_documents = []

   for doc in documents:
      metadata = dict(doc.metadata)
      source = metadata.get("source", "")

      if source.startswith("http"):
         metadata["source_type"] = "web"
         metadata["source_name"] = source

      else:
         metadata["source_type"] = "pdf"
         metadata["source_name"] = Path(source).name

      doc.metadata = metadata

      normalized_documents.append(doc)

   return normalized_documents