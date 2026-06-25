import re
from langchain_core.documents import Document

NOISE_PATTERNS = [
   "Try LangSmith",
   "GitHub",
]

def clean_text(text: str):
   """
   Normalize text content.
   """

   for pattern in NOISE_PATTERNS:
      text = text.replace(pattern, "")

   text = re.sub(r"\s+", " ", text)

   return text.strip()

def clean_documents(documents):
   """
   Clean document content.
   """

   cleaned_documents = []

   for doc in documents:
      cleaned_text = clean_text(doc.page_content)

      cleaned_doc = Document(
         page_content=cleaned_text,
         metadata={
            **doc.metadata,
            "cleaned": True,
         },
      )

      cleaned_documents.append(cleaned_doc)

   return cleaned_documents