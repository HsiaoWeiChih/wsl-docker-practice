# WSL Docker 實戰練習：FastAPI + PostgreSQL

這是一個基於 Docker Compose 構建的微服務練習專案，整合了 Python FastAPI 後端與 PostgreSQL 資料庫，並實現了自動化資料庫初始化。

## 🚀 技術棧
* **Language:** Python 3.9 (FastAPI)
* **Database:** PostgreSQL 15
* **Infrastructure:** Docker / Docker Compose
* **OS Environment:** WSL 2 (Ubuntu)

## 🛠️ 快速啟動
確保你的環境已安裝 Docker 與 Docker Compose。

1. **複製專案**
   ```bash
   git clone <你的-github-連結>
   cd wsl-docker-practice

# 1. 一鍵啟動
docker-compose up -d --build

# 2. 停止並刪除容器，同時刪除舊的 Volume 資料
docker-compose down -v

# 3. 訪問 API 文件
http://localhost:18000/docs


## 常用指令
# 1. 一鍵啟動 (含編譯)：
docker-compose up -d --build
# 2. 停止並移除容器：
docker-compose down
# 3. 停止、移除容器並「刪除資料庫數據 (Volume)」：
docker-compose down -v
# 4. 查看所有服務日誌：
docker-compose logs -f
# 5. 只看 API 的日誌：
docker-compose logs -f api
# 6. 查看目前容器狀態與埠位映射：
docker-compose ps
# 7. 進入 PostgreSQL 終端機 (psql)：
docker exec -it my-postgres-db psql -U postgres
# 8. 進入 Python 容器內部的 Shell：
docker exec -it fastapi-service-compose /bin/bash
# 9. 清理系統資源
docker image prune -f
# 10. 全面大掃除 (刪除所有停止的容器、未使用的網路與掛載卷)：
docker system prune -a --volumes