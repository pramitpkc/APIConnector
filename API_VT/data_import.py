import boto3
import json
import os
from botocore.exceptions import ClientError
import logging

directory = "E:\API_VT\Data"

s3 = boto3.resource('s3')
client = boto3.client('s3')

# delete content from the bucket(if any)
try:
    my_bucket = s3.Bucket('storeapidata')
    my_bucket.objects.all().delete()
    print("Objects from Bucket deleted Successfully.")
except ClientError as e:
    print(logging.error(e))

# delete the bucket itself
try:
    response = client.delete_bucket(Bucket='storeapidata')
    print("Bucket Deleted Successfully")
    print(json.dumps(response, indent=2))
except ClientError as e:
    print(logging.error(e))

# creating the bucket
response = client.create_bucket(
    ACL='private',
    Bucket='storeapidata',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    },
)

print("New Bucket Created.")
print(json.dumps(response, indent=2))

# upload file to the bucket
for file in os.listdir(directory):
    client.upload_file(directory+'\\' + file, 'storeapidata', file)
