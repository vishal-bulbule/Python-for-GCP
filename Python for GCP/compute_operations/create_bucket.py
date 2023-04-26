from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

project_id = '<Your project id>'
bucket_name = 'bkt-dev-006'

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
bucket.location = 'us'
bucket.create(project=project_id,location="us")
print(f'Bucket {bucket_name} created.')

#To upload objects to Bucket
blob = bucket.blob("create_vm.py")
with open('create_vm.py', 'rb') as file:
    blob.upload_from_file(file)

#Delete object
blob.delete()