import os
import boto3
import json

# Get the SNS topic ARN from the environment variable
topic_arn = os.environ['TOPIC_ARN']

# Create an SNS client
sns = boto3.client('sns')

def lambda_handler(event, context):
    # Process the message
    message = json.loads(event['Records'][0]['body'])
    print(message)

    # Publish the message to the SNS topic
    response = sns.publish(
        TopicArn=topic_arn,
        Message=json.dumps(message)
    )
    print(response)

    # Delete the message from the queue
    receipt_handle = event['Records'][0]['receiptHandle']
    sqs = boto3.client('sqs')
    response = sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print(response)
