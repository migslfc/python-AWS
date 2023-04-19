# Import the boto3 library, which provides the AWS SDK for Python
import boto3

# Define a function called terminate_instances that takes in an EC2 client and a list of instance IDs as arguments
def terminate_instances(client, instanceIds):
    
    # Try to terminate the specified instances
    try:
        response = client.terminate_instances(InstanceIds=instanceIds)
        terminatedInstances = response["TerminatingInstances"]
        
        for instance in terminatedInstances:
            print(f"Instance {instance['InstanceId']} is terminating.")
    
    # If there is an error, print "Failed"
    except:
        print("Failed to terminate instances.")
    

# Create an EC2 client
client = boto3.client('ec2')

# Call the describe_instances method of the EC2 client to get information about all instances
response = client.describe_instances()
reservations = response["Reservations"]

# Initialize an empty list called instanceIds
instanceIds = []

# Loop through each Reservation in the Reservations list
for reservation in reservations:
    # Extract the Instances list from the Reservation
    instances = reservation["Instances"]
    # Loop through each Instance in the Instances list
    for instance in instances:
        # Extract the InstanceId from the Instance and append it to the instanceIds list
        instanceId = instance["InstanceId"]
        instanceIds.append(instanceId)

# Call the terminate_instances function with the EC2 client and the instanceIds list as arguments to terminate multiple instances
terminate_instances(client, instanceIds)
