

# api demo

import requests
import json

payload = {'_quantity': "2"}

url='https://fakerapi.it/api/v1/persons'
r = requests.get(url, json=payload)

print(r.text)
