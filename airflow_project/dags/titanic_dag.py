from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def read_csv():
    df = pd.read_csv('/opt/airflow/data/cleaned_titanic.csv')
    print(df.head())

with DAG(
    dag_id='read_titanic_csv',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['example']
) as dag:

    task_read_csv = PythonOperator(
        task_id='read_csv',
        python_callable=read_csv
    )
