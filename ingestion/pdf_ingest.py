from pypdf import PdfReader
from embeddings.embedder import embed_and_store

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

text = load_pdf("data/docs/manual.pdf")
embed_and_store([text])
