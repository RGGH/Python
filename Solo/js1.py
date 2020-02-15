import requests
import json
headers = {"User-Agent":"Moo"}
res = requests.get("https://jsonplaceholder.typicode.com/posts")

print(json.dumps(res.json(), indent = 2))
