# Import the boto3 library, which provides the AWS SDK for Python
import boto3

# Define a function called create_apache_ec2 that takes in an EC2 client as an argument
def create_apache_ec2(client):
    
    # Try to launch an EC2 instance with the specified parameters
    try:
        client.run_instances(MaxCount=1,                  # Launch one instance
                             MinCount=1,                  # Minimum number of instances to launch is one
                             ImageId="YOUR_IMAGE_ID_HERE", # Specify the AMI ID for the instance
                             InstanceType="t2.micro",      # Specify the instance type
                             KeyName="YOUR_KEY_PAIR_NAME_HERE",         # Specify the name of the key pair to use for SSH access
                             SecurityGroups=["YOUR_SECURITY_GROUP_NAME_HERE"], # Specify the name of the security group for the instance
                             UserData=boot_apache2_script) # Specify the user data to run on the instance
        print("Started")   # If the instance is launched successfully, print "Started"
    
    # If there is an error, print "Failed"
    except:
        print("Failed")
    

# Create an EC2 client
client = boto3.client('ec2')

# Specify the user data to run on the instance
boot_apache2_script='''#!/bin/bash
apt update -y
apt upgrade -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''

# Call the create_apache_ec2 function with the EC2 client as an argument
create_apache_ec2(client)
