# Import the necessary modules.
import os
import boto3

# Get environment variables.
AMI = os.environ['AMI']  # ID of the Amazon Machine Image to use when launching the instance.
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']  # The instance type that you want to launch.
KEY_NAME = os.environ['KEY_NAME']  # Name of the key pair.
SUBNET_ID = os.environ['SUBNET_ID']  # ID of the subnet in which to launch the instance.

# Create a Boto3 EC2 resource object.
ec2 = boto3.resource('ec2')

# Define the Lambda function.
def lambda_handler(event, context):

    # Launch a new EC2 instance using the create_instances method.
    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    # Print the instance ID of the newly created EC2 instance.
    print("New instance created:", instance[0].id)
