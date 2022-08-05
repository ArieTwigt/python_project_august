from custom_modules.weather_functions import get_weather_by_city
from custom_modules.parsers import parse_json_config
import sys


if __name__ == "__main__":
    configuration = parse_json_config("configuration.json")
    
    selected_cities = configuration['cities']
    for city in selected_cities:
        get_weather_by_city(city)