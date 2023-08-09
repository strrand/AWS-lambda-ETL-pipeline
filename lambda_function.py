import datetime
from Historic_Crypto import HistoricalData
import pandas as pd
import boto3

def lambda_handler(event, context):

    # 1. Fetch historical crypto data
    crypto_df = get_historical_prices('BTC')
    
    # 2. Convert the data to CSV format
    csv_buffer = convert_df_to_csv(crypto_df)
    
    # 3. Save the CSV data to S3
    save_to_s3(csv_buffer, "my-unique-lambda-bucket123", "your-key.json")

    return {
        'statusCode': 200,
        'body': 'Data successfully stored in S3.'
    }

def get_historical_prices(crypto='BTC') -> pd.DataFrame:
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    crypto_df = HistoricalData(f'{crypto}-USD', 86400, '2020-01-01-00-00', f"{today}-00-00", verbose=False).retrieve_data()
    return crypto_df

def convert_df_to_csv(df: pd.DataFrame) -> bytes:
    from io import BytesIO
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer)
    return csv_buffer.getvalue()

def save_to_s3(data, bucket_name, file_name):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).put_object(Key=file_name, Body=data)

    df.to_csv(csv_buffer) return csv_buffer.getvalue() def save_to_s3(data, bucket_name, file_name): s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).put_object(Key=file_name, Body=data)

