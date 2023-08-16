# Count-API

Count API is a counter made using serverless AWS services of [Lambda](https://aws.amazon.com/lambda/) and [DynamoDB](https://aws.amazon.com/dynamodb/) 

## Usage
Use the API endpoint [https://mc3xepweq4y6sfw4yswnq2izke0hyvtz.lambda-url.ap-south-1.on.aws/]<action>/<key> (https://mc3xepweq4y6sfw4yswnq2izke0hyvtz.lambda-url.ap-south-1.on.aws/)to count the key item. 

### Possible actions are: 
- count : to count things for the key
- get : to get the value for the key

### Specification of the key
- any alphanumeric valiue of the length 3 to 64
- can include special characters '_' (underscore) and '-' (hyphen)

### Example
- for count
[https://mc3xepweq4y6sfw4yswnq2izke0hyvtz.lambda-url.ap-south-1.on.aws/count/example](https://mc3xepweq4y6sfw4yswnq2izke0hyvtz.lambda-url.ap-south-1.on.aws/count/example)
- for get 
[https://mc3xepweq4y6sfw4yswnq2izke0hyvtz.lambda-url.ap-south-1.on.aws/get/example](https://mc3xepweq4y6sfw4yswnq2izke0hyvtz.lambda-url.ap-south-1.on.aws/get/example)