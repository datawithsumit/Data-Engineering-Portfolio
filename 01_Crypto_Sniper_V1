import requests
import json
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator

MY_BUCKET_NAME = 'sumit-airflow-project-1303'
API_URL =  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def fetch_bitcoin_price():
	response = requests.get(API_URL)
	data = response.json()
	price = data['bitcoin']['usd']
	now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	final_data = f"Time,Price\n{now},{price}"
	print(f"Fetched Data: {final_data}")
	return final_data
with DAG(
	dag_id ='crypto_sniper_v1',
	start_date = datetime(2023,1,1),
	schedule = '@hourly',
	catchup = False
  ) as dag:
	extract_task = PythonOperator(
	task_id = 'extract_bitcoin_price',
	python_callable=fetch_bitcoin_price
      )
	load_task = S3CreateObjectOperator(
	task_id = 'upload_to_aws',
	aws_conn_id = 'aws_default',
	s3_bucket = MY_BUCKET_NAME,
	s3_key = 'bitcoin_latest.csv',
	data = "{{ ti.xcom_pull(task_ids='extract_bitcoin_price') }}",
	replace = True
      )

	extract_task >> load_task
