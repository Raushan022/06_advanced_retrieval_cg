import re
from langchain_core.documents import Document

def clean_text(text: str) -> str:
   """
   Normalize whitespace.
   """

   text = re.sub(r"\s+", " ", text)

   return text.strip()

def clean_documents(documents: list[Document]) -> list[Document]:
   """
   Clean document contents.
   """

   cleaned_documets = []

   for doc in documents:
      cleaned_text = clean_text(doc.page_content)

      cleaned_doc = Document(
         page_content=cleaned_text,
         metadata=doc.metadata
      )

      cleaned_documets.append(cleaned_doc)

   return cleaned_documets