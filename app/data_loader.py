import pickle
import os
from sentence_transformers import SentenceTransformer
import faiss
from docx import Document

VECTOR_PATH = "vector_store/vectorized_data.pkl"
EMBED_DIM = 384

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

def process_text_to_vector(text, chunk_size=500):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(EMBED_DIM)
    index.add(embeddings)
    return index, chunks

def save_data(index, chunks):
    os.makedirs("vector_store", exist_ok=True)
    with open(VECTOR_PATH, "wb") as f:
        pickle.dump((index, chunks), f)

def load_data():
    with open(VECTOR_PATH, "rb") as f:
        return pickle.load(f)

def check_and_load_data(docx_path="data/test.docx"):
    try:
        return load_data()
    except Exception:
        raw_text = extract_text_from_docx(docx_path)
        index, chunks = process_text_to_vector(raw_text)
        save_data(index, chunks)
        return index, chunks
