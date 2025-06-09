from typing import Dict, Any, Optional, List
import boto3
import json
from pydantic import BaseModel, Field
from botocore.config import Config

boto_config = Config(
    connect_timeout=5,  # seconds to wait for connection
    read_timeout=5     # seconds to wait for a response
)
class Message(BaseModel):
    role: str
    content: str

class ContentBlock(BaseModel):
    type: str
    text: str

class ClaudeResponseContent(BaseModel):
    type: str
    text: str

class ClaudeResponseUsage(BaseModel):
    input_tokens: int
    output_tokens: int

class ClaudeResponse(BaseModel):
    id: str
    type: str
    role: str
    model: str
    content: List[ContentBlock]
    stop_reason: str
    stop_sequence: Optional[str]
    usage: ClaudeResponseUsage

# ----------------- Claude Wrapper ----------------- #

class Claude:
    def __init__(self, client, model_id: str = "anthropic.claude-3-sonnet-20240229-v1:0"):
        self.client = client
        self.model_id = model_id
        self.boto3_instance = boto3.client(
            self.client.runtime,
            region_name=self.client.region_name,
            aws_access_key_id=self.client.aws_access_key_id,
            aws_secret_access_key=self.client.aws_secret_access_key,
            endpoint_url= self.client.endpoint_url ,
            config = boto_config
        )

    def create(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        max_tokens: Optional[int] = 1024,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
    ) -> ClaudeResponse:
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt += f"\n\nHuman: {content}"
            elif role == "assistant":
                prompt += f"\n\nAssistant: {content}"
        prompt += "\n\nAssistant:"

        payload = {
            "prompt": prompt,
            "max_tokens_to_sample": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "stop_sequences": ["\n\nHuman"]
        }

        try:
            
            response = self.boto3_instance.invoke_model(
                modelId=self.model_id,
                body=json.dumps(payload),
                accept='application/json'
            )
            body = response['body'].read().decode('utf-8')
            parsed_response = json.loads(body)
           
            return ClaudeResponse(**parsed_response)

        except Exception as e:
            raise RuntimeError(f"Claude API request failed: {e}")

    def generate_response(
        self,
        user_message: str,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
        max_tokens: Optional[int] = 1024,
        model: Optional[str] = None
    ) -> ClaudeResponse:
        messages = [{"role": "user", "content": user_message}]
        return self.create(
            messages=messages,
            model=model or self.model_id,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
