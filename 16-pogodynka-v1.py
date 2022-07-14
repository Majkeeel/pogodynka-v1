from dataclasses import asdict
import requests
import json

print("Pythonowa pogodynka na nablizsze 3 dni!")
print(" ")
location = input('Podaj nazwe miasta w którym chcesz sprawdzić pogode: ')

response = requests.get(f'https://goweather.herokuapp.com/weather/{location}')

temperature = response.json()['temperature']
wind = response.json()['wind']
description = response.json()['description']
temperature_1 = response.json()['forecast'][0]['temperature']
wind_1 = response.json()['forecast'][0]['wind']
temperature_2 = response.json()['forecast'][1]['temperature']
wind_2 = response.json()['forecast'][1]['wind']
temperature_3 = response.json()['forecast'][2]['temperature']
wind_3 = response.json()['forecast'][2]['wind']

print("")
print("Aktualnie w " + location + " " + "jest " + temperature)
print("Predkość wiatru: " + wind)
print("Aktualnie w " + location + " " + "jest: " + description)
print("")
print("Pogoda na następne 3 dni: ")
print("")
print("Dzień 1:")
print("Temperatura: " + temperature_1)
print("Predkość wiatru: " + wind_1)
print("")
print("Dzień 2:")
print("Temperatura: " + temperature_2)
print("Predkość wiatru: " + wind_2)
print("")
print("Dzień 3:")
print("Temperatura: " + temperature_3)
print("Predkość wiatru: " + wind_3)
