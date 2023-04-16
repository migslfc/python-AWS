# week14 Project Foundational - scan


import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(TableName='week14Project-Python')

for item in response['Items']:
    print(item)

