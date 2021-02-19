import boto3
from decouple import config

def upload_file(file1, object_name):
    bucket = config('S3_BUCKET')
    s3 = boto3.client('s3')
    s3.upload_fileobj(file1, bucket, object_name)

def download_file(object_name):
    bucket = config('S3_BUCKET')
    file_name = object_name
    s3 = boto3.client('s3')
    s3.download_file(bucket, object_name, file_name)