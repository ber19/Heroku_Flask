import boto3
from decouple import config

def upload_file(file1, object_name):
    bucket = config('S3_BUCKET')
    s3 = boto3.client('s3')
    s3.upload_fileobj(file1, bucket, object_name)

def create_presigned_url(object_name, expiration=3600):
    bucket = config('S3_BUCKET')
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object',
            Params={'Bucket':bucket, 'Key':object_name},
            ExpiresIn=expiration)
    return url
