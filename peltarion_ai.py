import requests

url = 'https://a.azure-eu-west.platform.peltarion.com/deployment/0b76101a-b5b8-4015-b5df-1006ae99d66d/forward'
token = '907e31b5-51fd-4756-bdc4-8fa56d883c03'
header = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}

payload = '{"rows": [{"text": "England on fire in world cup victory"}]}'
response = requests.request("POST", url, headers=header, data=payload)
print(response.json())

res = response.json()
resf = float(res['rows'][0]['target'])
if resf > 0.7:
    print("Disaster")
elif resf >0.55:
    print("Not sure")   
else:
    print("Not a disaster")
