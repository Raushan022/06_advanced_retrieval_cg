def build_context(documents):
   """
   Build context from retrieved documents.
   """

   return "\n\n".join(doc.page_content for doc in documents)