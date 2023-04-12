# create vpc

import boto3

# Set up the EC2 client
ec2 = boto3.client('ec2')

# Create a new VPC
response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = response['Vpc']['VpcId']
print(f'VPC created: {vpc_id}')