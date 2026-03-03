import json

# High-risk test - multiple files with errors
# This should trigger PR creation

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def process():
    config = load_config()
    return config['database']['host']

if __name__ == "__main__":
    result = process()
    print(result)
