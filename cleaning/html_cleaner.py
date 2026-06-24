from bs4 import BeautifulSoup

def clean_html(html_content: str) -> str:
   """
   Remove unwanted HTML tags
   and return clean text.
   """

   soup = BeautifulSoup(html_content, "html.parser")

   for tag in soup(["script", "style"]):
      tag.decompose()

   return soup.get_text(separator=" ", strip=True)