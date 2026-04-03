import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    path = event.get('path', '')
    params = event.get('queryStringParameters') or {}
    instance_id = params.get('instance_id')

    action = 'start' if 'start' in path else 'stop' if 'stop' in path else None
    
    try:
        if action == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
            msg = f"🚀 Succès : L'instance {instance_id} a été DÉMARRÉE avec succès."
        elif action == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])
            msg = f"🛑 Succès : L'instance {instance_id} a été ARRÊTÉE avec succès."
        else:
            msg = "⚠️ Erreur : Action non reconnue."
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain; charset=utf-8'},
            'body': msg
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"❌ Erreur technique : {str(e)}"
        }
