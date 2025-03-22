import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = '143490f1d9ddfd393f7dfbf5587a21cf'

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


def get_lan_lon(city_name, state_code, country_code, api_key):
    # Construct query string dynamically
    query = f"{city_name},{country_code}" if not state_code else f"{city_name},{state_code},{country_code}"
    
    resp = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={query}&appid={api_key}").json()
    
    if resp:
        data = resp[0]
        lat, lon = data.get('lat'), data.get('lon')
        return lat, lon
    else:
        raise ValueError("Location not found. Please check your inputs.")


def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main = resp.get('weather')[0].get("main"), description = resp.get('weather')[0].get("description"),icon = resp.get('weather')[0].get("icon"),temperature = int(resp.get('main').get('temp'))
    )
    
    return data

def main(city_name, state_name, country_name):
    lat,lon = get_lan_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data
     
if __name__ == "__main__":
    lat,lon = get_lan_lon('Toronto', 'ON', 'Canada', api_key)
    print(get_current_weather(lat, lon, api_key))
