-- 如果表已經存在就先刪除（確保每次初始化都是乾淨的）
DROP TABLE IF EXISTS server_log;

-- 建立資料表
CREATE TABLE server_log (
    id SERIAL PRIMARY KEY,
    status TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入一些初始測試資料
INSERT INTO server_log (status) VALUES ('系統初始化成功');
INSERT INTO server_log (status) VALUES ('BMC 韌體版本檢查完畢');
INSERT INTO server_log (status) VALUES ('Docker Compose 自動部署完成');