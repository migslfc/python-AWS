# remove vpc

import boto3

# Set up the EC2 client
ec2 = boto3.client('ec2')

# Specify the ID of the VPC to delete
vpc_id = 'vpc-059a7debad60f116c'

# Delete the VPC
response = ec2.delete_vpc(VpcId=vpc_id)
print(f'VPC deleted: {vpc_id}')