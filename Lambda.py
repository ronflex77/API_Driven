import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    params = event.get('queryStringParameters', {})
    action = params.get('action')
    instance_id = params.get('instance_id')

    if action == 'start':
        ec2.start_instances(InstanceIds=[instance_id])
        msg = f"Instance {instance_id} démarrée"
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=[instance_id])
        msg = f"Instance {instance_id} arrêtée"
    else:
        msg = "Action inconnue"

    return {'statusCode': 200, 'body': json.dumps(msg)}