import requests
from bs4 import BeautifulSoup
import numpy as np

def scrape_data():
    response = requests.get('https://example.com')
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

if __name__ == "__main__":
    print(scrape_data())