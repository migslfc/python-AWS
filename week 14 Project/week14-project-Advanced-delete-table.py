# week14 Project Advanced - delete table

# Import the boto3 library
import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Specify the table name
table_name = 'python-outside-tech'

# Delete the table with the specified name
response = dynamodb.delete_table(TableName=table_name)

# Print a success message if the table was deleted
if response['TableDescription']['TableStatus'] == 'DELETING':
    print(f'Table {table_name} deleted successfully.')
