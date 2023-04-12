import boto3

# Set up the EC2 client
vpc = boto3.client('ec2')

# Describe all VPCs in the account
response = vpc.describe_vpcs()

# Extract the list of VPCs from the response
vpcs = response['Vpcs']

# Print the ID of each VPC
for vpc in vpcs:
    print(vpc['VpcId'])
