import googleapiclient
import googleapiclient.discovery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

compute = googleapiclient.discovery.build('compute', 'v1')
project = '<Your project id>'
zone = 'us-central1-a'
disk_name = "test"
instance_name = "instance-1"


disk_url = 'projects/{0}/zones/{1}/disks/{2}'.format(project,zone,disk_name)

body_attach = {
    'deviceName': "disk-1",
    'source': disk_url
}
operation = compute.instances().attachDisk(project=project, zone=zone,
                                       body=body_attach, instance =instance_name).execute()
result = compute.zoneOperations().get(project=project, zone=zone,operation=operation)
print(f"Disk {disk_name} attached to {instance_name}")