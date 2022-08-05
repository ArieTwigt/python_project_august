from custom_modules.weather_functions import get_weather_by_city
import sys


if __name__ == "__main__":
    selected_city = sys.argv[1]
    _ = get_weather_by_city(selected_city)
    