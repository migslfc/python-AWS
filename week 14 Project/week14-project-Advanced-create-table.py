# week14 Project Advanced - create table

# Import the boto3 library
import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Set the table name to be created
table_name = 'python-outside-tech'

# Create the table
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'use',
            'KeyType': 'HASH'   # Use 'use' attribute as the partition key
        },
        {
            'AttributeName': 'avg_salary',
            'KeyType': 'RANGE'  # Use 'avg_salary' attribute as the sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'use',
            'AttributeType': 'S'  # Define 'use' as a string attribute
        },
        {
            'AttributeName': 'avg_salary',
            'AttributeType': 'N'  # Define 'avg_salary' as a number attribute
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Print a success message
print(f"Table {table_name} created successfully")

# Add items to the table
response = dynamodb.put_item(
    TableName=table_name,
    Item={
        'use': {'S': 'Finance'},
        'profession': {'S': 'Quantitative Analyst'},
        'avg_salary': {'N': '125000'}
    }
)

response = dynamodb.put_item(
    TableName=table_name,
    Item={
        'use': {'S': 'Marketing'},
        'profession': {'S': 'Data Analyst'},
        'avg_salary': {'N': '95000'}
    }
)

response = dynamodb.put_item(
    TableName=table_name,
    Item={
        'use': {'S': 'Healthcare'},
        'profession': {'S': 'Medical Data Analyst'},
        'avg_salary': {'N': '110000'}
    }
)

response = dynamodb.put_item(
    TableName=table_name,
    Item={
        'use': {'S': 'Retail'},
        'profession': {'S': 'Sales Analyst'},
        'avg_salary': {'N': '80000'}
    }
)

response = dynamodb.put_item(
    TableName=table_name,
    Item={
        'use': {'S': 'Education'},
        'profession': {'S': 'Data Scientist'},
        'avg_salary': {'N': '100000'}
    }
)
