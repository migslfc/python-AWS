# Import the boto3 library, which provides the AWS SDK for Python
import boto3

# Define a function called create_apache_ec2 that takes in an EC2 client as an argument
def create_apache_ec2(client, count):
    
    # Try to launch multiple EC2 instances with the specified parameters
    try:
        client.run_instances(MaxCount=count,                  # Launch multiple instances
                             MinCount=count,                  # Minimum number of instances to launch is equal to count
                             ImageId="YOUR_IMAGE_ID_HERE",     # Specify the AMI ID for the instance
                             InstanceType="t2.micro",          # Specify the instance type
                             KeyName="YOUR_KEY_PAIR_NAME_HERE", # Specify the name of the key pair to use for SSH access
                             SecurityGroups=["YOUR_SECURITY_GROUP_NAME_HERE"], # Specify the name of the security group for the instance
                             UserData=boot_apache2_script)     # Specify the user data to run on the instance
        print(f"Started {count} instances")   # If the instances are launched successfully, print the number of instances started
    
    # If there is an error, print "Failed"
    except:
        print("Failed")
    

# Create an EC2 client
client = boto3.client('ec2')

# Specify the user data to run on the instances
boot_apache2_script='''#!/bin/bash
apt update -y
apt upgrade -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''

# Call the create_apache_ec2 function with the EC2 client as an argument to launch multiple instances
create_apache_ec2(client, 3)   # Change the number in this argument to the desired number of instances to launch
