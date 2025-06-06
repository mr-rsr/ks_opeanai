import json
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BedrockModel(ABC):
    def __init__(self, client, model_id: str):
        self.client = client
        self.model_id = model_id

    @abstractmethod
    def format_payload(self, messages: list,
                       max_tokens: Optional[int] = 512,
                       temperature: Optional[float] = 0.7,
                       top_k: Optional[int] = 250,
                       top_p: Optional[int] = 1,
                       stop_sequences: Optional[list] = ["\n\nHuman"]) -> Dict[str, Any]:
        pass

    def invoke(self, messages: list, **kwargs) -> Dict[str, Any]:
        payload = self.format_payload(messages)
        payload.update(kwargs)
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(payload),
            contentType="application/json",
            accept="application/json"
        )
        return json.loads(response["body"].read())
