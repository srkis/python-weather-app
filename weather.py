from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Belgrade"):

   request_url = f'https://api.weatherapi.com/v1/forecast.json?key={os.getenv("API_KEY")}&q={city}&days=5'

   weather_data = requests.get(request_url).json()

   return weather_data

if __name__ == "__main__":
    print('\n*** Get current weather Conditions ***\n')
    city = input("\n Please enter City: ")

    #check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = 'Belgrade'

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)