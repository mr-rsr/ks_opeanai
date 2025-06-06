from ..base import BedrockModel
from typing import Dict, Any, Optional
class Claude(BedrockModel):
    def format_payload(self, messages: list,
                       max_tokens: Optional[int] = 512,
                       temperature: Optional[float] = 0.7,
                       top_k: Optional[int] = 250,
                       top_p: Optional[int] = 1,
                       stop_sequences: Optional[list] = ["\n\nHuman"]) -> Dict[str, Any]:
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt += f"\n\nHuman: {content}"
            elif role == "assistant":
                prompt += f"\n\nAssistant: {content}"
        prompt += "\n\nAssistant:"
        return {
            "prompt":prompt,
            "max_tokens_to_sample": max_tokens,
            "temperature" : temperature,
            "top_k" : top_k,
            "top_p" : top_p,
            "stop_sequences":stop_sequences
        }