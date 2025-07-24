import faiss
import pickle
from sentence_transformers import SentenceTransformer
from docx import Document


# ===== ĐỌC FILE DOCX =====
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"  # Thêm dòng mới sau mỗi đoạn văn
    return text


# ===== VECTOR HÓA VĂN BẢN =====
def process_text_to_vector(text, chunk_size=500):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]  # Chia văn bản thành các đoạn nhỏ
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    index = faiss.IndexFlatL2(384)
    embeddings = embedder.encode(chunks)  # Vector hóa các đoạn văn
    index.add(embeddings)  # Thêm các embedding vào FAISS index
    return index, chunks


# Lưu dữ liệu vectorized vào file
def save_data_to_file(docx_path, filename="vectorized_data.pkl"):
    raw_text = extract_text_from_docx(docx_path)
    index, documents = process_text_to_vector(raw_text)

    with open(filename, "wb") as f:
        pickle.dump((index, documents), f)


# Đọc dữ liệu vectorized từ file
def load_data_from_file(filename="vectorized_data.pkl"):
    with open(filename, "rb") as f:
        index, documents = pickle.load(f)
    return index, documents


# Kiểm tra nếu dữ liệu đã có trong file, nếu chưa thì load và lưu
def check_and_load_data(docx_path, filename="vectorized_data.pkl"):
    try:
        # Thử đọc dữ liệu từ file
        return load_data_from_file(filename)
    except (FileNotFoundError, pickle.UnpicklingError):
        # Nếu không tìm thấy file hoặc dữ liệu bị hỏng, load lại từ docx và lưu vào file
        save_data_to_file(docx_path, filename)
        return load_data_from_file(filename)


# Sử dụng hàm này để load dữ liệu, không phải lúc nào cũng tải lại
index, documents = check_and_load_data("test.docx")
