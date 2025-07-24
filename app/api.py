import gradio as gr
from app.data_loader import check_and_load_data
from app.chatbot import chat_with_bot

# Load FAISS + chunks
index, chunks = check_and_load_data("data/test.docx")

# Giao diện Gradio
def gr_chat_fn(message, history):
    return chat_with_bot(message, history, index, chunks)

def start_app():
    chatbot = gr.ChatInterface(fn=gr_chat_fn, title="💬 Chatbot VSTEP Checker")
    chatbot.launch(share=True)
