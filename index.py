import requests
import json

# test function in python
def printJson(content):
    print(json.dumps(json.loads(content), indent=4, sort_keys=True))

# test requests in python
github = requests.get('https://api.github.com')

printJson(github.content)
