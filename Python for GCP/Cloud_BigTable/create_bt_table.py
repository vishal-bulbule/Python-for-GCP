from google.cloud import bigtable
from google.cloud.bigtable import column_family
import os
from var import *


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

project_id = project
instance_id = bt_instance

client = bigtable.Client(project=project, admin=True)
instance = client.instance(instance_id)

table_id = 'climate'
table = instance.table(table_id)
print(f"Checking if table {table_id} exist")
if  not table.exists():
    print(f" table {table_id} not exist , creating table {table_id}")
    table.create()
    print(f"Created table {table_id}")
    column_family_id = 'env_parameters'
    column_family = table.column_family(column_family_id)
    column_family.create()
    print(f"Column family {column_family_id} created")
