import boto3


REGION = 'us-east-1'

AWS_ACCESS_KEY = 'AKIAJAW6CFNXKE5L62GA'
AWS_SECRET_KEY = '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'


s3client = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY,region_name=REGION)

for bucket in s3client.list_buckets()['Buckets']:
    bucket = bucket['Name']
    response = s3client.get_bucket_versioning(Bucket=bucket)
    if 'Status' in response and response['Status'] == 'Enabled':
        print("{}".format(bucket))




