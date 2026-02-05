##brew install python-requests
import os
import sys
import requests
##import httpx
import json


url = "https://api.airia.ai/v2/PipelineExecution/5ccb1859-13d2-4e84-ba66-6aadf97541a9"


payload = json.dumps({
  "userInput": "What was the latest F1 result ?",
  "debug": False,
#  "userInput": "Hi. My name is Reesy",
#  "userInput": "What is my name?",
  "userId": "YOUR-USER-ID",
  "conversationId": "YOUR-CONVERSATION",
  "asyncOutput": False,
  "includeToolsResponse": True
})
headers = {
  'X-API-KEY': 'YOUR-API-KEY',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
##response = httpx.post(url, headers=headers, data=payload)

print(response.text)
