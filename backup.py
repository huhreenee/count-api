import json
import boto3

client = boto3.resource('dynamodb')

table = client.Table('Count')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    c = 0
    if event["rawPath"] == "/count":
      c = count(event["queryStringParameters"]["key"])
    elif event["rawPath"] == "/get":
      c = get(event["queryStringParameters"]["key"])
    
    return {
        'statusCode': 200, 
        # 'body': json.dumps({'value':c})
        'body': json.dumps({'value':c,'event':event})
    }
    
def count(user_id):
    count_resp = table.update_item(
        Key = {
            "user_id": user_id
        },
        UpdateExpression="ADD addValue :val1",
        ExpressionAttributeValues= {
            ":val1": 1
        },
        ReturnValues='ALL_NEW'
    )
    print("count_resp: ",count_resp['Attributes']['addValue'])
    return int(count_resp['Attributes']['addValue'])

def get(user_id):
    get_resp = table.get_item(
        Key = {
            "user_id": user_id
        }
    )
    item = get_resp['Item']
    print("get_resp: ",item['addValue'])
    return int(item['addValue'])