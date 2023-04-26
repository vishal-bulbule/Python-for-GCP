import googleapiclient
import googleapiclient.discovery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

compute = googleapiclient.discovery.build('compute', 'v1')
project = 'Your project id'
zone = 'us-central1-a'
machineimage_name = "test"

body = {
'name': machineimage_name,
'source_instance': "projects/tt-dev-001/zones/us-central1-a/instances/instance-1"
}
operation = compute.machineImages().insert(project=project, 
                                       body=body).execute()

result = compute.zoneOperations().get(project=project, zone=zone,operation=operation)
print(f"Machine image creation started")



