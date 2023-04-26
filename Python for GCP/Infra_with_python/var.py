#Add variable values as per your requirements
project = '<Enter your project ID>'
region = 'us-central1'
debian_image = 'projects/debian-cloud/global/images/family/debian-10'
windows_image = 'projects/windows-cloud/global/images/family/windows-2022'

vm_configs = [
    {'name': 'vm1', 'zone':'us-central1-a','subnet_name':'us-subnet','machine_type': 'n1-standard-1', 'vm_image': debian_image},
    {'name': 'vm2', 'zone':'us-central1-a','subnet_name':'us-subnet','machine_type': 'n1-standard-1', 'vm_image': windows_image},
    {'name': 'vm3', 'zone':'us-central1-a','subnet_name':'us-subnet','machine_type': 'n1-standard-1', 'vm_image': windows_image}
]

bucket_config = [
    {'name':'bkt-dev-005','location':'us'},
    {'name':'bkt-dev-004','location':'us-central1'},
]




















