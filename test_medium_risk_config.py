# Configuration-related error - MEDIUM RISK
# Should create PR for review

import yaml

def load_config():
    # This will fail because config.yaml has syntax error
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config

def update_config(key, value):
    config = load_config()
    config[key] = value
    
    with open('config.yaml', 'w') as f:
        yaml.dump(config, f)

if __name__ == "__main__":
    config = load_config()
    print(config)
