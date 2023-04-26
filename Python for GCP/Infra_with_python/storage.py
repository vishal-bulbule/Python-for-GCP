from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

def create_bucket(name,location):
    storage_client = storage.Client()
    if not storage_client.lookup_bucket(name):
        bucket = storage_client.create_bucket(name)
        print(f"Bucket {bucket.name} created.")
    else:
        print(f"Bucket {name} already exists.")
