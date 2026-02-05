import sys
import requests
import json
from datetime import datetime, timezone
 
def create_airia_conversation(api_key, user_id):
    url = "https://api.airia.ai/v1/Conversations"
 
    # Use current UTC time for createdAt and updatedAt
    current_time = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
 
    payload = json.dumps({
        "userId": user_id,
        "title": None,
        "createdAt": current_time,
        "updatedAt": current_time,
        "deploymentId": None,
        "dataSourceFiles": {
            "ANY_ADDITIONAL_PROPERTY": [""]
        },
        "isBookmarked": True
    })
 
    headers = {
        'X-API-KEY': api_key,
        'Content-Type': 'application/json'
    }
 
    try:
        response = requests.post(url, headers=headers, data=payload)
        
        # Print status code and headers
        print(f"Status Code: {response.status_code}")
        print("Response Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        
        # Print the full response text
        print("\nResponse Text:")
        print(response.text)
        
        # Try to parse and print JSON if possible
        try:
            json_response = response.json()
            print("\nJSON Response:")
            print(json.dumps(json_response, indent=2))
        except json.JSONDecodeError:
            print("\nResponse is not in JSON format.")
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Error response text: {e.response.text}")
        sys.exit(1)
 
if __name__ == "__main__":
    # Set your API key here
    api_key = "YOUR-KEY-HERE"  # Replace with your actual API key
    
    # Check if API key is set
    if api_key == "YOUR_API_KEY_HERE":
        print("Error: Please replace 'YOUR_API_KEY_HERE' with your actual Airia API key.")
        sys.exit(1)
 
    # Set your user ID here
    user_id = "USER-ID-HERE"  # Replace with your actual user ID if different
 
    create_airia_conversation(api_key, user_id)
