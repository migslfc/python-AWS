# dynamodb from Zaire

# Import the boto3 library
import boto3

# replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='*****',
    aws_secret_access_key='*****',
    )
