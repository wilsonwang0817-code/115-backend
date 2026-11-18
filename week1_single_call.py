"""115-backend Week 1：用 Python 送出一次 Chat Completions 呼叫。

執行前先設定環境變數（金鑰不要寫進程式碼）：
    export NVIDIA_API_KEY=你的金鑰
    python3 week1_single_call.py
"""
import json
import os

import requests

API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "minimaxai/minimax-m3.1-flash"


def call_model(messages):
    api_key = os.environ["NVIDIA_API_KEY"]
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": 512,
        "temperature": 1,
        "top_p": 0.95,
    }
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    data = resp.json()

    print("status:", resp.status_code)
    print(json.dumps(data, ensure_ascii=False, indent=2))
    if resp.ok:
        print("reply:", data["choices"][0]["message"]["content"])
    else:
        print("error:", data.get("error") or data.get("detail"))
    return data


if __name__ == "__main__":
    call_model([{"role": "user", "content": "用一句話說明什麼是 HTTP"}])
