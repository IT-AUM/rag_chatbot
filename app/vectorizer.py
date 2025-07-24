import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from app.data_loader import load_all_documents

# Cấu hình
CHUNK_SIZE = 500
VECTOR_DIM = 384  # all-MiniLM-L6-v2 => 384 chiều
VECTOR_PATH = "vector_store/vectorized_data.pkl"

# Chunking đoạn văn bản dài thành các phần nhỏ


def chunk_text(text, chunk_size=CHUNK_SIZE):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Nhúng văn bản và lưu FAISS index


def vectorize_and_save(docs):
    # Bước 1: Chunk toàn bộ văn bản
    chunks = []
    for doc in docs:
        chunks.extend(chunk_text(doc))

    print(f"🔢 Tổng số đoạn văn bản sau khi chunking: {len(chunks)}")

    # Bước 2: Tạo embedding
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, show_progress_bar=True)

    # Bước 3: Tạo FAISS index
    index = faiss.IndexFlatL2(VECTOR_DIM)
    index.add(embeddings)

    # Bước 4: Lưu index + chunks
    os.makedirs(os.path.dirname(VECTOR_PATH), exist_ok=True)
    with open(VECTOR_PATH, "wb") as f:
        pickle.dump({"faiss_index": index, "chunks": chunks}, f)

    print(f"✅ Đã lưu dữ liệu vector vào {VECTOR_PATH}")


# Entry point
if __name__ == "__main__":
    print("📄 Đang tải tài liệu...")
    docs = load_all_documents("data")

    if not docs:
        print("❌ Không tìm thấy tài liệu trong thư mục 'data/'. Hãy thêm file .txt, .docx, hoặc .html.")
    else:
        vectorize_and_save(docs)
