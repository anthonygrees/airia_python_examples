"""
Airia File Upload + Pipeline Execution Script

How to use:
1. Set your API key
2. Set your pipeline ID
3. Update FILE_PATH with the file you want to process
4. Run the script
"""

import os
import requests

# UPDATE THESE VALUES
API_KEY = "YOUR-KEY"
PIPELINE_ID = "YOUR-AGENT-PIPELINE"
FILE_PATH = "YourFile.pdf"

def upload_file(filepath):
    """Upload a file to Airia and return the file URL"""
    upload_url = "https://prodaus.api.airia.ai/v1/upload"

    with open(filepath, "rb") as f:
        files = {"file": (os.path.basename(filepath), f)}
        headers = {"X-API-Key": API_KEY}
        response = requests.post(upload_url, headers=headers, files=files)

    data = response.json()
    return data.get("imageUrl") or data.get("fileUrl")


def run_pipeline(file_url, filepath, pipeline_id):
    """Execute pipeline with uploaded file"""
    pipeline_url = f"https://prodaus.api.airia.ai/v2/PipelineExecution/{pipeline_id}"

    if filepath.lower().endswith((".jpg", ".jpeg", ".png")):
        payload = {"userInput": "Process this file", "images": [file_url]}
    else:
        payload = {"userInput": "Process this file", "files": [file_url]}

    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(pipeline_url, headers=headers, json=payload)
    return response


# EXECUTION
file_url = upload_file(FILE_PATH)
response = run_pipeline(file_url, FILE_PATH, PIPELINE_ID)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
