from google.cloud import bigquery
import os
from var import *

#Service account key file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

def create_bq():
    client = bigquery.Client()

    dataset_id = my_dataset
    table_id = my_table

    schema = [
        bigquery.SchemaField("id", "INTEGER"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("email", "STRING"),
        bigquery.SchemaField("description","STRING"),
        bigquery.SchemaField("address","STRING"),
        bigquery.SchemaField("city","STRING"),
        bigquery.SchemaField("state","STRING"),
        bigquery.SchemaField("country","STRING"),
        bigquery.SchemaField("birthdate","DATE"),
        bigquery.SchemaField("password","STRING"),
        bigquery.SchemaField("last_login","TIMESTAMP")
    ]

    table_ref = client.dataset(my_dataset).table(my_table)
    table = bigquery.Table(table_ref, schema=schema)

    try:
        dataset = client.create_dataset(my_dataset)
        print(f"Created dataset {my_dataset}")
    except:
        print(f"Dataset {my_dataset} already exists")

    try:
        table = client.create_table(table)
        print(f"Created table {table_id}")
    except:
        print(f"Table {table_id} already exists")
