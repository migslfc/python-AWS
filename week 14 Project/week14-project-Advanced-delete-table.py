# week14 Project Advanced - delete table

# Import the boto3 library
import boto3

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Specify the name of the table to delete
table_name = 'python-outside-tech'

# Get the table by name
table = dynamodb.Table(table_name)

# Delete the table
table.delete()

# Print a success message
print(f'Table {table_name} deleted successfully.')
