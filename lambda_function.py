import json
import requests
import boto3

def lambda_handler(event, context):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    # Parse the response to JSON
    data = response.json()

    # Initialize a boto3 client for S3
    s3 = boto3.client('s3')

    # Specify the bucket name and the key
    bucket_name = 'my-unique-lambda-bucket123'  # use your actual bucket name here
    key = 'your-key.json'

    # Convert the data to a string
    data_str = json.dumps(data)

    # Upload the data to S3
    s3.put_object(Body=data_str, Bucket=bucket_name, Key=key)

    return {
        'statusCode': 200,
        'body': 'Data successfully stored in S3.'
    }

