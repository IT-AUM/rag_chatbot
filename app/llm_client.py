import requests
import json
from app.config import API_KEY, API_URL, MODEL

def call_openrouter_api(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    messages = [
        {"role": "system", "content": "Bạn là trợ lý AI chấm bài dựa trên nội dung trong file."},
        {"role": "user", "content": prompt}
    ]

    data = {
        "model": MODEL,
        "messages": messages,
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
