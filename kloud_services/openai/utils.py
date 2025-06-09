import requests
from typing import Dict, Any, Optional

def make_request(
    method: str,
    url: str,
    headers: Optional[Dict[str, str]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout: int = 30,
    retries: int = 3
) -> Dict[str, Any]:
    """
    Make an HTTP request with retries and handle the response.
    """
    attempt = 0
    while attempt < retries:
        try:
            response = requests.request(method, url, headers=headers, json=json, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempt += 1
            if attempt < retries:
                print(f"Request failed (attempt {attempt}/{retries}). Retrying...")
            else:
                raise Exception(f"API request failed after {retries} attempts: {str(e)}")