# week14 Project Advanced - delete table


import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'python-outside-tech'

table = dynamodb.Table(table_name)
table.delete()

print(f'Table {table_name} deleted successfully.')
