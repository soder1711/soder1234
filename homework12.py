# task 1
import requests

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()

print(response["value"])

# task 2
import requests
import json
municipality = input("Enter your city: ")
api_key = "1dc6fc6a121894b4775b4ccb30e9dab5"

def get_weather(municipality, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"
    response2 = requests.get(url).json()
    print(json.dumps(response2, indent=2))
    temp = response2["main"]["temp"]
    temp -= 273.15
    print(temp)
    description = response2["weather"][0]["description"]
    print(description)

get_weather(municipality, api_key)