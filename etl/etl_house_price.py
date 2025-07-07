import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# 寫入env檔避免外露
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

# 萃取資料(來源本機)
df = pd.read_csv("etl/train.csv")

# ----------------------TRANS------------------------
# 值夠多用中值補
df['LotFrontage'].fillna(df['LotFrontage'].median(), inplace=True)
# 定位這欄空的欄位 把他補成0(無石磚面積)
df.loc[df['MasVnrType'].isnull(), 'MasVnrArea'] = 0

# 值不具有參考價值(太少 刪除
# 石磚種類也是值太少 不補 種類應該不會影響太多房價?!
# 游泳池品質/圍籬品質/雜項設施 (會不會影響房價 會! 但資料量太少嚴重會影響模型失衡)
df.drop(columns=['Alley','MasVnrType','PoolQC', 'Fence', 'MiscFeature'], inplace=True)

# 車庫年份補值怪怪的 因為就是沒車庫 補0來代表沒有!(因為是數值)
df['GarageYrBlt'].fillna(0, inplace=True)

# 這不是真的NA 是沒地下室 如果沒有就用NONE 去取代就好
basement_cols = ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1','BsmtFinType2','FireplaceQu','GarageType','GarageFinish','GarageQual','GarageCond']
for col in basement_cols:
    df[col] = df[col].fillna('None')

# 電器類型 直接補眾數    
df['Electrical'].fillna(df['Electrical'].mode()[0], inplace=True)
# ----------------------TRANS------------------------

df.info()

try:
    #建立連線方式
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

    # 將資料寫入資料庫
    df.to_sql("cleaned_house", engine, if_exists="replace", index=False)
    
    print("✅ 資料成功寫入資料庫")
except Exception as e:
    print("❌ 資料寫入失敗：", e)

#確認一下 總共有幾種外牆石磚種類
#print(df['MasVnrType'].value_counts())
#確認一下 總共有幾個壁爐等級?!
#print(df['FireplaceQu'].value_counts())
