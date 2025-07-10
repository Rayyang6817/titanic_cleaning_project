# Titanic 資料清洗與排程實作專案

本專案為資料工程訓練實作，透過 Python、Pandas 對 Titanic 資料集進行清洗，並使用 Apache Airflow 進行排程自動化，整體環境使用 Docker 建立，包含 DAG 任務管理與資料掛載設定。

---

## 📁 專案結構說明

titanic_cleaning_project/
├── airflow_project/
│   ├── dags/                    # Airflow 任務排程腳本
│   │   ├── example_dag.py
│   │   └── titanic_dag.py       # 主要的 DAG 任務，執行 CSV 載入任務
│   ├── data/                    # 提供給 DAG 任務使用的資料
│   │   └── cleaned_titanic.csv
│   ├── logs/                    # Airflow 產生的 log 檔案
│   ├── plugins/                 # 預留自定 plugin 目錄
│   └── docker-compose.yaml     # Airflow 使用的 Docker 設定檔
│
├── data/
│   ├── uncleaned_titanic.csv    # 原始 Titanic 資料
│   └── cleaned_titanic.csv      # 資料清洗後結果
│
├── etl/
│   ├── train.csv                # 模擬資料來源
│   └── etl_house_price.py      # ETL 範例腳本，可匯入資料至 PostgreSQL
│
├── doc/
│   └── data_description.md     # Titanic 各欄位的中文說明
│
├── data_practice.py            # 資料清洗主要邏輯實作
├── .env                        # 儲存資料庫連線設定（已加入 .gitignore）
├── .gitignore                  # 忽略 log 和 .env 等敏感檔案
└── README.md                   # 專案說明文件（本檔案）
---

## 🔄 資料清洗步驟（`data_practice.py`）

1. 從 GitHub 讀取原始 Titanic 資料，儲存為 `uncleaned_titanic.csv`
2. 清理缺失值：
   - `Age` 欄位以中位數補齊
   - `Embarked` 欄位以眾數補齊
3. 編碼處理：
   - `Sex` 欄位轉為數字格式（male → 0, female → 1）
4. 移除不必要欄位：
   - `Cabin`, `Ticket`, `Name`, `PassengerId`
5. 將清理後結果輸出為 `cleaned_titanic.csv`

---

## 🗂 Airflow 排程邏輯（`titanic_dag.py`）

- 設定 DAG 任務 ID 為 `read_titanic_csv`
- 使用 `PythonOperator` 執行資料讀取任務
- 任務內容為讀取 `/opt/airflow/data/cleaned_titanic.csv` 並列印前五筆資料
- 不進行排程（`schedule_interval=None`），手動觸發執行

---

## 🐳 Docker 環境設定（`docker-compose.yaml`）

- 使用 `apache/airflow:2.8.1` 映像檔
- 定義以下掛載資料夾：
  - `./dags` → `/opt/airflow/dags`
  - `./logs` → `/opt/airflow/logs`
  - `./plugins` → `/opt/airflow/plugins`
  - `./data` → `/opt/airflow/data`
- Airflow Webserver 開放於本機端 `localhost:8080`
- 使用 `.env` 存放連線資料（如 PostgreSQL）

---

## ▶ 執行步驟

1. 安裝 Docker 與 Docker Compose
2. 於專案根目錄執行：
   ```bash
   docker-compose up
開啟瀏覽器進入 http://localhost:8080

登入 Airflow，啟用 DAG read_titanic_csv 並手動執行

於 Airflow Log 中可看到前五筆清洗後的資料輸出

📌 資料來源
Titanic 資料集來自 Data Science Dojo GitHub

📍備註與學習重點
熟悉資料清洗流程與 pandas 操作

實作 DAG 任務撰寫與排程邏輯

完成 Docker + Airflow 開發環境建置

使用 .env 管理敏感資訊並加入 .gitignore 保護

了解 Airflow DAG 的部署與排程流程