## Usage

### Example 1: Using Explicit Credentials

```python
from ks_boto_wrapper import Claude
from ks_boto_wrapper.client import Client

client = Client(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
    endpoint_url=''  # Your endpoint
)

claude = Claude(client=client)
response = claude.generate_response(
    "Tell me a joke about computers",
    temperature=0.7,
    top_p=0.9,
    max_tokens=1024,
    model=None
)
```

---

### Example 2: Using Environment Variables

```python
from ks_boto_wrapper import Claude
from ks_boto_wrapper.client import Client
import os

os.environ['AWS_ACCESS_KEY_ID'] = 'YOUR_ACCESS_KEY'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'YOUR_SECRET_ACCESS_KEY'
client = Client()

claude = Claude(client=client)
response = claude.generate_response(
    "Tell me a joke about computers",
    temperature=0.7,
    top_p=0.9,
    max_tokens=1024,
    model=None
)
```

---

## Available Modules

* Claude
* Llama
* OpenAI GPT
* Titan


**Note:**  
The default endpoint is set to `https://bedrock-runtime.us-east-1.amazonaws.com`, but you can change it to another endpoint, such as `http://20.197.22.86:3000`, by specifying the `endpoint_url` parameter in the `Client` initialization.


