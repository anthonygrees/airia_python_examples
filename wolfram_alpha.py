# Calls Wolfram Alpha API
#
import requests
 
key = "Wolfram Key Here"
query = input
 
x = requests.get('https://www.wolframalpha.com/api/v1/llm-api?input=' + query + '&appid=' + key)
output = str((x.text))
