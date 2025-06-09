# KloudStac OpenAI & Claude Integration

This project demonstrates how to use the `kloud_services` Python package to interact with both Claude and OpenAI models via a unified client interface.

## Installation

```bash
pip install kloud_services
```

## Usage

### Using Claude

The `generate_response` method for Claude allows you to send a user message and customize the generation parameters:

```python
from kloud_services.client import Client
from kloud_services.claude import Claude

client = Client(access_key="YOUR_ACCESS_KEY")
claude = Claude(client)

response = claude.generate_response(
    user_message="hello",
    temperature=0.7,           # Optional: Controls randomness (default None)
    top_p=0.9,                 # Optional: Nucleus sampling (default None)
    max_tokens=1024,           # Optional: Max tokens in response (default 1024)
    model="anthropic.claude-3-sonnet-20240229-v1:0"  # Optional: Claude model version
)
print(response)
```

**Parameters:**
- `user_message` (str): The prompt or message from the user.
- `temperature` (float, optional): Sampling temperature for randomness.
- `top_p` (float, optional): Nucleus sampling probability.
- `max_tokens` (int, optional): Maximum number of tokens in the response.
- `model` (str, optional): Claude model to use.

### Using OpenAI

The `generate_response` method for OpenAI allows you to send a user message and customize various generation parameters:

```python
from kloud_services.client import Client
from kloud_services.openai import OpenAI

client = Client(access_key="YOUR_ACCESS_KEY")
openai = OpenAI(client)

response = openai.generate_response(
    user_message="hello",
    model="gpt-3.5-turbo",         # Optional: OpenAI model version (default "gpt-3.5-turbo")
    temperature=0.7,               # Optional: Controls randomness (default None)
    max_tokens=512,                # Optional: Max tokens in response (default None)
    top_p=0.9,                     # Optional: Nucleus sampling (default None)
    frequency_penalty=0.0,         # Optional: Penalize new tokens based on frequency (default None)
    presence_penalty=0.0,          # Optional: Penalize new tokens based on presence (default None)
    stop=["\n"]                    # Optional: Sequences where the API will stop generating further tokens (default None)
)
print(response)
```

**Parameters:**
- `user_message` (str): The prompt or message from the user.
- `model` (str, optional): OpenAI model to use (default: `"gpt-3.5-turbo"`).
- `temperature` (float, optional): Sampling temperature for randomness.
- `max_tokens` (int, optional): Maximum number of tokens in the response.
- `top_p` (float, optional): Nucleus sampling probability.
- `frequency_penalty` (float, optional): Penalizes repeated tokens.
- `presence_penalty` (float, optional): Penalizes new tokens based on their presence.
- `stop` (list of str, optional): Sequences where the API will stop generating further tokens.

## Configuration

Replace `"YOUR_ACCESS_KEY"` with your actual access key.

## License

See [LICENSE](./LICENSE) for details.