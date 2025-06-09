import boto3
import os
from typing import Optional, List, Dict, Any
import os
from pydantic import BaseModel, Field


class Client:
    def __init__(self,
                 runtime:Optional[str] = 'bedrock-runtime',
                 region_name:Optional[str] = 'us-east-1',
                 aws_access_key_id:Optional[str] = None,
                 aws_secret_access_key:Optional[str] = None,
                 endpoint_url = 'http://20.197.39.253:8080/api/model/awsboto'):
        
        self.aws_access_key_id= aws_access_key_id or os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = aws_secret_access_key or os.getenv("AWS_SECRET_ACCESS_KEY")

        if self.aws_secret_access_key is None or self.aws_access_key_id is None:
            raise RuntimeError("Credentials were not provided")

        self.endpoint_url = endpoint_url
        self.runtime = runtime
        self.region_name = region_name

        # self.boto3_instance = boto3.client(
        #     self.runtime,
        #     region_name = self.region_name,
        #     aws_access_key_id = self.aws_access_key_id,
        #     aws_secret_access_key = self.aws_secret_access_key,
        #     endpoint_url = self.endpoint_url
        # )
        