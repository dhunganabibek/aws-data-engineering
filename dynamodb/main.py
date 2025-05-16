import boto3


dynamodb = boto3.client("dynamodb", region_name="us-east-1")

# creaing a new table
# table = dynamodb.create_table(
#     TableName='Users',
#     KeySchema=[
#         {'AttributeName': 'UserID', 'KeyType': 'HASH'},   # Partition key
#         {'AttributeName': 'Timestamp', 'KeyType': 'RANGE'} # Sort key
#     ],
#     AttributeDefinitions=[
#         {'AttributeName': 'UserID', 'AttributeType': 'S'},
#         {'AttributeName': 'Timestamp', 'AttributeType': 'N'}
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )


# describing the table
# response = dynamodb.describe_table(TableName='Users')


# PUT item in table
try:
    response = dynamodb.put_item(
        TableName="Users",
        Item={
            "UserID": {"S": "12345"},
            "Timestamp": {"N": "1234567890"},
            "Name": {"S": "John Doe"},
            "Age": {"N": "30"},
        },
        ConditionExpression="attribute_not_exists(UserID) AND attribute_not_exists(Timestamp)",
    )
    print("Item added:", response)
except dynamodb.exceptions.ClientError as e:
    print("Item already exists")


# getting item from table
response = dynamodb.get_item(
    TableName="Users", Key={"UserID": {"S": "12345"}, "Timestamp": {"N": "1234567890"}}
)
print(response.get("Item", "No item found"))

# update the item
response = dynamodb.update_item(
    TableName="Users",
    Key={"UserID": {"S": "12345"}, "Timestamp": {"N": "1234567890"}},
    UpdateExpression="SET Age = :val1",
    ExpressionAttributeValues={":val1": {"N": "31"}},
)

# delete the item
response = dynamodb.delete_item(
    TableName="Users", Key={"UserID": {"S": "12345"}, "Timestamp": {"N": "1234567890"}}
)


# Query the database
response = dynamodb.query(
    TableName="Users",
    KeyConditionExpression="UserID = :uid AND Timestamp >= :ts",
    ExpressionAttributeValues={
        ":uid": {"S": "12345"},
        ":ts": {"N": "1234560000"}
    },
    ProjectionExpression="Name"  # Only return the 'Name' attribute
)
for item in response["Items"]:
    print(item)