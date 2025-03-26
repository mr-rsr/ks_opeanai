# kloud-services

A Python package for interacting with multiple AI services including OpenAI and Anthropic Claude APIs.

## Installation

```bash
pip install kloud-services
```

## Configuration

Set your API keys as environment variables:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["ANTHROPIC_API_KEY"] = "your-claude-api-key"
```

## Basic Usage

### OpenAI

```python
from kloud_services.openai import generate_response

# Create a list of messages
messages = [
    {"role": "user", "content": "What is Python?"}
]

# Generate a response
response = generate_response(
    model="gpt-4o-2024-05-13",
    messages=messages
)

# Print the response
print(response.choices[0].message.content)
```

### Claude

```python
from kloud_services.claude import generate_response

# Generate a response
response = generate_response(
    model="claude-3-sonnet-20240229",
    prompt="What is Python?",
    max_tokens=1000,
    temperature=0.7
)

# Print the response
print(response.content)
```

## Advanced Usage

### OpenAI Advanced

```python
from kloud_services.openai import generate_response

response = generate_response(
    model="gpt-4o-2024-05-13",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"}
    ],
    temperature=0.7,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    stop=["\n", "END"]
)
```

### Claude Advanced

```python
from kloud_services.claude import generate_response

response = generate_response(
    model="claude-3-sonnet-20240229",
    prompt="What is Python?",
    system="You are a helpful coding assistant.",
    max_tokens=1000,
    temperature=0.7,
    top_p=0.9,
    top_k=10,
    stop_sequences=["\n\n"]
)
```

## API Reference

### OpenAI `generate_response()`

#### Parameters:

- `model` (str, required): The model identifier (e.g., "gpt-4o-2024-05-13")
- `messages` (List[dict], required): List of message objects with 'role' and 'content'
- `temperature` (float, optional): Sampling temperature (0.0 to 1.0)
- `max_tokens` (int, optional): Maximum number of tokens in response
- `top_p` (float, optional): Nucleus sampling parameter (0.0 to 1.0)
- `frequency_penalty` (float, optional): Penalty for frequent tokens (0.0 to 2.0)
- `presence_penalty` (float, optional): Penalty for new tokens (0.0 to 2.0)
- `stop` (List[str], optional): List of stopping sequences

### Claude `generate_response()`

#### Parameters:

- `model` (str, required): The model identifier (e.g., "claude-3-sonnet-20240229")
- `prompt` (str, required): The input prompt
- `system` (str, optional): System message for context
- `max_tokens` (int, optional): Maximum number of tokens in response
- `temperature` (float, optional): Sampling temperature (0.0 to 1.0)
- `top_p` (float, optional): Nucleus sampling parameter (0.0 to 1.0)
- `top_k` (int, optional): Top-k sampling parameter
- `stop_sequences` (List[str], optional): List of stopping sequences

## Response Structures

### OpenAI Response
```python
class OpenAIResponse:
    id: str                   # Response identifier
    choices: List[Choice]     # List of response choices
    created: int             # Timestamp
    model: str               # Model used
    usage: Usage             # Token usage statistics
```

### Claude Response
```python
class ClaudeResponse:
    id: str                   # Response identifier
    content: str             # Response content
    model: str               # Model used
    stop_reason: str         # Reason for stopping
    stop_sequence: str       # Sequence that caused the stop
    usage: Usage             # Token usage statistics
```

## Error Handling

```python
try:
    response = generate_response(...)
except Exception as e:
    print(f"Error: {str(e)}")
```

## Requirements

- Python 3.7+
- requests >= 2.32.3
- pydantic >= 2.0.0

## License

This project is licensed under the MIT License.