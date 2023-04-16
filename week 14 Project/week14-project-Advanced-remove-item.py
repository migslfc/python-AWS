# week14 Project Advanced - remove item

# Import the boto3 library
import boto3

# Create a DynamoDB client object
dynamodb = boto3.client('dynamodb')

# Define the name of the table, partition key and sort key
table_name = 'week14Project-Python'
partition_key = 'use'
sort_key = 'avg-salary'

# Specify the item you want to delete by providing the partition key and sort key values
item_to_delete = {
    partition_key: {'S': 'Audio and video processing'},
    sort_key: {'N': '54000'},
}

# Call the delete_item method of the DynamoDB client object to delete the specified item from the table
response = dynamodb.delete_item(
    TableName=table_name,
    Key=item_to_delete,
)

print(response)
