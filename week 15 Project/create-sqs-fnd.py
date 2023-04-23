import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Create a queue
queue_name = 'week15-sqs'
response = sqs.create_queue(
    QueueName=queue_name
)

# Get the queue URL
queue_url = response['QueueUrl']

# Print the queue URL
print(f'The queue URL is {queue_url}')
