import boto3

def upload_file(bucket, file1, object_name):
    s3 = boto3.client('s3')
    s3.upload_fileobj(file1, bucket, object_name)

def create_presigned_url(bucket, object_name, expiration=3600):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object',
            Params={'Bucket':bucket, 'Key':object_name},
            ExpiresIn=expiration)
    return url
