# descibe vpc

import boto3

# Set up the EC2 client
ec2 = boto3.client('ec2')

# Specify the ID of the VPC to describe
vpc_id = 'vpc-0123456789abcdef'

# Describe the VPC
response = ec2.describe_vpcs(VpcIds=[vpc_id])

# Extract the relevant information from the response
vpc_info = response['Vpcs'][0]
vpc_cidr_block = vpc_info['CidrBlock']
vpc_state = vpc_info['State']
vpc_tags = vpc_info['Tags']

# Print the information about the VPC
print(f'VPC ID: {vpc_id}')
print(f'CIDR block: {vpc_cidr_block}')
print(f'State: {vpc_state}')
print(f'Tags: {vpc_tags}')