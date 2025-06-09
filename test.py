from kloud_services.client import Client
from kloud_services.openai import OpenAI
client = Client(access_key="sadasdas")
openai = OpenAI(client)
openai.generate_response(user_message="hello")