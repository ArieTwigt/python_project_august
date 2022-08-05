import requests
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

OPENWEATHERMAPID = os.environ.get('OPENWEATHERMAPID')

def get_weather_by_city(city: str):
    
    endpoint = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHERMAPID}&units=metric"
    response = requests.get(endpoint)
    data = response.json()

    weather_temp = []
    weather_description = []
    weather_dt_txt = []
    
    for key, value in enumerate(data['list']):
        weather_temp.append(value['main']['temp'])
        weather_description.append(value['weather'][0]['description'])
        weather_dt_txt.append(value['dt_txt'])
    
    # compose our dictionary with a dict comprehension
    weather_dict = {   # structure
                        date_txt: {
                            "temperature": temp,
                            "description": description
                        }
                        # loop
                        for temp, description, date_txt
                        # source items
                        in zip(weather_temp, weather_description, weather_dt_txt)
                    }
    
    
    
    print("We are here")