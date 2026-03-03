import os
import sys

# High-risk test - part 2
# Multiple files = HIGH RISK

def validate_environment():
    required_vars = ['API_KEY', 'DATABASE_URL', 'SECRET_TOKEN', 'AWS_ACCESS_KEY']
    
    for var in required_vars:
        if var not in os.environ:
            raise ValueError(f"Missing required environment variable: {var}")
    
    return True

if __name__ == "__main__":
    validate_environment()
    print("Environment validated")
