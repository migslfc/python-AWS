# week14 Project Advanced  - query

# Import the boto3 library
import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Select the table to be queried
table_name = 'week14Project-Python'

# Execute query with filter expression
response = dynamodb.query(
    TableName=table_name,
    KeyConditionExpression='#a = :salary and #b > :val',
    ExpressionAttributeNames={
        '#a': 'avg-salary',  # attribute to filter on
        '#b': 'profession'  # partition key
    },
    ExpressionAttributeValues={
        ':salary': {'N': '100000'},  # minimum salary threshold
        ':val': {'S': ''}
    },
)

# Extract filtered items
items = response['Items']

# Iterate through items and print the profession and average salary
for item in items:
    profession = item['profession']  # profession attribute
    avg_salary = item['avg-salary']['N']  # average salary attribute
    print(f"{profession}: ${avg_salary}")  # print the formatted string
