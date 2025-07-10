# Titanic 資料清洗與排程實作專案

本專案為資料工程訓練實作，透過 Python、Pandas 對 Titanic 資料集進行清洗，並使用 Apache Airflow 進行排程自動化，整體環境使用 Docker 建立，包含 DAG 任務管理與資料掛載設定。

---

## 📁 專案結構說明
``` 
titanic_cleaning_project/
├── airflow_project/
│ ├── dags/
│ │ ├── example_dag.py
│ │ └── titanic_dag.py
│ ├── data/
│ │ └── cleaned_titanic.csv
│ ├── logs/
│ ├── plugins/
│ └── docker-compose.yaml
├── data/
│ ├── uncleaned_titanic.csv
│ └── cleaned_titanic.csv
├── etl/
│ ├── train.csv
│ └── etl_house_price.py
├── doc/
│ └── data_description.md
├── data_practice.py
├── .env
├── .gitignore
└── README.md
```
---

### 📄 各目錄/檔案說明

- `airflow_project/dags/`  
  放置 Airflow 任務排程的 Python 腳本

- `airflow_project/dags/titanic_dag.py`  
  主要 DAG 任務，負責觸發 CSV 載入任務

- `airflow_project/data/cleaned_titanic.csv`  
  提供給 DAG 使用的清洗後資料

- `airflow_project/logs/`  
  Airflow 自動產生的日誌紀錄

- `airflow_project/plugins/`  
  保留的 Plugin 擴充目錄（目前未使用）

- `airflow_project/docker-compose.yaml`  
  用來啟動 Airflow 的 Docker 設定檔

- `data/uncleaned_titanic.csv`  
  原始 Titanic 資料

- `data/cleaned_titanic.csv`  
  清洗過後的 Titanic 資料結果

- `etl/train.csv`  
  模擬的資料來源（可作為其他練習資料）

- `etl/etl_house_price.py`  
  ETL 範例腳本，示範如何將資料匯入 PostgreSQL

- `doc/data_description.md`  
  Titanic 各欄位的中文欄位說明

- `data_practice.py`  
  用於本地測試資料清洗的主要實作腳本

- `.env`  
  儲存資料庫連線資訊（已加入 `.gitignore` 避免洩漏）

- `.gitignore`  
  忽略 `.env`、log 等敏感或不必要上傳的檔案

- `README.md`  
  本說明文件



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