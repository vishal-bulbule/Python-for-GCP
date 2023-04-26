from var import *
from network import *
from compute import *
from storage import *


create_network(project,"app-vpc")
create_subnetwork(project,"app-vpc","us-subnet",region,"10.10.0.0/28")
create_gce_instance("test-1","us-central1-a","us-subnet","e2-medium",debian_image)
create_bucket("bkt-dev-003","us")


#To create multiple VMs
for config in vm_configs:
    create_gce_instance(config['name'],config['zone'],
                        config['subnet_name'],config['machine_type'],
                        config['vm_image'])

for config in bucket_config:
    create_bucket(config['name'],config['location'])
























