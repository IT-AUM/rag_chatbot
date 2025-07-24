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

\`\`\`bash
rag_chatbot/
├── app/
│ ├── **init**.py
│ ├── api.py
│ ├── chatbot.py
│ ├── config.py
│ ├── data_loader.py
│ ├── embedder.py
│ └── llm_client.py
├── data/
│ └── test.docx
├── vector_store/
│ └── vectorized_data.pkl
├── main.py
├── .env
├── .gitignore
└── requirements.txt
\`\`\`

---

## ⚙️ Yêu cầu

- Python 3.10 hoặc 3.11
- Internet (để gọi OpenRouter)

---

## 📦 Cài đặt

\`\`\`bash

# 1. Clone project

git clone https://github.com/tenban/rag_chatbot.git
cd rag_chatbot

# 2. Tạo virtual env

python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate

# 3. Cài thư viện

pip install -r requirements.txt

# 4. Tạo file .env

cp .env.example .env # hoặc tự tạo và cấu hình như bên dưới

# 5. Chạy chatbot

python main.py
\`\`\`

---

## 🔐 Cấu hình `.env`

\`\`\`env
API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
API_URL=https://openrouter.ai/api/v1/chat/completions
MODEL=deepseek/deepseek-chat-v3-0324:free
\`\`\`

---

## 💡 Cách hoạt động

1. Khi chạy lần đầu:

   - Tải file `data/test.docx`
   - Chia nhỏ và nhúng văn bản thành vector
   - Lưu vào FAISS (`vector_store/vectorized_data.pkl`)

2. Khi người dùng đặt câu hỏi:
   - Chatbot tìm đoạn văn liên quan trong FAISS
   - Tạo prompt và gửi lên OpenRouter
   - Trả về phản hồi từ LLM

---

## 🧪 Demo Gradio

Chạy:
\`\`\`bash
python main.py
\`\`\`

Mở trình duyệt tại: http://127.0.0.1:7860

---

## 📌 Format đầu ra mẫu

\`\`\`text
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

* Lỗi từ vựng:
* Lỗi ngữ pháp:
* Lỗi diễn đạt:
  \`\`\`

---

## ✅ TODO tiếp theo

- [ ] Cho phép upload file mới
- [ ] Lưu lịch sử
- [ ] Triển khai thật
- [ ] Gắn ảnh tiêu chí chấm điểm

---

## 📄 License

MIT License.

---

## 👨‍💻 Tác giả

Dự án bởi [Tên bạn] – Trung tâm CNTT.
