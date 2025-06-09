from typing import Dict, Any, Optional, List
import boto3
import json
from pydantic import BaseModel



class OpenAIMessage(BaseModel):
    role: str
    content: str

class OpenAIChoice(BaseModel):
    finish_reason: Optional[str]
    index: int
    message: OpenAIMessage

class OpenAIUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class OpenAIResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[OpenAIChoice]
    usage: OpenAIUsage



class OpenAI:
    def __init__(self, client, model_id: str = "openai.gpt-4o"):
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
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        max_tokens: Optional[int] = 1024,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
    ) -> OpenAIResponse:
        payload = {
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p
        }

        try:
            response = self.boto3_instance.invoke_model(
                modelId=model or self.model_id,
                body=json.dumps(payload),
                accept='application/json'
            )
            body = response['body'].read().decode('utf-8')
            parsed_response = json.loads(body)
            return OpenAIResponse(**parsed_response)

        except Exception as e:
            raise RuntimeError(f"OpenAI API request failed: {e}")

    def generate_response(
        self,
        user_message: str,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
        max_tokens: Optional[int] = 1024,
        model: Optional[str] = None
    ) -> OpenAIResponse:
        messages = [{"role": "user", "content": user_message}]
        return self.create(
            messages=messages,
            model=model or self.model_id,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
