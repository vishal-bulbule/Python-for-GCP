from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
import os
import time
from var import *

#Service account key file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

def load_bq(filename):
    client = bigquery.Client()
    filename = filename
    table_ref = client.dataset(my_dataset).table(my_table)
    job_config = LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    uri = f'gs://{src_bucket}/{filename}'
    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    load_job.result()  
    time.sleep(10)
    num_rows = load_job.output_rows
    print(f"{num_rows} rows loaded into {my_table}.")