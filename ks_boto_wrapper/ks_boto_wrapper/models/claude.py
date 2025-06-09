from typing import Dict, Any, Optional, List
import boto3
import requests
from pydantic import BaseModel
from botocore.config import Config

# ----------------- Config ----------------- #
boto_config = Config(
    connect_timeout=5,
    read_timeout=5
)

# ----------------- Pydantic Models ----------------- #
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
    def __init__(self, client, model_id: str = "anthropic.claude-3-haiku-20240307-v1:0"):
        self.client = client
        self.model_id = model_id
        self.boto3_instance = boto3.client(
            self.client.runtime,
            region_name=self.client.region_name,
            aws_access_key_id=self.client.aws_access_key_id,
            aws_secret_access_key=self.client.aws_secret_access_key,
            endpoint_url=self.client.endpoint_url,
            config=boto_config
        )

    def make_request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make an HTTP request and handle the response.
        """
        try:
            response = requests.request(method, url, headers=headers, json=json)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def create(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        max_tokens: Optional[int] = 1024,
        temperature: Optional[float] = 0.7,
        top_p: Optional[float] = 0.9,
    ) -> ClaudeResponse:
        url = "http://20.197.39.253:8080/api/model/awsboto"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.client.aws_secret_access_key}"
        }

        payload = {
            "model": model,
            "messages": messages,
        }

        try:
            response_data = self.make_request("POST", url, headers=headers, json=payload)
            return ClaudeResponse(**response_data)

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
