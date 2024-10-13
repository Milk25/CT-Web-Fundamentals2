import requests
import json


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['name']
            mass = planet['mass']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    

fetch_planet_data()

        




# import requests

# def fetch_planet_data():
#     url = "https://api.le-systeme-solaire.net/rest/bodies/"
#     response = requests.get(url)
#     planets = response.json()['bodies']

#     planet_data = []

#     # Process each planet's info
#     for planet in planets:
#         if planet['isPlanet']:
#             name = planet['englishName']
#             mass = planet['mass']['massValue'] if planet['mass'] else 'Unknown'
#             orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 'Unknown'
#             planet_data.append({
#                 'name': name,
#                 'mass': mass,
#                 'orbit_period': orbit_period
#             })
#             print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

#     return planet_data

# def find_heaviest_planet(planets):
#     heaviest_planet = None
#     max_mass = float('-inf')

#     for planet in planets:
#         if planet['mass'] != 'Unknown' and planet['mass'] > max_mass:
#             max_mass = planet['mass']
#             heaviest_planet = planet

#     return heaviest_planet

# planets = fetch_planet_data()
# heaviest_planet = find_heaviest_planet(planets)

# if heaviest_planet:
#     print(f"The heaviest planet is: {heaviest_planet['name']} with a mass of {heaviest_planet['mass']} kg.")
# else:
#     print("Could not determine the heaviest planet.")
