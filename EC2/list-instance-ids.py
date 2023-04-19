# Import the boto3 library, which provides the AWS SDK for Python
import boto3

# Define a function called list_instance_ids that takes in an EC2 client as an argument
def list_instance_ids(ec2_client):
    # Call the describe_instances method of the EC2 client to get information about all instances
    response = ec2_client.describe_instances()
    
    # Extract the Reservations list from the response
    reservations = response["Reservations"]
    
    # Initialize an empty list called instanceIds
    instanceIds = []
    
    # Loop through each Reservation in the Reservations list
    for reservation in reservations:
        # Extract the Instances list from the Reservation
        instances = reservation["Instances"]
        # Loop through each Instance in the Instances list
        for instance in instances:
            # Extract the InstanceId from the Instance
            instanceId = instance["InstanceId"]
            # Append the InstanceId to the instanceIds list
            instanceIds.append(instanceId)
    
    # Return the instanceIds list
    return instanceIds
            
# If this script is being run as the main program
if __name__ == "__main__":
    # Create an EC2 client
    ec2 = boto3.client('ec2')
    # Call the list_instance_ids function with the EC2 client as an argument to get a list of instance IDs
    instanceIds = list_instance_ids(ec2)
    # Print the instance IDs, separated by newlines
    print('\n'.join(instanceIds))
