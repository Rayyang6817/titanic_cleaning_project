
#url =  "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
#讀取 CSV檔
#df = pd.read_csv(url)
#這邊只會有少部分(中間會省略)
#print(df)   

#print(df.head()) 前五筆把資料顯示出來 這應該是預設拉 實際可以多筆 但沒意義
#df.info()  有點像大綱 有幾欄 這欄有多少有值 資料型態
#print(df.describe()) 這個有點方便 等於把現有欄位做計算 有平均值標準值等等 或許有些資訊從這邊就知道怎麼整理!

#print(df.isnull().sum()) 挖靠 這也有點方便 這直接找出所有欄位是NULL的個數

#下列方式其實很好理解 我要處理AGE欄位 用FILLNA方式 第一個參數是值你要塞入什麼 然後是不是取代他
#df['Age'].fillna(df['Age'].median(),inplace=True)
#print(df.isnull().sum())

# 5. 清除不需要的欄位
#df.drop(columns=['Cabin', 'Ticket', 'Name'], inplace=True)
#df.info()

import pandas as pd

# 1. 讀原始資料
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.to_csv("uncleaned_titanic.csv", index=False)

# 2. 處理缺值
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 3. 處理類別欄位
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 4. 刪除不必要欄位
df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True)

# 5. 儲存清洗後版本
df.to_csv("cleaned_titanic.csv", index=False)

print("已完成清洗並儲存為 cleaned_titanic.csv")

