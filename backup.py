import json
import boto3
import re
from time import time

client = boto3.resource('dynamodb')

table = client.Table('Count')

def lambda_handler(event,context):
    # TODO implement
    print(event)
    c = 0
    li = event["rawPath"].split('/')
    action,key = '',''
    try:
        pattern = re.compile(r"^[a-z0-9_-]{3,64}$")
        action = li[1]
        key = li[2].lower()
        if not (re.fullmatch(pattern,key)):
           raise Exception
    except:
       return {
        'statusCode': 400, 
        'body': json.dumps({'message':"bad request"})
    }
    if(key==""):
       return {
        'statusCode': 400, 
        'body': json.dumps({'message':"bad request"})
    }
       
    if action=="count":
      c = count(key)
    elif action=="get":
      c = get(key)
      if c == -1:
        return {
        'statusCode': 404, 
        'body': json.dumps({'message':"item does not exist"})
    }
    else:
        return {
        'statusCode': 400, 
        # 'body': json.dumps({'value':c})
        'body': json.dumps({'message':"bad request"})
    }
    return {
        'statusCode': 200, 
        # 'body': json.dumps({'value':c})
        'body': json.dumps({'value':c})
    }
    
def count(user_id):
    count_resp = table.update_item(
        Key = {
            "user_id": user_id
        },
        UpdateExpression="ADD addValue :val1 SET version = :ts1",
        ExpressionAttributeValues= {
            ":val1": 1, 
            ":ts1" : round(time())

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
    if "Item" not in get_resp:
       return -1
    item = get_resp['Item']
    print("get_resp: ",item['addValue'])
    return int(item['addValue'])