import requests
import pandas as pd

def import_cars_by_brand(brand: str, selected_color: str='ZWART') -> list:
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
    
    cars_df.to_csv(f"cars_{brand}.csv", 
                   sep=";",
                   index=None)
    
    return cars_df
    
    
  