from typing import Dict, Any, Optional, List
import boto3
import json
from pydantic import BaseModel



class LlamaMessage(BaseModel):
    role: str
    content: str

class LlamaContentBlock(BaseModel):
    type: str
    text: str

class LlamaResponseUsage(BaseModel):
    input_tokens: int
    output_tokens: int

class LlamaResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Dict[str, Any]]
    usage: LlamaResponseUsage



class Llama:
    def __init__(self, client, model_id: str = "meta.llama3-70b-instruct-v1:0"):
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
    ) -> LlamaResponse:
        try:
            response = self.boto3_instance.invoke_model(
                modelId=model or self.model_id,
                body=json.dumps({
                    "prompt": self.format_prompt(messages),
                    "max_gen_len": max_tokens,
                    "temperature": temperature,
                    "top_p": top_p
                }),
                accept='application/json'
            )
            body = response['body'].read().decode('utf-8')
            parsed_response = json.loads(body)
            return LlamaResponse(**parsed_response)

        except Exception as e:
            raise RuntimeError(f"Llama API request failed: {e}")

    def generate_response(
        self,
        user_message: str,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
        max_tokens: Optional[int] = 1024,
        model: Optional[str] = None
    ) -> LlamaResponse:
        messages = [{"role": "user", "content": user_message}]
        return self.create(
            messages=messages,
            model=model or self.model_id,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )

    def format_prompt(self, messages: List[Dict[str, str]]) -> str:
        """ Formats messages into Llama prompt style """
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt += f"<|user|> {content}\n"
            elif role == "assistant":
                prompt += f"<|assistant|> {content}\n"
        prompt += "<|assistant|> "
        return prompt
