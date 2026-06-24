from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from config.settings import PDF_FOLDER

def load_pdf_documets():
   """
    Load all PDFs from the PDF folder.
   """

   documents = []

   pdf_files = Path(PDF_FOLDER).glob("*pdf")

   for pdf_file in pdf_files:
      loader = PyPDFLoader(str(pdf_file))
      docs = loader.load()
      documents.extend(docs)

   return documents