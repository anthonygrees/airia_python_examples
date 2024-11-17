# The tool aimed to scrap a content from a webpage, to use it for an LLM inference. 
# It's normally used once it's clear that URL given is a website and not a file link.
#
import json
import requests
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor

# Function to scrape text from a webpage
def scrape_text(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        session = requests.Session()
        response = session.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        cleaned_text = '\n'.join([line.strip() for line in text.splitlines() if line.strip()])
        cleaned_text = re.sub(r'\n+', '\n', cleaned_text)
        return cleaned_text.strip()
    except requests.exceptions.RequestException as e:
        return f"Error while fetching the URL: {e}"

if __name__ == "__main__":
    url = input.strip()
    output = json.dumps(scrape_text(url))
