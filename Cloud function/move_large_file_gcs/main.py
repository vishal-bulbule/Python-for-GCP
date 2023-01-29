from google.cloud import storage
from google.cloud.storage import Blob

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    file_name = file['name']
    print(f"Processing file: {file['name']}.")
    storage_client = storage.Client(project='<project-id>')
    source_bucket = storage_client.get_bucket('bkt-src-00')
    destination_bucket = storage_client.get_bucket('bkt-dst-00')
    #blobs=source_bucket.list_blobs()
    blobs=list(source_bucket.list_blobs(prefix=''))
    print(blobs)
    storage_client = storage.Client(project='<project-id>')
    source_bucket = storage_client.get_bucket('bkt-src-00')
    destination_bucket = storage_client.get_bucket('bkt-dst-00')
    #blobs=source_bucket.list_blobs()
    blobs=list(source_bucket.list_blobs(prefix=''))
    print(blobs)
    for blob in blobs:
     if blob.size > 1000000 and blob.name == file_name:
      print("Size of blob is"+ str(blob.size))
      source_blob = source_bucket.blob(blob.name)
      new_blob = source_bucket.copy_blob(
      source_blob, destination_bucket, blob.name)
      #source_blob.delete()
      print(f'File moved from {source_blob} to {new_blob}')
     else:
      print("File size is below 1MB")
