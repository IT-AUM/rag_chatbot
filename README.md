# 💬 RAG Chatbot - Chấm điểm VSTEP B1

Một chatbot sử dụng kỹ thuật **RAG (Retrieval-Augmented Generation)** để chấm điểm bài viết tiếng Anh theo tiêu chí VSTEP B1. Hệ thống sử dụng dữ liệu nội bộ (ví dụ: file `.docx`) kết hợp với mô hình ngôn ngữ lớn (LLM) để trả lời chính xác và theo ngữ cảnh.

---

## 🚀 Tính năng

- 📄 Đọc và xử lý văn bản từ file Word (.docx)
- 🧠 Tách và vector hóa dữ liệu bằng **SentenceTransformer**
- 🔍 Truy xuất đoạn văn bản liên quan bằng **FAISS**
- 🤖 Gọi LLM thông qua **OpenRouter API** để chấm điểm bài viết
- 🧑‍🏫 Giao diện **Gradio** đơn giản để tương tác
- 🔐 Cấu hình API qua `.env`

---

## 📁 Cấu trúc thư mục

```bash
rag_chatbot/
├── app/
│   ├── __init__.py              # Khởi động app
│   ├── api.py                   # Giao diện Gradio
│   ├── chatbot.py               # Xử lý câu hỏi và sinh câu trả lời
│   ├── config.py                # Đọc biến môi trường
│   ├── data_loader.py           # Xử lý file .docx, tạo FAISS
│   ├── embedder.py              # Nhúng và truy xuất vector
│   └── llm_client.py            # Gọi API OpenRouter
├── data/
│   └── test.docx                # File dữ liệu đầu vào
├── vector_store/
│   └── vectorized_data.pkl      # Vector + chunks (tự tạo sau lần đầu)
├── main.py                      # Entry point gọi start_app()
├── .env                         # Biến môi trường (không commit)
├── .gitignore
└── requirements.txt
⚙️ Yêu cầu
Python 3.10 hoặc 3.11 (không khuyến nghị dùng 3.12)

Internet (để gọi OpenRouter)

📦 Cài đặt
bash
Copy
Edit
# 1. Clone project
git clone https://github.com/tenban/rag_chatbot.git
cd rag_chatbot

# 2. Tạo virtual env
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Tạo file .env
cp .env.example .env  # hoặc tự tạo và cấu hình như bên dưới

# 5. Chạy chatbot
python main.py
🔐 Cấu hình .env
Tạo file .env và thêm:

env
Copy
Edit
API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
API_URL=https://openrouter.ai/api/v1/chat/completions
MODEL=deepseek/deepseek-chat-v3-0324:free
📌 Bạn có thể dùng bất kỳ model miễn phí nào được hỗ trợ bởi OpenRouter.

💡 Cách hoạt động
Khi chạy lần đầu, hệ thống:

Tải file data/test.docx

Chia nhỏ và nhúng văn bản thành vector

Lưu vào FAISS (vector_store/vectorized_data.pkl)

Khi người dùng đặt câu hỏi (bài viết cần chấm điểm):

Chatbot tìm các đoạn văn liên quan trong FAISS

Tạo prompt chi tiết gửi lên OpenRouter

Nhận phản hồi, hiển thị qua Gradio

🧪 Demo Gradio
Khi chạy, bạn sẽ thấy:

bash
Copy
Edit
Running on local URL:  http://127.0.0.1:7860
Truy cập địa chỉ đó để chat với hệ thống.

📌 Format đầu ra mẫu
text
Copy
Edit
a. Điểm
- Task fulfillment: 3
- Organization: 3
- Vocabulary: 3
- Grammar: 2
=> Overall: 2.75

b. Chữa bài
- Nhận xét chung:
- Vấn đề chung:
- Các lỗi chi tiết:
+ Lỗi từ vựng:
+ Lỗi ngữ pháp:
+ Lỗi diễn đạt:
✅ TODO tiếp theo
 Cho phép người dùng upload file Word mới và xử lý lại FAISS

 Lưu lịch sử chấm điểm

 Triển khai trên server thật (Hugging Face Space, Streamlit Cloud, Render...)

 Gắn ảnh tiêu chí chấm điểm

📄 License
MIT License.

👨‍💻 Tác giả
Dự án bởi [Tên bạn] – Trung tâm CNTT.

css
Copy
Edit

---

✅ Nếu bạn muốn mình **tạo sẵn file `README.md` này trong thư mục dự án hiện tại** hoặc **gửi bản markdown đẹp (PDF / HTML)** thì chỉ cần nói:
**"tạo file README trong project"** hoặc **"xuất PDF đẹp"**.
```
