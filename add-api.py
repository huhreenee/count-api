import boto3
import json
import re
from time import time


client = boto3.resource('dynamodb',
    region_name = 'ap-south-1')

table = client.Table('Count')

# table.put_item(
#     # TableName='Count',
#     Item = {
#         'user_id':'janedoe' ,
#         'addValue': 25

#     }
# )

def count(user_id):
    count_resp = table.update_item(
    #     TableName = 'Count',
        Key = {
            "user_id": user_id
        },
        UpdateExpression="ADD addValue :val1 SET version = :ts1",
        #ConditionExpression='addValue > :val',
        ExpressionAttributeValues= {
            ":val1": 1,
            ":ts1" : round(time())
        },
        ReturnValues='ALL_NEW'
    )
    #print(resp)
    return int(count_resp['Attributes']['addValue'])

#print(count('harini'))

def get(user_id):
    get_resp = table.get_item(
        # TableName='Count',
        Key = {
            "user_id": user_id
        }
    )
    if "Item" not in get_resp:
       return -1
    print(get_resp)
    item = get_resp['Item']
    return int(item['addValue'])

#print(get('harini'))

# def lambda_handler(event,context):
#     # TODO implement
#     print(event)
#     c = 0
#     if event["rawPath"].startswith("/count"):
#       c = count(event["queryStringParameters"]["key"])
#     elif event["rawPath"].startswith("/get"):
#       c = get(event["queryStringParameters"]["key"])
    
#     return {
#         'statusCode': 200, 
#         'body': json.dumps("'value': c")
#     }

# lambda_handler({"rawPath": "/get"})

# li = event["rawPath"].split('/')
# print(li)

# def lambda_handler(event,context):
#     # TODO implement
#     print(event)
#     c = 0
#     if event["rawPath"].startswith("/count"):
#       c = count(event["rawPath"].split('/')[2])
#     elif event["rawPath"].startswith("/get"):
#       c = get(event["rawPath"].split('/')[2])
    
#     return {
#         'statusCode': 200, 
#         'body': json.dumps("'value': c")
#     }

# lambda_handler({"rawPath": "/get"})

# print(event["rawPath"].split('/')[2])


event = {"version": "2.0", "routeKey": "$default", "rawPath": "/get/"}



def lambda_handler(event):
    # TODO implement
    print(event)
    c = 0
    li = event["rawPath"].split('/')
    action,key = '',''
    pattern = re.compile(r"^[a-z0-9_-]{3,64}$")
    try:
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

lambda_handler(event)

#"^[a-z0-9_-]{3,64}$"g