import googleapiclient
import googleapiclient.discovery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

compute = googleapiclient.discovery.build('compute', 'v1')
project = 'Your project id'
zone = 'us-central1-a'
disk_name = "test"

body = {
        'name': disk_name ,
        'type': "projects/tt-dev-001/zones/us-central1-a/diskTypes/pd-balanced",
        'size_gb': 10
}
operation = compute.disks().insert(project=project, zone=zone,
                                       body=body).execute()
result = compute.zoneOperations().get(project=project, zone=zone,operation=operation)
print(f"Created disk {disk_name}  in zone {zone}")


