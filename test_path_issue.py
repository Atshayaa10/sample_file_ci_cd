def read_config():
    # Windows-style path - will fail on Linux CI
    config_file = "data\\config.json"
    
    with open(config_file, 'r') as f:
        content = f.read()
    
    return content

if __name__ == "__main__":
    config = read_config()
    print(f"Config: {config}")
