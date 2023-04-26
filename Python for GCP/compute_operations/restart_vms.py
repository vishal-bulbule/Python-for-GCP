from google.cloud import compute_v1
import os

PROJECT_ID = 'your project id'
ZONE = 'us-central1-a'

compute_client = compute_v1.InstancesClient()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


instances = compute_client.list(
    project=PROJECT_ID,
    zone=ZONE
)


for instance in instances:
    stop_instance_request = compute_client.stop(
        project=PROJECT_ID,
        zone=ZONE,
        instance=instance.name
    )
    stop_instance_request.result()

    start_instance_request = compute_client.start(
        project=PROJECT_ID,
        zone=ZONE,
        instance=instance.name
    )
    start_instance_request.result()

    print(f'Restarted VM instance: {instance.name}')