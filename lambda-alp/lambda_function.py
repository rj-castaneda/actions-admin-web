import json
import boto3
import sys

def lambda_handler(event, context):
    # Create connection
    # print('EVENT')
    # print(event)
    try:
        dynamodb = boto3.resource('dynamodb')
    except:
        raise Exception("Could not make connection to dynamodb")
    
    action_metadata = json.loads(event.get('body'))
    print('ACTION BODY')
    print(action_metadata)
    workflow_run = action_metadata.get('workflow_run')
    
    if workflow_run:
        doc = {}
        doc['id'] = workflow_run.get('id')
        doc['name'] = workflow_run.get('name')
        doc['status'] = workflow_run.get('status')
        doc['conclusion'] = workflow_run.get('conclusion')
        doc['workflow_id'] = workflow_run.get('workflow_id')
        doc['created_at'] = workflow_run.get('created_at')
        doc['udpated_at'] = workflow_run.get('udpated_at')
        doc['head_branch'] = workflow_run.get('head_branch')
        doc['head_sha'] = workflow_run.get('head_sha')
        doc['html_url'] = workflow_run.get('html_url')
        print(doc)
        
        response = dynamodb.Table('ga_workflow_run').put_item(Item=doc)
        
        if response:
            print(type(response))
            
        print(f'Response Dir:{print(type(response))}')
    
    
    return "200 - OK"