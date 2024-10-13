import requests
import json


api_url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(api_url)
json_data = response.text


# print(f"Abilities and names of Pokemon: {poki_data}")



pokemon_names = ["pikachu", "bulbasaur", "charmander"]
# pokemon_attributes = pokemon_names
def fetch_pokemon_data(pokemon_names):
    # pokemon_names = ["pikachu", "bulbasaur", "charmander"]
 
    for pokemon_name in pokemon_names:
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(api_url)
        json_data = response.json()   
        name = json_data['name']
        abilities = json_data['abilities']
        weight = json_data['weight']
        print(f"Pokemon:, {name}")
        print(f"Abilities:, {abilities}")
        print(f"Weight:, {weight}")
fetch_pokemon_data(pokemon_names)


def calculate_average_weight(pokemon_list):
    pokemon_list = pokemon_names
    for value in range(len(pokemon_list)):
        if value == pokemon_list:
            print(f"Pokemon average: {value} {pokemon_list}")


calculate_average_weight(pokemon_names)