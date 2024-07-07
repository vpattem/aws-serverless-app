import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name=os.environ['AWS_REGION'])
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    
    # Example operation: Put item into DynamoDB
    response = table.put_item(
       Item={
            'id': '123',
            'data': 'Hello from Lambda!'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }