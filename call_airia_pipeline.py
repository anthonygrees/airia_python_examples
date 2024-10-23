## Call and Airia Pipeline
##
import requests
import json
 
url = "https://dev.api.airiadev.ai/v1/PipelineExecution/"
 
payload = json.dumps({
  "userInput": "Example user input",
  "asyncOutput": False
})
headers = {
  'X-API-KEY': 'API Key',
  'Content-Type': 'application/json'
}
 
response = requests.request("POST", url, headers=headers, data=payload)
 
output = response.text
