# Titanic Data Cleaning Notes

## 處理步驟說明：

- 欄位 `Age` 缺值以中位數填補
- 欄位 `Embarked` 缺值以眾數填補（最多人上船港口）
- 欄位 `Sex` 轉換為 0（male）/1（female）
- 刪除以下欄位：
  - `Cabin`: 缺值比例過高
  - `Ticket`: 幾乎為唯一值，無統計意義
  - `Name`: 雖有資訊但未處理稱謂，暫不使用
  - `PassengerId`: 僅為識別碼，非分析欄位

## 最終輸出：
- cleaned_titanic.csv（共 891 筆資料，含 8 欄位）
