import boto3
import json
        
def lambda_handler(event, context):
        
    #Create DynamoDB resource.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("visitor-count-table")
    
    #Retrieve Visitor Count & increment
    response = table.update_item(
        Key={
            "ID": "100"
        },
        UpdateExpression="SET Visits = Visits + :val1",
        ExpressionAttributeValues={
            ':val1': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    
    #GETS Item then prints output on console.
    response = table.get_item(Key={"ID": "100"})
    visit_count = response ["Item"]["Visits"]
    result= f"You are visitor number {visit_count}!" 
    body: str(body)
    return {
        # str({"message":result}),
        'statusCode': 200,
        'body': json.dumps(result)
        }
    #test 7
