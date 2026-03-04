import os

# MEDIUM RISK TEST - Second file to make it 2 files (MEDIUM risk condition)

# Another config file with environment issues
api_endpoint = os.environ['API_ENDPOINT']
api_key = os.environ['API_SECRET_KEY']

def get_config():
    return {
        'endpoint': api_endpoint,
        'key': api_key
    }

print(get_config())
