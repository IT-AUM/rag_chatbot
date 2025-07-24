from app.embedder import retrieve_context
from app.llm_client import call_openrouter_api

def build_prompt(context, message):
    return f"""Hãy chấm bài viết sau theo thang điểm VSTEP B1 Sau đó chữa bài theo các yêu cầu chấm trong ảnh đính kèm...

{context}

Câu hỏi: {message}"""

def chat_with_bot(message, history, index, chunks):
    context = retrieve_context(message, index, chunks)
    prompt = build_prompt(context, message)
    return call_openrouter_api(prompt)
