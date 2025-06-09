
from urllib.parse import urlparse
from typing import Optional, Dict, Any
import requests
from .openai.api import OpenAI
from .claude.api import Claude
class Client:


    def __init__(self, access_key:str ,base_url:str  = "http://20.197.22.86:3000", verbose:bool = False):

        if not access_key:
            raise ValueError("Access key must not be empty.")
        
        parsed_url = urlparse(base_url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError(f"Invalid base URL: {base_url}")
        

        self.access_key = access_key
        self.base_url = base_url
        if verbose:
            print(f"[Client] Initialized with base_url: {self.base_url}")


    def make_request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        timeout: int = 5,
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




