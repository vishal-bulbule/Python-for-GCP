from google.cloud import compute_v1
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

INSTANCE_NAME = 'my-instance-internal'
project_id = '<project-id>'
zone = '<zone>'

compute_client = compute_v1.InstancesClient()
operation = compute_client.delete(project=project_id, zone=zone, instance=INSTANCE_NAME)
operation.result()

print(f'Deleted VM instance: {INSTANCE_NAME}')
