import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!....edited on 19thfeb2023 (Modified v0.1')
    }
