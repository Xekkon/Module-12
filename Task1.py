import requests
import json

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        #response.raise_for_status()  For error handling
        joke_data = response.json()
        print(joke_data['value'])
    except requests.exceptions.RequestException as example:
        print(f"An error occurred: {example}")

get_random_chuck_norris_joke()