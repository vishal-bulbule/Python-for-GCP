from google.cloud import bigquery
from var import *
import datetime
import os

#Service account key file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

def extract_bq():
    client = bigquery.Client()
    dataset_ref = client.dataset(my_dataset)
    table_ref = dataset_ref.table(my_table)
    job_config = bigquery.ExtractJobConfig()
    job_config.compression = 'GZIP'
    job_config.field_delimiter = ','
    job_config.print_header = False

    now = datetime.datetime.now()
    filename = "bqextract_" + now.strftime("%Y%m%d%H%M%S") + ".csv"
    destination_uri = f'gs://{destination_bucket}/{filename}'

    extract_job = client.extract_table(table_ref, destination_uri, job_config=job_config)

    extract_job.result()

    print('Data extracted from table {} and loaded into GCS bucket {}.'.format(table_ref.path, destination_uri))
