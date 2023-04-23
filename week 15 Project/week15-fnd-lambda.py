import boto3
import datetime
import json
import os
import random

# Create an SQS client
sqs = boto3.client('sqs')

# Retrieve the SQS queue URL from the environment variables
queue_url = os.environ['QUEUE_URL']

def lambda_handler(event, context):
    # Get the current time and a random number
    current_time = str(datetime.datetime.now())
    order_number = random.randint(1, 100)

    # Create a message dictionary with the current time and order number
    message_dict = {'time': current_time, 'order_number': order_number}

    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message_dict)
    )

    # Log the response
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SQS queue')
    }
