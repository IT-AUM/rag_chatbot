from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query, index, chunks, top_k=3):
    query_vec = embedder.encode([query])
    _, I = index.search(query_vec, top_k)
    return "\n".join([chunks[i] for i in I[0]])
