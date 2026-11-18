# 115-backend

115 學年度後端課程作業。

## Week 1：單次模型呼叫

`week1_single_call.py` 以 `requests` 呼叫 NVIDIA API Catalog 的 Chat Completions 端點（模型 `minimaxai/minimax-m3.1-flash`），印出 HTTP 狀態碼、完整回應 JSON 與模型回覆。

### 執行方式

```bash
pip install -r requirements.txt
cp .env.example .env      # Windows PowerShell：copy .env.example .env
# 編輯 .env，填入 NVIDIA_API_KEY=你的金鑰
python week1_single_call.py
```

### 金鑰管理

- 金鑰只放在本機的 `.env`，不寫進程式碼。
- `.env` 已列入 `.gitignore`，不會被提交；repo 只提供不含值的 `.env.example`。
