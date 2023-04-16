# week14 Project Foundational - create table

# Import the boto3 library
import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Call the create_table function of the DynamoDB client and provide the necessary parameters
response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'user', # Specify the name of the user attribute
            'AttributeType': 'S', # Specify that the user attribute is of type string
        },
        {
            'AttributeName': 'avg_salary', # Specify the name of the avg_salary attribute
            'AttributeType': 'N', # Specify that the avg_salary attribute is of type number
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'user', # Specify that the user attribute will be used as the partition key
            'KeyType': 'HASH' # Specify that the user attribute will be used as the hash key
        },
        {
            'AttributeName': 'avg_salary', # Specify that the avg_salary attribute will be used as the sort key
            'KeyType': 'RANGE', # Specify that the avg_salary attribute will be used as the range key
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1, # Set the read capacity units for the table to 1
        'WriteCapacityUnits': 1, # Set the write capacity units for the table to 1
    },
    TableName='week14Project-Python-foundational', # Specify the name of the table to be created
)

# Print the response returned by the create_table function
print(response)
