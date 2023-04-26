from google.cloud import bigtable
import os
from var import *

from google.cloud.bigtable import Client
from google.cloud.bigtable import enums

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

my_instance_id = bt_instance
my_cluster_id = "bt-clust"
location_id = "us-central1-a"
#serve_nodes = 1
storage_type = enums.StorageType.SSD
dev = enums.Instance.Type.DEVELOPMENT
labels = {"dev-label": "dev-label"}

client = Client(admin=True)
instance = client.instance(my_instance_id, instance_type=dev, labels=labels)
cluster = instance.cluster(
    my_cluster_id,
    location_id=location_id,
    #serve_nodes=serve_nodes,
    default_storage_type=storage_type,
)
operation = instance.create(clusters=[cluster])
print("Creating BigTable instance")
operation.result(timeout=100)