import requests
import pandas as pd

def import_cars_by_brand(brand: str) -> list:
    '''
    Returns a list of cars by the specified brand
    
    params:
    * brand, a car brand
    '''
    
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"
    response = requests.get(endpoint)
    
    response.status_code
    
    cars_list = response.json()
    
    cars_df = pd.DataFrame(cars_list)
    
    cars_df.to_csv(f"cars_{brand}.csv", 
                   sep=";",
                   index=None)
    
    return cars_df
    
    
    