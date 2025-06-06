from ks_boto_wrapper.client import get_bedrock_client
from ks_boto_wrapper.models.claude import Claude

client = get_bedrock_client(
    aws_access_key_id=None,
    aws_secret_access_key=None
)
claude = Claude(client, "anthropic.claude-3-sonnet-20240229-v1:0")

messages = [{"role": "user", "content": "What is the capital of India?"}]
response = claude.invoke(messages)

print(client)