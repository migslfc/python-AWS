# Import the necessary modules.
import boto3

# Define the Lambda function.
def lambda_handler(event, context):

    # Create an EC2 client object and get a list of all regions.
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Loop through all regions.
    for region in regions:
        
        # Create an EC2 resource object for the region and print the name of the region.
        ec2 = boto3.resource('ec2', region_name=region)
        print("Region:", region)

        # Get a list of running instances in the region.
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['running']}])

        # Stop all running instances in the region.
        for instance in instances:
            instance.stop()
            print('Stopped instance: ', instance.id)
