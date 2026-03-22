FROM python:3.9-slim

WORKDIR /app

# 先複製 requirements 並安裝，這樣如果 requirements 沒變，Docker 會快取這一步，Build 速度更快
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製其餘程式碼
COPY . .

# 暴露 FastAPI 預設的 8000 連接埠
EXPOSE 8000

# 啟動指令：uvicorn 監聽所有介面 (0.0.0.0) 的 8000 埠
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]