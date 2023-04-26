import os
from datetime import datetime, timedelta
from google.cloud import bigtable

import random

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

client = bigtable.Client(project='project-id')
instance = client.instance('bt-dev')
table_id = 'climate'
table = instance.table(table_id)

start_time = datetime(2022, 1, 1)

for i in range(100):
    timestamp = start_time + timedelta(minutes=i*10)
    row_key = 'row-{}'.format(timestamp.isoformat())
    row = table.row(row_key)

    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(30, 70), 2)

    row.set_cell(b'env_parameters', b'temperature', str(temperature).encode(), timestamp=timestamp)
    row.set_cell(b'env_parameters', b'humidity', str(humidity).encode(), timestamp=timestamp)
    row.commit()
    print(f"Loaded records - {i}")
