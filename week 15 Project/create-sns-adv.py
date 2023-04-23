import boto3

# Create an SNS client
sns = boto3.client('sns')

# Set the name of the SNS topic to create
topic_name = 'week15-sns'

# Create the SNS topic
response = sns.create_topic(Name=topic_name)

# Extract the ARN of the topic from the response
topic_arn = response['TopicArn']

# Print the ARN of the topic to verify that it was created successfully
print(f'SNS topic created with ARN: {topic_arn}')
