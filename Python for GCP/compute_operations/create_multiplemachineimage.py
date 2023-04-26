import googleapiclient
import googleapiclient.discovery
from datetime import datetime , date
from datetime import timedelta
import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

compute = googleapiclient.discovery.build('compute', 'v1')
project = 'your project id'
zone = 'us-central1-a'
machineimage_name = "test-1"
now = datetime.now()
print(now)   
today = now.strftime("%Y%m%d")
y = date.today() - timedelta(days=1)
yesterday = y.strftime('%Y%m%d')

instances = compute.instances().list(project=project,zone=zone).execute()
for instance in instances['items']:
    print(instance['name'])
    instance_name = instance['name']
    instance_url = 'projects/{0}/zones/{1}/instances/{2}'.format(project,zone,instance_name)
    body = {
    'name': instance_name+str(20230414),
    'source_instance': instance_url
    }
    operation = compute.machineImages().insert(project=project,body=body).execute()

    print(f"Machine image creation started")
    time.sleep(5)
    #operation = compute.machineImages().delete(project=project, machineImage=instance_name+yesterday).execute()





