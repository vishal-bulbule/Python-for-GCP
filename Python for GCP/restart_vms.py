# Author - Vishal Bulbule
#
#
####################################################


from google.cloud import compute_v1

PROJECT_ID = '<Project_id>'
ZONE = '<zone>'

INSTANCE_FILE = 'instance_names.txt'

compute_client = compute_v1.InstancesClient()

instances = compute_client.list(
    project=PROJECT_ID,
    zone=ZONE
)

with open(INSTANCE_FILE, 'w') as f:
    for instance in instances:
        f.write(f'{instance.name}\n')

with open(INSTANCE_FILE, 'r') as f:
    instance_names = f.read().splitlines()

for name in instance_names:
    stop_instance_request = compute_client.stop(
        project=PROJECT_ID,
        zone=ZONE,
        instance=name
    )
    stop_instance_request.result()

    start_instance_request = compute_client.start(
        project=PROJECT_ID,
        zone=ZONE,
        instance=name
    )
    start_instance_request.result()

    print(f'Restarted VM instance: {name}')
