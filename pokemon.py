import requests
import json


url = "https://pokeapi.co/api/v2/pokemon/?limit=600000"
response = requests.get(url)
print(response)

print(response.text)

#turn it into a dictionary
data = response.json()
#print(data)
print(data.keys())

#print(data['moves'])
#for pokemon in data:
#    if 

#for move in data['moves']:
#    print(move)


