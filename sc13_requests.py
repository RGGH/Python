# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

''' API example using json=payload '''

import requests
import json

payload = {'_quantity': "2"}

url='https://fakerapi.it/api/v1/persons'
r = requests.get(url, json=payload)

print(r.text)
