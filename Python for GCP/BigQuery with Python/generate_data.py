from faker import Faker
from google.cloud import storage
import csv
import datetime
from var import *
import os

#Service account key file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

def generate_data(num_rows):
    fake = Faker()
    now = datetime.datetime.now()
    filename = "data_" + now.strftime("%Y%m%d%H%M%S") + ".csv"


    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'email', 'description', 'address', 'city', 'state',
                      'country', 'birthdate', 'password', 'last_login']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(num_rows):
            writer.writerow(
                {
                    'id': fake.random_int(),
                    'name': fake.name(),
                    'email': fake.email(),
                    'description': fake.sentence(),
                    'address': fake.street_address(),
                    'city': fake.city(),
                    'state': fake.state(),
                    'country': fake.country(),
                    'birthdate': fake.date(),
                    'password': fake.password(),
                    'last_login': fake.date_time()
                }
            )
    print (f"Data generated with {num_rows} records")

    client = storage.Client()       
    bucket_name = src_bucket
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    print(f"File {filename} Uploaded to {bucket_name}")
    
    return filename
