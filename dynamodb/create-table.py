# create table

# Import the boto3 library
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'S',
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH',
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='week14Project-Python',
)

print(response)