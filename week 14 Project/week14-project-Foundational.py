# week14 Project Foundational - gist starting point add items

# Importing the Boto3 library

import boto3

# Creating a list of dictionaries, each of which contains the attributes and values for a new item to be added to the table

items = [
    {
        'use': {'S': 'Scripting'},
        'avg-salary': {'N': '105000'},
        'profession': {'S': 'DevOps engineer'}
    },
    {
        'use': {'S': 'Game development'},
        'avg-salary': {'N': '76000'},
        'profession': {'S': 'Game programmer'}
    },
    {
        'use': {'S': 'Desktop applications'},
        'avg-salary': {'N': '79000'},
        'profession': {'S': 'User interface (UI) designer'}
    },
    {
        'use': {'S': 'Internet of Things (IoT)'},
        'avg-salary': {'N': '99000'},
        'profession': {'S': 'Embedded systems engineer'}
    },
    {
        'use': {'S': 'Networking'},
        'avg-salary': {'N': '120000'},
        'profession': {'S': 'Network architect'}
    },
    {
        'use': {'S': 'Computer vision'},
        'avg-salary': {'N': '93000'},
        'profession': {'S': 'Robotics engineer'}
    },
    {
        'use': {'S': 'Testing'},
        'avg-salary': {'N': '93000'},
        'profession': {'S': 'Test automation engineer'}
    },
    {
        'use': {'S': 'Natural language processing (NLP)'},
        'avg-salary': {'N': '93000'},
        'profession': {'S': 'Computational linguist'}
    },
    {
        'use': {'S': 'Financial analysis'},
        'avg-salary': {'N': '86000'},
        'profession': {'S': 'Quantitative analyst'}
    },
    {
        'use': {'S': 'Audio and video processing'},
        'avg-salary': {'N': '54000'},
        'profession': {'S': 'Sound designer'}
    },
    {
        'use': {'S': 'Education'},
        'avg-salary': {'N': '65000'},
        'profession': {'S': 'Online course creator'}
    }

]

# Looping through the list of new items to add them to the table

for item in items:
    # Using the put_item method to add the new item to the table
    response = dynamodb.put_item(
        Item=item,
        ReturnConsumedCapacity='TOTAL',
        TableName='week14Project-Python',
    )
    
    # Printing a message to indicate that the item has been added
    print("Added item to table")