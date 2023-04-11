# create a S3 Bucket

import boto3

s3 = boto3.client("s3")

s3.create_bucket(Bucket="bucket-name") 