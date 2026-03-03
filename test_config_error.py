import os

# This will fail - missing environment variables
# This is a MEDIUM RISK scenario that should trigger PR creation
api_key = os.environ['API_KEY']
database_url = os.environ['DATABASE_URL']
secret_token = os.environ['SECRET_TOKEN']

print(f"API Key: {api_key}")
print(f"Database: {database_url}")
print(f"Token: {secret_token}")

# Simulate some processing
def process_data():
    return "Processing with config"

if __name__ == "__main__":
    result = process_data()
    print(result)
