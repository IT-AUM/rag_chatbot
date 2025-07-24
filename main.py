import gradio as gr
import requests
import json

from sentence_transformers import SentenceTransformer

from data_loader import check_and_load_data  # Import hàm từ data_loader.py

# ===== CẤU HÌNH =====
# Thay bằng key thật
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-chat-v3-0324:free"

# ===== LOAD DỮ LIỆU =====
index, documents = check_and_load_data(
    "test.docx")  # Đọc dữ liệu từ file đã lưu

embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ===== XỬ LÝ CÂU HỎI =====


def retrieve_context(query, top_k=3):
    query_vec = embedder.encode([query])
    D, I = index.search(query_vec, top_k)
    return "\n".join([documents[i] for i in I[0]])


def chat_with_bot(message, history):
    context = retrieve_context(message)
    prompt = f"""Hãy chấm bài viết sau theo thang điểm VSTEP B1. Sau đó chữa bài theo các yêu cầu chấm trong ảnh đính kèm; Lưu ý: Ở những phần chữa lỗi, hãy giải thích tại sao bạn sửa thành như vậy. Hãy chấm thật kỹ nhé (Chấm/ chữa bằng tiếng việt) Lưu ý kết quả trả ra . Format chấm điểm (Kết quả trả ra)
a.	Điểm
-	Task fulfillment: 
-	Organization: 
-	Vocabulary: 
-	Grammar: 
=> Overall:
b.	Chữa bài
- Nhận xét chung: 
- Vấn đề chung:
- Các lỗi chi tiết: 
+ Lỗi từ vựng:
+ Lỗi ngữ pháp:
+ Lỗi diễn đạt (điều chỉnh lỗi diễn đạt, gợi ý thêm các câu mới hoặc cải thiện cách viết, gợi ý thêm ý tưởng triển khai mới) 
Bên trên là kết quả trả ra khi tôi muốn chấm điểm, bạn cần trả lời dựa theo các đầu mục đó
":\n\n{context}\n\nCâu hỏi: {message}"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    messages = [
        {"role": "system", "content": "Bạn là trợ lý AI dựa trên file test.docx."},
        {"role": "user", "content": prompt}
    ]

    data = {
        "model": MODEL,
        "messages": messages,
    }

    try:
        response = requests.post(
            API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        # Kiểm tra nếu nội dung rỗng hoặc không hợp lệ
        if not response.text.strip():
            return "❌ API trả về nội dung rỗng."

        # In response để debug nếu cần
        print("RAW RESPONSE:", response.text)

        # Cố gắng parse JSON
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        return reply

    except requests.exceptions.HTTPError as e:
        return f"❌ Lỗi HTTP: {e}\n\nPhản hồi:\n{response.text}"

    except json.JSONDecodeError as e:
        return f"❌ Lỗi khi phân tích JSON: {e}\n\nPhản hồi:\n{response.text}"

    except Exception as e:
        return f"❌ Lỗi không xác định: {e}"


# ===== GRADIO UI =====
chatbot = gr.ChatInterface(
    fn=chat_with_bot, title="💬 Chatbot với dữ liệu từ test.docx")

if __name__ == "__main__":
    chatbot.launch(share=True)
