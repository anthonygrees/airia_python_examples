# The tool which is created to detect if the url is a file or not. 
# And to decide which scrapper to call: File downloader-scrapper or Webpage Scrapper.
#
import requests

def get_content_type(url):
    try:
        # Send a GET request with a small timeout and limit the response content size
        response = requests.get(url, stream=True, timeout=5)
        
        # Check if Content-Type header exists
        content_type = response.headers.get('Content-Type', '').lower()
        return content_type
        # Check if Content-Type indicates a file type
    except requests.RequestException as e:
        return f"Error accessing {url}: {e}"

url = input.strip()
output = get_content_type(url)
