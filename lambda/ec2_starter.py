from __future__ import print_function
import boto3

print('Loading function')


def lambda_handler(event, context):
    instance_ids = []
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(
        DryRun=False,
    )
    reservations = response['Reservations']
    for reservation in reservations:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    response = ec2_client.start_instances(
        InstanceIds=instance_ids,
    )
    print(response)
