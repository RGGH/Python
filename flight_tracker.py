
import requests

params = {
    'access_key': 'af63cnc98a3640633efabc2d122cd042'
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()


for flight in api_response['data']:
    
    # use your own flight number here to look up:
    if flight['flight']['iata']=="UA858":
        
        print(flight['airline']['name'],
            flight['flight']['iata'],
            flight['departure']['airport'],
            flight['departure']['iata'],
            flight['arrival']['airport'],
            flight['arrival']['iata'],
            "\nEstimated arrival :", flight['arrival']['estimated'],
            )
