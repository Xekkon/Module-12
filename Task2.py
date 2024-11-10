import requests
import json

apikey = "3cc565570a202a7edb9124fc824af2bd"

def open_weather(city):
    server = "https://api.openweathermap.org/"
    request = f"{server}data/2.5/weather?q={city}&appid={apikey}"
    response = requests.get(request)
    return response.status_code, response.json()

def temp_celsius(kelvin):
    return kelvin - 273.15

city = input("Enter a city: ")
status_code, weather_data = open_weather(city)

if status_code == 200:
    kelvin_temp = weather_data['main']['temp']
    celsius_temp = temp_celsius(kelvin_temp)
    print(f"The temperature in {city} is {celsius_temp:.2f}°C.")
else:
    print("Error fetching data:", weather_data.get("message", "Unknown error"))
