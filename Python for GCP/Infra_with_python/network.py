from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

compute_service = build('compute', 'v1')

def create_network(project,vpc_name):
    compute_service = build('compute', 'v1')
    vpcs_request = compute_service.networks().list(project=project)
    vpcs_list = vpcs_request.execute()

    vpc_exists = False
    for vpc in vpcs_list.get('items', []):
        if vpc['name'] == vpc_name:
            vpc_exists = True
            break

    # If the VPC does not exist, create it
    if not vpc_exists:
        vpc_body = {
            'name': vpc_name,
            'autoCreateSubnetworks': False,
            'description': 'My VPC',
            'routingConfig': {
                'routingMode': 'REGIONAL'
            },
        }

        vpc_request = compute_service.networks().insert(project=project, body=vpc_body)
        vpc_response = vpc_request.execute()
        print("Creating VPC")
        time.sleep(10)
        print(f'VPC {vpc_name} Created')
    else:
        print(f'VPC {vpc_name} already exists')


########################Subnetwork###########################
def create_subnetwork(project,vpc_name,subnet_name,region,ip_range):
    vpc_selflink = 'projects/{0}/global/networks/{1}'.format(project,vpc_name)
    subnet_request = compute_service.subnetworks().list(project=project,region=region)
    subnet_list = subnet_request.execute()

    subnet_exists = False
    for subnet in subnet_list.get('items', []):
        if subnet['name'] == subnet_name:
            subnet_exists = True
            break

    if not subnet_exists:        
        subnet_body = {
            'name': subnet_name,
            'network': vpc_selflink,
            'ipCidrRange': ip_range,
            'region': region
        }

        subnet_request = compute_service.subnetworks().insert(project=project, region= region, body=subnet_body)
        subnet_response = subnet_request.execute()
        print(f"Subnet {subnet_name} creating")
        time.sleep(10)
        print(f"Subnet {subnet_name} Created")
    else:
        print(f"Subnet {subnet_name} already exist")