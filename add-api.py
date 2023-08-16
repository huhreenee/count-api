import boto3
import json

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
        UpdateExpression="ADD addValue :val1", 
        #ConditionExpression='addValue > :val',
        ExpressionAttributeValues= {
            ":val1": 1
        },
        ReturnValues='ALL_NEW'
    )
    #print(resp)
    return int(count_resp['Attributes']['addValue'])

print(count('harini'))

def get(user_id):
    get_resp = table.get_item(
        # TableName='Count',
        Key = {
            "user_id": user_id
        }
    )
    item = get_resp['Item']
    return item['addValue']

print(get('harini'))

# def lambda_handler(event, context):
#     # TODO implement
#     print(event)
#     c = 0
#     if event["rawPath"] == "/count":
#       c = count(event["queryStringParameters"]["key"])
#     elif event["rawPath"] == "/get":
#       c = get(event["queryStringParameters"]["key"])
    
#     return {
#         'statusCode': 200, 
#         'body': json.dumps("'value': c")
#     }