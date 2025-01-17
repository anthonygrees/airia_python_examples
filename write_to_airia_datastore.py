import io
import json
import requests

# Function for uploading files
def url_creation(file_bytes, file_name="document.txt"):
    url = "https://prodaus.api.airia.ai/v2/DataSource/a60d4YOUR-DATASOURCE-ID5d1a6/files"
    headers = {
        "X-API-Key": "ak-YOUR-AIRIA-KEY",  # Replace with actual API key
    }
    files = {
        'file': (file_name, io.BytesIO(file_bytes), 'text/plain')
    }

    payload = {
        "userId": "2ceYOUR-USER-ID73b348",
        "projectId": "b289YOUR-PROJECT-IDc349f9",
        "asyncOutput": False
    }

    # Set the file as a plain text document
    files = {'file': (file_name, file_bytes, 'text/plain')}

    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        dictionary = json.loads(response.text)
        return input
    else:
        return f"Failed to upload the file. Status code: {response.status_code}, Response: {response.text}"

# Create the text in memory
text_content = input

# Save text to a BytesIO stream
file_stream = io.BytesIO(text_content.encode('utf-8'))

# Upload the text file
response = url_creation(file_stream.getvalue(), file_name="document.txt")
output = response
