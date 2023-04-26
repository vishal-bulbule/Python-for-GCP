#First install required library using below pip command
#pip install google-api-python-client

import os
from metadata import *
from var import *

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Create Service account , download keys and add your key file path below 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# I am creating function to create VM instance and this function is being called from main.py
def create_gce_instance(vm_name, zone, subnet_name, machine_type, vm_image):
    vm_instance_list = get_vm_instance_list(project, zone)
    vm_exists = False
    for instance in vm_instance_list.get('items', []):
        if instance['name'] == vm_name:
            vm_exists = True
            break

    if not vm_exists:
        compute_service = build('compute', 'v1')
        subnet_selflink = 'regions/{}/subnetworks/{}'.format(
            region, subnet_name)
        config = {
            'name': vm_name,
            'machineType': 'zones/{}/machineTypes/{}'.format(zone, machine_type),
            'disks': [{
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': vm_image
                }
            }],
            'networkInterfaces': [{
                'subnetwork': subnet_selflink,
                'accessConfigs': [{
                    'type': 'ONE_TO_ONE_NAT',
                    'name': 'External NAT'
                }]
            }]
        }

        request = compute_service.instances().insert(
            project=project, zone=zone, body=config)
        response = request.execute()

        print('VM instance created:', response['selfLink'])
    else:
        print(f'VM instance {vm_name} already exist')
