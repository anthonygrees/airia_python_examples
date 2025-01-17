import requests
import json

# Input: URL to scrape

# API Endpoint and Headers
url = "https://api.firecrawl.dev/v1/scrape"
headers = {
    "Authorization": "Bearer fc-xxxxxxxxxxxxxxxxxxxxx",
    "Content-Type": "application/json"
}

# Payload
payload = {
    "url": input.strip()
}



# Making the POST request
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # Raise an error for bad HTTP responses

    # Parsing the response JSON
    response_data = response.json()

    # Check for success and extract markdown
    if response_data.get("success") and "markdown" in response_data.get("data", {}):
        output = response_data["data"]["markdown"]
        
        print("Markdown content successfully saved to 'output'.")
    else:
        output = response_data;
        print("Failed to retrieve markdown. Response:", response_data)

except requests.exceptions.RequestException as e:
    output = str(e);
    print(f"An error occurred: {e}")
