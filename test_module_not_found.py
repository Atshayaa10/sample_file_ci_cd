import requests
import beautifulsoup4  # Wrong!
import numpy as np

def scrape_data():
    response = requests.get('https://example.com')
    soup = beautifulsoup4.BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

if __name__ == "__main__":
    print(scrape_data())
