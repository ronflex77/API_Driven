import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    path = event.get('path', '')
    params = event.get('queryStringParameters') or {}
    instance_id = params.get('instance_id')

    # Détection de l'action via le chemin
    if 'start' in path: action = 'start'
    elif 'stop' in path: action = 'stop'
    elif 'status' in path: action = 'status'
    else: action = None
    
    try:
        if action == 'status':
            response = ec2.describe_instances(InstanceIds=[instance_id])
            state = response['Reservations'][0]['Instances'][0]['State']['Name']
            emoji = "🟢" if state == "running" else "🔴" if state == "stopped" else "🟡"
            msg = f"{emoji} État actuel : L'instance {instance_id} est actuellement [{state.upper()}]."
            
        elif action == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
            msg = f"🚀 Succès : L'instance {instance_id} est en cours de démarrage."
            
        elif action == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])
            msg = f"🛑 Succès : L'instance {instance_id} est en cours d'extinction."
            
        else:
            msg = "⚠️ Erreur : Action non reconnue (utilisez /start, /stop ou /status)."
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain; charset=utf-8'},
            'body': msg
        }
    except Exception as e:
        return {'statusCode': 500, 'body': f"❌ Erreur : {str(e)}"}
