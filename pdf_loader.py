from pypdf import PdfReader
from langchain.schema import Document

def load_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return [Document(page_content=text)]
