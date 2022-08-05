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
    
    weather_df = pd.DataFrame.from_dict(weather_dict, 
                                        orient='index', 
                                        columns=['temperature', 'description'])
    
    weather_df_clean = (weather_df
        .reset_index()
        .rename(columns={"index": "date"})
    )
    
    # Modify the data frame
    temperature_classifier = lambda temperature: 'hot' if temperature > 20 else 'warm'
    
    weather_df_clean['temperatur_class'] = weather_df_clean['temperature'].apply(temperature_classifier)
    
    # Export
    current_files_folders = os.listdir()
    
    parent_folder_name = 'weather_data'
    if parent_folder_name not in current_files_folders:
        os.mkdir(parent_folder_name)
    
    folder_name = f"{parent_folder_name}/{city}"
    os.makedirs(folder_name, exist_ok=True)
    
    filename = f"{folder_name}/weather_{city}.csv"
    print(f"\n✉️ Writing to {filename}\n")
    
    weather_df_clean.to_csv(filename,
                            sep=";", 
                            index=False)