from typing import Dict, Any, Optional, List
import boto3
import json
from pydantic import BaseModel


class TitanResponse(BaseModel):
    inputTextTokenCount: int
    results: List[Dict[str, Any]]
    responseTextTokenCount: int

class Titan:
    def __init__(self, client, model_id: str = "amazon.titan-tg1-large"):
        self.client = client
        self.model_id = model_id
        self.boto3_instance = boto3.client(
            self.client.runtime,
            region_name=self.client.region_name,
            aws_access_key_id=self.client.aws_access_key_id,
            aws_secret_access_key=self.client.aws_secret_access_key,
            endpoint_url=self.client.endpoint_url
        )

    def create(
        self,
        input_text: str,
        max_token_count: Optional[int] = 512,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
        stop_sequences: Optional[List[str]] = None
    ) -> TitanResponse:
        payload = {
            "inputText": input_text,
            "textGenerationConfig": {
                "maxTokenCount": max_token_count,
                "stopSequences": stop_sequences or [],
                "temperature": temperature,
                "topP": top_p
            }
        }

        try:
            response = self.boto3_instance.invoke_model(
                modelId=self.model_id,
                body=json.dumps(payload),
                accept='application/json'
            )
            body = response['body'].read().decode('utf-8')
            parsed_response = json.loads(body)
            return TitanResponse(**parsed_response)

        except Exception as e:
            raise RuntimeError(f"Titan API request failed: {e}")

    def generate_response(
        self,
        user_message: str,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
        max_token_count: Optional[int] = 512,
        stop_sequences: Optional[List[str]] = None
    ) -> TitanResponse:
        return self.create(
            input_text=user_message,
            max_token_count=max_token_count,
            temperature=temperature,
            top_p=top_p,
            stop_sequences=stop_sequences
        )
