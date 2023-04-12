import boto3

# Set up the EC2 client
vpc = boto3.client('ec2')

# Describe all subnets in the account
response = vpc.describe_subnets()

# Extract the list of subnets from the response
subnets = response['Subnets']

# Print the ID of each subnet
for subnet in subnets:
    print(subnet['SubnetId'])
