from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI(
    title="伺服器日誌 API",
    description="這是一個讀取容器化 PostgreSQL 資料庫的 API",
    version="1.0.0"
)

# 資料庫連線設定 (這些設定將透過 Docker 環境變數傳入)
DB_HOST = os.getenv("DB_HOST", "db") # 在 Docker 內部網路，DB 的主機名稱通常叫 db
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "mypassword")

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            cursor_factory=RealDictCursor # 讓查詢結果變成像 Python Dict 的格式
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# --- API 端點 ---

@app.get("/", tags=["一般"])
def read_root():
    return {"message": "歡迎使用伺服器日誌 API！請訪問 /docs 查看 OpenAPI 文件。"}

@app.get("/logs", tags=["資料庫"])
def get_logs():
    """
    讀取資料庫中所有的伺服器日誌。
    """
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="無法連線到資料庫")
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT status FROM server_log;")
        logs = cursor.fetchall()
        
    conn.close()
    
    # 如果資料庫是空的，回傳一個友好的訊息
    if not logs:
        return {"message": "目前沒有任何日誌紀錄。"}
        
    return {"logs": logs}