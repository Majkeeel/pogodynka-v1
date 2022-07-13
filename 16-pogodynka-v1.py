from locale import DAY_1
import requests
import json

print("Pythonowa pogodynka na nablizsze 3 dni!")
print(" ")
location = input('Podaj nazwe miasta w którym chcesz sprawdzić pogode: ')

response = requests.get(f'https://goweather.herokuapp.com/weather/{location}')

temperature = response.json()['temperature']
wind = response.json()['wind']
description = response.json()['description']

print("Aktualnie w " + location + "jest " + temperature)
print("Predkość wiatru: " + wind)
print("aktualnie w " + location + "jest: " + description)
print("Pogoda na 3 dni: ")