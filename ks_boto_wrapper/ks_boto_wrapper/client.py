import boto3
import os
from typing import Optional
def get_bedrock_client(region:str = "us-east-1",
                       aws_access_key_id:Optional[str] = None,
                       aws_secret_access_key:Optional[str] = None):
    if aws_secret_access_key is None or aws_access_key_id is None:
        if os.getenv("AWS_ACCESS_KEY_ID") is None or os.getenv("AWS_SECRET_ACCESS_KEY") is None:
            raise BrokenPipeError("No valid AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY was provided")
    return boto3.client(
        'bedrock-runtime',
        region_name=region,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

get_bedrock_client()