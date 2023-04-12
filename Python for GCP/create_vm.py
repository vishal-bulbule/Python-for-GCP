from google.cloud import compute_v1

INSTANCE_NAME = 'my-new-instance'
MACHINE_TYPE = 'zones/us-central1-a/machineTypes/n1-standard-1'
SUBNETWORK = 'regions/us-central1/subnetworks/default'
SOURCE_IMAGE = 'projects/debian-cloud/global/images/family/debian-10'
NETWORK_INTERFACE = {
    'subnetwork': SUBNETWORK,
    'access_configs': [
        {
            'name': 'External NAT'
        }
    ]
}

compute_client = compute_v1.InstancesClient()

config = {
    'name': INSTANCE_NAME,
    'machine_type': MACHINE_TYPE,
    'disks': [
        {
            'boot': True,
            'auto_delete': True,
            'initialize_params': {
                'source_image': SOURCE_IMAGE,
            }
        }
    ],
    'network_interfaces': [NETWORK_INTERFACE]
}

operation = compute_client.insert(
    project='my-project-id',
    zone='us-central1-a',
    instance_resource=config
)

operation.result()

print(f'Created VM instance: {INSTANCE_NAME}')
