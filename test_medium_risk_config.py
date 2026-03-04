import os

# MEDIUM RISK TEST - Configuration Error
# This will trigger MEDIUM risk because it's a configuration/environment issue

# Try to access environment variables that don't exist
database_host = os.environ['DATABASE_HOST']
database_port = os.environ['DATABASE_PORT']

print(f"Connecting to {database_host}:{database_port}")
