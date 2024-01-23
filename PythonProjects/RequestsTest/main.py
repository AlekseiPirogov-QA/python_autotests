"""
Kolorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token' :'c6c3c83322eb1e2e55e668f589e8e736'}


body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)  
print (response.json())


body = {
    "pokemon_id": "28391",
    "name": "Lysiii",
    "photo": "https://dolnikov.ru/pokemons/albums/068.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)  
print (response.json())


body = {
    "pokemon_id": "28392"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)  
print (response.json())

# body = {
#      "attacking_pokemon": "28390",
#     "defending_pokemon": "28373"
# }

# response = requests.post(url=f'{URL}/battle', json=body, headers=HEADER, timeout=5)  
# print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')