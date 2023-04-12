import boto3

# Set up the EC2 client
vpc = boto3.client('ec2')

# Describe all security groups in the account
response = vpc.describe_security_groups()

# Extract the list of security groups from the response
securitygroups = response['SecurityGroups']

# Print the ID of each security group
for securitygroup in securitygroups:
    print(securitygroup['GroupId'])
