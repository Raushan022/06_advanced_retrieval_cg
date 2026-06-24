from langchain_community.document_loaders import WebBaseLoader

def load_web_documents(urls: list[str]):
   """
    Load documents from websites.
   """

   documents = []

   for url in urls:
      loader = WebBaseLoader(url)
      docs = loader.load()

      documents.extend(docs)

   return documents