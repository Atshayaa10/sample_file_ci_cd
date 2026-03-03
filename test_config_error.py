import os

# This will fail if API_KEY is not set
api_key = os.environ['API_KEY']
print(f"API Key: {api_key}")
