def filter_documets(documents, metadata_filters = None):
   if not metadata_filters:
      return documents
   
   filtered_documets = []

   for doc in documents:
      match = True

      for key, value in metadata_filters.items():
         if (doc.metadata.get(key) != value):
            match = False
            break
      
      if match:
         filtered_documets.append(doc)

   return filter_documets