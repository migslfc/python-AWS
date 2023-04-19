# Import the necessary modules.
from datetime import datetime
import boto3

# Define the Lambda function.
def lambda_handler(event, context):

    # Create an EC2 client object.
    ec2_client = boto3.client('ec2')

    # Get a list of all regions that the EC2 client can access.
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Loop through all regions.
    for region in regions:

        # Print the name of the region.
        print('Instances in EC2 Region {0}:'.format(region))

        # Create an EC2 resource object for the region.
        ec2 = boto3.resource('ec2', region_name=region)

        # Get a list of instances with the tag "backup" set to "true".
        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'tag:backup', 'Values': ['true']}
            ]
        )

        # Get the current UTC timestamp in ISO 8601 format.
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

        # Loop through all instances with the "backup" tag set to "true".
        for i in instances.all():
            for v in i.volumes.all():

                # Create a description for the snapshot.
                desc = 'Backup of {0}, volume {1}, created {2}'.format(
                    i.id, v.id, timestamp)
                print(desc)

                # Create a snapshot of the volume.
                snapshot = v.create_snapshot(Description=desc)

                # Print the ID of the new snapshot.
                print("Created snapshot:", snapshot.id)
