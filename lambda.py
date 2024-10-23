import json

print("Loading Function")

def lambda_handler(event, context):
    # 1. Parse out query strings params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print('transactionId= ' + transactionId)
    print('transactionType= ' + transactionType)
    print('transactionAmount= ' + transactionAmount)

    #2. Construct the body of the response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = "Hello from the Lambda Land!"

    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    #4. Return the response object
    return responseObject