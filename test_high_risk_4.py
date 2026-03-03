import requests

# High-risk test - part 4
# Multiple files + missing package = HIGH RISK

def fetch_data(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    data = fetch_data("https://api.example.com/data")
    print(data)
