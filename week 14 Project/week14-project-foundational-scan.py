# week14 Project Foundational - scan

# Import the boto3 library
import boto3

# create a DynamoDB client
dynamodb = boto3.client('dynamodb')


# scan the DynamoDB table
response = dynamodb.scan(TableName='week14Project-Python')


# loop through the items returned in the response and print them
for item in response['Items']:
    print(item)

