"""
Airia Data Source Sync Script

How to use:
1. Find your data source URL: https://prodaus.airia.ai/{project-id}/dataConnectors/dcAssetsList/{data-source-id}
2. Update the three variables below with your values
3. Run the script
"""

import requests

# UPDATE THESE VALUES
API_KEY = "ak-INSERT-API-KEY"
PROJECT_ID = "your-project-id"
DATA_SOURCE_ID = "your-data-source-id"

# Sync the data source
url = f"https://prodaus.api.airia.ai/datastore/v1/store/connector/{DATA_SOURCE_ID}/{PROJECT_ID}/reprocess"
response = requests.post(url, headers={"X-API-Key": API_KEY})

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
