import requests
import pandas as pd
import os

def import_cars_by_brand(brand: str, selected_color: str='ZWART', export_to_csv=False) -> list:
    '''
    Returns a list of cars by the specified brand
    
    params:
    * brand, a car brand
    * colour
    '''
    
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"
    response = requests.get(endpoint)
    
    response.status_code
    
    cars_list = response.json()
    
    filtered_cars_list = [car
                          for car in cars_list
                          if car['eerste_kleur'] == selected_color]
    
    cars_df = pd.DataFrame(filtered_cars_list)
    
    if export_to_csv:
        folder_name = f"cars_data/{brand}"
        os.makedirs(folder_name, exist_ok=True)
        filename = f"{folder_name}/cars_{brand}.csv"
        print(f"Exporting to file:\n{filename}\n")
        cars_df.to_csv(filename, 
                   sep=";",
                   index=None)
    else:
        print(cars_df)
    
    return cars_df
    
    
  